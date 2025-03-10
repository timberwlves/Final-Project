import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import random

# Create the main window
root = tk.Tk()
root.geometry("500x450")
# Title
root.title("Rate games")

games_list = [ 
    {"name": "Minecraft", "image": "minecraft.png"},
    {"name": "Baldur's Gate 3", "image": "bg3.png"},
    {"name": "The Sims 4", "image": "sims4.png"},
    {"name": "Bloodborne", "image": "bloodborne.png"},
    {"name": "Silent Hill 2", "image": "sh2.png"},
    {"name": "Stardew Valley", "image": "stardew.png"},
    {"name": "Final Fantasy 7", "image": "ff7.png"},
    {"name": "Marvel Rivals", "image": "rivals.png"}
] 

#List to store games rated
games_rated = []

unplayed_list = [game["name"] for game in games_list]


#Label for displaying image

image_label = tk.Label(root)
image_label.pack(pady=10)

#Functions -

def show_random_game():



    game = random.choice(games_list)
    game_name_label.config(text=game["name"])

   # game_image = PhotoImage(file=game["image"])
    #image_label.config(image=game_image)
    #image_label.image = game_image   - unable to get images to function properly

    return game



#Rating function used chatgpt reference
def rate_game():
    rating = entry_rating.get()

    if rating.isdigit() and 1 <= int(rating) <= 5:
        game_name = game_name_label.cget("text")
        rated_game = {"name": game_name, "rating": int(rating)}
        games_rated.append(rated_game)
        entry_rating.delete(0, tk.END)
        show_random_game()


            # Clear the rating entry
        entry_rating.delete(0, tk.END)

           
        show_random_game()

    
    else:
        messagebox.showerror("Invalid" , "Please enter a number between 1 and 5.")



# Mark the game as unplayed 
def mark_as_unplayed():
    game_name = game_name_label.cget("text")
    
    if game_name != "":
        # Check if the game is rated and add it back to the unplayed list
        if game_name not in unplayed_list:
            unplayed_list.append(game_name)
            messagebox.showinfo("Game Marked as Unplayed", "Game has been marked as unplayed!")
        else:
            messagebox.showinfo("Unplayed", "Marked Unplayed!")

        # Show the next random game
        show_random_game()


#Show games that have been rated
def view_rating():
    ratings_window = tk.Toplevel(root)
    ratings_window.title("Rated games")
    ratings_window.geometry("300x300")

    listbox = tk.Listbox(ratings_window, height=10, width=40)
    for game in games_rated:
        listbox.insert(tk.END, f"{game['name']} - Rating: {game['rating']}/5") #Referenced CHATGPT Here
        listbox.pack(pady=10)
    else:
        label = tk.Label(ratings_window, text ="No games rated!")
        label.pack(pady=20)

    
#Show unplayed games
def show_unplayed_games():
    unplayed_window = tk.Toplevel(root)  # Create a new top-level window
    unplayed_window.title("Unplayed Games")
    unplayed_window.geometry("300x300")

    if unplayed_list:
        label = tk.Label(unplayed_window, text="Unplayed Games")
        label.pack(pady=10)

        # Create a listbox to display the unplayed games
        listbox = tk.Listbox(unplayed_window, height=10, width=40)
        for game in unplayed_list:
            listbox.insert(tk.END, game)
        listbox.pack(pady=10)
    else:
        label = tk.Label(unplayed_window, text="No unplayed games!")
        label.pack(pady=20)



#UI Stuff - 
#Rate the game
label = tk.Label(root, text="Rate this game out of 5 stars")
label.pack(pady=20)
entry_rating = tk.Entry(root)
entry_rating.pack(pady=5)

game_name_label = tk.Label(root, text="")
game_name_label.pack(pady=10)

#Rate Button
rate_button = tk.Button(root, text="Rate", command= rate_game)
rate_button.pack(pady=5)

#Button to sort games that haven't been played yet
unplayed_button=tk.Button(root, text="Unplayed", command=mark_as_unplayed)
unplayed_button.pack(pady=5) 

#View games with rating
view_list=tk.Button(root, text="View Ratings", command = view_rating)
view_list.pack(pady=5)

# View Unplayed Games Button
view_unplayed = tk.Button(root, text="View Unplayed Games", command=show_unplayed_games)
view_unplayed.pack(pady=5)

#Show a game when program starts
show_random_game()

# Start the Tkinter event loop
root.mainloop()
