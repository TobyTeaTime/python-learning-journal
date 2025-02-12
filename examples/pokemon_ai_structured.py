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
        print(f"{self.name} took {damage} damage! {self.name} has {self.hp} HP left.\n")

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

# Battle function
def battle(player_pokemon, opponent_pokemon):
    while not player_pokemon.is_fainted() and not opponent_pokemon.is_fainted():
        print(f"Your Pokémon: {player_pokemon.name} (HP: {player_pokemon.hp})")
        print(f"Opponent's Pokémon: {opponent_pokemon.name} (HP: {opponent_pokemon.hp})\n")

        # Display options
        print("What will you do?")
        print("1. Battle")
        print("2. Open Bag")
        print("3. Switch Pokémon")
        print("4. Run")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            # Display moves
            print("\nChoose a move:")
            for i, move in enumerate(player_pokemon.moves, start=1):
                print(f"{i}. {move.name}")

            move_choice = input("Select a move (1-4): ")
            if move_choice.isdigit() and 1 <= int(move_choice) <= len(player_pokemon.moves):
                selected_move = player_pokemon.moves[int(move_choice) - 1]
                print(f"\n{player_pokemon.name} used {selected_move.name}!")
                opponent_pokemon.take_damage(selected_move.damage)

                # Opponent's turn
                if not opponent_pokemon.is_fainted():
                    opponent_move = random.choice(opponent_pokemon.moves)
                    print(f"{opponent_pokemon.name} used {opponent_move.name}!")
                    player_pokemon.take_damage(opponent_move.damage)
            else:
                print("Invalid move choice. Try again.\n")

        elif choice in ["2", "3", "4"]:
            print("This option is not yet implemented. Please choose 'Battle' for now.\n")
        else:
            print("Invalid choice. Please select a valid option.\n")

    # Determine the winner
    if player_pokemon.is_fainted():
        print(f"{player_pokemon.name} fainted! You lost the battle.")
    else:
        print(f"{opponent_pokemon.name} fainted! You won the battle!")

# Start the battle
print("A wild Squirtle appeared!")
battle(charmander, squirtle)