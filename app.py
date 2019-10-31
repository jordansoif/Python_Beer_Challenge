import csv
import random

with open("breweries.csv") as breweries_csv:
    csv_reader_breweries = csv.reader(breweries_csv)  # open CSV file to read
    header_breweries = next(csv_reader_breweries)  # header for CSV file
    data_breweries = [row for row in csv_reader_breweries]
    # data_breweries is all data in CSV file besides header


with open("beers.csv") as beers_csv:  # same as above, for beers.csv
    csv_reader_beers = csv.reader(beers_csv)
    header_beers = next(csv_reader_beers)
    data_beers = [row for row in csv_reader_beers]


def abv_range(lower_range_abv, higher_range_abv):
    try:
        count_abv = 0
        if float(lower_range_abv) < 0 or float(higher_range_abv) < float(lower_range_abv):
            return ("Lower parameter cannot be over higher parameter or below 0 for ABV search.")
        for line in data_beers:
            if len(line[1]) != 0:  # to ignore empty cells
                if float(line[1]) >= float(lower_range_abv) and float(line[1]) <= float(higher_range_abv):
                    count_abv += 1  # add to counter when a beer matches the search criteria
        return ("Beers between an ABV of " + str(lower_range_abv) +
                " and " + str(higher_range_abv) + ": " + str(count_abv))
    except:
        raise TypeError(
            "Invalid input. Please input numbers only for ABV search.")


def ibu_range(lower_range_ibu, higher_range_ibu):
    try:
        if float(lower_range_ibu) < 0 or float(higher_range_ibu) < float(lower_range_ibu):
            return ("Lower parameter cannot be over higher parameter or below 0 for IBU search.")
        count_ibu = 0
        for line in data_beers:
            if len(line[2]) != 0:  # to ignore empty cells
                if float(line[2]) >= float(lower_range_ibu) and float(line[2]) <= float(higher_range_ibu):
                    count_ibu += 1
        return ("Beers between an IBU of " + str(lower_range_ibu) + " and " + str(higher_range_ibu) + ": " + str(count_ibu))
    except:
        raise TypeError(
            "Invalid input. Please input numbers only for IBU search.")


def beer_type_count(beer_type):
    count_beer_type = 0
    for line in data_beers:
        if len(line[5]) != 0:
            # casefold is used for comparison since there are foreign letters, which makes the search more accurate than using something like .lower()
            try:
                if line[5].casefold() == beer_type.casefold():
                    count_beer_type += 1
            except:
                continue
    if count_beer_type > 0:
        return ("Amount of " + beer_type.title() +
                " beers: " + str(count_beer_type))
    else:
        return ("Input for specified beer type returned no results.")


def all_brewery_beers(brewery_name):
    brewery_beers = []
    try:
        for line in data_breweries:  # find brewery in brewery.csv
            if line[1].casefold() == brewery_name.casefold():
                # brewery_id needed, beers.csv doesn't use brewery name
                brewery_id = line[0]
        for line in data_beers:
            if line[6] == brewery_id:
                # add beer name to list if brewery_id matches
                brewery_beers.append(line[4])
        if len(brewery_beers) > 0:
            return (brewery_name.title() + " beers: " + (', '.join(brewery_beers)))
    except:
        return ("Brewery entered for beer list not found.")


def random_beers(search_amount=10):
    random_beers = []
    try:
        # find total number of rows in data_beers
        total_rows = sum(1 for row in data_beers)
        if int(search_amount) > total_rows:
            return ("Requested random search amount is larger than available beers.")
        random_num_generator = random.sample(
            range(total_rows - 1), int(search_amount))
        # random.sample use to only find unique values, no duplicates. (total_rows - 1) used to account for line[0] starting at 0
        for value in random_num_generator:  # loop through random numbers generated
            for line in data_beers:
                if line[0] == str(value):  # line[0] is unique value
                    random_beers.append(line[4])
        return ("Random Beers: " + (', '.join(random_beers)))
    except:
        return ("Invalid input for random beers. Please input a whole number above 0.")


# Input Fields and their corresponding functions for running in terminal
def challenge_questions():
    print("Search to see how many beers are between specified ABV's.")
    lower_abv_input = input("Enter lower search parameter of ABV search:")
    higher_abv_input = input("Enter higher search parameter of ABV search:")
    print(abv_range(lower_abv_input, higher_abv_input))

    print("Search to see how many beers are between specified IBU's.")
    lower_ibu_input = input("Enter lower search parameter of IBU search:")
    higher_ibu_input = input("Enter higher search parameter of IBU search:")
    print(ibu_range(lower_ibu_input, higher_ibu_input))

    print("Search a beer type to see how many beers are that type.")
    beer_type_input = input("Enter beer type:")
    print(beer_type_count(beer_type_input))

    brewery_name_input = input(
        "Enter brewery name to find their available beers:")
    print(all_brewery_beers(brewery_name_input))

    random_beers_input = input("Enter a number to find that many random beers:")
    print(random_beers(random_beers_input))


if __name__ == '__main__':
    challenge_questions()
