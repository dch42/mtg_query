# mtg_query
CLI script to conditionally query Magic: The Gathering API using the [Python SDK](https://github.com/MagicTheGathering/mtg-sdk-python) for card data. Useful for quick lookups/deckbuilding/etc.

## Setup 🔧
clone the repo and change to directory:
~~~
git clone https://github.com/dch42/mtg_query.git && cd mtg_query
~~~

Running `make` will install dependencies and add executable permissions to the script.

~~~
make
~~~

## Usage

To search for all *black instant* cards with a CMC of *2* which contain the text *sacrifice*:

~~~
./mtg_query.py -c black -t instant -cmc 2 -txt sacrifice
~~~

Will yield:

~~~
Searching for matching cards...

             46 matching cards found:             
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━━━━━┓
┃ Card Title           ┃ Set   ┃ CMC ┃ Mana Cost ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━━━━━┩
│ Final Payment        │ RNA   │   2 │    {W}{B} │
│ Devour Flesh         │ GTC   │   2 │    {1}{B} │
│ Urborg Justice       │ WTH   │   2 │    {B}{B} │
│ Altar's Reap         │ M14   │   2 │    {1}{B} │
│ Altar's Reap         │ C15   │   2 │    {1}{B} │
...
~~~

### Options
- `-h, --help`
    - show this help message and exit
- `-n, --name [NAMES...]`
    - search for term(s) in card name
- `-t, --type [TYPES...]`
    - search for term(s) in card type
- `-c, --color [COLORS...]`
    - search for color(s) in card mana cost 
- `-txt, --text [TERMS...]`
    - search for term(s) in card text 
- `-cmc`
    - search for cards with 'x' converted mana cost 

