import json
import os

def read_json_file(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"The file {file_path} was not found. Creating new file...")
        write_json_file(file_path, [])
        return []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                print("File is empty. Initializing with empty array.")
                write_json_file(file_path, [])
                return []
            data = json.loads(content)
            return data
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON. Initializing with empty data.")
        write_json_file(file_path, [])
        return []

def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def add_pokemon_to_json(file_path):
    data = read_json_file(file_path)
    
    if data is not None:
    
        new_name = input("Enter the Pokémon name (in English): ")
        new_type = input("Enter the Pokémon type (comma separated if multiple): ")
        new_hp = int(input("Enter the base HP: "))
        new_attack = int(input("Enter the base Attack: "))
        new_defense = int(input("Enter the base Defense: "))
        new_sp_attack = int(input("Enter the base Special Attack: "))
        new_sp_defense = int(input("Enter the base Special Defense: "))
        new_speed = int(input("Enter the base Speed: "))


        new_pokemon = {
            "name": {
                "english": new_name
            },
            "type": new_type.split(","),
            "base": {
                "HP": new_hp,
                "Attack": new_attack,
                "Defense": new_defense,
                "Sp. Attack": new_sp_attack,
                "Sp. Defense": new_sp_defense,
                "Speed": new_speed
            }
        }

        data.append(new_pokemon)
        write_json_file(file_path, data)
        print("Pokémon added successfully.")
    else:
        print("Could not add Pokémon due to error in reading JSON.")


file_path = 'my_pokemons.json'
add_pokemon_to_json(file_path)