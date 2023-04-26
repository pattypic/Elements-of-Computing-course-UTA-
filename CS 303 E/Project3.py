# File: Project3.py
# Student: Patrick Pichardo
# UT EID: pjp953
# Course Name: CS303E
# 
# Date Created: 04/17/23
# Date Last Modified: 04/18/23
# Description of Program:This Python code is a program that provides census data for cities in Texas, including the population in the 2020 census and estimated population in 2023.

def read_city_data():
    # This function reads the data from the `citiesData.csv` file and returns a dictionary of city names and population data.
    city_data = {}
    city_names = []
    # did find this bit from a text book I have for python. this was the last code I implemented since I fogot to account for if th file does not exist.
    try:
        file = open("citiesData.csv", "r")
    except FileNotFoundError:
        print("Error: File not found.")
        exit()
    for line in file:
        # Ignore lines that start with a hash character (#).
        if not line.startswith("#"):
            # Split the line into a list of parts, separated by commas.
            parts = line.strip().split(",")
            # The first part is the city name.
            city_name = parts[3].strip('"')
            # The second part is the population in 2020.
            census2020 = int(parts[1])
            # The third part is the estimated population in 2023.
            estimated2023 = int(parts[0])
            # Add the city name and population data to the dictionary.
            city_data[city_name] = (census2020, estimated2023)
            # Add the city name to the list of city names.
            city_names.append(city_name)
    total_census2020 = sum(x[0] for x in city_data.values())
    total_estimated2023 = sum(x[1] for x in city_data.values())
    city_data["Texas"] = (total_census2020, total_estimated2023)
    city_names.sort()
    # Return the dictionary of city names and population data.
    return city_data, city_names


def help(): # This function prints a list of available commands.
    return print("Enter any of the following commands:\n\033[1mHelp\033[0m - list available commands;\n\033[1mQuit\033[0m - exit this dashboard;\n\033[1mCities\033[0m - list all Texas cities\n\033[1mCensus\033[0m <cityName>/Texas - population in 2020 census by specified city or statewide;\n\033[1mEstimated\033[0m <cityName>/Texas - estimated population in 2023 by specified city or statewide.\n\033[1mGrowth\033[0m <cityName>/Texas - percent change from 2020 to 2023, by city or statewide.")

def quit(): # This function exits the dashboard.
    print("\033[1mThank you for using the Texas Cities Population Database Dashboard.  Goodbye!\033[0m")
    exit()

def cities():   # This function lists all the cities in Texas.
    _, city_names = read_city_data()
    print("\n".join(city_names))

def census2020(city_name):
    # This function prints the population of a city in 2020.
    city_data, city_names = read_city_data()
    city_name = city_name.title()
    if city_name == "Texas":
        total_census = city_data[city_name][0]
        print(f"Total population in Texas in the 2020 Census: {total_census}")
    elif city_name in city_data:
        population = city_data[city_name][0]
        if city_name in city_names:
            print(f"{city_name}'s total population in the 2020 Census: {population}")
        else:
            print(f"{city_name} is not in Texas")
    else:
        print(f"{city_name} not found in the database.")

def estimated2023(city_name):
    # This function prints the estimated population of a city in 2023.
    city_data, city_names = read_city_data()
    city_name = city_name.title()
    if city_name == "Texas":
        total_estimated = city_data[city_name][1]
        print(f"Total population in Texas in the 2023 Census: {total_estimated}")
    elif city_name in city_data:
        population = city_data[city_name][1]
        if city_name in city_names:
            print(f"{city_name}'s estimated population in 2023:: {population}")
        else:
            print(f"{city_name} is not in Texas")
    else:
        print(f"{city_name} not found in the database.")

def growth(city_name):   
    # This function prints the percent change from 2020 to 2023, by city or statewide.
    city_data, city_names = read_city_data()
    city_name = city_name.title()
    if city_name == "Texas":
        total_census = city_data[city_name][0]
        total_estimated = city_data[city_name][1]
        total_growth = ((total_estimated - total_census) / total_census) * 100
        print(f"Texas had percent population change from 2020 to 2023: {total_growth:.2f} %")
    elif city_name in city_data:    
        total_census = city_data[city_name][0]
        total_estimated = city_data[city_name][1]
        total_growth = ((total_estimated - total_census) / total_census) * 100
        if city_name in city_names:
            print(f"{city_name}'s percent population change from 2020 to 2023: {total_growth:.2f} %")
        else:
            print(f"{city_name} is not in Texas")
    else:
        print(f"{city_name} not found in the database.")

# makes for a faster time time complexity then not using a dict here
command_dict = {
    "help": help,
    "quit": quit,
    "cities": cities,
    "census": census2020,
    "estimated": estimated2023,
    "growth": growth
}

def main():
    # Welcome prompt
    print("\n\033[1mWelcome to the Texas Cities Population Dashboard.\033[0m\nThis provides census data from the 2020 census and\nestimated population data in Texas as of 2023.")
    print("\nCreating dictionary from file: citiesData.csv\n")
    print("Enter any of the following commands:\n\033[1mHelp\033[0m - list available commands;\n\033[1mQuit\033[0m - exit this dashboard;\n\033[1mCities\033[0m - list all Texas cities\n\033[1mCensus\033[0m <cityName>/Texas - population in 2020 census by specified city or statewide;\n\033[1mEstimated\033[0m <cityName>/Texas - estimated population in 2023 by specified city or statewide.\n\033[1mGrowth\033[0m <cityName>/Texas - percent change from 2020 to 2023, by city or statewide.")

    # loop for the input promts
    while True:
        command = input("\n\033[1mEnter a command:\033[0m ").lower()
        if command in command_dict.keys():
            # Couldn't figure out how to keep these if statements within one if statement
            # regardless these allow for an extra input statement when needing to find a city name or Texas. 
            if command == "census":
                input_str = input("\nEnter city name or Texas (e.g. <cityName>/Texas): ")
                command_dict[command](input_str)
            elif command == "estimated":
                input_str = input("\nEnter city name or Texas (e.g. <cityName>/Texas): ")
                command_dict[command](input_str)
            elif command == "growth":
                input_str = input("\nEnter city name or Texas (e.g. <cityName>/Texas): ")
                command_dict[command](input_str) 
            else:
                command_dict[command]()      
        else:
            print('Command not found. Type "Help" for command options.')


if __name__ == "__main__":
    main()
