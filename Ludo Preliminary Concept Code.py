
# coding: utf-8

# In[23]:


#Class - player 
#Class - Play


#have 1 super - ultra - mega - super long map 0-58, 59-117, 118-176, 177-235
#each color rotation is 58
#each map has 54 --> "b/g/r/y" + [1,2,3,4,5,6]
#Map needs to support collisions (kills) (Do only after you get a working build)

#Player take turns
#


#------------------------------------------------------------------------------------------------------------------











import numpy as num
from IPython.display import clear_output


class Player:
    def __init__(self,name,color,position):
        self.name = name
        self.color = color
        self.position = position
        self.outside = False
        
        
        
        
        
class Map:
    def __init__(self):
        self.map = {}
        
    def CreateMap(self):
        colorTile = ["red","green","blue"]
        
        for i in range(40):
            for j in range(3):
                if (j == 0):
                    self.map[i] = ["position " + str(i), colorTile[0]]
                    break
                elif (j == 1):
                    self.map[i] = ["position "+ str(i), colorTile[1]]
                    break
                else:
                    self.map[i] = ["position "+ str(i), colorTile[2]]
                    break
            
player1 = Player("Derek", "red",0)
player2 = Player("Jing", "blue",5)
player3 = Player("Rafay", "green",10)

worldMap = Map()

worldMap.CreateMap()





print(worldMap.map)



class Play:
    def __init__(self):
        None
    
    def RollDiceToBeginMovement(self,player):
        player.outside = True
    
    def RollDiceForMovement(self):
        diceRoll = num.random.randint(1,7)
        return diceRoll
    
    def ReturnPositionAfterDiceRoll(self,diceRoll,player):
        #player is the playerObject
        player.position += diceRoll
        
        
    def play(self,mapObject,player):
        #player refers to the player object
        #MapObject refers to the object for the gameboard! use with .map for the gameboard dictionary!
        
        try:
            diceRoll = self.RollDiceForMovement()
            print(player.name + " for " + player.color + " team is on" + " " + mapObject.map[player.position][0])

            
            if (player.outside):
                self.ReturnPositionAfterDiceRoll(diceRoll,player)
                print("you rolled " + str(diceRoll) + " and your position is " + mapObject.map[player.position][0])
                return " "
            
            if(not player.outside and diceRoll == 6):
                self.RollDiceToBeginMovement(player)
                player.position = 1
                
            
            
            print("you rolled " + str(diceRoll) + " and your position is " + mapObject.map[player.position][0])
            return " "
        except KeyError:
            return "win"
            
            #self.position = 1
            
            #return " "
        
        
Game = Play()
playerOutcome = ""
counter = 1
while True:
    
    playerInput = input()
    
    if (str.lower(playerInput) == 'quit'):
        break
        
    elif (str.lower(playerOutcome) == "win"):
        print("you have reached the last tile, you win")
        break
    else:
        
        if (counter %3 == 1):
            playerOutcome = Game.play(worldMap,player1)
            counter +=1
        elif (counter%3 == 2):
            playerOutcome = Game.play(worldMap,player2)
            counter +=1
        else:
            playerOutcome = Game.play(worldMap,player3)
            counter +=1

        


# In[ ]:




