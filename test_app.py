import unittest
import unittest.mock
import csv
from app import abv_range, ibu_range, beer_type_count, all_brewery_beers, random_beers, breweries_csv, beers_csv


class TestApp(unittest.TestCase):
    def test_abv_range(self):
        # I tried to use as many different argument types and situations so
        # the function can run with any argument.
        result_1 = "Beers between an ABV of 0.05 and 0.07: 1478"
        self.assertEqual(abv_range(0.05, 0.07), result_1)
        result_2 = "Beers between an ABV of 0 and 0: 0"
        self.assertEqual(abv_range(0, 0), result_2)
        result_3 = "Beers between an ABV of 50 and 100: 0"
        self.assertEqual(abv_range("50", 100), result_3)
        result_4 = "Lower parameter cannot be over higher parameter or below 0 for ABV search."
        self.assertEqual(abv_range(-.05, .02), result_4)
        self.assertEqual(abv_range(.07, .05), result_4)
        with self.assertRaises(TypeError):
            abv_range("abc", .07)
        with self.assertRaises(TypeError):
            abv_range("0.06", "zero")

    def test_ibu_range(self):
        result_1 = "Beers between an IBU of 20 and 30: 357"
        self.assertEqual(ibu_range(20, 30), result_1)
        result_2 = "Beers between an IBU of 0 and 0: 0"
        self.assertEqual(ibu_range(0, 0), result_2)
        result_3 = "Beers between an IBU of 50 and 100: 465"
        self.assertEqual(ibu_range("50", 100), result_3)
        result_4 = "Beers between an IBU of 0.5 and 17: 199"
        self.assertEqual(ibu_range(.5, 17), result_4)
        result_5 = "Lower parameter cannot be over higher parameter or below 0 for IBU search."
        self.assertEqual(ibu_range(-5, 10), result_5)
        self.assertEqual(ibu_range(60, .40), result_5)
        with self.assertRaises(TypeError):
            ibu_range("abc", .07)
        with self.assertRaises(TypeError):
            ibu_range("20", "zero")

    def test_beer_type_count(self):
        result_1 = "Amount of Tripel beers: 11"
        self.assertEqual(beer_type_count("tripel"), result_1)
        result_2 = "Amount of Cider beers: 37"
        self.assertEqual(beer_type_count("CiDeR"), result_2)
        result_3 = "Input for specified beer type returned no results."
        self.assertEqual(beer_type_count("American IPPA"), result_3)
        # Spelled IPPA for spelling mistake
        self.assertEqual(beer_type_count("1234"), result_3)
        self.assertEqual(beer_type_count("&"), result_3)

    def test_all_brewery_beers(self):
        result_1 = "Tapistry Brewing beers: Peck's Porter, Reactor, Mr. Orange"
        self.assertEqual(all_brewery_beers("Tapistry brewing"), result_1)
        result_2 = "Harpoon Brewery beers: UFO Gingerland, The Long Thaw White IPA, Honey Cider, Harpoon Summer Beer, Harpoon IPA, UFO Pumpkin, Harpoon Octoberfest, Harpoon IPA (2012), Harpoon Summer Beer (2012), UFO White, Harpoon Summer Beer (2010), Harpoon IPA (2010)"
        self.assertEqual(all_brewery_beers("HarPoon BREwery"), result_2)
        result_3 = "Brewery entered for beer list not found."
        self.assertEqual(all_brewery_beers("nighshift brewery"), result_3)
        self.assertEqual(all_brewery_beers(1234), result_3)
        self.assertEqual(all_brewery_beers("&"), result_3)

    def test_random_beers(self):
        # I tried to think outside the box for this since it is a randomized function
        # My solution was to breakdown the return string and count the beers that were
        # returned to see if it matched the argument passed in
        random_length_check_1 = len((random_beers()[14:]).split(","))
        result_1 = 10
        self.assertEqual(random_length_check_1, result_1)
        random_length_check_2 = len((random_beers(5)[14:]).split(","))
        result_2 = 5
        self.assertEqual(random_length_check_2, result_2)
        random_length_check_3 = len((random_beers(20)[14:]).split(","))
        result_3 = 20
        self.assertEqual(random_length_check_3, result_3)
        result_4 = "Requested random search amount is larger than available beers."
        self.assertEqual(random_beers(4000), result_4)
        result_5 = "Invalid input for random beers. Please input a whole number above 0."
        self.assertEqual(random_beers("abc"), result_5)
        self.assertEqual(random_beers("twenty"), result_5)
        self.assertEqual(random_beers(-30), result_5)


if __name__ == '__main__':
    unittest.main()
