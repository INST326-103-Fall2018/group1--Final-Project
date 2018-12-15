# Name: Miracle Agyapong
# Directory ID: miryland
# Date: 2018-12-14
# Assignment: Final Project

import time
import random
import smtplib


# Class of moods
class Moods:
    # function reads random line from file and returns the line
    def happy(self):
        lines = open("/Users/miry/Downloads/happy1.txt").read().splitlines()
        line = random.choice(lines)
        return line

    # function reads random line from file and returns the line
    def sad(self):
        lines = open("/Users/miry/Documents/sadmood.txt").read().splitlines()
        line = random.choice(lines)
        return line

    # function reads random line from file and returns the line
    def anxious(self):
        lines = open("/Users/miry/Downloads/anxiousmood.txt").read().splitlines()
        line = random.choice(lines)
        return line

    # function reads random line from file and returns the line
    def upset(self):
        lines = open("/Users/miry/Downloads/upsetmood.txt").read().splitlines()
        line = random.choice(lines)
        return line

    # function reads random line from file and returns the line
    def annoyed(self):
        lines = open("/Users/miry/Downloads/annoyedmood.txt").read().splitlines()
        line = random.choice(lines)
        return line


def main():
    # Prints welcome message with current time
    print("*************************************************")
    print("Hello!" + '\n'
                     "Welcome to Affirm Now")
    print(time.strftime("The Current Time is: %H:%M:%S"))
    print("How are you feeling today?" + '\n')

    # Prints message to gets users' mood
    print("Please enter the number that best describes your current emotion "
          "1= Happy,"
          "2= Sad, "
          "3= Anxious, "
          "4= Upset, "
          "5= Annoyed,"
          "6= Calm")

    # Global variable
    global mood

    while True:
        try:
            #
            mood = float(input("Please enter your mood:"))
            if mood == 1 or mood == 2 or mood == 3 or mood == 4 or mood == 5:
                break
        except:
            #
            print("Please enter one of the numbers")
            continue
    moodsInst = Moods()

    # If user enters 1 for happy, print affirmation
    if mood == 1:
        print(moodsInst.happy())
        # Ask user if they want to add affirmations to file for happy
        addedAffirm = int(input("Do you want to add any affirmations: Enter 1 for "
                                "'Yes', Enter any other digit for 'No"))

        # If user enters 'yes', open text file
        if addedAffirm == 1:
            filename = "/Users/miry/Downloads/happy1.txt"
            file = open(filename, 'a')
            # Ask user how many affirmations they want to add
            numOfAffirm = int(input("How many affirmations"))
            # Lets users manually add the amount of affirmations they want
            for i in range(0, numOfAffirm):
                name = input("Enter a new affirmation:")
                # Add to file
                file.write(name + "\n")
                # Close file and go to "exitForHappy" function
            file.close()
            exitForHappy()

            # If user enters 'no', go straight to exitForHappy function
        else:
            exitForHappy()
            # Ask user if they want a quote sent to their email
            emailSend = int(input("Do you want a quote also sent to your email?, Enter 1 for 'Yes'"
                                  "or Enter any other digit for 'No"))
            # If user enters '1'...
            if emailSend == 1:
                emailAddress = str(input("What is your email address?"))
                # Go to email function and print message

                email(emailAddress)
                print("Message sent!")
                # If user enters any other key, print message
            else:
                print("Bye!")

    # If user enters 2 for sad, print affirmation
    elif mood == 2:
        print(moodsInst.sad())
        # Ask user if they want to add affirmations to file for sad
        addedAffirm = int(input("Do you want to add any affirmations: Enter 1 for "
                                "'Yes', Enter any other digit for 'No"))
        # If user enters 'yes', open text file
        if addedAffirm == 1:
            filename = "/Users/miry/Downloads/sad.txt"
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
            exitForSad()
            # Send goodbye message w/ information
        else:
            exitForSad()
            # Ask user if they want a quote sent to their email
            emailSend = int(input("Do you want a quote also sent to your email?, Enter 1 for 'Yes'"
                                  "or Enter any other digit for 'No"))
            # If user enters '1'...
            if emailSend == 1:
                # Go to email function and print message
                email(emailAddress)
                print("Message sent!")
                # If user enters any other key, print message
            else:
                print("Bye!")

    # If user enters 3 for anxious, print affirmation
    elif mood == 3:
        print(moodsInst.anxious())
        # Ask user if they want to add affirmations to file for anxious
        addedAffirm = int(input("Do you want to add any affirmations: Enter 1 for "
                                "'Yes', Enter any other digit for 'No"))
        # If user enters 'yes', open text file
        if addedAffirm == 1:
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
            # Send goodbye message w/ information
        else:
            exitForAnxious()
            # Ask user if they want a quote sent to their email
            emailSend = int(input("Do you want a quote also sent to your email?, Enter 1 for 'Yes'"
                                  "or Enter any other digit for 'No"))
            # If user enters '1'...
            if emailSend == 1:
                # Go to email function and print message
                email(emailAddress)
                print("Message sent!")
                # If user enters any other key, print message
            else:
                print("Bye!")

    # If user enters 4 for upset, print affirmation
    elif mood == 4:
        print(moodsInst.upset())
        # Ask user if they want to add affirmations to file for upset
        affirm = int(input("Do you want to add any affirmations: Enter 1 for "
                           "'Yes', Enter any other digit for 'No"))
        # If user enters 'yes', open text file
        if addedAffirm == 1:
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
            exitForUpset()
            # Ask user if they want a quote sent to their email
            emailSend = int(input("Do you want a quote also sent to your email?, Enter 1 for 'Yes'"
                                  "or Enter any other digit for 'No"))
            # If user enters '1'...
            if emailSend == 1:
                # Go to email function and print message
                email(emailAddress)
                print("Message sent!")
                # If user enters any other key, print message
            else:
                print("Bye!")

    # If user enters 5 for annoyed, print affirmation
    elif mood == 5:
        print(moodsInst.annoyed())
        # Ask user if they want to add affirmations to file for annoyed
        affirm = int(input("Do you want to add any affirmations: Enter 1 for "
                           "'Yes', Enter any other digit for 'No"))
        # If user enters 'yes', open text file
        if addedAffirm == 1:
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
            # Send goodbye message w/ information
        else:
            exitForAnnoyed()
            # Ask user if they want a quote sent to their email
            emailSend = int(input("Do you want a quote also sent to your email?, Enter 1 for 'Yes'"
                                  "or Enter any other digit for 'No"))
            # If user enters '1'...
            if emailSend == 1:
                # Go to email function and print message
                email(emailAddress)
                print("Message sent!")
                # If user enters any other key, print message
            else:
                print("Bye!")


def exitForHappy():
    #print message
    print("Thank you for coming to Affirm, see you later" + '\n')

def exitForSad():
    # print message
    print("Thank you for coming to Affirm, see you later" + '\n')

def exitForAnxious():
    # print message
    print("Thank you for coming to Affirm, see you later" + '\n')

def exitForUpset():
    # print message
    print("Thank you for coming to Affirm, see you later" + '\n')

def exitForAnnoyed():
    # print message
    print("Thank you for coming to Affirm, see you later" + '\n')

def email(emailAddress):
    #initalize variables
    host = "smtp.gmail.com"
    port = 587
    username = "shopatazizi@gmail.com"
    password = "Blessing1"
    from_email = username
    to_list = emailAddress

    #Sending mail from Python using SMTP
    from smtplib import SMTP
    ABC = SMTP(host, port)
    ABC.ehlo()
    ABC.starttls()
    ABC.login(username, password)
    ABC.sendmail(from_email, to_list, "A positive attitude gives you power over"
                                      " your circumstances instead of your circumstances "
                                      "having power over you."
                                      + "\n" + "Have a great day!" +"\n"+ " -Affirm Now")
    ABC.quit()


if __name__ == "__main__":
    main()