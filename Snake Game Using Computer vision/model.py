import math
import random
import time
import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=1)

# Snake speed control
snake_speed = 0.1  

# Target frame rate
FPS = 30
frame_time = 1.0 / FPS  # Time per frame

class SnakeGameClass:
    def __init__(self, pathFood):
        self.points = []
        self.lengths = []
        self.currentLength = 0
        self.allowedLength = 150
        self.previousHead = 0, 0
    
        self.imgFood = cv2.imread(pathFood, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint = 0, 0
        self.randomFoodLocation()

        self.score = 0
        self.gameOver = False
        self.last_update_time = time.time()

    def randomFoodLocation(self):
        self.foodPoint = random.randint(100, 1000), random.randint(100, 600)

    def update(self, imgMain, currentHead):
        currentTime = time.time()

        # Speed control
        if currentTime - self.last_update_time > snake_speed:
            self.last_update_time = currentTime

        if self.gameOver:
            cvzone.putTextRect(imgMain, "Game Over", [300, 400],
                            scale=7, thickness=5, offset=20)
            cvzone.putTextRect(imgMain, f'Your Score: {self.score}', [300, 550],
                            scale=7, thickness=5, offset=20)
            return imgMain  # Exit update when game is over
        
        px, py = self.previousHead
        cx, cy = currentHead

        self.points.append([cx, cy])
        distance = math.hypot(cx - px, cy - py)
        self.lengths.append(distance)
        self.currentLength += distance
        self.previousHead = cx, cy

        # Length Reduction
        while self.currentLength > self.allowedLength and self.lengths:
            self.currentLength -= self.lengths.pop(0)
            self.points.pop(0)

        # Check if snake ate the Food
        rx, ry = self.foodPoint
        if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and \
                ry - self.hFood // 2 < cy < ry + self.hFood // 2:
            self.randomFoodLocation()
            self.allowedLength += 50
            self.score += 1
            print(self.score)

        # Draw Snake
        if self.points:
            for i in range(1, len(self.points)):
                cv2.line(imgMain, self.points[i - 1], self.points[i], (0, 0, 255), 20)
            cv2.circle(imgMain, self.points[-1], 20, (0, 255, 0), cv2.FILLED)

        # Draw Food
        imgMain = cvzone.overlayPNG(imgMain, self.imgFood,
                                    (rx - self.wFood // 2, ry - self.hFood // 2))

        cvzone.putTextRect(imgMain, f'Score: {self.score}', [50, 80],
                        scale=3, thickness=3, offset=10)

        # Check for Collision
        if len(self.points) > 2:
            pts = np.array(self.points[:-2], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(imgMain, [pts], False, (0, 255, 0), 3)
            minDist = cv2.pointPolygonTest(pts, (cx, cy), True)

            if -1 <= minDist <= 1:
                print("Hit")
                self.gameOver = True
                self.points = []  # all points of the snake
                self.lengths = []  # distance between each point
                self.currentLength = 0  # total length of the snake
                self.allowedLength = 150  # total allowed Length
                self.previousHead = 0, 0  # previous head point
                self.randomFoodLocation()

        return imgMain

    def reset_game(self):
        self.points = []
        self.lengths = []
        self.currentLength = 0
        self.allowedLength = 150
        self.previousHead = 0, 0
        self.randomFoodLocation()
        self.score = 0
        self.gameOver = False

game = SnakeGameClass("resource/donut.png")

while True:
    start_time = time.time()

    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]
        
        if not game.gameOver:
            img = game.update(img, pointIndex)
        else:
            # Game Over display
            cvzone.putTextRect(img, "Game Over", [300, 400],
                               scale=7, thickness=5, offset=20)
            cvzone.putTextRect(img, f'Your Score: {game.score}', [300, 550],
                               scale=7, thickness=5, offset=20)
    
    cv2.imshow("Image", img)
    elapsed_time = time.time() - start_time
    if elapsed_time < frame_time:
        time.sleep(frame_time - elapsed_time)

    key = cv2.waitKey(1)

    if key == ord('r'):  #'r' key to reset
        game.reset_game()
    elif key == 13:  # 'Enter' key to exit
        break

cap.release()
cv2.destroyAllWindows()
