import random

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

if answ_game_1=='right'or answ_game_1=='left':
   print('Ok you are moving')
else:
    print('Invalid input.Try again',answ_game_1)

#first room
if 'right' in dictionary_action.values():
   dictionary_action.update({'woods':'1'})
   print('You meet an animal.','Do you want to escape or fight it?')
if 'left'  in dictionary_action.values():
    print('You are lost.You loose game.')
    quit()
    

def fourroom():
 if 'river' in dictionary_action.keys():
     print('It is the last room.Game well!')
     print('You are safe.You are next home.But you have a last mission.You have to guess this question.How many years do you have if you lives in 2070?')
     question_1=input('In which year you are born:')
     question_2=int(input('Enter your answer:'))
     age=2070-int(question_1)
     print(age)
     if age==question_2:
        print('You guess the game.You are at home.Goodbye!')
        dictionary_action.update({'home':'4'})
        print(dictionary_action)
     else:
          print('You loose game')
        

    
#threeroom   
def three_room():
 answer_3=input('Take three steps and write them down(left,right,back,fowards)')
 if answer_3=='left':
    print('Stop!You are facing a wall')
    dictionary_action.update({'wall':'3'})
 elif answer_3=='right':
      print('You have found a clue to the rebus that will lead you home.It is a secret formula from an ancient witch who lived in the woods and you have two letters ap.')
      print('Ok you have reached the river.')
      dictionary_action.update({'river':'3'})
      fourroom()
 elif answer_3=='back':
      print('Stop!You can not go back')
      key_game()
 else:
      print('Keep walking',answer_3)
    
