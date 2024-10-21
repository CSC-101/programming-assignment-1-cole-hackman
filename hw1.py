import unittest
import data
import math

from data import Employee, Price, Rectangle, Circle, Book, Employee, Point

# Write your functions for each part in the space below.

# Part 1
# This function accepts a string as input, and returns the number of vowels that appear in the string
def vowel_count(inputStr: str) -> int:
    vowelNum= 0
    for char in inputStr.lower():
        if char in ("a","e","i","o","u"):
            vowelNum += 1
    return vowelNum


# Part 2
# This function accepts a list of nested lists, and returns the nested lists of length 2
def short_lists(inputList: list[list[int]])-> list:
    newList = []
    for sublist in inputList:
        if len(sublist) == 2:
            newList.append(sublist)
    return newList


# Part 3
# This function accepts a list of nested lists, and returns the nested lists where pairs of two integers are in ascending order
def ascending_pairs(inputList: list[list[int]]):
    newList = []
    for sublist in inputList:
        if len(sublist) == 2:
            if sublist[0] > sublist[1]:
                sublist[0], sublist[1] = sublist[1], sublist[0]
            newList.append(sublist)
        else:
            newList.append(sublist)
    return newList


# Part 4
# This function accepts two Price objects, and returns a new Price object that is the sum of the two
def add_prices(price1: Price, price2: Price) -> Price:
    sum_dollars = price1.dollars + price2.dollars
    sum_cents = price1.cents + price2.cents
    if (sum_cents) >= 100:
        sum_dollars += (sum_cents // 100)
        sum_cents = sum_cents % 100
    return Price(sum_dollars, sum_cents)


# Part 5
# This function accepts a Rectangle object, and returns the area of the rectangle
def rectangle_area(rectangle: Rectangle) -> float:
    width = abs(rectangle.bottom_right.x - rectangle.top_left.x)
    height = abs(rectangle.top_left.y - rectangle.bottom_right.y)
    return width * height

# Part 6
# This function accepts an author's name and a list of Book objects, and returns a list of books written by that author
def books_by_author(author: str, book_catalog: list[Book]) -> list[Book]:
    same_author = [book for book in book_catalog if author in book.authors]
    return same_author


# Part 7
# This function accepts a Rectangle object, and returns a Circle object that bounds the rectangle
def circle_bound(rectangle: Rectangle) -> Circle:
    circle_center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    circle_center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    center = Point(circle_center_x, circle_center_y)

    radius = math.sqrt((circle_center_x - rectangle.bottom_right.x)**2 + (circle_center_y - rectangle.bottom_right.y)**2)
    return Circle(center, radius)


# Part 8
# This function accepts a list of Employee objects, and returns a list of employees who earn under the average pay rate
def below_pay_average(employees: list[Employee]) -> list:
    if len(employees) == 0:
        return []

    pay_average = sum(employee.pay_rate for employee in employees) / len(employees)
    below_pay_employees = [employee.name for employee in employees if employee.pay_rate < pay_average]
    return below_pay_employees



