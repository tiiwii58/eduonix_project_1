import random

def input_number():
    try:
        number_choose = input('Select a random number between 1 - 25 : ')
        number_choose = int(number_choose)
        
        if(number_choose > 25 or number_choose < 1):
           raise ValueError('You didn\'t select a number between 1 and 25')
        
        return number_choose
    except Exception as e:
        print(e)
        return input_number()
    except:
        print('You must enter a number')
        return input_number()

games = input('How many games you want to play ? ')
games = int(games)

for x in range(games):
    print('Game %d'% (x+1))
    
    secret_number = random.randint(1,26)
    
    number_choose = input_number()
    
    counter = 1
    while number_choose != secret_number:
        counter += 1
        if number_choose > secret_number:
            print('Too high !')
        else:
            print('Too low !')
        number_choose = input_number()
        
    print('You win in %d turns\n' % counter)
    
print('End of games')
