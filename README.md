# Zombie Survival
 A simple python text-based game of survival, resource management and strategic deision making.

 ## Game Overview
 Zombie Survival is a game designed for 1 to 4 players, where each player is a member of a camp collecting resource and fighting against zombie attacks.
 The objective is survive for ten days by gathering resource on scavenging missions during the day and defending against zombie attacks during the night.
 Any players remaining at the end of the ten days win.

 ## Programming
 The game was built using fundamentals of Object-Orientated Programming.
 Models are created for Players, Locations and Camp which each inherits resource attributes from an overall GameEntity class and then adds specific attributes for each class. 
 Design operates from small functions for gameplay mechanics, larger functions to operate the 4 main stages of gameplay and a master function to runs the game loop.

 ## Game Features

 ### Resource Management
 Players must scavenge and manage 3 key resources:
 * Food: Each player must consume 1 food token per day.
 * Medicine: Used to heal injuries received on missions or illess in the camp.
 * Weapons: Used to fight against zombie attacks during the night, and aid in settling conflicts between players.

## Players
* At the start of the game the players begin with 1 weapon token
* Players can hold a maximum of 8 resources at one time.
* Player may suffer injuries/illness from missions/problems at camp.

Health Chart:

3 - Full Health
2 - Wounded - Player must consume 1 medicine token or rest at camp for one day to recover. 
1 - Severely Wounded - Player is unable to go out on missions. Player must consume 2 medicine tokens and stay at camp for one day to recover. 
0 - Dead - Player is out.

## Camp
At the start of the game the camp begins with:
* 10 food tokens
* 2 medicine tokens
* 0 weapon tokens

Throughout the game if there are zombie attacks, player health issues and daily food consumption.
In each instance camp resources are the first to be used.
If the camp don't not have sufficent resources then player may use their own personal resources.
Player may choose to help other players who do not have personal resources, but do not have to.

## Locations
There are 12 game locations with a variety of different resources.
At the beginning of the game, locations are randomly selected as Easy (4 locations), Medium (4 locations) and Hard (4 locations).

### Missions
During the day players choose locations of varying difficulty to collect resources. Outcomes are decided by rolling of a d6 dice.
* Easy: A player rolls 2 d6s and takes the highest roll
* Medium: A player rolls a single d6
* Hard: A player rolls 2 d6s and takes the lowest roll

Mission Roll Chart:
1. Disaster - Player receives a severe injury and fails to collect any resources.
2. Bad - Player receives a minor injury and collects only half resources.
3. Complication - Player may choose between receving a minor injury or collecting only half resourcs.
4. Success - Player may collect as many resources as they can carry.
5. Success - Player may collect as many resources as they can carry.
6. Perfect - Player may collect as many resources as they can carry and also collect one extra resource of their choice.

### End of Day
At the end of the day each player must consume 1 food token or lose 1 health point.

Zombie Attacks - If zombies attack player must fight back with weapons, a weapon token must be used for every zombie that attacks.
If there are insufficent weapons to fight back then a random player dies.

Daily Event Roll Chart:
1. Major Zombie Attack - Zombies double to the number of the current day attack.
2. Zombie Attack - Zombies equal to the number of the current day attack.
3. Zombie Attack - Zombies equal to the number of the current day attack.
4. Camp Illness - Each player must use 1 medicine token or lose 1 health point.
5. Quiet Night - No event.
6. Quiet Night - No event.
