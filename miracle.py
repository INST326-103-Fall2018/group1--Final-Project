#Miracle Agyapong

import time
import random
import smtplib


    #Class of moods
class Moods:
    # function reads random line from file and returns the line
    def happy(self):
        lines = open("/Users/miry/Downloads/happy1.txt").read().splitlines()
        line = random.choice(lines)
        return line

    # function reads random line from file and returns the line
    def sad(self):
        lines = open("/Users/miry/Documents/sad1.txt").read().splitlines()
        line = random.choice(lines)
        return line

    # function reads random line from file and returns the line
    def anxious(self):
        lines = open("/Users/miry/Documents/anxious.txt").read().splitlines()
        line = random.choice(lines)
        return line

    # function reads random line from file and returns the line
    def upset(self):
        lines = open("/Users/miry/Documents/upset.txt").read().splitlines()
        line = random.choice(lines)
        return line

    # function reads random line from file and returns the line
    def annoyed(self):
        lines = open("/Users/miry/Documents/annoyed.txt").read().splitlines()
        line = random.choice(lines)
        return line

def main():
    #Prints welcome message with current time
        print("*************************************************")
        print("Hello!" +'\n'
              "Welcome to Affirm Now")
        print(time.strftime("The Current Time is: %H:%M:%S"))
        print("How are you feeling today?"+'\n')

    #Prints message to gets users' mood
        print("Please enter the number that best describes your current emotion "
          "1= Happy,"
          "2= Sad, "
          "3= Anxious, "
          "4= Upset, "
          "5= Annoyed,"
          "6= Calm")

    #Global variable
        global mood
    #While true...
        while True:
            try:
                #
                mood = float(input("Please enter your mood:"))
                if mood==1 or mood==2 or mood==3 or mood==4 or mood==5:
                    break
            except:
                #
                print("Please enter one of the numbers")
                continue
        moodsInst = Moods()

    #If user enters 1 for happy, print affirmation
        if mood==1:
            print(moodsInst.happy())
            #Ask user if they want to add affirmations to file for happy
            affirm = int(input("Do you want to add any affirmations: Enter 1 for "
                               "'Yes', Enter any other digit for 'No"))

            #If user enters 'yes', open text file
            if affirm==1:
                filename = "/Users/miry/Downloads/happy1.txt"
                file = open(filename, 'a')
                #Ask user how many affirmations they want to add
                numOfAffirm = int(input("How many affirmations"))
                #Lets users manually add the amount of affirmations they want
                for i in range(0, numOfAffirm):
                    name = input("Enter a new affirmation:")
                    #Add to file
                    file.write(name + "\n")
                    #Close file and go to "exit" function
                file.close()
                exitForHappy()
                # Send goodbye message w/ information
            elif affirm==2:
                #
                exitForHappy()
                emailSend = int(input("Do you want to add any affirmations: Enter 1 for "
                                   "'Yes', Enter any other digit for 'No"))
                if emailSend==1:
                    email()
                    print("Message sent!")
                else:
                    print("Bye!")
        # If user enters 1 for sad, print affirmation
        elif mood==2:
            print(moodsInst.sad())
            #Ask user if they want to add affirmations to file for sad
            affirm = int(input("Do you want to add any affirmations: Enter 1 for "
                               "'Yes', Enter any other digit for 'No"))
            # If user enters 'yes', open text file
            if affirm == 1:
                filename = "/Users/miry/Downloads/sad.txt"
                file = open(filename, 'a')
                # Ask user how many affirmations they want to add
                numOfAffirm = int(input("How many affirmations" ))
                # Lets users manually add the amount of affirmations they want
                for i in range(0, numOfAffirm):
                    name = input("Enter a new affirmation:")
                    # Add to file
                    file.write(name + "\n")
                    # Close file and go to "exit" function
                file.close()
                exitForSad()
                # Send goodbye message w/ information
            else:
                print("Bye!")
                exitForSad()

        # If user enters 3 for anxious, print affirmation
        elif mood==3:
            print(moodsInst.anxious())
            # Ask user if they want to add affirmations to file for anxious
            affirm = int(input("Do you want to add any affirmations: Enter 1 for "
                               "'Yes', Enter any other digit for 'No"))
            # If user enters 'yes', open text file
            if affirm == 1:
                filename = "/Users/miry/Downloads/happy1.txt"
                file = open(filename, 'a')
                # Ask user how many affirmations they want to add
                numOfAffirm = int(input("How many affirmations"))
                # Lets users manually add the amount of affirmations they want
                for i in range(0, numOfAffirm):
                    name = input("Enter a new affirmation:")
                    # Add to file
                    file.write(name + "\n")
                    # Close file and go to "exit" function
                file.close()
                exitForAnxious()
                #Send goodbye message w/ information
            else:
                print("Bye!")
                exitForAnxious()

        # If user enters 4 for upset, print affirmation
        elif mood==4:
            print(moodsInst.upset())
            # Ask user if they want to add affirmations to file for upset
            affirm = int(input("Do you want to add any affirmations: Enter 1 for "
                               "'Yes', Enter any other digit for 'No"))
            # If user enters 'yes', open text file
            if affirm == 1:
                filename = "/Users/miry/Downloads/happy1.txt"
                file = open(filename, 'a')
                # Ask user how many affirmations they want to add
                numOfAffirm = int(input("How many affirmations"))
                # Lets users manually add the amount of affirmations they want
                for i in range(0, numOfAffirm):
                    name = input("Enter a new affirmation:")
                    # Add to file
                    file.write(name + "\n")
                    # Close file and go to "exit" function
                file.close()
                exitForUpset()
                # Send goodbye message w/ information
            else:
                print("Bye!")
                exitForUpset()

    #If user enters 5 for annoyed, print affirmation
        elif mood==5:
            print(moodsInst.annoyed())
            # Ask user if they want to add affirmations to file for annoyed
            affirm = int(input("Do you want to add any affirmations: Enter 1 for "
                               "'Yes', Enter any other digit for 'No"))
            # If user enters 'yes', open text file
            if affirm == 1:
                filename = "/Users/miry/Downloads/happy1.txt"
                file = open(filename, 'a')
                # Ask user how many affirmations they want to add
                numOfAffirm = int(input("How many affirmations"))
                # Lets users manually add the amount of affirmations they want
                for i in range(0, numOfAffirm):
                    # Add to file
                    file.write(name + "\n")
                    # Close file and go to "exit" function
                file.close()
                exitForAnnoyed()
                #Send goodbye message w/ information
            else:
                print("Bye!")
                exitForAnnoyed()

def exitForHappy():
    print("Thank you for coming to Affirm, see you later" + '\n')
    f = open("/Users/miry/Downloads/happy1.txt")
    print(f.read())

def exitForSad():
    print("Thank you for coming to Affirm, see you later" + '\n')
    f = open("/Users/miry/Downloads/happy1.txt")
    print(f.read())

def exitForAnxious():
    print("Thank you for coming to Affirm, see you later" + '\n')
    f = open("/Users/miry/Downloads/happy1.txt")
    print(f.read())

def exitForUpset():
    print("Thank you for coming to Affirm, see you later" + '\n')
    f = open("/Users/miry/Downloads/happy1.txt")
    print(f.read())

def exitForAnnoyed():
    print("Thank you for coming to Affirm, see you later" + '\n')
    f = open("/Users/miry/Downloads/happy1.txt")
    print(f.read())

def email():
    host = "smtp.gmail.com"
    port = 587
    username = "shopatazizi@gmail.com"
    password = "Blessing1"
    from_email = username
    to_list = ["miryland@terpmail.umd.edu"]

    from smtplib import SMTP
    ABC = SMTP(host, port)
    ABC.ehlo()
    ABC.starttls()
    ABC.login(username, password)
    ABC.sendmail(from_email, to_list, "Thank you for using Affirm Now! Have a great day.")
    ABC.quit()


if __name__ == "__main__":
    main()

