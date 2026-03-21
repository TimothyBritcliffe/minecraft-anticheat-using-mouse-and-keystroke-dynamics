#add teh functions for mouse logging here. Keep it modular - using functions for everything (also give specific tasks separate functions)
# will also need a write_csv() function etc etc etc
# Make sure to include a 'main-guard' that runs the main mouse_log() function to test the functionality
#

# Keynote I was having some issues with 

import csv
import mouse # Since I'm using the [https://github.com/boppreh/mouse?tab=readme-ov-file#mouse.ButtonEvent] github repository,most of the heavy lifting in this space has been done. 
             # Im essentilly just reusing some of thier components and adding a bit of my own code to make it work for the project purposes.

def write_csv(writer, event):# This essentially triggers each time you move the mouse on your screen
    writer.writerow([event.time, type(event).__name__, str(event)]) # All this is doing is writing if striaght into the csv file

def event_handler(event, writer):
    write_csv(writer, event)

def mouse_log():
    with open("data/mouse_log.csv", "w", newline="") as file: # This is just essentially creating the file to store the newly created mouse_log.cscv into the data folder
        field_names = ["timestamp", "event_type", "event_info"]
        writer = csv.writer(file)
        writer.writerow(field_names)
        mouse.hook(lambda event: event_handler(event, writer))
        # mouse.wait(button="right", target_types=("down",)) #I wasn't too sure ont his so Im just trying to make sure and I got an online refrence for this, but not sure if this si the correct implementation
        

if __name__ == "__main__":
    mouse_log()