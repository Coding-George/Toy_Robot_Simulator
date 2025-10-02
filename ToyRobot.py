class ToyRobot:
    """
    A Robot simulator that can be placed on a table and moved around.
    The robot has position (x, y) and facing direction (North, South, East, West).
    """

    def __init__(self):
        self.x = None
        self.y = None
        self.facing = None
        self.is_placed = False
        self.directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def place(self, x, y, f):
        """
        Place the robot on the table at position (x, y) facing direction f.

        Args:
            x (int): X coordinate (0-4)
            y (int): Y coordinate (0-4)
            f (str): Facing direction ('NORTH', 'SOUTH', 'EAST', 'WEST')
        """

        # Validate coordinates are numbers and that f is a string
        if not (isinstance(x, int) and isinstance(y, int) and isinstance(f, str)):
            return False

        # Validate coordinates (5x5 table: 0-4 for both x and y)
        if 0 <= x <= 4 and 0 <= y <= 4 and f.upper() in self.directions:
            self.x = x
            self.y = y
            self.facing = f.upper()
            self.is_placed = True
            return True
        return False

    def move(self):
        """
        Move the robot one unit forward in the direction it is currently facing.
        The robot will not move if it would fall off the table.
        """
        if not self.is_placed:
            return False

        new_x, new_y = self.x, self.y

        if self.facing == 'NORTH':
            new_y += 1
        elif self.facing == 'SOUTH':
            new_y -= 1
        elif self.facing == 'EAST':
            new_x += 1
        elif self.facing == 'WEST':
            new_x -= 1

        # Check if new position is within table bounds
        if 0 <= new_x <= 4 and 0 <= new_y <= 4:
            self.x = new_x
            self.y = new_y
            return True
        return False

    def left(self):
        """
        Rotate the robot 90 degrees to the left (counterclockwise).
        """
        if not self.is_placed:
            return False

        current_index = self.directions.index(self.facing)
        self.facing = self.directions[(current_index - 1) % 4]
        return True

    def right(self):
        """
        Rotate the robot 90 degrees to the right (clockwise).
        """
        if not self.is_placed:
            return False

        current_index = self.directions.index(self.facing)
        self.facing = self.directions[(current_index + 1) % 4]
        return True

    def report(self):
        """
        Report the current position and facing direction of the robot.

        Returns:
            str: Current position and facing direction, or None if not placed
        """
        if not self.is_placed:
            return "Robot is not placed on the table"

        return f"{self.x},{self.y},{self.facing}"


# Example usage
if __name__ == "__main__":
    # Create a robot instance
    robot = ToyRobot()

    # Test the robot
    print("Testing Robot:")
    print("Initial report:", robot.report())

    # Place the robot
    robot.place(0, 0, 'NORTH')
    print("After placing at (0,0) facing NORTH:", robot.report())

    # Move and rotate
    robot.move()
    print("After moving:", robot.report())

    robot.right()
    print("After turning right:", robot.report())

    robot.move()
    print("After moving:", robot.report())

    robot.left()
    print("After turning left:", robot.report())
