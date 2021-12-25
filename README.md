# mtg_query
CLI script to conditionally query Magic: The Gathering API using the [Python SDK](https://github.com/MagicTheGathering/mtg-sdk-python) for card data. Useful for quick look ups, deck building, etc. Console tables and markdown handled with [rich](https://github.com/willmcgugan/rich).

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

### Options
- `-h, --help`
    - show this help message and exit
- `-cmc`
    - search for cards with 'x' converted mana cost     
- `-n, --name [NAMES...]`
    - search for term(s) in card name
- `-t, --type [TYPES...]`
    - search for term(s) in card type
- `-c, --color [COLORS...]`
    - search for color(s) in card mana cost 
- `-txt, --text [TERMS...]`
    - search for term(s) in card text 

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

Entering `0 7` will yield:

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
║                              Liliana's Triumph {1}{B}                              ║
╚════════════════════════════════════════════════════════════════════════════════════╝

                                  Instant - Special                                   

Text: Each opponent sacrifices a creature. If you control a Liliana planeswalker, each
opponent also discards a card.                                                        

Flavor Text: Her triumph came not from escaping her death, but in claiming her        
independence.                                                                         

 • CMC: 2                                                                             
 • Colors: ['Black']                                                                  
 • Set: Time Spiral Remastered (TSR)

Press `ENTER` to return to card list, `CTRL+C` to quit
~~~

To view more card data, return to the initial list by hitting 'ENTER'.

Planeswalker cards will display loyalty points, creatures power/toughness:
~~~
╔════════════════════════════════════════════════════════════════════════════════════╗
║                       Ajani, Strength of the Pride {2}{W}{W}                       ║
╚════════════════════════════════════════════════════════════════════════════════════╝

                       Legendary Planeswalker — Ajani - Mythic                        

Text: [+1]: You gain life equal to the number of creatures you control plus the number
of planeswalkers you control. [−2]: Create a 2/2 white Cat Soldier creature token     
named Ajani's Pridemate with "Whenever you gain life, put a +1/+1 counter on Ajani's  
Pridemate." [0]: If you have at least 15 life more than your starting life total,     
exile Ajani, Strength of the Pride and each artifact and creature your opponents      
control.                                                                              

Flavor Text: None                                                                     

Loyalty: 5                                                                            

 • CMC: 4                                                                             
 • Colors: ['White']                                                                  
 • Set: Core Set 2020 Promos (PM20)  

╔════════════════════════════════════════════════════════════════════════════════════╗
║                              Ajani's Pridemate {1}{W}                              ║
╚════════════════════════════════════════════════════════════════════════════════════╝

                          Creature — Cat Soldier - Uncommon                           

Text: Whenever you gain life, put a +1/+1 counter on Ajani's Pridemate.               

Flavor Text: Planeswalkers conjured replicas of old allies, reminders of the          
homeworlds that would fall next if Bolas prevailed.                                   

Power/Toughness: 2/2                                                                  

 • CMC: 2                                                                             
 • Colors: ['White']                                                                  
 • Set: War of the Spark (WAR)                                                        
 ~~~
