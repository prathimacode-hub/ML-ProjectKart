# Tetris Object counter
![image](https://github.com/TusharAMD/ML-ProjectKart/blob/issue50/Tetris%20Object%20Counter/Images/Screenshots/illustration%20for%20readme.jpg)

### Goal
The goal of the project is to identify all the tetris objects (tetrominoes) in the given tetris input image and return the count. It is seen that during gameplay the tetris blocks are broken and this program should be able to identify such blocks too.

### Dataset
Dataset used in the project is screenshots from the https://tetris.com/play-tetris website. Currently there are 5 input images in the project.

### Steps I followed
1. Collect images from https://tetris.com/play-tetris.
2. Detect contours to crop out correct playarea of tetris
3. Check for all the cells inside the area. (Standard Tetris has 10X20 cells)
4. Find out Total Unoccupied cells
5. Create a 2Dimensional list specifying the color in each cell 
5. Using two for loops traverse 2D List and draw circle over center of each cell.
6. Use 3 Dicts blockClrs (To specify color of particular block), noOfBlocks (To get total no of blocks of particular type for eg. 10 blocks of L shape), noOfTetrominoes (To count whole tetrominoes which is main task of the project)
7. Traverse the 2D List and check if color is identified if yes increment noOfTetrominoes of that type of block else continue.
8. Display 3 Dicts and also matrix which specify colors of all the blocks.
9. End

### Libraries Needed
opencv_python==4.4.0.42

numpy==1.19.

pandas==1.1.1

imutils==0.5.4

### Results

Here is one of the input image
![image](https://github.com/TusharAMD/ML-ProjectKart/blob/issue50/Tetris%20Object%20Counter/Dataset/5.png)

And this is the Result
![image](https://github.com/TusharAMD/ML-ProjectKart/blob/issue50/Tetris%20Object%20Counter/Images/Screenshots/Updated.png)

### Created By
This project was made by Tushar Amdoskar - Prefinal Year student of Computer Engineering, University of Mumbai
You can connect me on linkedin https://www.linkedin.com/in/tushar-amdoskar/
