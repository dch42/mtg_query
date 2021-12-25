# mtg_query
CLI script to conditionally query Magic: The Gathering API using the [Python SDK](https://github.com/MagicTheGathering/mtg-sdk-python) for card data. Useful for quick lookups/deckbuilding/etc. Tables constructed with [rich](https://github.com/willmcgugan/rich).

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
*Note: Parameters are evaluated cumulatively, rather than individually.*

Query parameters are passed as arguments when invoking the script. 

For example, to search for all ***'black' 'instant'*** cards with a CMC of ***'2'*** which contain the text ***'sacrifice'***:

~~~
./mtg_query.py -c black -t instant -cmc 2 -txt sacrifice
~~~

Result:

~~~
 __  __ _____ ____    ___                        
|  \/  |_   _/ ___|  / _ \ _   _  ___ _ __ _   _ 
| |\/| | | || |  _  | | | | | | |/ _ \ '__| | | |
| |  | | | || |_| | | |_| | |_| |  __/ |  | |_| |
|_|  |_| |_| \____|  \__\_\\__,_|\___|_|   \__, |
                                           |___/ 

Searching for matching cards...

               46 matching cards found:                
┏━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━━━━━┓
┃ ID ┃ Card Title           ┃ Set   ┃ CMC ┃ Mana Cost ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━━━━━┩
│ 0  │ Final Payment        │ RNA   │   2 │    {W}{B} │
│ 1  │ Devour Flesh         │ GTC   │   2 │    {1}{B} │
│ 2  │ Urborg Justice       │ WTH   │   2 │    {B}{B} │
│ 3  │ Altar's Reap         │ M14   │   2 │    {1}{B} │
│ 4  │ Altar's Reap         │ C15   │   2 │    {1}{B} │
│ 5  │ Liliana's Triumph    │ WAR   │   2 │    {1}{B} │
│ 6  │ Corpse Cobble        │ MID   │   2 │    {U}{B} │
│ 7  │ Liliana's Triumph    │ TSR   │   2 │    {1}{B} │
...

Input card ID number to see more detailed information.            
Multiple card IDs can be entered at once, separated by spaces.            
Hit `ENTER` when done, or `CTRL+C` to quit: 
~~~

To view more detailed card information, enter the 'ID' of the cards, separated by spaces.

Entering `0 1` will yield:

~~~
╔════════════════════════════════════════════════════════════════════════════════════╗
║                                Final Payment {W}{B}                                ║
╚════════════════════════════════════════════════════════════════════════════════════╝

                                   Instant - Common                                   

Text: As an additional cost to cast this spell, pay 5 life or sacrifice a creature or 
enchantment. Destroy target creature.                                                 

Flavor Text: There's nothing quite like the feeling of paying off a large debt.       

 • CMC: 2                                                                             
 • Colors: ['Black', 'White']                                                         
 • Set: Ravnica Allegiance (RNA)                                                      
╔════════════════════════════════════════════════════════════════════════════════════╗
║                                Devour Flesh {1}{B}                                 ║
╚════════════════════════════════════════════════════════════════════════════════════╝

                                   Instant - Common                                   

Text: Target player sacrifices a creature, then gains life equal to that creature's   
toughness.                                                                            

Flavor Text: His twisted mind concluded that if he was what he ate, and he wanted to  
stay human, . . .                                                                     

 • CMC: 2                                                                             
 • Colors: ['Black']                                                                  
 • Set: Gatecrash (GTC)                                                               
Press `ENTER` to return to card list, `CTRL+C` to quit
~~~

To view more card data, return to the initial list by hitting 'ENTER'.

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

