import random

from datetime import datetime

print('Welcome to new game','I will tell you which room you are in. You will have four missions to complete to find your way home.Two only way are correct.')
answer_1=input('Do you want to game?')

def tempt():
    global user
    user=input('Enter action:')
    user_1=input('Enter pass:')
    global dictionary_action
    dictionary_action={}
    dictionary_action.update({user_1:user})
    
def tempt_0():
    user_0=input('Enter action:')
    user_00=input('Enter pass:')
    dictionary_action.update({user_00:user_0})
    
    
def key_game():
 key='4'
 if answer_1=='yes':
    print('You are in the woods.Follow me.')
 else:
    print('Game stop')
    exit()
    
key_game()

answ_game_1=input('The are two paths.One to the right and one to the left.Which do you choose?\n')
tempt()

if answ_game_1=='right' or answ_game_1=='left':
   print('Ok you are moving')
else:
    print('Invalid input.Try again',answ_game_1)

#first room
if 'right' in dictionary_action.values():
   dictionary_action.update({'woods':'1'})
   print('You meet an animal.','Do you want to escape or fight it?')
if 'left'  in dictionary_action.values():
    print('You are lost.Use the compass.Try again.',answ_game_1)

    
#threeroom   
def three_room():
 answer_3=input('Take three steps and write them down(left,right,back,fowards)')
 if answer_3=='left':
    print('Stop!You are facing a wall',answer_3)
    dictionary_action.update({'wall':'3'})
 elif answer_3=='right':
      print('You have found a clue to the rebus that will lead you home.It is a secret formula from an ancient witch who lived in the woods and you have two letters ap.')
      print('Ok you have reached the river.')
      dictionary_action.update({'river':'3'})
 elif answer_3=='back':
      print('Stop!You can not go back')
      key_game()
 else:
      print('Keep walking',answer_3)

    
#guesstheword

def word_guess():
 secret_word='delphin'
 secret_dict={}
 for secret in range(10):
     user=input('\n Enter your letter:')
     print('You have 10 attempts.')
     if user in secret_word:
        print('The letter is correct.')
        index=secret_word.find(user)
        secret_dict.update({index:user})
        dict_new=sorted(secret_dict.items())
        print(dict_new)
        for k in sorted(secret_dict):
            list_1=secret_dict[k]
            print('-',end="")
            for tratt in list_1:
                if user in list_1:
                   fuc=list_1.replace('-',user)
                   print(fuc)
                   if len(dict_new)==len(secret_word):
                      print('You guess','The word is',secret_word)
                      dictionary_action.update({'word':'4'})
                      three_room()
                      break
                   
     if user not in secret_word:
        print('The letter is not correct.Try again.')
     if secret==10:
        print('You loose game.')
        break

#guessmathproblem

def math_problem():
    print('Guess the math problem.Find a number between 1 and 10')
    global number 
    number=random.randint(1,10)
    print(number)
    for i in range(5):
        global answer_number
        answer_number=int(input('Enter number:'))
        if answer_number==number:
           print('You guessed.You can pass to the next mission')
           print('Good adventurer! You have passed the second mission but the way back home is still long.You are still in the woods but you are thirsty and nee to find a river')
           three_room()
           break
        else:
           print('Try again',answer_number)
        if i==5:
           print('You loose game.')
           break
       
def letter():
    print('Write a letter which has 7 letters.It has two wovels.')
    secret_secret='company'
    for letter_1 in range(7):
        game=input('Enter letter:')
        wovel=['a','e','i','o','u']
        if len(game)==7:
           print('Ok go on.')
        for wovel_vowel in wovel:
            if wovel_vowel in enumerate(game):
               finder=game.find(wovel_vowel)
               if finder=='o' or finder=='a':
                  print('Ok it is correct.Go on.')
        else:
            print('Try again')
        if game==secret_secret:
           print('You guess')
           dictionary_action.update({'letter':'2'})
           three_room()
           break
       
                  
    

#second room
tempt_0()

if 'fight' in dictionary_action.values():
    dictionary_action.update({'swamp':'2'})
    print('You are in a swamp and you have other mission.','The swamp is full of sharks.')
    print('Do you want to go back,forward,the narrow or the right?(Please write as the question)')
    direction=input('Enter answer:')
    if direction=='back':
       print('You can not go back')
       key_game()
    elif direction=='forward':
        print('You are trapped in branches and you can only save yourself if you guess the word right')
        print('Guess the word.It is an animal who lives in puddle')
        word_guess()
    elif direction=='the narrow':
        print('You can not go by the narrow.The road is blocked')
    elif direction=='the right':
        dictionary_action.update({'puddle':'5'})
        print('You fell into a puddle and to get out you solve the math problem.')
        math_problem()
    else:
        print('Invalid input',direction)
        exit()
if 'escape' in dictionary_action.values():
    dictionary_action.update({'escape':'2'})
    letter()

print('Your path is',dictionary_action)


#fourroom
#use fuction sopra


if 'river' in dictionary_action:
    print('It is the last room.Game well!')
    print('You are safe.You are next home.But you have a last mission.You have to guess this question.How many years do you have if you lives in 2070?')
    question_1=int(input('In which year you are born:'))
    time=datetime.today().strftime('%Y-%m-%d')
    time_1="".join(time)
    time_2=time_1[0:4]
    age=int(time_2)-question_1
    question_2=int('Enter your answer:')
    if question_2==age:
       print('Oh you guessed.You have to cross the river.')
       question_3=input('What you use to cross?(raft,tree,swim)')
       if question_3=='raft':
          print('You guess the game.You are at home.Goodbye!')
          dictionary_action.update({'home':'4'})
       elif question_3=='tree':
            print('You loose game')
       elif question_3=='swim':
            print('You died drowned')
       else:
            print('Invalid input',question_3)
        
elif 'word' in dictionary_action:
    print('It is the last room.Game well!')
    print('You have to croos the rickety bridge.What year was thr discovery of America?')
    question_4=input('Enter year:')
    dictionary_action.update({'bridge':'6'})
    if question_4=='1492':
       print('You guess.You are at home.')
    else:
        print('Try again',question_4)
elif 'swamp' in dictionary_action:
    print('You loose game.Goodbye.')
    exit()
    
print('Your path is',dictionary_action)




















