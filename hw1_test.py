import unittest
import math
from hw1 import vowel_count, short_lists, ascending_pairs, add_prices, rectangle_area, books_by_author, circle_bound, below_pay_average
from data import Price, Point, Rectangle, Circle, Book, Employee
# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        result = vowel_count("hello")
        expected = 2
        self.assertEqual(result, expected)

    def test_vowel_count_2(self):
        result = vowel_count("by")
        expected = 0
        self.assertEqual(result, expected)


    # Part 2
    def test_short_lists_1(self):
        result = short_lists([[3, 4], [1, 2, 9, 0], [1], [5, 6]])
        expected = [[3, 4], [5, 6]]
        self.assertEqual(result, expected)

    def test_short_lists_2(self):
        result = short_lists([[3, 4, 8], [1, 2, 9, 0], [1], [7, 5, 6]])
        expected = []
        self.assertEqual(result, expected)


    # Part 3
    def test_ascending_pairs_1(self):
        result = ascending_pairs([[3, 3], [6, 4], [5, 1]])
        expected = [[3, 3], [4, 6], [1, 5]]
        self.assertEqual(result, expected)

    def test_ascending_pairs_2(self):
        result = ascending_pairs([[6, 3], [9, 4], [1, 1]])
        expected = [[3, 6], [4, 9], [1, 1]]
        self.assertEqual(result, expected)


    # Part 4
    def test_add_prices_1(self):
        result = add_prices(Price(1, 75), Price(2, 50))
        expected = Price(4, 25)
        self.assertEqual(result.dollars, expected.dollars)
        self.assertEqual(result.cents, expected.cents)

    def test_add_prices_2(self):
        result = add_prices(Price(1, 2), Price(2, 99))
        expected = Price(4, 1)
        self.assertEqual(result.dollars, expected.dollars)
        self.assertEqual(result.cents, expected.cents)


    # Part 5
    def test_rectangle_area_1(self):
        result = rectangle_area(Rectangle(Point(1,5), Point(6,1)))
        expected = 20
        self.assertEqual(result, expected)

    def test_rectangle_area_2(self):
        result = rectangle_area(Rectangle(Point(0,10), Point(10,0)))
        expected = 100
        self.assertEqual(result, expected)


    # Part 6
    def test_books_by_author_1(self):
        b1 = Book("X Author", ["A Book"])
        b2 = Book("Y Author", ["B Book"])
        b3 = Book("X Author", ["C Book"])
        result = books_by_author("X Author", [b1, b2, b3])
        expected = [b1, b3]
        self.assertEqual(result, expected)

    def test_books_by_author_12(self):
        b1 = Book("X Author", ["A Book"])
        b2 = Book("Y Author", ["B Book"])
        b3 = Book("Z Author", ["C Book"])
        result = books_by_author("Z Author", [b1, b2, b3])
        expected = [b3]
        self.assertEqual(result, expected)

    # Part 7
    def test_circle_bound_1(self):
        result = circle_bound(Rectangle(Point(0.0,4.0), Point(4.0,0.0)))
        expected = Circle(Point(2.0,2.0), 2.8284271247461903)
        self.assertEqual(result.center.x, expected.center.x)
        self.assertEqual(result.center.y, expected.center.y)
        self.assertAlmostEqual(result.radius, expected.radius)

    def test_circle_bound_2(self):
        result = circle_bound(Rectangle(Point(10.0,8.0), Point(15.0,4.0)))
        expected = Circle(Point(12.5,6.0), 3.2015621187)
        self.assertEqual(result.center.x, expected.center.x)
        self.assertEqual(result.center.y, expected.center.y)
        self.assertAlmostEqual(result.radius, expected.radius)
    # Part 8
    def test_below_pay_average_1(self):
        result = below_pay_average([Employee("Bob", 10), Employee("Jake", 20), Employee("Charlie", 30)])
        expected = ["Bob"]
        self.assertEqual(result, expected)

    def test_below_pay_average_1(self):
        result = below_pay_average([Employee("Bob", 500), Employee("Jake", 600), Employee("Charlie", 700)])
        expected = ["Bob"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
