import time
class Even_Odd:
    def __init__(self, life):
        '''
        returns print statements based on the user's input (favorite number)
        and adds or takes away life points accordingly
        '''

        #testing purposes:
        # print('''In this mini game, the user is told a story in which the user will
        # be prompted to choose a number.
        # Even number choice: bad! Loose life points
        # Odd number choice: good! Gain life points''')


        print('')
        self.life = life
        while True:
            try:
                time.sleep(2)
                self.fav_num = float(input("What is your favorite number?   "))   #asks user to input their favorite number
                break
            except ValueError:
                pass

        if self.fav_num % 2 == 1 and self.fav_num <= 20:
            time.sleep(1.75)
            print()                       #if number odd and less than 20 then it is a good choice and gain life points
            print("That's my favorite too! Hooray!")
            self.life += 3
        else:
            time.sleep(1.75)           #if the number is even or odd but greater than 20 then bad choice and lose life points
            print()
            print('Ew. That number has bad mojo.')
            self.life -= 4
# Even_Odd()
