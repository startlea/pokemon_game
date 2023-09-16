import random
import requests

while True:
    #
    #
    # Task 1 - Generate a random number between 1 and 151 to use as the Pokemon ID number
    def choose_pokemon(amount=1):
        # print('[DEBUG]amount = {}'.format(amount))
        pokemon_list = []
        for i in range(amount):
            pokemon_number = random.randint(1, 151)
            # print('[DEBUG]Drawn pokemon: {}'.format(pokemon_number))
            # 3. Create a dictionary that contains the returned Pokemon's name, id, height and weight
            url = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon_number)  # API URL
            response = requests.get(url)  # getting information from the API
            pokemon = (
                response.json()
            )  # returns a JSON object of the result (if the result was written in JSON format, if not it raises an error
            pokemon_list.append(
                {
                    "name": pokemon["name"],
                    "id": pokemon["id"],
                    "height": pokemon["height"],
                    "weight": pokemon["weight"],
                    "exp": pokemon["base_experience"],
                }
            )
        # print('[DEBUG]pokemon_list: {}'.format(pokemon_list))
        # print('[DEBUG]pokemon: {}'.format(pokemon_list[1]))
        # print('[DEBUG]pokemon name: {} pokemon id: {}'.format(pokemon_list[1]['name'], pokemon_list[1]['id']))
        return pokemon_list


    # Display all pokemons stats
    def display_pokemon_list(pokemon_list):
        pokemon_number = 1
        for pokemon in pokemon_list:
            print(
                "{}. Pokemon name {}, id {}, height {}, weight {}, experience {}".format(
                    pokemon_number,
                    pokemon["name"],
                    pokemon["id"],
                    pokemon["height"],
                    pokemon["weight"],
                    pokemon["exp"],
                )
            )
            pokemon_number += 1


    # Pick a pokemon number/ which pokemon you choose
    def pick_pokemon(choice, pokemon_list):
        return pokemon_list[choice - 1]


    # 2. Get a Pokemons based on its ID number
    my_pokemon_list = choose_pokemon(int(input("How many pokemons do you need? (1-10) ")))
    display_pokemon_list(my_pokemon_list)
    my_pokemon = pick_pokemon(
        int(input("Which pokemon number you choose? ")), my_pokemon_list
    )

    # 4. Get a random Pokemon for the player and another for their opponent
    print("You get {} with ID number {}".format(my_pokemon["name"], my_pokemon["id"]))
    # Choose from stats
    stat_choice = input(
        "Which stat of your pokemon do you want to use? (id, height, weight, exp) "
    )  ##5. Ask the user which stat they want to use (id, height or weight)

    # Opponent pokemon
    opponent_pokemon_count = random.randint(1, 10)
    opponent_pokemon_list = choose_pokemon(opponent_pokemon_count)
    display_pokemon_list(opponent_pokemon_list)
    opponent_choice = random.randint(1, opponent_pokemon_count)
    # print('[DEBUG]opponent_choice: {}, '.format(opponent_choice))
    opponent_pokemon = pick_pokemon(opponent_choice, opponent_pokemon_list)
    print(
        "The opponent gets {} with ID number {}".format(
            opponent_pokemon["name"], opponent_pokemon["id"]
        )
    )
    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    print(
        "Your pokemon has {} of {} your opponent pokemon has {}.".format(
            my_pokemon[stat_choice], stat_choice, opponent_pokemon[stat_choice]
        )
    )

    # 6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
    if my_stat > opponent_stat:
        print("You Win!")
    elif my_stat < opponent_stat:
        print("You Lose!")
    else:
        print("Draw!")


    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break
