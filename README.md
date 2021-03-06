# mtg_query
CLI script to conditionally query Magic: The Gathering API using the [Python SDK](https://github.com/MagicTheGathering/mtg-sdk-python) for card data. Useful for quick look ups, deck building, etc. Console tables and markdown handled with [rich](https://github.com/willmcgugan/rich).

## Setup ๐ง
clone the repo and change to directory:
~~~
git clone https://github.com/dch42/mtg_query.git && cd mtg_query
~~~

Run `setup.sh` to install the script: 
~~~
chmod +x setup.sh && ./setup.sh
~~~

This will install dependencies and make the script available as `mtgq` in' ~/bin', adding it to bash or zsh $PATH. 

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
mtgq -c black -t instant -cmc 2 -txt sacrifice
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
โโโโโโณโโโโโโโโโโโโโโโโโโโโโโโณโโโโโโโโณโโโโโโณโโโโโโโโโโโโ
โ ID โ Card Title           โ Set   โ CMC โ Mana Cost โ
โกโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโฉ
โ 0  โ Final Payment        โ RNA   โ   2 โ    {W}{B} โ
โ 1  โ Devour Flesh         โ GTC   โ   2 โ    {1}{B} โ
โ 2  โ Urborg Justice       โ WTH   โ   2 โ    {B}{B} โ
โ 3  โ Altar's Reap         โ M14   โ   2 โ    {1}{B} โ
โ 4  โ Altar's Reap         โ C15   โ   2 โ    {1}{B} โ
โ 5  โ Liliana's Triumph    โ WAR   โ   2 โ    {1}{B} โ
โ 6  โ Corpse Cobble        โ MID   โ   2 โ    {U}{B} โ
โ 7  โ Liliana's Triumph    โ TSR   โ   2 โ    {1}{B} โ
...

Input card ID number to see more detailed information.            
Multiple card IDs can be entered at once, separated by spaces.            
Hit `ENTER` when done, or `CTRL+C` to quit: 
~~~

To view more detailed card information, enter the 'ID' of the cards, separated by spaces.

Entering `0 7` will yield:

~~~
โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ
โ                                Final Payment {W}{B}                                โ
โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ

                                   Instant - Common                                   

Text: As an additional cost to cast this spell, pay 5 life or sacrifice a creature or 
enchantment. Destroy target creature.                                                 

Flavor Text: There's nothing quite like the feeling of paying off a large debt.       

 โข CMC: 2                                                                             
 โข Colors: ['Black', 'White']                                                         
 โข Set: Ravnica Allegiance (RNA)                                                      
โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ
โ                              Liliana's Triumph {1}{B}                              โ
โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ

                                  Instant - Special                                   

Text: Each opponent sacrifices a creature. If you control a Liliana planeswalker, each
opponent also discards a card.                                                        

Flavor Text: Her triumph came not from escaping her death, but in claiming her        
independence.                                                                         

 โข CMC: 2                                                                             
 โข Colors: ['Black']                                                                  
 โข Set: Time Spiral Remastered (TSR)

Press `ENTER` to return to card list, `CTRL+C` to quit
~~~

A table of card legalities will also be rendered to the console:

~~~
   Final Payment Legalities   
โโโโโโโโโโโโโโโโโโโณโโโโโโโโโโโ
โ Format          โ Legality โ
โกโโโโโโโโโโโโโโโโโโโโโโโโโโโโโฉ
โ Commander       โ Legal    โ
โ Duel            โ Legal    โ
โ Gladiator       โ Legal    โ
โ Historic        โ Legal    โ
โ Historicbrawl   โ Legal    โ
โ Legacy          โ Legal    โ
โ Modern          โ Legal    โ
โ Pauper          โ Legal    โ
โ Paupercommander โ Legal    โ
โ Penny           โ Legal    โ
โ Pioneer         โ Legal    โ
โ Vintage         โ Legal    โ
โโโโโโโโโโโโโโโโโโโดโโโโโโโโโโโ
~~~

To view more card data, return to the initial list by hitting 'ENTER'.

Planeswalker cards will display loyalty points, creatures power/toughness:
~~~
โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ
โ                       Ajani, Strength of the Pride {2}{W}{W}                       โ
โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ

                       Legendary Planeswalker โ Ajani - Mythic                        

Text: [+1]: You gain life equal to the number of creatures you control plus the number
of planeswalkers you control. [โ2]: Create a 2/2 white Cat Soldier creature token     
named Ajani's Pridemate with "Whenever you gain life, put a +1/+1 counter on Ajani's  
Pridemate." [0]: If you have at least 15 life more than your starting life total,     
exile Ajani, Strength of the Pride and each artifact and creature your opponents      
control.                                                                              

Flavor Text: None                                                                     

Loyalty: 5                                                                            

 โข CMC: 4                                                                             
 โข Colors: ['White']                                                                  
 โข Set: Core Set 2020 Promos (PM20)  

โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ
โ                              Ajani's Pridemate {1}{W}                              โ
โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ

                          Creature โ Cat Soldier - Uncommon                           

Text: Whenever you gain life, put a +1/+1 counter on Ajani's Pridemate.               

Flavor Text: Planeswalkers conjured replicas of old allies, reminders of the          
homeworlds that would fall next if Bolas prevailed.                                   

Power/Toughness: 2/2                                                                  

 โข CMC: 2                                                                             
 โข Colors: ['White']                                                                  
 โข Set: War of the Spark (WAR)                                                        
 ~~~
