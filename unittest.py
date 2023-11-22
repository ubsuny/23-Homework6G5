import calculus
import unittest
import numpy as np
class RootFindingTest(unittest.TestCase):

    def test_root_print_header(self):
        """
        Tests the `root_print_header` function.
        """
        algorithm = "Simple Search with Step Halving"
        accuracy = 1.0e-6
        expected_output = "\n ROOT FINDING using " + algorithm + "\n Requested accuracy = " + repr(accuracy) + "\n Step     Guess For Root          Step Size      " + "\n ----  --------------------  --------------------" + "\n"
        actual_output = root_print_header(algorithm, accuracy)
        self.assertEqual(actual_output, expected_output)

    def test_root_print_step(self):
        """
        Tests the `root_print_step` function.
        """
        step = 4
        x = 2.718281828459045
        dx = 0.0001
        f_of_x = -1.0
        expected_output = "  4  " + repr(x).ljust(20) + " " + repr(dx).ljust(20) + " " + repr(f_of_x).ljust(20) + "\n"
        actual_output = root_print_step(step, x, dx, f_of_x)
        self.assertEqual(actual_output, expected_output)

    def test_root_max_steps(self):
        """
        Tests the `root_max_steps` function.
        """
        algorithm = "root_simple"
        max_steps = 10
        with self.assertRaises(Exception) as e:
            root_max_steps(algorithm, max_steps)
        self.assertEqual(str(e.exception), " " + algorithm + ": maximum number of steps " + repr(max_steps) + " exceeded\n")

    def test_root_simple(self):
        """
        Tests the `root_simple` function with a linear function.
        """
        f = lambda x: x - 2
        x = 1
        dx = 1
        accuracy = 1.0e-6
        max_steps = 1000
        root, iterations = root_simple(f, x, dx, accuracy, max_steps)
        self.assertEqual(root, 2)
        self.assertAlmostEqual(iterations[-1, 0], root, accuracy)

    def test_root_bisection(self):
        """
        Tests the `root_bisection` function with a quadratic function.
        """
        f = lambda x: x**2 - 4
        x1 = -2
        x2 = 2
        accuracy = 1.0e-6
        max_steps = 1000
        root, iterations = root_bisection(f, x1, x2, accuracy, max_steps)
        self.assertAlmostEqual(root, 2, accuracy)
        self.assertAlmostEqual(iterations[-1, 0], root, accuracy)

    def test_root_secant(self):
        """
        Tests the `root_secant` function with a cubic function.
        """
        f = lambda x: x**3 - 3 * x**2 + 2
        x0 = 1
        x1 = 2
        accuracy = 1.0e-6
        max_steps = 100
        root, iterations = root_secant(f, x0, x1, accuracy, max_steps)
        self.assertAlmostEqual(root, 2, accuracy)
        self.assertAlmostEqual(iterations[-1, 0], root, accuracy)

    def test_root_tangent(self):
        """
        Tests the `root_tangent` function with a quartic function.
        """
        f = lambda x: x**4 - 4 * x**3 + 6 * x**2 - 4 * x + 1
        fp = lambda x: 4 * x**3 - 12 * x**2 + 12 * x - 4
        x0 = 1
        accuracy = 1.0e-6
        max_steps = 100
        root, iterations = root_tangent(f, fp, x0, accuracy, max_steps)
        self.assertAlmostEqual(root, 2, accuracy)
        self.assertAlmostEqual(iterations[-1, 0], root, accuracy)
