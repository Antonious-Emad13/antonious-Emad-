# antonious-Emad

                        #   read  #

print(" AGE ".center(64,'#'))
# here i import the moduele termcolor
from termcolor import colored
# and i ask for user to age with integer and i color it
age = int(input(colored("Enter Your Age :",'blue')))
# if age between the 1 and 13
if age in range(1,13):
# print that
    print(colored('You Baby',"red"))
# and if the age between the 13 and 20
elif age in range(13,20):
# print that
    print(colored('You Are Teenager',"green"))
# and same thing
elif age in range(21,40):
    print(colored('You Adult',"yellow"))
# else so you are older than 40 so you grandfather
else:
    print('Hello GrandFather')

                        # good by #
