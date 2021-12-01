"""Tests file """
import logging
import sys
import unittest
import pandas as pd
from pyunitreport import HTMLTestRunner
from calculator.calculator import Calculator

# test data file path, the file is a csv file.

def _init_logger():
    logger = logging.getLogger('LoggingCalculatorResults')  #1
    logger.setLevel(logging.INFO)  #2
    handler = logging.FileHandler('debug.log', mode="w")  #3
    handler.setLevel(logging.INFO)  #4
    formatter = logging.Formatter(
            '%(asctime)s:%(name)s:%(message)s') #5
    handler.setFormatter(formatter)  #6
    logger.propagate = 0
    logger.addHandler(handler)  #7


_init_logger()
_logger = logging.getLogger('LoggingCalculatorResults')

df = pd.read_csv('/done/data.csv',
                 sep=',', )

class TestApp(unittest.TestCase):
    """Test for Calculator program"""
    # this is the Calculator class instance.
    calculator = None

    # execute before every test case function run.
    def setUp(self):
        self.calculator = Calculator()
        print('')
        print('setUp')

    # execute after every test case function run.
    def tearDown(self):
        # release the Calculator object.
        if self.calculator is not None:
            self.calculator = None
        print('')
        print('tearDown')

    def test_0001_add(self):
        """Case1:Addition"""
        print('')
        print('******test_addition******')

        # get each row text from the csv file.

        # the first column in the text line is x value.
        operation = df.loc[0][0]
        # the second column in the text line is y value.
        x = df.loc[0][1]
        y = df.loc[0][2]
        # the third column in the text line is (x + y) value.
        expect_result = df.loc[0][3]
        # Act
        calc = Calculator()
        result = calc.addition(x, y)
        # result = self.calculator.plus(x, y)
        print(operation, ':', str(x) + ' + ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
        _logger.info("Operation %s ,Input file %s ,record %s,Sum of % s and %s is % s" %( operation,'data.csv',df[df['OPERATION'] == 'ADDITION'].index[0],x, y, expect_result))
        # Assert
        self.assertEqual(float(result), float(expect_result))

    def test_0002_subtract(self):
        """Case2 :Subtraction"""
        print('')
        print('******test_subtract******')
        operation = df.loc[1][0]
        x = df.loc[1][1]
        y = df.loc[1][2]
        # the third column in the text line is (x - y) value.
        expect_result = df.loc[1][3]
        # result = self.calculator.minus(x, y)
        calc = Calculator()
        result = calc.subtraction(x, y)

        print(operation, ':', str(x) + ' - ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
        _logger.info("Operation %s ,Input file %s ,Record %s,Difference of % s and %s is % s" % (
        operation, 'data.csv', df[df['OPERATION'] == 'SUBTRACTION'].index[0], x, y, expect_result))
        self.assertEqual(float(result), float(expect_result))

    def test_0003_multiply(self):
        """Case4 :Multiplication"""
        print('')
        print('******test_multiple******')
        operation = df.loc[2][0]
        x = df.loc[2][1]
        y = df.loc[2][2]
        # the third column in the text line is (x * y) value.
        expect_result = df.loc[2][3]
        calc = Calculator()
        result = calc.multiplication(x, y)
        # result = self.calculator.multiple(x, y)

        print(operation, ':', str(x) + ' * ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
        _logger.info("Operation %s ,Input file %s ,Record %s,Product of % s and %s is % s" % (
        operation, 'data.csv', df[df['OPERATION'] == 'MULTIPLICATION'].index[0], x, y, expect_result))
        self.assertEqual(float(result), float(expect_result))

    def test_0004_division(self):
        """Case5 :Division"""
        print('')
        print('******test_divide******')
        operation = df.loc[3][0]
        x = df.loc[3][1]
        y = df.loc[3][2]
        # the sixth column in the text line is (x / y) value.
        expect_result = df.loc[3][3]
        calc = Calculator()
        result = calc.division(x, y)
        print(operation, ':', str(x) + ' % ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
        _logger.info("Operation %s ,Input file %s ,Record %s,Division of % s by %s is % s" % (
        operation, 'data.csv', df[df['OPERATION'] == 'DIVISION'].index[0], x, y, expect_result))
        self.assertEqual(float(result), float(expect_result))

    def test_0005_division_zero(self):
        """Case5 :Division"""
        print('')
        print('******test_divide******')
        operation = df.loc[4][0]
        x = df.loc[4][1]
        y = df.loc[4][2]
        # the sixth column in the text line is (x / y) value.
        expect_result = df.loc[4][3]
        calc = Calculator()
        result = calc.division(x, y)
        print(operation, ':', str(x) + ' % ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
        _logger.info("Operation %s ,Input file %s ,Record %s,Division of % s by %s is % s" % (
        operation, 'data.csv', df[df['OPERATION'] == 'DIVISIONBYZERO'].index[0], x, y, 'INVALID-ATTEMPT TO DIVIDE BY ZERO'))
        self.assertRaises(Exception, result)



