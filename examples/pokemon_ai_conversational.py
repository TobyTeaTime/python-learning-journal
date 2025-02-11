import random

class Pokemon:
    def __init__(self, name, hp, moves):
        self.name = name
        self.hp = hp
        self.moves = moves

    def attack(self, move, target):
        damage = random.randint(move['damage_min'], move['damage_max'])
        target.hp -= damage
        print(f"{self.name} used {move['name']} and dealt {damage} damage to {target.name}!")
        if target.hp <= 0:
            print(f"{target.name} has fainted!")

def choose_move(pokemon):
    print(f"Choose a move for {pokemon.name}:")
    for i, move in enumerate(pokemon.moves, 1):
        print(f"{i}. {move['name']} (Damage: {move['damage_min']}-{move['damage_max']})")
    choice = int(input("Enter the move number: ")) - 1
    return pokemon.moves[choice]

def battle(pokemon1, pokemon2):
    print(f"A wild {pokemon2.name} appeared!")
    print(f"Go, {pokemon1.name}!")
    
    while pokemon1.hp > 0 and pokemon2.hp > 0:
        print(f"\n{pokemon1.name} HP: {pokemon1.hp}")
        print(f"{pokemon2.name} HP: {pokemon2.hp}")
        
        # Player's turn
        move = choose_move(pokemon1)
        pokemon1.attack(move, pokemon2)
        if pokemon2.hp <= 0:
            break
        
        # Opponent's turn
        move = random.choice(pokemon2.moves)
        pokemon2.attack(move, pokemon1)
    
    if pokemon1.hp > 0:
        print(f"\n{pokemon1.name} wins!")
    else:
        print(f"\n{pokemon2.name} wins!")

# Define some moves
moves = [
    {'name': 'Tackle', 'damage_min': 10, 'damage_max': 20},
    {'name': 'Ember', 'damage_min': 15, 'damage_max': 25},
    {'name': 'Water Gun', 'damage_min': 12, 'damage_max': 22},
    {'name': 'Vine Whip', 'damage_min': 13, 'damage_max': 23}
]

# Create two Pokémon
pikachu = Pokemon("Pikachu", 100, [moves[0], moves[1]])
bulbasaur = Pokemon("Bulbasaur", 100, [moves[2], moves[3]])

# Start the battle
battle(pikachu, bulbasaur)