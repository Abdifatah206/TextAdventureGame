
import time
import random
from itertools import permutations

yes = ["yes","YES","Y","y","Yes"]
no = ["no","n","N","No","NO"]
directions = ["left", "right", "upward", "downward"]
down = ["d","D",13]

print("Welcome student locker text adventure game:\n")
name = input("What is your name, adventurer?\n")
def encrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher
 
text = input("Create temparory username: ")
s = int(input("Create temparory password numbers only: "))
print("username: ", text)
print("password encryption: ", encrypt(text, s))
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the corner of the student locker boxes.")
print("lets do quick heat up quest, enter number 1-5 to get answer.")



def hex2dec(s):
   
    s = input("enter number:")
    
    print(int(s, 16))
hex2dec(s)


# part one before game questions

def intro():
    answer = ""
    score = 0
    mean = 0
    median = 0
    mode = 0
    

    while answer not in no:
        answer = str(input(" would you like find  locker?"))
        if answer  in yes:
           print("you head to locker directions:")
           print("Get points and win prizes in the lockers ")
           print("please select these direcitons up, down, left and right")
        elif answer in no:
          print("see you next time" " " + name + ".")
          exit()
        else: 
              print("I didn't understand that.\n")
        def bubsort(randlist):
          for find in range (len(randlist)-1,0,-1):  
            for i in range(find):
              if randlist[i] > randlist[i+1]:
                randlist[i],randlist[i+1] = randlist[i+1],randlist[i]
        a = ('L1','L2','L3','L4','L5','L6')
        randlist = [i for i in (a)]
        print("Quick view of all locker before start in random way.")

        from random import shuffle
        shuffle(randlist)
        print(randlist)#
        bubsort(randlist);
  
                



#part two  start game
##****************** locker one *************************#
        L1 = ""        
        while L1 not in directions:          
          L1 = str(input("what direction do you want move?"))
          if L1 != "up":
            score += 0         
            print("locker exit, good bye " + name + ".")           
          elif L1 == "up":
            score += 10
            print("Oops you are at locker one, one down"" "   + name + ".",score, "points")                 
          else:
            print("I didn't understand that.\n")
  #******************locker two *********************#
          if L1 == "up":           
            L2 = str(input("what direction do you want move for next locker?"))
            if L2 != "right":
                score -= 5
                print("locker exit" + name + ".", score)
                print ("\nYou're finished, " + name +". You got", score, "points." )                    
            elif L2 == "right":
                score += 10
                print("Oops you are at locker 2, two down" " " + name + ".",score, "points")       
            else:
                print("I didn't understand that.\n")
          
 #******************* locker three ********************#   
            if L2 == "right":           
              L3 = str(input("what direction do you want move for next locker?"))
              if L3 != "up":
                  score -= 5
                  print("locker exit" + name + ".", score)
                  print ("\nYou're finished, " + name +". You got", score, "points." )                  
              elif L3 == "up":
                  score += 15
                  print("Oops you are at locker 2, two down" " " + name + ".",score, "points")       
              else:
                  print("I didn't understand that.\n")
#************************** locker four ********************#
              if L3 == "up":               
                L4 = str(input("what direction do you want move for next locker?"))
                if L4 != "right":
                    score -= 5
                    print("locker exit" + name + ".", score)
                    print ("\nYou're finished, " + name +". You got", score, "points.")                 
                elif L4 == "right":
                    score += 15
                    print("Oops you are at locker four, four down" " " + name + ".",score, "points")          
                else:
                    print("I didn't understand that.\n")
  #************************** locker five ********************#
                if L4 == "right":
                  while True:
                    print("Lets play lottery to win 50 points")
                    print("your chance is 2/6 to win")
                    input("Press any key to roll dice:")
                    rolled_num = random.randint(1,6)
                    if rolled_num == 6:
                      print( "congratulation you got " " " + name + ".",score, "points" )
                      print("success")
                    elif rolled_num == 5:
                      print("congratulation you got " " " + name + ".",score, "points"  )                    
                    else:
                      print("fail")
                    print("The dice rolled and you got: ", rolled_num)
                    L5 = str(input("what direction do you want move for next locker?"))
                    if L5 != "down":
                        score -= 10
                        print("locker exit" + name + ".", score)
                        print ("\nYou're finished, " + name +". You got", score, "points.")
                              
                    elif L5 == "down":
                        score += 20
                        print("Oops you are at locker five, two down" " " + name + ".",score, "points")            
                    else:
                        print("I didn't understand that.\n")
    #************************** locker six ********************#

                    if L5 == "down":
                      print("let find code of the golden gate before reach master locker")
                      A = input("Enter number:")
                      B = list(permutations(A))                    
                      if B == ('2', '0', '6'):
                        print("success")
                        score += 50
                      else:
                        print("fail")
                      L6 = str(input("what direction do you want move for next locker?"))
                      if L6 != "right":
                          score -= 10
                          print("locker exit" + name + ".", score)
                          print ("\nYou're finished, " + name +". You got", score, "points.")              
                      elif L6 == "right":
                          score += 30 
                          mean = score/6
                          
                          #mode = 6 ÷ 2                            
                          print("Oops you are at locker six, six down" " " + name + ".",score, "points")
                          print( " your average score per locker is:" "", + mean )
                          if score >= 120:
                            print("you get good score to play ")
                            an = input('Would you like to play again?')
                            if an == 'yes':
                                return intro()
                            else:
                                print ('Thanks for playing!')
                                exit()               
                                  
                      else:
                          print("I didn't understand that.\n")


intro();
 







 


  






