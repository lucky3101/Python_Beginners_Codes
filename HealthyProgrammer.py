import pygame
import time
import datetime
from dateutil.parser import parse

pygame.mixer.init()

t = datetime.datetime.now()

start_time = parse('09:00:00')
end_time=parse('17:00:00')

x = open("Logs.txt", "r+")

def water():
    pygame.mixer.music.load('water.mp3')
    pygame.mixer.music.play()

    while (True):

        a = raw_input("Enter 'Drank', once you drink the water : ")

        if (a != "Drank"):
            print ("You have not entered correct input")
            continue

        else:
            pygame.mixer.music.stop()
            x.write("You drank water at : " + time.ctime() + "\n")
            break

def eye():
    pygame.mixer.music.load('eyes.mp3')
    pygame.mixer.music.play()

    while (True):

        a = raw_input("Enter 'EyDone', once you complete eyes exercise : ")

        if (a != "EyDone"):
            print ("You have not entered correct input")
            continue

        else:
            pygame.mixer.music.stop()
            x.write("You completed eyes exercise at : " + time.ctime() + "\n")
            break

def exercise():
    pygame.mixer.music.load('exercise.mp3')
    pygame.mixer.music.play()

    while (True):

        a = raw_input("Enter 'ExDone', once you complete exercise : ")

        if (a != "ExDone"):
            print ("You have not entered correct input")
            continue

        else:
            pygame.mixer.music.stop()
            x.write("You completed exercise at : " + time.ctime() + "\n")
            break

while (t > start_time and t < end_time):

    curr_time=datetime.datetime.now()

    diff = (curr_time - start_time).seconds/60

    if (diff % 45 == 0 and diff % 30 == 0):
        water()
        eye()
        exercise()

    elif (diff % 45 == 0):
        water()
        exercise()

    elif (diff % 30 == 0):
        water()
        eye()

    elif (diff % 15 == 0):
        water()


x.close()