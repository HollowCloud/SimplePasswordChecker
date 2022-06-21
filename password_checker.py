import re
import getpass


def sign_in():
    while True:
        password = getpass.getpass('Password: ')#This is where we are using getpass()

        requirements = re.compile(r".{8}")

        a = requirements.match(password)

        if a == None:
            print('Password should contain at least 8 characters.')
            print()
            continue
        else:
            print('You have successfully written password.')
            print()
            choice = input('Do you want to check your password?(Y/N)')
            if choice == 'Yes' or choice == 'Y':
                print()
                checker(password)
                break
            elif choice == 'No' or choice == 'N':
                print()
                print('See you.')
                break    

def checker(password):
    while True:
        pasw = getpass.getpass('Enter password one more time: ')

        if pasw != password:
            print()
            print('Try again. Wrong password. {} is not right'.format(pasw))
            print()
        else:
            print()
            print('Successful Match.')
            break

sign_in()