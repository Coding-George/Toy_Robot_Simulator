#!/usr/bin/env python3
"""
Toy Robot Console Application

This console application provides an interactive interface to control a toy robot
using the ToyRobot class. The robot can be placed on a 5x5 table and moved around
with various commands.

Commands:
- PLACE X,Y,F: Place the robot at position (X,Y) facing direction F
- MOVE: Move the robot one step forward
- LEFT: Turn the robot 90 degrees left
- RIGHT: Turn the robot 90 degrees right
- REPORT: Display the robot's current position and direction
- HELP: Show available commands
- QUIT/EXIT: Exit the application
"""

from ToyRobot import ToyRobot
import sys


class ToyRobotConsoleApp:
    """Console application for controlling the Toy Robot."""
    
    def __init__(self):
        self.robot = ToyRobot()
        self.running = True
        
    def display_welcome(self):
        """Display welcome message and instructions."""
        print("=" * 60)
        print("Welcome to a Console based Toy Robot Simulator!")
        print("=" * 60)
        print("\nThe robot moves on a 5x5 table (coordinates 0-4)")
        print("Directions: NORTH, SOUTH, EAST, WEST")
        print("\nType 'HELP' to see available commands")
        print("Type 'QUIT' or 'EXIT' to quit the application")
        print("-" * 60)
        
    def display_help(self):
        """Display help information with all available commands."""
        print("\n Available Commands:")
        print("-" * 40)
        print("PLACE X,Y,F  - Place robot at position (X,Y) facing F")
        print("               Example: PLACE 0,0,NORTH")
        print("MOVE         - Move robot one step forward")
        print("LEFT         - Turn robot 90 degrees left")
        print("RIGHT        - Turn robot 90 degrees right")
        print("REPORT       - Show robot's current position")
        print("HELP         - Show this help message")
        print("QUIT/EXIT    - Exit the application")
        print("-" * 40)
        print(" Valid coordinates: 0-4 for both X and Y")
        print(" Valid directions: NORTH, SOUTH, EAST, WEST")
        print()
        
    def parse_place_command(self, command):
        """
        Parse the PLACE command and extract coordinates and direction.
        
        Args:
            command (str): The full command string
            
        Returns:
            tuple: (x, y, facing) or None if invalid
        """
        try:
            # Remove 'PLACE ' prefix and split by comma
            params = command[6:].strip().split(',')
            
            if len(params) != 3:
                raise ValueError("PLACE command requires exactly 3 parameters")
                
            x = int(params[0].strip())
            y = int(params[1].strip())
            facing = params[2].strip().upper()
            
            return x, y, facing
            
        except (ValueError, IndexError) as e:
            print(f"❌ Invalid PLACE command format: {e}")
            print("   Correct format: PLACE X,Y,F (example: PLACE 0,0,NORTH)")
            return None
            
    def execute_command(self, command):
        """
        Execute a robot command.
        
        Args:
            command (str): The command to execute
        """
        command = command.strip().upper()
        
        if not command:
            return
            
        if command in ['QUIT', 'EXIT']:
            self.running = False
            print("Thank you!")
            return
            
        elif command == 'HELP':
            self.display_help()
            return
            
        elif command.startswith('PLACE'):
            params = self.parse_place_command(command)
            if params:
                x, y, facing = params
                if self.robot.place(x, y, facing):
                    print(f" Robot placed at ({x},{y}) facing {facing}")
                else:
                    print(" Invalid placement. Check coordinates (0-4) and direction.")
                    
        elif command == 'MOVE':
            if self.robot.move():
                print("Robot moved forward")
            else:
                if not self.robot.is_placed:
                    print("Robot not placed. Use PLACE command first.")
                else:
                    print("Cannot move - would fall off the table!")
                    
        elif command == 'LEFT':
            if self.robot.left():
                print("Robot turned left")
            else:
                print("Robot not placed. Use PLACE command first.")
                
        elif command == 'RIGHT':
            if self.robot.right():
                print("Robot turned right")
            else:
                print("Robot not placed. Use PLACE command first.")
                
        elif command == 'REPORT':
            report = self.robot.report()
            if self.robot.is_placed:
                print(f"Robot position: {report}")
            else:
                print("Robot is not placed on the table")
                
        else:
            print(f"Unknown command: '{command}'")
            print("   Type 'HELP' to see available commands")
            
    def display_table_visualization(self):
        """Display a visual representation of the table and robot position."""
        if not self.robot.is_placed:
            return
            
        print("\n  Table visualization:")
        print("   0 1 2 3 4")
        
        # Direction symbols
        direction_symbols = {
            'NORTH': '↑',
            'SOUTH': '↓', 
            'EAST': '→',
            'WEST': '←'
        }
        
        robot_symbol = direction_symbols.get(self.robot.facing, '🤖')
        
        for y in range(4, -1, -1):  # Print from top to bottom (y=4 to y=0)
            row = f"{y} "
            for x in range(5):
                if self.robot.x == x and self.robot.y == y:
                    row += f"{robot_symbol} "
                else:
                    row += ". "
            print(row)
        print()
            
    def run(self):
        """Main application loop."""
        self.display_welcome()
        
        while self.running:
            try:
                # Show current status
                if self.robot.is_placed:
                    print(f"Current position: {self.robot.report()}")
                    self.display_table_visualization()
                else:
                    print("Robot not placed - use PLACE command to start")
                
                # Get user input
                command = input("\n> ").strip()
                
                if command:
                    print()  # Add spacing
                    self.execute_command(command)
                    print()  # Add spacing after command execution
                    
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except EOFError:
                print("\n\nGoodbye!")
                break
                

def main():
    """Main entry point of the application."""
    app = ToyRobotConsoleApp()
    app.run()


if __name__ == "__main__":
    main()
