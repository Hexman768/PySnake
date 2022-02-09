# PySnake
PySnake is a simple console-based implementation of the classic game Snake using the curses library.

## Data Structure
The Snake is managed by a Stack structure. We push and pop {x, y} vectors to the stack to grow the Snake.

## Screenshot
![image](https://user-images.githubusercontent.com/41409007/153133818-468cb4f9-1a6f-4c7a-8c05-fb3d4720b990.png)

## Dependencies
The only external dependency that PySnake requires is the windows-curses module. I have not yet tested this in a linux environment.

## How to play
Use the arrow keys to change the direction the Snake is moving. Try to get as many apples as you can!

## Upcoming features
1. Collision detection for the Snake's tail
2. Automatic score keeping
3.  Terminal flags that user can use to change the game settings, such as the size of the board.
