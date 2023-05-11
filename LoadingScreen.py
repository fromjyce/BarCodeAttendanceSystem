import tkinter as tk
import time

def showloadingscreen():
    loading_screen = tk.Toplevel()
    loading_screen.title("Loading")
    loading_screen.geometry("300x100")
    loading_screen.resizable(False, False)
    loading_screen.configure(bg="black")
    loading_screen.overrideredirect(True)
    screen_width = loading_screen.winfo_screenwidth() # Get the screen width and height
    screen_height = loading_screen.winfo_screenheight()
    x = int(screen_width/2 - 150)     # Calculate the x and y coordinates to center the loading screen on the screen
    y = int(screen_height/2 - 50)
    loading_screen.geometry("+{}+{}".format(x, y)) # Set the position of the loading screen
    name_label = tk.Label(loading_screen, text="CYBERX \nATTENDANCE", font=("AkiraExpanded-SuperBold", 20), fg="white", bg="black")
    name_label.pack(pady=1, anchor="center")
    label = tk.Label(loading_screen, text="Loading...", font=("8514oem", 12), fg="white", bg="black")
    label.pack(pady=1, anchor="center")
    loading_screen.update()
    time.sleep(3) # Simulate loading process
    loading_screen.destroy()
    time.sleep(0.5) #Delay after loading
