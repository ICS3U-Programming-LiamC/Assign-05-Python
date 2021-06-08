#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: June 8, 2021
# This program calcualtes the area of a triangle using Heron's formula

import math


# this calculates the semi perimeter for use in the area funciton
def semi(a_semi, b_semi, c_semi):
    semi_perimeter_before_div = a_semi + b_semi + c_semi
    semi_perimeter = semi_perimeter_before_div / 2
    return semi_perimeter


# this calculates the area using Heron's formula
def area(semi_area, a_area, b_area, c_area):
    area_step1 = semi_area * (semi_area - a_area)
    area_step2 = area_step1 * (semi_area - b_area) * (semi_area - c_area)
    area_step3 = math.sqrt(area_step2)
    return area_step3


# these three funcitons calculate one angle of the triangle each
def angle_A(len_a, len_b, len_c):
    # makes the ^2 version of all the lengths
    pow_a = math.pow(len_a, 2)
    pow_b = math.pow(len_b, 2)
    pow_c = math.pow(len_c, 2)

    # this is cosine law but reorganized to fit the circumstances
    angle_A = (pow_b + pow_c - pow_a) / (2*len_b*len_c)
    angle_A = math.acos(angle_A)
    # converts the radians to degrees
    angle_A = angle_A * (180/math.pi)

    # returns the angle
    return angle_A


def angle_B(len_a, len_b, len_c):
    pow_a = math.pow(len_a, 2)
    pow_b = math.pow(len_b, 2)
    pow_c = math.pow(len_c, 2)

    angle_B = pow_a + pow_c - pow_b
    angle_B = angle_B / (2*len_a*len_c)
    angle_B = math.acos(angle_B)
    angle_B = angle_B * (180/math.pi)

    return angle_B


def angle_C(len_a, len_b, len_c):
    pow_a = math.pow(len_a, 2)
    pow_b = math.pow(len_b, 2)
    pow_c = math.pow(len_c, 2)

    angle_C = (pow_a + pow_b - pow_c) / (2*len_a*len_b)
    angle_C = math.acos(angle_C)
    angle_C = angle_C * (180/math.pi)

    return angle_C


# greets the user
def greet():
    print("Welcome, this program takes 3 side lengths of a triangle, then\
 it calculates the area")


# main function
def main():
    # get sides a, b, c, and units
    side_a = input("What is side length a: ")
    side_b = input("What is side length b: ")
    side_c = input("What is side length c: ")
    units = input("What are your units: ")

    # make sure the users num can be an integer
    try:
        side_a = float(side_a)
        side_b = float(side_b)
        side_c = float(side_c)

        # A blob of function calls, gets all the results from the functions
        semi_perim = semi(side_a, side_b, side_c)
        area_final = area(semi_perim, side_a, side_b, side_c)
        result_angle_A = angle_A(side_a, side_b, side_c)
        result_angle_B = angle_B(side_a, side_b, side_c)
        result_angle_C = angle_C(side_a, side_b, side_c)

        # print the area
        print("The area of your triangle is {:.2f}{}²".format
              (area_final, units))
        # pritn the angles
        print("∠A of your triangle is {:.4f}°".format(result_angle_A))
        print("∠B of your triangle is {:.4f}°".format(result_angle_B))
        print("∠C of your triangle is {:.4f}°".format(result_angle_C))

    # if there was an error with the conversion from string to int
    except ValueError:
        print("All inputs must be real numbers")


if __name__ == "__main__":
    greet()
    main()
