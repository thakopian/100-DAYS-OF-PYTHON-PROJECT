# list exercise replit https://repl.it/@thakopian/day-4-list-practice#main.py

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


# print any value from 0-49 index avilable in the 50 states list
print(states_of_america[1])

# modify any value by choosing the index value and assigning it a new value
states_of_america[1] = "PencilTown"

# append a value to the end of the list
states_of_america.append("ThunderDome")

# extend the list with a new list
states_of_america.extend(["LegoLand", "DisneyLand", "JurassicPark"])

# print the list with the new values
print(states_of_america)
