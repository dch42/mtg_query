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

~~~
./mtg_query.py -n ajanji pride -t planeswalker
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
- `-cmc`
    - search for cards with 'x' converted mana cost 

