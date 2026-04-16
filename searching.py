from pathlib import Path
import json

import time
import matplotlib.pyplot as plt
from generators import unordered_sequence
from generators import  ordered_sequence

def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name

    with open(file_path, "r") as file:
        data = json.load(file)

    allowed_fields = ["unordered_numbers", "ordered_numbers", "dna_sequence"]
    if field in allowed_fields:
        return(data[field])


def linear_search(seq, number):
    positions = []
    count = 0

    for i, x in enumerate(seq, start=0):
        if x == number:
            positions.append(i)
            count += 1
    return positions, count

def binary_search(seq, target):
    left = 0
    right = len(seq) -1

    middle = (left + right) // 2

    while left <= right:
        if seq[middle] == target:
            return middle
        elif seq[middle] < target:
            left = middle + 1
            middle = (left + right) // 2
        else:
            right = middle - 1
            middle = (left + right) // 2
    return None



sizes = [100, 500, 1000, 5000, 10000]
linear_times = []
binary_times = []
target = 54

for i in range(len(sizes)):
    ordered = ordered_sequence(sizes[i])
    unordered = unordered_sequence(sizes[i])

    #     linear_search
    start = time.perf_counter()
    linear_search(unordered, target)
    end = time.perf_counter()
    linear_times.append(end - start)

        # binary_search
    start = time.perf_counter()
    binary_search(ordered, target)
    end = time.perf_counter()
    binary_times.append(end - start)


plt.plot(sizes, linear_times)
plt.plot(sizes, binary_times)

plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.show()



def pattern_search(seq, target = "ATA"):
    for i in range(len(seq)):
        kodon = seq[i:i:2]
        if kodon == target:




def main():
# nacitani dat
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    ordered_numbers = read_data("sequential.json", "ordered_numbers")
    print(ordered_numbers)

# funkce linear search
    number = 5
    print(linear_search(sequential_data, number))

# funkce binary search
    target = 5
    result = binary_search(ordered_numbers, target)

#  funkce pattern search


if __name__ == "__main__":
    main()





#
