Snake Game with Hand Tracking

This Python project uses OpenCV and MediaPipe's hand tracking module to create a fun and interactive Snake game controlled by your hand!

How it Works:

Hand Tracking: The code utilizes the cvzone.HandTrackingModule to detect and track the index finger tip of your hand.

Snake Movement: The index finger tip's position is used to control the snake's direction. The snake moves towards the fingertip.

Food: A randomly placed food item appears on the screen.

Eating: When the snake's head touches the food, the food is replaced, the snake grows, and the score increases.

Game Over: The game ends if the snake collides with itself or the edges of the screen.

Features:

Hand Control: Control the snake's direction using your index finger.

Snake Growth: The snake grows longer as it eats food.

Score: Track your progress with a score counter.

Game Over: A game over screen appears when the game ends.

Reset Option: Press 'r' to restart the game.

Dependencies:

OpenCV (pip install opencv-python)

cvzone (pip install cvzone)

mediapipe (pip install mediapipe)

How to Run:

Install the necessary dependencies.

Run the model.py script: python model.py

Point your hand at the webcam.

Move your index finger to guide the snake.

If Game over press 'r' to reset and start playing game

press 'Enter' for exit 

Code Explanation:

SnakeGameClass: This class manages all aspects of the game, including:

Snake position and movement.

Food placement and consumption.

Scorekeeping.

Game over logic.

Game reset logic

HandDetector: This object detects and tracks your hand using MediaPipe.

Game Loop: The main loop continuously captures frames from the webcam, tracks your hand, updates the game state, and displays the game on the screen.

Possible Enhancements:

Difficulty Levels: Implement different speeds or food placement strategies for varying difficulty levels.

Multiple Players: Allow for two players to control snakes simultaneously.

Obstacles: Add obstacles to the game to make it more challenging.

Sound Effects: Incorporate sound effects for actions like eating food or game over.

Enjoy playing this fun and engaging Snake game!