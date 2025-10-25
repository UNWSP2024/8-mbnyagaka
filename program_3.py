# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys,
# and their capitals as values.
# The program should then randomly quiz the user by displaying the name of a state
# and asking the user to enter the state's capital.
# The program should count of the number of correct and incorrect responses.
# (You could alternatively use another country and provinces,
# or countries of the world and capitals).]

import random

def capital_quiz():
    # Dictionary of states and their capitals
    states_capitals = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "Saint Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson City",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",
        "New York": "Albany",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismarck",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "West Virginia": "Charleston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne"
    }

    # Initialize counters
    correct = 0
    incorrect = 0

    # Convert keys to list and shuffle order
    states = list(states_capitals.keys())
    random.shuffle(states)

    # Ask the user how many questions they want
    num_questions = int(input("How many states would you like to be quizzed on? (1–50): "))

    for state in states[:num_questions]:
        answer = input(f"What is the capital of {state}? ").strip()
        if answer.lower() == states_capitals[state].lower():
            print("✅ Correct!")
            correct += 1
        else:
            print(f"❌ Incorrect. The capital of {state} is {states_capitals[state]}.")
            incorrect += 1

    # Display summary
    print("\nQuiz complete!")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")

# Run the quiz
capital_quiz()