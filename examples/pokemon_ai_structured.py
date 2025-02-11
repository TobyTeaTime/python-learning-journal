import tkinter as tk
from tkinter import messagebox
import random

# Define Pokémon classes
class Pokemon:
    def __init__(self, name, hp, moves):
        self.name = name
        self.hp = hp
        self.moves = moves

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_fainted(self):
        return self.hp <= 0

# Define moves
class Move:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

# Create moves
tackle = Move("Tackle", 20)
ember = Move("Ember", 25)
water_gun = Move("Water Gun", 22)
vine_whip = Move("Vine Whip", 24)

# Create Pokémon
charmander = Pokemon("Charmander", 100, [tackle, ember])
squirtle = Pokemon("Squirtle", 100, [tackle, water_gun])

# GUI Application
class PokemonBattleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon Battle")
        self.player_pokemon = charmander
        self.opponent_pokemon = squirtle

        # Create GUI elements
        self.create_widgets()

        # Start the battle
        self.update_display()

    def create_widgets(self):
        # Display Pokémon HP
        self.player_hp_label = tk.Label(self.root, text=f"{self.player_pokemon.name} HP: {self.player_pokemon.hp}")
        self.player_hp_label.pack()

        self.opponent_hp_label = tk.Label(self.root, text=f"{self.opponent_pokemon.name} HP: {self.opponent_pokemon.hp}")
        self.opponent_hp_label.pack()

        # Battle options
        self.battle_button = tk.Button(self.root, text="Battle", command=self.open_battle_menu)
        self.battle_button.pack()

        self.bag_button = tk.Button(self.root, text="Open Bag", command=self.open_bag)
        self.bag_button.pack()

        self.switch_button = tk.Button(self.root, text="Switch Pokémon", command=self.switch_pokemon)
        self.switch_button.pack()

        self.run_button = tk.Button(self.root, text="Run", command=self.run)
        self.run_button.pack()

        # Move selection menu (hidden initially)
        self.move_menu = tk.Frame(self.root)
        self.move_buttons = []
        for i, move in enumerate(self.player_pokemon.moves):
            button = tk.Button(self.move_menu, text=move.name, command=lambda m=move: self.use_move(m))
            button.pack()
            self.move_buttons.append(button)
        self.move_menu.pack_forget()

    def update_display(self):
        self.player_hp_label.config(text=f"{self.player_pokemon.name} HP: {self.player_pokemon.hp}")
        self.opponent_hp_label.config(text=f"{self.opponent_pokemon.name} HP: {self.opponent_pokemon.hp}")

        # Check for fainted Pokémon
        if self.player_pokemon.is_fainted():
            messagebox.showinfo("Battle Over", f"{self.player_pokemon.name} fainted! You lost the battle.")
            self.root.quit()
        elif self.opponent_pokemon.is_fainted():
            messagebox.showinfo("Battle Over", f"{self.opponent_pokemon.name} fainted! You won the battle!")
            self.root.quit()

    def open_battle_menu(self):
        # Hide main buttons and show move selection
        self.battle_button.pack_forget()
        self.bag_button.pack_forget()
        self.switch_button.pack_forget()
        self.run_button.pack_forget()
        self.move_menu.pack()

    def use_move(self, move):
        # Player's turn
        print(f"{self.player_pokemon.name} used {move.name}!")
        self.opponent_pokemon.take_damage(move.damage)
        self.update_display()

        # Opponent's turn (if not fainted)
        if not self.opponent_pokemon.is_fainted():
            opponent_move = random.choice(self.opponent_pokemon.moves)
            print(f"{self.opponent_pokemon.name} used {opponent_move.name}!")
            self.player_pokemon.take_damage(opponent_move.damage)
            self.update_display()

        # Hide move menu and show main buttons
        self.move_menu.pack_forget()
        self.battle_button.pack()
        self.bag_button.pack()
        self.switch_button.pack()
        self.run_button.pack()

    def open_bag(self):
        messagebox.showinfo("Open Bag", "This feature is not yet implemented.")

    def switch_pokemon(self):
        messagebox.showinfo("Switch Pokémon", "This feature is not yet implemented.")

    def run(self):
        messagebox.showinfo("Run", "This feature is not yet implemented.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonBattleApp(root)
    root.mainloop()