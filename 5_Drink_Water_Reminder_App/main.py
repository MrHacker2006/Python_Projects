import time
from plyer import notification


while True:
    print("Please Drink Some Water.")
    notification.notify(title = "Please drink some water", message="You need to drink some water right now")
    time.sleep(60*60)  # It will notify you in every one hour