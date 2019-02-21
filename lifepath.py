import time
import datetime


class Life_Path:
    def __init__(self, life):
        '''
        returns print statements based on the user's input (birth information)
        and adds or takes away life points accordingly
        '''

        #testing purposes:
        # print(''' This minigame tells a story about walking down the path of life
        #  and asks the user's birth day (month, day, and year).
        #  If the user's birth day generates a master number the user advances and gains life points.
        #  Otherwise, the user's path of life is horrible, full of stress, and the user loses detrimental life points.
        #  The number of life points the user loses is based off of the number that is generated from
        #  the user's birthday.''')

        print('')
        self.life = life
        print("You are walking down the path of Life. When did you begin your journey down this path?   ")
        time.sleep(2)
        print()


        while True:
            try:
                self.useryr = int(input("Enter the year you were born in. [Integer only please]   "))
                print()
                self.usermonth = int(input("Enter the month you were born in. [Integer only please]   "))
                print()
                self.userbday = int(input("Enter the day you were born on. [Integer only please]   "))
                datetime.date(self.useryr, self.usermonth, self.userbday)
                break
            except ValueError:
                print()
                print("Invalid input. Please try again!")

        self.convert_month()
        self.convert_day()
        self.convert_yr()
        self.life_num()
        self.inform()

    def convert_month(self):
        '''
        evaluates if month is divisible by 11 and adds it to a list
        :param self: object of life path class
        :return: none
        '''

        if int(self.usermonth) % 11 == 0 and int(self.usermonth) != 0 and int(
                self.usermonth) <= 33:  # if month is divisible by 11 just keep it as is
            return (self.usermonth)
        else:
            self.tot_sum = 0
            self.usermonth = str(self.usermonth)
            for i in self.usermonth:  # if not divisible by 11 put number into list/string and return it into list
                self.tot_sum = self.tot_sum + int(i)  # Converts to string to utilize Python's strong string features
            return (self.tot_sum)  # adds numbers from list together

    def convert_day(self):
        '''
        evaluates if month is divisible by 11 and  less than or equal to 33
        and adds it to a list
        :param self: object of life path class
        :return: none
        '''
        if self.userbday % 11 == 0 and self.userbday != 0 and self.userbday <= 33:  # if day number is divisble by 11 just keep birth num up
            return (self.userbday)
        else:
            self.userbday = str(self.userbday)  # Converts to string to utilize Python's strong string features
            self.tot_sum = 0
            for i in self.userbday:  # if not divisible by 11 put number into list/string and reutrn it into list
                self.tot_sum += int(i)
            if len(str(self.tot_sum)) > 1:  # if the length of number is more than one digit it will repeat process
                self.tot_sum2 = 0
                for j in str(self.tot_sum):
                    self.tot_sum2 += int(j)
                    return (self.tot_sum2)  # adds numbers from list together
            else:
                return (self.tot_sum)

    def convert_yr(self):
        '''
        adds year to a list
        :param self: object of life path class
        :return:none
        '''
        self.useryr = str(self.useryr)  # Converts to string to utilize Python's strong string features
        self.tot_sum = 0
        for i in self.useryr:  # puts number into a list/string
            self.tot_sum += int(i)
        if len(str(self.tot_sum)) > 1:  # if the length of number is more than one digit it will repeat process
            self.tot_sum2 = 0
            for j in str(self.tot_sum):
                self.tot_sum2 += int(j)
            return (self.tot_sum2)  # adds the numbers from the list together
        else:
            return (self.tot_sum)

    def life_num(self):
        '''
        determines the life path number based on the information given above
        :param self: object of life path class
        :return: none
        '''
        self.final_sum = int(self.usermonth) + int(self.userbday) + int(
            self.useryr)  # adds number from the month fucntion, day, function, and year function together
        if self.final_sum % 11 == 0 and self.final_sum != 0 and self.final_sum <= 33:
            return (self.final_sum)  # this would return a master number
        else:
            self.tot_sum = 0
            for i in str(self.final_sum):
                self.tot_sum += int(i)
            return (self.tot_sum)  # would return the life path number

    def inform(self):
        '''
        returns print statement based off of the user's determined life path number
        :param self: object of life path class
        :return: none
        '''
        if self.life_num() % 11 == 0 and self.life_num() != 0 and self.life_num() <= 33:
            print('')
            print('''Master Number''', self.life_num(), '''!! This number suggests that you have skills that allow you to be a natural leader.
Your nature is charged with individualistic desires, a demand for independence, and need for personal attainment. 
Your mind is capable of significant creative inspiration. You are destined to accomplish a great deal! ''')
            self.life += 4               #if user's life path number is a master number then gain life points
            time.sleep(0.75)
            print("Go you!")
            time.sleep(4)
            print()
        else:
            print('')                      #if the user's life path number is not a master number thenn they will lose life points
            time.sleep(1.75)
            print("Life Path Number", self.life_num(), '''suggests that your path is horrible, full of stress, 
and you lose detrimental life points!''')
            print()
            time.sleep(1.75)
            print("So sad :(")
            self.life -= 5
            print()

# def main():
#     Life_Path()
# main()
