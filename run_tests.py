#!/usr/bin/env python3
"""
Simple test runner for ToyRobot tests.
"""

import unittest
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_tests():
    """Run the ToyRobot tests."""
    print("Running ToyRobot Unit Tests...")
    print("=" * 50)

    try:
        from test_robot import TestToyRobot

        suite = unittest.TestLoader().loadTestsFromTestCase(TestToyRobot)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)

        print()
        print("=" * 50)
        if result.wasSuccessful():
            print(f"All {result.testsRun} tests passed!")
        else:
            print(f"{len(result.failures + result.errors)} tests failed")

        return result.wasSuccessful()

    except ImportError as e:
        print(f"Could not run tests: {e}")
        return False


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
