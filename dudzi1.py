import tkinter as tk

def display_dot():
    # create a small dot in the center of the screen
    dot = tk.Toplevel()
    dot.geometry("40x40+640+10") # size and position of the dot
    dot.configure(bg='black') # color of the dot
    dot.overrideredirect(True) # remove the title bar and border of the dot window
    dot.attributes("-topmost", True) # make the dot window always on top

    # create a label with the text "pip install pygame"
    label = tk.Label(dot, text="pip install pygame", fg="white", bg="black", font=("Arial", 8))
    label.pack(side="top", pady=3)

    dot.after(2000, lambda: dot.withdraw()) # display the dot for 2 seconds and then hide it
    dot.after(2500, lambda: dot.deiconify()) # show the dot again after 0.5 seconds
    dot.after(3500, lambda: dot.withdraw()) # hide the dot again after 1 second
    dot.after(30000, display_dot) # repeat the loop every 30 seconds

if __name__ == "__main__":
    # create a button to start the program
    root = tk.Tk()
    root.geometry("80x80+550+150")
    root.title("dudziiiiiiifuckyouuuu::)))")
    button = tk.Button(root, text="IK, it's crazy!", command=display_dot, bg="black", fg="white", activebackground="white", activeforeground="white", relief="groove", borderwidth=1)
    button.pack(pady=10)
    root.mainloop()
