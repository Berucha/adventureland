import time

class Places:
    def __init__(self, life):
        '''
        returns print statements based on the user's input (car color)
        and adds or takes away life points accordingly
        '''

        #testing purposes:
        # print('''In this minigame, the user has been walking along to Adventurland.
        # However, the user has stumbled across three cars. This car will take you to a mysterious location!
        # The user must select a car. Which color car do you choose.. Red, Blue, or Green?
        time.sleep(3)
        print('')
        self.life = life
        print("* Some time later *...")   #introduction to the game of places
        time.sleep(2)
        print()
        print('You have been walking through Adventurland trying to reach the castle. It seems forever away.')
        time.sleep(2.75)
        print()
        print("Luckily you have stumbled across three cars. Each car will take you to a mysterious location!")
        self.car_colors()
        time.sleep(2.5)

    def car_colors(self):
        '''
        evaluates which color the user picks and returns the according print statements and life points
        :param self: object of the places class
        :return:none
        '''
        print()
        time.sleep(2)
        self.user_color = input("You must select a car. Which color car do you choose.. Red, Blue, or Green?   ").lower()  #user must select a car

        while self.user_color != ("red") and self.user_color != ("green") and self.user_color != ("blue"):
            self.user_color = (input("You must select a car. Which color car do you choose.. Red, Blue, or Green?   ")).lower()

        if self.user_color == "red":
            print()                  #if user chooses red then it is a bad choice and they lose life points
            time.sleep(1.75)
            print('''Uh-Oh! Your car takes you to the home of a troll who is one of the wicked ruler's minions!
    You are forced to become his prisoner.''')
            self.life -= 3
            print('* 2 years later you escape and continue on with your journey *')
        elif self.user_color == "blue":
            print()    #if user chooses blue then it is a good choice and they gain life points
            time.sleep(1.75)
            print(
                "Yayyy! Your car takes you to the home of the Leaders of the  Adventurer Revolution, where they feed and shelter you for the night.")
            self.life += 2
        elif self.user_color == "green":    #if user chooses green then it is a okay choice and they dont gain life points nor lose them
            print()
            time.sleep(1.75)
            print(
                "Your car takes you to Adventureland's forest and then breaks down, you must continue your journey from here.")

#
# Places()
