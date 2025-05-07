import random # Import the random module for generating random numbers
import requests # Import the requests module for making HTTP requests

while True:  # Main program loop - repeats the game until the player quits

    # Task 1 - Generate a random number between 1 and 151 to use as the Pokemon ID number
    def choose_pokemon(amount=1):
        """
        Retrieves information about Pokemon from the API.

        Args:
            amount (int): The number of Pokemon to retrieve (default is 1).

        Returns:
            list: A list of dictionaries containing information about the Pokemon.
        """
        # print('[DEBUG]amount = {}'.format(amount))
        pokemon_list = []  # Initialize an empty list for Pokemon
        for i in range(amount):  # Loop iterating through the number of Pokemon to retrieve
            pokemon_number = random.randint(1, 151)  # Generate a random Pokemon ID number (1-151)
            # print('[DEBUG]Drawn pokemon: {}'.format(pokemon_number))  # Debugging line (commented out)
            # 3. Create a dictionary that contains the returned Pokemon's name, id, height and weight
            url = "https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon_number)  # Create API URL
            response = requests.get(url)  # Retrieve information from the API
            pokemon = (
                response.json()
            )  # Convert the response to JSON format
            pokemon_list.append(  # Add Pokemon data to the list
                {
                    "name": pokemon["name"],  # Pokemon name
                    "id": pokemon["id"],  # Pokemon ID
                    "height": pokemon["height"],  # Pokemon height
                    "weight": pokemon["weight"],  # Pokemon weight
                    "exp": pokemon["base_experience"],  # Pokemon base experience
                }
            )

        '''
        Debugging lines (commented out)
        print('[DEBUG]pokemon_list: {}'.format(pokemon_list))
        print('[DEBUG]pokemon: {}'.format(pokemon_list[1]))
        print('[DEBUG]pokemon name: {} pokemon id: {}'.format(pokemon_list[1]['name'], pokemon_list[1]['id']))
        '''
        return pokemon_list  # Return the list of Pokemon


    # Display all pokemons stats
    def display_pokemon_list(pokemon_list):
        """
         Displays a list of Pokemon with their stats.

        Args:
        pokemon_list (list): A list of dictionaries containing information about the Pokemon.
        """
        pokemon_number = 1  # Initialize Pokemon number
        for pokemon in pokemon_list:  # Iterate through the list of Pokemon
            print(  # Display Pokemon data
                "{}. Pokemon name {}, id {}, height {}, weight {}, experience {}".format(
                    pokemon_number,  # Pokemon number
                    pokemon["name"],  # Pokemon name
                    pokemon["id"],  # Pokemon ID
                    pokemon["height"],  # Pokemon height
                    pokemon["weight"],  # Pokemon weight
                    pokemon["exp"],  # Pokemon base experience
                )
            )
            pokemon_number += 1  # Increment the Pokemon number


    # Pick a pokemon number/ which pokemon you choose
    def pick_pokemon(choice, pokemon_list):
        """
        Selects a Pokemon from the list based on the choice number.

        Args:
            choice (int): The number of the selected Pokemon.
            pokemon_list (list): A list of dictionaries containing information about the Pokemon.

        Returns:
            dict: A dictionary containing information about the selected Pokemon.
        """
        return pokemon_list[choice - 1]  # Return the selected Pokemon from the list


    # 2. Get a Pokemons based on its ID number
    my_pokemon_list = choose_pokemon(int(input("How many pokemons do you need? (1-10) ")))  # Get a list of Pokemon from the user
    display_pokemon_list(my_pokemon_list)  # Display the list of Pokemon
    my_pokemon = pick_pokemon(  # Select a Pokemon by the user
        int(input("Which pokemon number you choose? ")), my_pokemon_list
    )

    # 4. Get a random Pokemon for the player and another for their opponent
    print("You get {} with ID number {}".format(my_pokemon["name"], my_pokemon["id"]))  # Display information about the selected Pokemon
    stat_choice = input(  # Get information from the user about the selected statistic
        "Which stat of your pokemon do you want to use? (id, height, weight, exp) "
    )  #Ask the user which stat they want to use (id, height or weight)

    # Opponent pokemon
    opponent_pokemon_count = random.randint(1, 10)  # Generate a random number of opponent Pokemon
    opponent_pokemon_list = choose_pokemon(opponent_pokemon_count)  # Retrieve a list of opponent Pokemon
    display_pokemon_list(opponent_pokemon_list)  # Display the list of opponent Pokemon
    opponent_choice = random.randint(1, opponent_pokemon_count)  # Generate a random choice for the opponent Pokemon
    # print('[DEBUG]opponent_choice: {}, '.format(opponent_choice))  # Debugging line (commented out)
    opponent_pokemon = pick_pokemon(opponent_choice, opponent_pokemon_list)  # Select the opponent Pokemon

    # Display information about the selected opponent Pokemon
    print(
        "The opponent gets {} with ID number {}".format(
            opponent_pokemon["name"], opponent_pokemon["id"]
        )
    )
    my_stat = my_pokemon[stat_choice]  # Retrieve the stat of the selected Pokemon
    opponent_stat = opponent_pokemon[stat_choice]  # Retrieve the stat of the opponent Pokemon

    # Display the statistics
    print(
        "Your pokemon has {} of {} your opponent pokemon has {}.".format(
            my_pokemon[stat_choice], stat_choice, opponent_pokemon[stat_choice]
        )
    )

    # 6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
    if my_stat > opponent_stat:  # Check if we won
        print("You Win!")
    elif my_stat < opponent_stat:  # Check if we lost
        print("You Lose!")
    else:  # It's a draw
        print("Draw!")


    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':  # Ask if the player wants to repeat the program
        break  # Break the loop if the player doesn't want to repeat
