#!/usr/bin/env python
# coding: utf-8

# ## Game Mechanics And Engine Requirment
# 
# 
# # Start of Game Setup
# 
# Create the No of Players and starting totals
# Setup Camp and starting Supplies
# Distribute random locations as Easy, Medium or Hard
# Start Round Tracker
# 
# # Classes to Create
# 
# Camp
# 
# * Attributes - Food, Weapons, Medicine
# * Print Camp details
# 
# Locations
# 
# * Attributes - Food, Weapons, Medicine, Difficulty
# * Print Location details
# 
# Players
# 
# * Attributes - Food, Weapons, Medicine, Injury)
# * Function to randomly select name from a list
# * Print player details
# 
# # Functions to Create
# 
# Overall game flow
# Print Game State
# * Camp
# * Players
# * Locations
# Player Round
# Computer Rounds
# Mission Outcome Random Generator
# Camp End of Day Random Generator
# Attacking another player
# 
# 
# # Game flow
# * Initialise the game
#     * Flavour introduction
#     * Create the No of Players and starting totals
#         * Ask for number of players total
#         * Ask for number of human players
#         * Ask for human players names
#         * Randomly generate computer player names
#         * Create instances of of player classes
#         * Store player classes in a list
#     * Setup camp and starting supplies
#         * Create instance of camp class
#     * Distribute random locations as Easy, Medium or Hard
#         * Create instances of location classes
#     * Setup round tracker
#     * Initialise Rounds
#         * game_state()
#         * player round loop
#         * computer round loop
#         * end of day outcome
#         * game_state()
#         * Update Rounds Tracker
#     

# ## Imports

# In[1]:


from math import floor
import random


# ## Models

# In[2]:


# Game Entity Parent Class

class GameEntity:
    def __init__(self, name, food, medicine, weapons):
        self.name = name
        self.food = food
        self.medicine = medicine
        self.weapons = weapons    
        
    def __repr__(self):
        return f"{self.name} has {self.food} food, {self.medicine} medicine, and {self.weapons} weapon(s)."

    
class Camp(GameEntity):
    
    pass


class Location(GameEntity):
    
    difficulties = {0:'Easy',1:'Medium',2:'Hard'}
    
    def __init__(self, name, food, medicine, weapons):
        super().__init__(name, food, medicine, weapons)
        self.difficulty = 0
        self.empty = False

        
class Player(GameEntity):
    
    # Injury states
    
    injury_states = {-2:'dead',-1:'dead',0:'dead',1:'severely wounded',2:'wounded',3:'healthy'}
    
    def __init__(self, name, food=0, medicine=0, weapons=1, computer=True):
        super().__init__(name, food, medicine, weapons)
        self.computer = computer
        self.health = 3
        self.had_dinner = False

    def __repr__(self):
        return f"{self.name} has {self.food} food, {self.medicine} medicine, and {self.weapons} weapon(s) and they are {self.injury_states[self.health]}."        


# ## Initialise Base Variables

# In[3]:


# Camp

camp = Camp('Base Camp',10,2,0)

# Players Lists

starting_players = []

players = []


# ## Locations

# In[4]:


# Locations

abandoned_farm = Location('Abandoned Farm',6,0,2)
corner_shop = Location('Corner Shop',5,0,1)
hospital = Location('Hospital',3,5,2)
military_base = Location('Military Base',1,1,7)
pharmacy = Location('Pharmacy',2,5,0)
police_station = Location('Police Station',2,2,6)
prison = Location('Prison',2,2,5)
research_lab = Location('Research Lab',1,4,1)
school = Location('School',3,1,2)
shopping_mall = Location('Shopping Mall',2,2,1)
supermarket = Location('Supermarket',8,1,0)
warehouse = Location('Warehouse',3,2,3)

# List

locations = [abandoned_farm,corner_shop,hospital,
             military_base,pharmacy,police_station,
             prison,research_lab,school,
             shopping_mall,supermarket,warehouse]

# Special location for bonuses

bonus_resources = Location('Bonus Resources',100,100,100)


# ## Computer Players

# In[5]:


# Random name generator

computer_names = ['Rick','Lori','Carl','Shane',
                 'Glenn','Dale','Carol','Andrea',
                 'Maggie','Daryl','Michonne','Morgan',
                 'Hershel','Merle','Philip','Beth',
                 'Tyreese','Sasha','Bob','Abraham',
                 'Eugene','Rosita','Tara','Gabriel',
                 'Jessie','Aaron','Deanna','Spencer']

def generate_name():
    return random.choice(computer_names)


# ## Functions
# 
# ### Game State Details

# In[6]:


def game_state(day_tracker):
    
    print(f'DAY: {day_tracker}\n')
    
    print('CAMP:\n')
    
    print(camp)
    
    print('\nLOCATIONS:')
    
    print('\nEASY:')
    for location in locations:
        
        if location.difficulty == 0 and location.empty == False:
            print(location)
        elif location.difficulty == 0 and location.empty == True:
            print(f'{location.name} is empty.')
            
    print('\nMEDIUM:')
    for location in locations:
        
        if location.difficulty == 1 and location.empty == False:
            print(location)
        elif location.difficulty == 1 and location.empty == True:
            print(f'{location.name} is empty.')
            
    print('\nHARD:')
    for location in locations:
        
        if location.difficulty == 2 and location.empty == False:
            print(location)
        elif location.difficulty == 2 and location.empty == True:
            print(f'{location.name} is empty.')
            
        
    print('\nPLAYERS:\n')
    
    for player in starting_players:
        if player.health <= 0:
            print(f'{player.name} is dead.')
        else:
            print(player)


# ### Roll d6

# In[7]:


def roll_a(number):
    
    return random.randrange(1,number+1)


# ### Mission Rolls

# In[8]:


def mission_rolls(player,location):
    # Iterate through each player's rolls for the specific difficulty
    
    if location.difficulty == 0:

        # Difficulty is easy, take higher of 2 rolls

        roll1 = roll_a(6)
        roll2 = roll_a(6)

        print(f'{player.name} rolled a {roll1} and a {roll2}.')

        if roll1 > roll2:
            return(roll1)
        else:
            return(roll2)

    elif location.difficulty == 2:

        # Difficulty is hard, take lower of 2 rolls

        roll1 = roll_a(6)
        roll2 = roll_a(6)

        print(f'{player.name} rolled a {roll1} and a {roll2}.')

        if roll1 < roll2: 
            return(roll1)
        else:
            return(roll2)
    else:

        roll3 = roll_a(6)

        print(f'{player.name} rolled a {roll3}.')

        return(roll3)        


# ### Injury Function

# In[9]:


def injury(player, wound):
    
    player.health -= wound
    
    if player.health < 1:
        print(f'{player.name} fought their best but died.')
        players.remove(player)
        camp.food += player.food
        camp.medicine += player.medicine
        camp.weapons += player.weapons     
        player.food = 0
        player.medicine = 0
        player.weapons = 0
        
    elif player.health == 1:
        print(f'{player.name} is severely ill/wounded.')
    else:
        print(f'{player.name} is ill/wounded.')   


# ### Bonus Resource Function

# In[10]:


def bonus_resource(player, resource):
    
        if resource == 'food':
            player.food += 1
        elif resource == 'medicine':
            player.medicine += 1
        else:
            player.weapons +=1
        print(f'{player.name} also collects extra {resource}!')


# ### Player Can Get

# In[11]:


def player_can_get(player,location,half=False):

    # Current player resources total
    
    player_current = player.food + player.medicine + player.weapons
    
    # Player can have a maximum of 8 resources at a time
    
    player_free_slots = 8 - player_current
    
    # Current location resources total
    
    location_available = location.food + location.medicine + location.weapons
    
    # Check if half resources outcome from mission
    
    if half == True:
        
        location_available = floor(location_available/2)
        
    # If location has less resources that player's limit then reassign
        
    if location_available < player_free_slots:
        
        return location_available
        
    return player_free_slots


# ### Location Empty

# In[12]:


def location_empty(location):
    if location.food + location.medicine + location.weapons <= 0:
        print(f'{location.name} has run out of resources.')
        location.empty = True


# ## Computer Decision Logic
# 
# ### Decide Best Resource to collect

# In[13]:


# Check lowest resources at camp then pick from location accordingly

"""
Currently, the function has an inherent bias from the order of
the resource in the orignal list. It will always pick weapons
over food or medicine if the value is the same. As well as
food over medicine accordingly.

We can fine tune and improve the computer decesion process later.
Or simply re-order the list if we find other resources to be more
important for winning the game.
"""

def best_resource(camp, location):
    resources = ['weapons', 'food', 'medicine']
    
     # Sort the resources in ascending order based on supplies at camp
    sorted_resources = sorted(resources, key=lambda res: getattr(camp, res))
    
    # Iterate through the list to find the first available resource at the location
    for resource in sorted_resources:
        if getattr(location, resource) > 0:
            return resource

    # If no resource with positive supply at the location, return the lowest resource from the camp
    return sorted_resources[-1]


# ### Computer collects resources

# In[14]:


# Computer takes input of location, camp and personal resources to decide what to take.

def computer_collects(camp, location, player, half=False):           
        
    # Set counters for the selections
    
    food_track = 0
    medicine_track = 0
    weapons_track = 0
        
    # Pick a resource
    
    for resource in range(player_can_get(player,location,half)):

        pick = best_resource(camp, location)
        
        if pick == 'food':
            player.food += 1
            location.food -= 1
            food_track += 1
        elif pick == 'medicine':
            player.medicine += 1
            location.medicine -= 1
            medicine_track += 1
        else:
            player.weapons += 1
            location.weapons -= 1
            weapons_track += 1
            
    # Report what player took
    
    message = f'{player.name} took:'
    if food_track > 0:
        message += f'\n  {food_track} food'
    if medicine_track > 0:
        message += f'\n  {medicine_track} medicine'
    if weapons_track > 0:
        message += f'\n  {weapons_track} weapons'
    
    print(message)


# ## Mission

# In[15]:


def mission(players,location,camp):
      
    rolls = [] # List to add each player's roll
    
    for player in players:
        
        # Add the final roll from each player's rolls depending on difficulty
        
        rolls.append(mission_rolls(player,location))
    
    # Sort to numerical order then index the highest number
    
    rolls.sort()
    
    roll = rolls[-1]
    
    print(f'The final roll is {roll}.\n')
    
    
    if roll == 1:
        # Disaster - severe injury and receive nothing
        
        for player in players:
            # Injuries
            print(f'{player.name} receives a severe injury and collects no resources!')
            injury(player, 2)
            
    elif roll == 2:
        # Bad - injury and half resources
                
        for player in players:
            # Injuries
            injury(player, 1)
            
            if player.computer == False:
                # Human collects half resources
                pass
            else:
                # Computer collects half resources
                print(f'{player.name} receives an injury and collects only half resources.')
                computer_collects(camp, location, player, half=True)
        
    elif roll == 3:
        # Complications - injury or half
        
        for player in players:
            if player.computer == False:
                # Human chooses injury or half resources
                pass
            else:
                # Computer decides injury or half resources
                if player.health == 3:
                    # Take the injury
                    print(f'{player.name} chooses to take the injury and collects full resources.')
                    injury(player, 1)
                    computer_collects(camp, location, player)
                else:
                    # Computer collects half resources
                    print(f'{player.name} chooses to avoid an injury and collects only half resources.')
                    computer_collects(camp, location, player, half=True)
        
    elif roll == 4:      
        # Success  
        for player in players:
            if player.computer == False:
                # Human collects resources
                pass
            else:
                # Computer collects resources
                print(f'{player.name} collects full resources.')
                computer_collects(camp, location, player)
                
    elif roll == 5:       
        # Success   
        for player in players:
            if player.computer == False:
                # Human collects resources
                pass
            else:
                # Computer collects resources
                print(f'{player.name} collects full resources.')
                computer_collects(camp, location, player)
                
    elif roll == 6:      
        # Perfect Success   
        for player in players:
            if player.computer == False:
                # Human collects resources
                
                # Bonus resource
                bonus_pick = input('Type food, medicine or weapons')
                bonus_resource(player, bonus_pick)
                
            else:
                # Computer collects resources
                print(f'{player.name} collects full resources.')
                computer_collects(camp, location, player)
                
                # Bonus resource
                bonus_resource(player,best_resource(camp,bonus_resources)) 
                
    location_empty(location)
    print('\n')
    input('Continue?')
    print('\n')


# In[16]:


### Zombie Attack


# In[17]:


def zombie_attack(camp, players, day_tracker, double=False):    
    
    num_players = len(players)
    
    num_of_zombies = day_tracker
    
    if double == True:
        num_of_zombies = num_of_zombies*2
        
    print(f'{num_of_zombies} zombies attack!')
          
    if camp.weapons >= num_of_zombies:
        camp.weapons -= num_of_zombies
        print(f'The group successfully fight back against the zombies, {num_of_zombies} weapons are used.\n')
    
    else:
        # Check to see if players have enough
        
        total_weapons = 0 + camp.weapons
                
        for player in players:
            total_weapons += player.weapons
                
        if total_weapons < num_of_zombies:
            print(f'Players have insufficient weapons to fight back against the horde.\nA random player is sacrificed to hold back the zombies.')
            roll = roll_a(num_players)
            tracker = 1
            for player in players:
                if tracker == roll:
                    injury(player,3)
                    print(f'{player.name} was sacrificed for the greater good.\n')
                    break
                tracker += 1
        else:
            while camp.weapons < num_of_zombies:
                for player in players:
                    if player.weapons > 0:
                        player.weapons -= 1
                        camp.weapons += 1
                        
            camp.weapons -= num_of_zombies
            print(f'The group successfully fight back against the zombies, {num_of_zombies} weapons are used.\n') 


# ## End of Day Outcomes

# In[18]:


def end_of_day(camp, players, day_tracker):
    
    roll = roll_a(6)
    
    players_alive = [player for player in players if player.health > 0]
    
    num_players_alive = len(players_alive)
    
    food_empty = False
    
    # Daily Food
        
    if camp.food == 0:
        # Players must suffer 1 health point or use from their own resources
        print('\nThe group settles down for a night of dinner but no food is left at camp.')
        for player in players:
            if player.food > 0:
                player.food -= 1
                player.had_dinner = True
                print(f'{player.name} consumes food from their personal resources.')
            else:
                print(f'{player.name} cannot eat and suffers illness.')
                player.had_dinner = False
                injury(player,1)
        print('\n')

    elif camp.food >= num_players_alive:
        camp.food -= num_players_alive
        print(f'\nThe group settles down for a night of dinner and consumes {num_players_alive} food.\n')
        for player in players:
            player.had_dinner = True
        
    else:
    
        # Calculate camp and player food combined
        
        total_food = 0 + camp.food

        for player in players:
            total_food += player.food
            
        if total_food >= num_players_alive:
            
            # Camp and player food combined is sufficient
            
            for player in players:
                    if player.food <= 0:
                        
                        camp.food -= 1
                        player.had_dinner = True
                    else:
                        print(f'{player.name} consumes food from their personal resources.')
                        player.had_dinner = True
                        player.food -= 1
                        
            """
            Current system has a bias towards players based on their order in list.
            Must improve later to improve which players must give their resources to camp.
            Or challenge with personal weapons.
            """
            
            while camp.food < 0:
                for player in players:
                    if player.food > 0:
                        print(f'{player.name} contributes food to the camp to help everyone eat.')
                        camp.food += 1
                        
            print(f'There is enough food to go round and remaining players consume food.')
            
        else:
            
            # Camp and player food combined in not sufficient
            
            """
            Current system has a bias towards players based on their order in list.
            Must improve later to create random selection of player who gets food.
            Or challenge with personal weapons.
            """

            for player in players:
                if player.food > 0:
                    print(f'{player.name} consumes food from their personal resources.')
                    player.had_dinner = True
                    player.food -= 1
                elif camp.food > 0:
                    print(f'{player.name} is able to grab some of the last food from camp.')
                    player.had_dinner = True
                    camp.food -= 1
                else:
                    print(f'{player.name} does not grab the camp food in time and suffers illness.')
                    player.had_dinner = False
                    injury(player,1)
         
        
        
    print(f'The event roll for the night is a {roll}!')
    
    if roll == 1:
        # Double attack     
    
        print('\nMajor Zombie attack, double numbers!\n')
        
        zombie_attack(camp, players, day_tracker, double=True)
        
    elif roll == 2 or 3:
        # Normal attack
        
        print('\nZombie attack!\n')
        
        zombie_attack(camp, players, day_tracker)
        
    elif roll == 4:
        # Illness
        
        if camp.medicine == 0:
            # Players must suffer 1 health point or use from their own resources
            print('\nIllness breaks out with no medicine at camp.')
            for player in players:
                if player.medicine > 0:
                    player.medicine -= 1
                    print(f'{player.name} uses medicine from their personal resources.')
                else:
                    print(f'{player.name} has no medicine and suffers illness.')
                    injury(player,1)
            print('\n')
        
        elif camp.medicine >= num_players_alive:
            camp.medicine -= num_players_alive
            print('\nIllness breaks out, every player uses medicine from camp.\n')
        else:
            
            # Calculate camp and player medicine combined
                
            total_meds = 0 + camp.medicine

            for player in players:
                total_meds += player.medicine
                
            if total_meds >= num_players_alive:
                
                # Camp and player medicine combined is sufficient
                
                for player in players:
                    if player.medicine <= 0:
                        camp.medicine -= 1
                    else:
                        player.medicine -= 1
                
                """
                Current system has a bias towards players based on their order in list.
                Must improve later to improve which players must give their resources to camp.
                Or challenge with personal weapons.
                """
                
                while camp.medicine < 0:
                    for player in players:
                        if player.medicine > 0:
                            camp.medicine += 1
            
            else:
                
                # Camp and player medicine combined is not sufficient
                
                """
                Current system has a bias towards players based on their order in list.
                Must improve later to create random selection of player who gets medicine.
                Or challenge with personal weapons.
                """
            
                for player in players:
                    if player.medicine > 0:
                        print(f'{player.name} uses medicine from their personal resources.')
                        player.medicine -= 1
                    elif camp.medicine > 0:
                        print(f'{player.name} is able to grab some of the last medicine from camp.')
                        camp.medicine -= 1
                    else:
                        print(f'{player.name} does not grab the camp medicine in time and suffers illness.')
                        injury(player,1)
                                                
    elif roll == 5 or roll == 6:
        
        # Quiet Night
        print('\nThe night goes past without incident.\n')


# # Game Flow

# In[19]:


def the_game():
    
    # 1. INITIALISE GAME

    # Round/Day Tracker

    day_tracker = 1
               
    # Camp
    
    camp.food = 10
    camp.medicine = 2
    camp.weapons = 0
    
    # Players
    
    num_of_human_players = int(input('How many human players?'))
    
    print('\n')

    # Create players
    if num_of_human_players:
        player1 = Player(input('Player Name?'),computer=False)
        num_of_human_players -= 1
    else:
        player1 = Player(generate_name())
    starting_players.append(player1)
    players.append(player1)

    if num_of_human_players:
        player2 = Player(input('Player Name?'),computer=False)
        num_of_human_players -= 1
    else:
        player2 = Player(generate_name())
    starting_players.append(player2)
    players.append(player2)

    if num_of_human_players:
        player3 = Player(input('Player Name?'),computer=False)
        num_of_human_players -= 1
    else:
        player3 = Player(generate_name())
    starting_players.append(player3)
    players.append(player3)

    if num_of_human_players:
        player4 = Player(input('Player Name?'),computer=False)
        num_of_human_players -= 1
    else:
        player4 = Player(generate_name())
    starting_players.append(player4)
    players.append(player4)

    # Locations
    
    random.shuffle(locations)
    
    for location in locations[:4]:
        location.difficulty = 0
        
    for location in locations[4:-4]:
        location.difficulty = 1
        
    for location in locations[-4:]:
        location.difficulty = 2
          
    # 2. GAME LOOP
    
    playing = True
    
    while playing:
        
        game_state(day_tracker)
    
        # Stage 1 - Choose Missions
        
        print('\nSTAGE 1: CHOOSE A MISSION\n')
        
        location_dict = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[]}
        
        for player in players:
            if player.computer == False:
                print(f'{player.name}, where do you want to go?')
                selection = int(input('Pick a location: 0 to 11'))
                location_dict[selection].append(player)
                print(f'{player.name} chooses to go to {locations[selection].name}')
            else:
                # For now picks a random location
                picking_location = True
                while picking_location:
                    selection = random.randint(0,11)
                    if locations[selection].empty == False:
                        location_dict[selection].append(player)
                        print(f'{player.name} chooses to go to {locations[selection].name}')
                        break
        
        input('Continue?')
        
        # Stage 2 - Missions
        
        print('\nSTAGE 2: MISSIONS\n')
        
        for index in location_dict:
            if location_dict[index] != []:
                mission(location_dict[index], locations[index], camp)
        
        # Stage 3 - Allocate Resources
        
        print('\nSTAGE 3: ALLOCATE RESOURCES\n')
        
        for player in players:
            if player.computer == False:
                print(f'{player.name}, how much of these resources do you want to give to camp?')
                food = int(input('Food:'))
                medicine = int(input('Medicine:'))
                weapons = int(input('Weapons:'))
                player.food -= food
                camp.food += food
                player.medicine -= medicine
                camp.medicine += medicine
                player.weapons -= weapons
                camp.weapons += weapons
            else:
                pass
        
        input('Continue?')             
        
        # Stage 4 - End of Day
        
        print('\nSTAGE 4: NIGHT\n')
        
        end_of_day(camp, players, day_tracker)
        
        day_tracker += 1
        
        if day_tracker > 10:
            
            playing = False
        
        input('Continue?')
        
    # 3. END GAME
    
    for player in players:
        print(f'Congrats {player.name}, you won!')
       


# In[20]:


the_game()


# In[ ]:




