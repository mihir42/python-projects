import time
import os

messege = input("Enter messege to display: ")
wait = int(input("Enter watiting time: "))
def reminder(messege):
    os.system('msg * "' + messege + '"')

time.sleep(wait)
reminder(messege)   



