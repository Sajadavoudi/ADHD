import tkinter as tk

class CustomPomodoro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Po Mo Do Ro")
        self.root.geometry("400x300")
        
        # Work & break duration variables (in minutes)
        self.work_time_var = tk.IntVar(value=25)
        self.break_time_var = tk.IntVar(value=5)
        
        # Create a settings frame
        settings_frame = tk.Frame(self.root)
        settings_frame.pack(pady=10)
        
        tk.Label(settings_frame, text="Work (minutes):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Entry(settings_frame, textvariable=self.work_time_var, width=5).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(settings_frame, text="Break (minutes):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Entry(settings_frame, textvariable=self.break_time_var, width=5).grid(row=1, column=1, padx=5, pady=5)
        
        # Start and Stop buttons
        self.start_button = tk.Button(self.root, text="Ready!", command=self.start_pomodoro)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_pomodoro, state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        
        # Status & countdown labels
        self.status_label = tk.Label(self.root, text="Ummm do it", font=("Helvetica", 12))
        self.status_label.pack(pady=10)
        self.countdown_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.countdown_label.pack(pady=5)
        
        # For the blinking dot overlay
        self.dot = None
        
        # Control variables
        self.running = False
        self.remaining_time = 0
        self.current_phase = None  # "work" or "break"
        self.quarter_count = 0
        
        self.root.mainloop()
        
    def start_pomodoro(self):
        # Convert durations from minutes to seconds
        self.work_duration = self.work_time_var.get() * 60
        self.break_duration = self.break_time_var.get() * 60
        self.quarter_time = self.work_duration // 4
        
        self.running = True
        self.current_phase = "work"
        self.quarter_count = 0
        
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="workworkworkwork!")
        
        # Start the blinking dot
        self.blinking_dot()
        
        # Begin the work phase countdown
        self.remaining_time = self.work_duration
        self.update_timer()
        
        # Schedule quadrant flash at every quarter of the work phase
        self.schedule_quadrant_flash()
    
    def stop_pomodoro(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Pomodoro Stopped.")
        self.countdown_label.config(text="")
        if self.dot:
            self.dot.destroy()
            self.dot = None
    
    def update_timer(self):
        if not self.running:
            return
        minutes, seconds = divmod(self.remaining_time, 60)
        self.countdown_label.config(text=f"{minutes:02d}:{seconds:02d}")
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            # When the timer ends, switch phases
            if self.current_phase == "work":
                self.start_break_phase()
            elif self.current_phase == "break":
                self.reset_cycle()
    
    def schedule_quadrant_flash(self):
        if not self.running or self.current_phase != "work":
            return
        if self.quarter_count < 4:
            self.root.after(self.quarter_time * 1000, self.flash_quadrant)
    
    def flash_quadrant(self):
        if not self.running:
            return
        self.show_quadrant(self.quarter_count)
        self.quarter_count += 1
        if self.quarter_count < 4:
            self.schedule_quadrant_flash()
    
    def show_quadrant(self, part):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        positions = [
            (0, 0, screen_width // 2, screen_height // 2),              # Top-left
            (screen_width // 2, 0, screen_width, screen_height // 2),      # Top-right
            (0, screen_height // 2, screen_width // 2, screen_height),     # Bottom-left
            (screen_width // 2, screen_height // 2, screen_width, screen_height)  # Bottom-right
        ]
        if part < len(positions):
            x1, y1, x2, y2 = positions[part]
            overlay = tk.Toplevel(self.root)
            overlay.geometry(f"{x2 - x1}x{y2 - y1}+{x1}+{y1}")
            overlay.configure(bg='blue')
            overlay.overrideredirect(True)
            overlay.attributes("-topmost", True)
            overlay.after(4000, overlay.destroy)  # Remove after 4 seconds
    
    def start_break_phase(self):
        if not self.running:
            return
        self.current_phase = "break"
        self.status_label.config(text="shol kon!")
        self.remaining_time = self.break_duration
        self.update_timer()
        
        # Display a full-screen green overlay during the break
        break_overlay = tk.Toplevel(self.root)
        break_overlay.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        break_overlay.configure(bg='black')
        break_overlay.overrideredirect(True)
        break_overlay.attributes("-topmost", True)
        break_overlay.after(self.break_duration * 1000, break_overlay.destroy)
    
    def reset_cycle(self):
        self.running = False
        self.current_phase = None
        self.status_label.config(text="suck it up n do it agian!")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        if self.dot:
            self.dot.destroy()
            self.dot = None
    
    def create_blinking_dot(self):
        self.dot = tk.Toplevel(self.root)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        dot_size = 40
        center_x = (screen_width // 2) - (dot_size // 2)
        center_y = (screen_height // 2) - (dot_size // 2)
        self.dot.geometry(f"{dot_size}x{dot_size}+{center_x}+{center_y}")
        self.dot.configure(bg='#00CC66')
        self.dot.overrideredirect(True)
        self.dot.attributes("-topmost", True)
        label = tk.Label(self.dot, text="Focus", fg="white", bg='#00CC66', font=("Arial", 8, "bold"))
        label.pack(pady=3)
    
    def blinking_dot(self):
        if not self.running:
            if self.dot:
                self.dot.destroy()
                self.dot = None
            return
        if self.dot is None or not self.dot.winfo_exists():
            self.create_blinking_dot()
        # Show dot briefly then hide it
        self.dot.deiconify()
        self.root.after(500, lambda: self.dot.withdraw())
        self.root.after(3000, self.blinking_dot)
        
if __name__ == "__main__":
    CustomPomodoro()
