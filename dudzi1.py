import tkinter as tk
import time
import random

'''                                             
 _______   __    __  _______   ________  ______        ________  __    __   ______   __    __        __    __ 
/       \ /  |  /  |/       \ /        |/      |      /        |/  |  /  | /      \ /  |  /  |      /  |  /  |
$$$$$$$  |$$ |  $$ |$$$$$$$  |$$$$$$$$/ $$$$$$/       $$$$$$$$/ $$ |  $$ |/$$$$$$  |$$ | /$$/       $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |    /$$/    $$ |        $$ |__    $$ |  $$ |$$ |  $$/ $$ |/$$/        $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |   /$$/     $$ |        $$    |   $$ |  $$ |$$ |      $$  $$<         $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |  /$$/      $$ |        $$$$$/    $$ |  $$ |$$ |   __ $$$$$  \        $$ |  $$ |
$$ |__$$ |$$ \__$$ |$$ |__$$ | /$$/____  _$$ |_       $$ |      $$ \__$$ |$$ \__/  |$$ |$$  \       $$ \__$$ |
$$    $$/ $$    $$/ $$    $$/ /$$      |/ $$   |      $$ |      $$    $$/ $$    $$/ $$ | $$  |      $$    $$/ 
$$$$$$$/   $$$$$$/  $$$$$$$/  $$$$$$$$/ $$$$$$/       $$/        $$$$$$/   $$$$$$/  $$/   $$/        $$$$$$/  
'''
def display_dot(count=30, dot_count=1):
    #small dot in the center of the screen
    dot = tk.Toplevel()
    dot.geometry("100x100+640+200") # size and position of the dot
    random_color=0
    if dot_count % 60 == 0:
        random_color = random.randint(1, 9)
    
    list_color = ['red', 'white', 'black', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink', 'gray']
    dot.configure(bg=list_color[random_color]) # color of the dot
    dot.overrideredirect(True) # remove the title bar and border of the dot window
    dot.attributes("-topmost", True) # make the dot window always on top
 
    dot.after(2000, lambda: dot.withdraw()) # display the dot for 2 seconds and then hide it
    dot.after(2500, lambda: dot.deiconify()) # show the dot again after 0.5 seconds
    dot.after(3500, lambda: dot.withdraw()) # hide the dot again after 1 second
    dot.after(30000, lambda: display_dot(count, dot_count+1)) # repeat the loop every 30 seconds
    
    


if __name__ == "__main__":
    # create a button to start the program
    root = tk.Tk()
    root.geometry("80x80+550+150")
    root.title("dudziiiiiiifuckyouuuu::)))")
    button = tk.Button(root, text="RESPECT THE DOT", command=display_dot, bg="black", fg="white", activebackground="white", activeforeground="white", relief="groove", borderwidth=10)
    button.pack(pady=10)
    root.mainloop()
