# Toy Robot Simulator

A Python implementation for the Cellular Origins Code Challenge

## Description

The Toy Robot Simulator is an application that simulates a toy robot moving on a square tabletop of dimensions 5 units x 5 units. The robot can move around the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table is prevented, however further valid movement commands are still allowed.

## Requirements

- Python 3.7+
- Virtual environment (recommended)

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd Toy_Robot_Simulator
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv Toy_Robot_Simulator_Env.venv

   # On Windows:
   Toy_Robot_Simulator_Env.venv\Scripts\activate

   # On macOS/Linux:
   source Toy_Robot_Simulator_Env.venv/bin/activate
   ```

3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Example

```python
from ToyRobot import Robot

# Create a robot instance
robot = Robot()

# Place the robot on the table
robot.place(0, 0, 'NORTH')

# Move and rotate the robot
robot.move()
robot.right()
robot.move()

# Get current position
print(robot.report())  # Output: 1,1,EAST
```

### Running the Simulator

```bash
python ToyRobot.py
```

### Interactive Console Application

For an interactive experience, use the console application:

```bash
python ToyRobot_ConsoleApp.py
```

The console application provides a user-friendly interface with:

- **Interactive Commands**: Type commands directly into the console
- **Visual Table Display**: See the robot's position with directional arrows (↑ ↓ → ←)
- **Real-time Feedback**: Immediate confirmation of actions and errors
- **Built-in Help**: Type `HELP` to see all available commands
- **Input Validation**: Helpful error messages for invalid commands

#### Console Commands

- `PLACE X,Y,F` - Place robot at position (X,Y) facing direction F
  - Example: `PLACE 0,0,NORTH`
- `MOVE` - Move robot one step forward
- `LEFT` - Turn robot 90 degrees left
- `RIGHT` - Turn robot 90 degrees right
- `REPORT` - Show robot's current position
- `HELP` - Display command help
- `QUIT` or `EXIT` - Exit the application

## Robot Commands

The robot understands the following commands:

### `place(x, y, f)`

- **Description**: Places the robot on the table at position (x, y) facing direction f
- **Parameters**:
  - `x` (int): X coordinate (0-4)
  - `y` (int): Y coordinate (0-4)
  - `f` (str): Facing direction ('NORTH', 'SOUTH', 'EAST', 'WEST')
- **Returns**: `True` if placement successful, `False` otherwise

### `move()`

- **Description**: Moves the robot one unit forward in the current facing direction
- **Safety**: Will not move if it would cause the robot to fall off the table
- **Returns**: `True` if move successful, `False` otherwise

### `left()`

- **Description**: Rotates the robot 90 degrees to the left (counterclockwise)
- **Returns**: `True` if rotation successful, `False` if robot not placed

### `right()`

- **Description**: Rotates the robot 90 degrees to the right (clockwise)
- **Returns**: `True` if rotation successful, `False` if robot not placed

### `report()`

- **Description**: Reports the current position and facing direction
- **Returns**: String in format "X,Y,FACING" or error message if not placed

## Table Coordinates

The tabletop is a 5x5 grid with coordinates:

```
(0,4) (1,4) (2,4) (3,4) (4,4)
(0,3) (1,3) (2,3) (3,3) (4,3)
(0,2) (1,2) (2,2) (3,2) (4,2)
(0,1) (1,1) (2,1) (3,1) (4,1)
(0,0) (1,0) (2,0) (3,0) (4,0)
```

- **Origin (0,0)**: Bottom-left corner
- **Directions**:
  - NORTH: Towards increasing Y
  - SOUTH: Towards decreasing Y
  - EAST: Towards increasing X
  - WEST: Towards decreasing X

## Example Test Cases

```python
# Test Case 1
robot = Robot()
robot.place(0, 0, 'NORTH')
robot.move()
print(robot.report())  # Expected: 0,1,NORTH

# Test Case 2
robot = Robot()
robot.place(0, 0, 'NORTH')
robot.left()
print(robot.report())  # Expected: 0,0,WEST

# Test Case 3
robot = Robot()
robot.place(1, 2, 'EAST')
robot.move()
robot.move()
robot.left()
robot.move()
print(robot.report())  # Expected: 3,3,NORTH
```

## Unit Tests

This project includes comprehensive unit tests to ensure the robot functionality works correctly.

### Running Tests

To run the unit tests, use the following command:

```bash
python run_tests.py
```

### Test Coverage

The test suite includes 12 unit tests covering:

- **Core Functionality**: Placement, movement, rotation, and reporting
- **Edge Cases**: Boundary protection and invalid input handling
- **Error Handling**: Commands before placement and invalid coordinates
- **Input Validation**: Case sensitivity and coordinate bounds

### Test Results

```
Running ToyRobot Unit Tests...
==================================================
Ran 12 tests in 0.002s
All 12 tests passed!
```

The unit tests ensure the robot:

- Prevents falling off the table
- Validates all input parameters
- Handles edge cases gracefully
- Maintains state correctly

## Safety Features

- **Boundary Protection**: Robot cannot move outside the 5x5 table
- **Placement Validation**: Invalid coordinates or directions are rejected
- **State Checking**: Commands ignored until robot is properly placed
- **Error Handling**: Graceful handling of invalid operations

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Future Enhancements

- [ ] GUI interface with Tkinter
- [x] Command-line interface for interactive use ✅
- [ ] Multiple robots on the same table
- [ ] Obstacle placement and navigation
- [ ] Path recording and playback
- [x] Unit tests with unittest ✅
- [ ] Configuration file support
- [ ] Command history and replay functionality
- [ ] Save/load robot sessions

---
