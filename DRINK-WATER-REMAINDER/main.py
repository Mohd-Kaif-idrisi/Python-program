import time
from notifypy import Notify

notification = Notify()

while True:
    print("Drink your water")
    notification.title = "Drink water remainder"
    notification.message = "Please sip some water"
    notification.send()
    
    time.sleep(3)    