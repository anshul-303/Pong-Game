 # 🏓 Pong Game
 
Welcome to the Pong Game! A modern take on the classic arcade game, built using Python's turtle module. Challenge a friend and see who can score the most points!


# 🎮 How to Play

Player 1: Use the W (up) and S (down) keys to move the left paddle.
Player 2: Use the Up Arrow (up) and Down Arrow (down) keys to control the right paddle.
Score a point by making the ball pass your opponent's paddle.
The game ends when one player reaches the winning score which in this case is 10.

# 🚀 Features

Two-player mode: Play against a friend on the same computer.
Smooth gameplay with responsive controls.
Simple yet nostalgic design, reminiscent of the classic Pong arcade game.
Real-time score tracking displayed on the screen.

# 🔧 Installation Instructions

Follow these steps to get the Pong Game running on your local machine:

Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/pong-game.git
Navigate to the project directory:

bash
Copy code
cd pong-game
Run the game using Python:

bash
Copy code
python pong_game.py



# 🖼️ Screenshots
Here are some screenshots to give you a glimpse of the game in action:

Image 1: The game start screen.
Image 2: Player 1 and Player 2 in action.
Image 3: Game over screen displaying the final scores.

# 🛠️ Technologies Used
This project utilizes the following technologies:

Python: A powerful programming language used to build the game.
turtle Module: A simple and easy-to-use Python library for creating graphics and animations.
OOP Concepts: Object-Oriented Programming principles used to structure the game components.


# 🖥️ How the turtle Module is Used
The turtle module provides the graphical interface for the game. Here's how it's used:

Paddles:

- Each paddle is a turtle object that moves up and down the screen.
The paddle movement is controlled via keyboard event handlers.
The paddles invokes its set of methods which are defined in its respective class.

Ball:

- The ball is a turtle object that moves around the screen, bouncing off walls and paddles.
Collision detection is handled to reflect the ball when it hits a paddle or wall.

Game Window:

- The game window is created using the turtle module's screen setup. It contains designated dimensions to ensure correct
  display of game elements.
The background color, screen dimensions, and other properties are configured to enhance gameplay.

Score Display:

- The score for both players is displayed using turtle’s text rendering capabilities.
- The score updates in real-time as players score points.
💡 How OOP Concepts are Used

Object-Oriented Programming (OOP) is used to structure the game into modular components:

1. Paddle Class
Purpose: Manages paddle movement and positioning.
Attributes:
paddle: A turtle object representing the paddle.
position: Starting position of the paddle (left or right side).
Methods:
go_up(): Moves the paddle up.
go_down(): Moves the paddle down.
2. Ball Class
Purpose: Manages the ball's movement, speed, and collision detection.
Attributes:
ball: A turtle object representing the ball.
x_move, y_move: Control the ball’s movement direction and speed.
Methods:
move(): Updates the ball’s position on the screen.
bounce(): Reverses the ball’s direction upon collision.
reset_position(): Resets the ball to the center after scoring.
game_over(): Displays the final score after tracking it real time and game over message.
3. Main Game Loop:
The main game loop runs continuously based pre defined boolean condition, checking for collisions, updating the ball's position, and handling user input.
The loop keeps the game running smoothly, updating the score and managing game flow.

# 📜 License
This project is licensed under the MIT License – see the LICENSE file for details.


# 🙏 Acknowledgments
Inspired by the classic Pong game, a staple of early arcade gaming.
Thank you for checking out the Pong Game! 🏓 Feel free to contribute or share your thoughts.

GitHub: anshul303
