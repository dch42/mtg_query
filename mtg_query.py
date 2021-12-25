#!/usr/bin/env python3
"""CLI script to conditionally query Magic: The Gathering API using the Python SDK for card data."""
import argparse
from mtgsdk import Card
import pyfiglet
from rich.console import Console
from rich.table import Table

cards = []

# define and parse args
parser = argparse.ArgumentParser(
    description="Conditionally query Magic: The Gathering API for card data")
parser.add_argument("-n", "--name", type=str, nargs='+',
                    help='search for term(s) in card name')
parser.add_argument("-t", "--type", type=str, nargs='+',
                    help='search for term(s) in card type')
parser.add_argument("-c", "--color", type=str, nargs='+',
                    help='search for color(s) in card mana')
parser.add_argument("-cmc", type=int,
                    help='search for cards matching converted mana cost')
args = parser.parse_args()

# convert args to query-friendly format
NAMES, COLORS, TYPES = '', '', ''
if args.name:
    NAMES = (','.join(args.name))
if args.type:
    TYPES = (','.join(args.type))
if args.color:
    COLORS = (','.join(args.color))

def print_table(cards):
    """Print a table of cards matching query"""
    table = Table(title=f"{len(cards)} matching cards found:")
    table.add_column("Title", justify="left", style="cyan", no_wrap=True)
    table.add_column("Set", style="magenta")
    table.add_column("CMC", justify="right", style="green")
    table.add_column("Mana Cost", justify="right", style="white")
    for card in cards:
        table.add_row(f"{card.name}",f"{card.set}",f"{int(card.cmc)}", f"{card.mana_cost}")
    console = Console()
    console.print(table)

if __name__ == '__main__':
    pyfiglet.print_figlet("MTG Query")
    cards = Card.where(name=f'{NAMES}', type=f'{TYPES}', colors=f'{COLORS}', cmc=f'{int(args.cmc)}').all()
    if len(cards):
        print_table(cards)
    else:
        print("No matching cards found.")
