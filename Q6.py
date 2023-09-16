def search_city(city_name):
    with open('cities.txt', 'r') as file:
        cities = file.readlines()
        if city_name + '\n' in cities:
            print(f"{city_name} is in the file.")
        else:
            print(f"{city_name} is not in the file.")

city_to_search = "Los Angeles"  # Replace with the city you want to search
search_city(city_to_search)
