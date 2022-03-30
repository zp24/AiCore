import unittest

from my_sum import sum #imports sum() from the my_sum package
from fractions import Fraction


class TestSum(unittest.TestCase): #class inherits from unittest.TestCase
    def test_list_int(self): #method tests a list of integers
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3] #declare variable data with a list of numbers
        result = sum(data) #assign result of my_sum.sum(data) to result variable
        self.assertEqual(result, 6)
        #assert value of result equals 6 by using .assertEqual() on class

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)
        
if __name__ == '__main__': 
    #command-line entry point runs unittest test-runner .main()
    unittest.main()