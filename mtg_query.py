#!/usr/bin/env python3
"""CLI script to conditionally query Magic: The Gathering API using the Python SDK for card data."""
import argparse
from mtgsdk import Card
import pyfiglet
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown

cards = []
detailed_cards = []

# define and parse args
parser = argparse.ArgumentParser(
    description="Conditionally query Magic: The Gathering API for card data")
parser.add_argument("-n", "--name", type=str, nargs='+',
                    help='search for term(s) in card name')
parser.add_argument("-t", "--type", type=str, nargs='+',
                    help='search for term(s) in card type')
parser.add_argument("-c", "--color", type=str, nargs='+',
                    help='search for color(s) in card mana')
parser.add_argument("-txt", "--text", type=str, nargs='+',
                    help='search for term(s) in card text')
parser.add_argument("-cmc", type=int,
                    help='search for cards matching converted mana cost')
args = parser.parse_args()

# convert args to query-friendly format
CMC, NAMES, COLORS, TYPES, TEXT = '', '', '', '', ''
if args.name:
    NAMES = (','.join(args.name))
if args.type:
    TYPES = (','.join(args.type))
if args.color:
    COLORS = (','.join(args.color))
if args.text:
    TEXT = (','.join(args.text))
if args.cmc:
    CMC = int(args.cmc)


def print_table(cards):
    """Print a table of cards matching query"""
    table = Table(title=f"{len(cards)} matching cards found:")
    table.add_column("ID", style="white")
    table.add_column("Card Title", justify="left", style="cyan", no_wrap=True)
    table.add_column("Set", style="magenta")
    table.add_column("CMC", justify="right", style="green")
    table.add_column("Mana Cost", justify="right", style="white")
    for idx, card in enumerate(cards):
        table.add_row(f"{idx}", f"{card.name}", f"{card.set}",
                      f"{int(card.cmc)}", f"{card.mana_cost}")
    console = Console()
    console.print(table)
    detailed_cards = input(
        """\nInput card ID number to see more detailed information.\
            \nMultiple card IDs can be entered at once, separated by spaces.\
            \nHit `ENTER` when done, or `CTRL+C` to quit: """).split()
    print_details(detailed_cards)


def print_card_md(card):
    """Create and print detailed markdown for cards"""
    # eval whether to show loyalty, p/t, or none
    loyal_power = f'Loyalty: {card.loyalty}' if 'Planeswalker' in card.type else f'Power/Toughness: {card.power}/{card.toughness}' if 'None' not in f'str({card.power})' else ''
    card_md = f"""# {card.name} {card.mana_cost}
### {card.type} - {card.rarity}
Text: {card.text}\n
Flavor: *{card.flavor}*
{loyal_power}
- CMC: {int(card.cmc)}
- Colors: {card.colors}
- Set: {card.set_name} ({card.set})
"""
    console = Console()
    md = Markdown(card_md)
    console.print(md)


def print_details(detailed_cards):
    """Loop through cards"""
    for card_id in detailed_cards:
        card = cards[int(card_id)]
        print_card_md(card)
    input("Press `ENTER` to return to card list, `CTRL+C` to quit")
    print_table(cards)


if __name__ == '__main__':
    pyfiglet.print_figlet("MTG Query")
    print("Searching for matching cards...\n")
    cards = Card.where(name=f'{NAMES}', type=f'{TYPES}',
                       colors=f'{COLORS}', cmc=f'{CMC}', text=f'{TEXT}').all()
    if len(cards):
        print_table(cards)
    else:
        print("No matching cards found.")
