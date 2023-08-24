import random
from datetime import datetime
from collections import Counter
from tqdm import tqdm  # Import the tqdm module


def generate_random_birthdays(n):
    birthdays = []
    for _ in range(n):
        month = random.randint(1, 12)
        max_day = 31 if month in [1, 3, 5, 7, 8,
                                  10, 12] else 30 if month != 2 else 29
        day = random.randint(1, max_day)
        birthdays.append((month, day))
    return birthdays


def has_duplicate_birthdays(birthdays):
    birthday_counts = Counter(birthdays)
    return any(count > 1 for count in birthday_counts.values())


def birthday_paradox_simulation(group_size, num_simulations):
    matching_birthday_count = 0

    # Use tqdm to create a progress bar
    for _ in tqdm(range(num_simulations), desc="Simulations", unit="sim"):
        birthdays = generate_random_birthdays(group_size)
        if has_duplicate_birthdays(birthdays):
            matching_birthday_count += 1
    return matching_birthday_count / num_simulations * 100


def main():
    print("Birthday Paradox Simulation")
    group_size = int(input("How many people in the group? "))
    num_simulations = 100000
    matching_percentage = birthday_paradox_simulation(
        group_size, num_simulations)

    print(f"\nOut of {num_simulations} simulations of {group_size} people, "
          f"there was a matching birthday in that group {matching_percentage:.2f}% of the time.")

    if matching_percentage > 50:
        print("That's more than you would expect!")


if __name__ == "__main__":
    main()
