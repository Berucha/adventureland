import time

class Chocolate:
    def __init__(self, life):
        '''
        returns print statements based on the user's input (ounces of chocolate)
        and adds or takes away life points accordingly
        '''

        #testing purposes:
        # print('''In this minigame, the user chooses how much chocolate the user desires to eat.
        # If the user chooses too much chocolate: bad choice!
        # The user will receive a message saying:
        # You ate way too many chocolates and now have diabetes, you loose life points.
        # If the user chooses too little: bad!
        # The user will receive a message saying:
        # You have not eaten enough to sustain your body's nutrients, you loose life points.
        # The user must choose just enough to survive. Thus there needs to be
        # parameters in the code to determine this.''')

        # need to have a condition that makes it so a user can only input an integer
        print('')
        print("Gosh, you're starving. Along your journey you discover trees that grow chocolate!") #intro to minigame of chocolate
        self.life = life
        time.sleep(2)
        print()
        while True:
            try:
                self.num_boxes = int(input("How many chocolate boxes you would like?   ")) #asks user to input amount of chocolate
                time.sleep(1.5)
                self.num_lbs = float(input("How many lbs of chocolate in a box?   "))
                break
            except ValueError:
                pass

        self.lbs_choc = self.num_boxes * self.num_lbs
        self.oz_per_lb = 16
        self.oz_choc = self.lbs_choc * self.oz_per_lb

        if self.oz_choc > 500:
            print('')
            print()      #if ounces of chocolate greater than 500 they get diabetes and lose life points
            time.sleep(2)
            print("You ate " + str(self.oz_choc) + " ounces of chocolate!")
            time.sleep(2)
            print()
            print("You ate way too many chocolates and now have diabetes!")
            self.life -= 3
            print()
        elif self.oz_choc < 300: #if less than 300 ounces of chocolate they do not get enough calories and lose life points
            print()
            time.sleep(2)
            print("You ate " + str(self.oz_choc) + " ounces of chocolate!")
            print()
            time.sleep(2)
            print("You have not eaten enough calories to sustain your body!")
            self.life -= 4
            print()
        else:
            print()             #if ounces of chocolate are between 300 and 500 then you gain life points
            time.sleep(2)
            print("You ate " + str(self.oz_choc) + " ounces of chocolate!")
            print()
            time.sleep(2)
            print("You have eaten enough calories to sustain your body. You may continue along Adventureland.")
            self.life += 3
            print()
#
# Chocolate()
#
