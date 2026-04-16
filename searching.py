from pathlib import Path
import json

from generators import ordered_sequence


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




def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    number = 5
    print(linear_search(sequential_data, number))


if __name__ == "__main__":
    main()





#
