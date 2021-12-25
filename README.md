# mtg_query
CLI script to conditionally query Magic: The Gathering API for card data. Useful for quick lookups/deckbuilding/etc. 

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
- `-n, --name [TERMS...]`
    - search for term(s) in card name
- `-t, --type [TERMS...]`
    - search for term(s) in card type 
