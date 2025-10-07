#!/usr/bin/env python3
"""
Unit Tests for ToyRobot

This module contains focused unit tests that demonstrate key functionality
"""

import unittest
from ToyRobot import ToyRobot


class TestToyRobot(unittest.TestCase):
    """Test cases for the ToyRobot class."""

    def setUp(self):
        """Set up a new robot instance for each test."""
        self.robot = ToyRobot()

    def test_initial_state(self):
        """Test robot starts in unplaced state."""
        self.assertFalse(self.robot.is_placed)
        self.assertEqual(self.robot.report(),
                         "Robot is not placed on the table")

    def test_valid_placement(self):
        """Test successful robot placement."""
        result = self.robot.place(2, 3, 'NORTH')
        self.assertTrue(result)
        self.assertTrue(self.robot.is_placed)
        self.assertEqual(self.robot.report(), "2,3,NORTH")

    def test_invalid_placement(self):
        """Test placement with invalid coordinates."""
        result = self.robot.place(-1, 5, 'NORTH')
        self.assertFalse(result)
        self.assertFalse(self.robot.is_placed)

    def test_movement_success(self):
        """Test successful movement within table bounds."""
        self.robot.place(2, 2, 'NORTH')
        result = self.robot.move()
        self.assertTrue(result)
        self.assertEqual(self.robot.report(), "2,3,NORTH")

    def test_movement_blocked_at_edge(self):
        """Test movement is blocked at table edge."""
        self.robot.place(0, 4, 'NORTH')  # Top edge
        result = self.robot.move()
        self.assertFalse(result)
        # Position unchanged
        self.assertEqual(self.robot.report(), "0,4,NORTH")

    def test_movement_before_placement(self):
        """Test movement is ignored before placement."""
        result = self.robot.move()
        self.assertFalse(result)

    def test_left_rotation(self):
        """Test left rotation changes direction correctly."""
        self.robot.place(1, 1, 'NORTH')
        result = self.robot.left()
        self.assertTrue(result)
        self.assertEqual(self.robot.report(), "1,1,WEST")

    def test_right_rotation(self):
        """Test right rotation changes direction correctly."""
        self.robot.place(1, 1, 'NORTH')
        result = self.robot.right()
        self.assertTrue(result)
        self.assertEqual(self.robot.report(), "1,1,EAST")

    def test_rotation_before_placement(self):
        """Test rotation is ignored before placement."""
        left_result = self.robot.left()
        right_result = self.robot.right()
        self.assertFalse(left_result)
        self.assertFalse(right_result)

    def test_case_insensitive_direction(self):
        """Test direction input is case insensitive."""
        result = self.robot.place(1, 1, 'north')
        self.assertTrue(result)
        self.assertEqual(self.robot.facing, 'NORTH')

    def test_invalid_direction(self):
        """Test invalid direction is rejected."""
        result = self.robot.place(1, 1, 'INVALID')
        self.assertFalse(result)
        self.assertFalse(self.robot.is_placed)

    def test_basic_sequence(self):
        """Test a basic command sequence works correctly."""
        # PLACE -> MOVE -> LEFT -> MOVE -> REPORT
        self.robot.place(1, 1, 'EAST')
        self.robot.move()      # Should be at (2,1,EAST)
        self.robot.left()      # Should be at (2,1,NORTH)
        self.robot.move()      # Should be at (2,2,NORTH)

        self.assertEqual(self.robot.report(), "2,2,NORTH")


if __name__ == '__main__':
    unittest.main(verbosity=2)
