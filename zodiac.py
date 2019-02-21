import time
class Zodiac:
    def __init__(self, life):
        '''
        returns print statements based on the user's input (phone number)
        and adds or takes away life points accordingly
        '''

        #testing purposes:
        # print('''In this minigame, the user is given an animal based off of the user's
        # birth year (or something else, still figuring it out).
        # If the animal is apart of the bad animal list:
        # The animal does something bad to the user and the user loses life points
        # Otherwise:
        # The animal grants the user life points''')

        print('')
        self.life = life
        self.birthyr()
        self.useranimal()
        self.result()

    def birthyr(self):
        '''
        asks for user's last 4 phone number digits
        :param self: object of the zodiac class
        :return: none
        '''
        while True:
            try:
                self.birth_year = int(float(input("Enter the last four digits of your phone number (i.e., 3496)   ")))
                break
            except ValueError:  #user inputs phone nubmer and a zodiac sign will be given to them
                pass

    def useranimal(self):
        '''
        evaluates the user's input and assigns the them an animal
        :param self: object of the zodiac class
        :return: none
        '''
        print('')
        if self.birth_year % 12 == 0:
            self.animal = "Monkey"
            print("Your animal is the", self.animal, "!")
            time.sleep(1.5)
        elif self.birth_year % 12 == 1:
            self.animal = "Rooster"               #all the different animal scenarios
            print("Your animal is the", self.animal, "!")
            time.sleep(1.5)
        elif self.birth_year % 12 == 2:
            self.animal = "Dog"
            print("Your animal is the", self.animal, "!")
            time.sleep(1.5)
        elif self.birth_year % 12 == 3:
            self.animal = "Pig"
            print("Your animal is the", self.animal, "!")
            time.sleep(1.5)
        elif self.birth_year % 12 == 4:
            self.animal = "Rat"
            print("Your animal is the", self.animal, "!")
            time.sleep(1.5)
        elif self.birth_year % 12 == 5:
            self.animal = "Ox"
            print("Your animal is the", self.animal, "!")
            time.sleep(1.5)
        elif self.birth_year % 12 == 6:
            self.animal = "Tiger"
            print("Your animal is the", self.animal, "!")
            time.sleep(1.5)
        elif self.birth_year % 12 == 7:
            self.animal = "Rabbit"
            print("Your animal is the", self.animal, "!")
            time.sleep(1.5)
        elif self.birth_year % 12 == 8:
            self.animal = "Dragon"
            print("Your animal is the", self.animal, "!")
            time.sleep(1.5)
        elif self.birth_year % 12 == 9:
            self.animal = "Snake"
            print("Your animal is the", self.animal, "!")
            time.sleep(1.5)
        elif self.birth_year % 12 == 10:
            self.animal = "Horse"
            print("Your animal is the", self.animal, "!")
            time.sleep(1.5)
        elif self.birth_year % 12 == 11:
            self.animal = "Goat"
            print("Your animal is the", self.animal, "!")
            time.sleep(1.5)

    def result(self):
        '''
        returns the result
        :param self: object of the zodiac class
        :return: none
        '''
        if self.animal == "Monkey" or self.animal == "Snake" or self.animal == "Ox" or \
                self.animal == "Tiger" or self.animal == "Dragon" or self.animal == "Horse":   #all the bad choices
            print()
            time.sleep(2)
            print("Oh no! Your ", self.animal, " attacks you!")
            self.life -= 3
        else:
            print()
            print("Yayyy! Your ", self.animal, ''' licks your face, granting you life points and   
allowing you to advance along your journey through Adventureland.''')  #all the good choices
            self.life += 2


