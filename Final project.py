import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("500x450")
# Title
root.title("Rate games")

label = tk.Label(root, text="Rate this game out of 5 stars")
label.pack(pady=20)
entry = tk.Entry(root)
entry.pack(pady=5)

unplayed_button=tk.Button(root, text="Unplayed")
unplayed_button.pack(pady=5) 





# Start the Tkinter event loop
root.mainloop()