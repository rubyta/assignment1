#Source file name: dragon.py
#Author: Rubyta Herwinda
#Last Modified by: Rubyta Herwinda
#Date: Monday 20, 2013
#Date last Modified: Thursday 23, 2013
#Purpose: taking guess number from the player

#Revision history: May 19, 2013 Make string array right and left for player direction decision'
#                  May 20, 2013 Changing string array to random number as split roads
#                               Adding another funcion that show the result of their journey
#                  May 21, 2013 Try to figure out the loop problem and global/local variable
#                  May 22, 2013 Try to add another function inside a function
#                  May 23, 2013 Try to use simple loop and passing values

import random
import time

def displayIntro():
        print ('You are on a planet full of dragons. In front of you,')
        print ('you see two caves. In one cave, the dragon in friendly')
        print ('and will share his treasure with you. The other dragon')
        print ('is greedy and hungry, and will eat you on sight.')

def chooseCave():
        #player choose the cave number
        cave = ''
        while cave != '1' and cave != '2':
                print ('Which cave will you go into?(1 or 2)')
                cave = raw_input()
        return cave

def checkCave(chosenCave):

        #function for player that choose first cave
        #def firstCave():
        #    if friendlyCave == 1:
        #        print('which way you want to choose? (1 or 2)')
        #        way = raw_input()
        #        return way
        #    else:
        #        print('suddenly cave number 1 blocked! left you no choice.')

        #function for player that choose second cave
        #def secondCave():
        #    if friendlyCave == 1:
        #        print('where is the best road to go? (3 or 4)')
        #        turn = raw_input()
        #        return turn
        #    else:
        #        print('Wind push you to the road number 3')

        #string array for turn direction
        #way = ['right', 'left']

        print ('On your way to the cave...')
        time.sleep(2)
        print ('It is dark and spooky...')
        time.sleep(2)
        print ('There is a split road in front of you.')
        print ('What would that be? ...')
        print
        time.sleep(2)

        friendlyCave = random.randint(1,2)

        #match the player number with available number
        if chosenCave == str(friendlyCave):
            #firstCave()
            #ask player to choose a split road between 1 and 2
            friendlyCave = raw_input('which way you want to choose? (1 or 2) :')
            friendlyCave = friendlyCave.isdigit()
            #return friendlyCave
        else:
            #secondCave()
            #ask player to choose a split road between 3 and 4
            print ('where is the best road to go? (3 or 4)')
            turn = raw_input()
            turn = turn.isdigit()
        
def checkSplit(chosenSplit):

         #adding 4 functions for the result after player choose a split road
         
         #def firstSplit():
         #   if trueRoad == 1:
         #       print ('The blue dragon open his mouth and you got the treasure')
         #   else:
         #       print ('Are you sure this is the right treasure? Seems fake')


         #def secondSplit():
         #   if trueRoad == 2:
         #       print ('Just missed one cave. Now you have to play with Red dragon.')
         #   else:
         #       print ('Dont make Red dragon upset! Just play with Red dragon.')

         #def thirdSplit():
         #   if trueRoad == 3:
         #       print ('The Yellow dragon put you in the cage!')
         #   else:
         #       print ('The Yellow dragon trick you to go inside the cage.')

         #def fourthSplit():
         #    if trueRoad == 4:
         #        print ('The black dragon threaten you and ate you')
         #    else:
         #        print ('The black dragon fired you like BBQ and ate you.')

         #single function with simple loop of results
         def randSplit():
              if trueRoad == 1:
                 print ('The blue dragon open his mouth and you got the treasure!')
              elif trueRoad == 2:
                 print ('The red dragon lick you as his treat!')
              elif trueRoad == 3:
                 print ('The yellow dragon put you in the cage!')
              else:
                 print ('The black dragon fired you like BBQ and ate you!')                             

         print ('You have a long walk that never ends..')
         time.sleep(2)
         print ('You feel thirsty along the way..')
         time.sleep(2)
         print ('Until you found another cave that seems occupied..')
         print
         time.sleep(2)

         #assign random number between 1 and 4
         trueRoad = random.randint(1,4)

         #match between player input to number 1 to 4
         if chosenSplit == 1:
         #    print ('Arrive in the end of first split..')
             randSplit()
         elif chosenSplit == 2:
         #    print ('Arrive in the end of second split..')
             randSplit()
         elif chosenSplit == 3:
         #    print ('Arrive in the end of third split..')
             randSplit()
         else:
         #    print ('Arrive in the end of fourth split..')
             randSplit()
             

def main():

        playAgain = 'yes'
        while playAgain == 'yes' or playAgain == 'y':
                displayIntro()
                #get cave number
                caveNumber = chooseCave()
                #get road split number 
                checkCave(caveNumber)
                #return the result of split road number
                checkSplit(checkCave) 
                print ('Do you want to play again? (yes or no)')
                playAgain = raw_input()

if __name__ == "__main__": main()
                
