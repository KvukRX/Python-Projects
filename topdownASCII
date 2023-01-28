import numpy as np
from os import system as sys

def main():
    game = True
    playerX = 3
    playerY = 3
    while game:
        gameMap=[
            ["#","#","#","#","#","#","#","#","#","#"],
            ["#","_","_","_","_","_","_","_","_","#"],
            ["#","_","_","_","#","_","_","_","_","#"],
            ["#","_","_","_","_","*","_","_","_","#"],
            ["#","_","_","_","_","_","_","_","_","#"],
            ["#","_","_","_","_","_","_","_","_","#"],
            ["#","_","_","_","_","_","_","_","_","#"],
            ["#","_","_","_","_","_","_","_","_","#"],
            ["#","_","_","_","_","_","_","Y","_","#"],
            ["#","_","_","_","_","_","_","_","_","#"],
            ["#","_","_","_","_","_","_","_","_","#"],
            ["#","#","#","#","#","#","#","#","#","#"]
        ]
        sys('clear')
        currentMap = gameMap
        currentMap[playerY][playerX] = "😋"
        output = str(np.matrix(currentMap))
        output = output.replace("[","")
        output = output.replace("#","⬜")
        output = output.replace("]","")
        output = output.replace(",","")
        output = output.replace("'","")
        print(" " + output)
        #input check
        currentMap[playerY][playerX] = "_" #to remove previous player position
        direction = input("direction: ")
        if direction == "left":
            if currentMap[playerY][playerX - 1] == "*":
                game = False
            if currentMap[playerY][playerX - 1] == "_":
                playerX-=1
        if direction == "right":
            if currentMap[playerY][playerX + 1] == "*":
                game = False
            if currentMap[playerY][playerX + 1] == "_":
                playerX+=1
        if direction == "up":
            if currentMap[playerY - 1][playerX] == "*":
                game = False
            if currentMap[playerY - 1][playerX] == "_":
                playerY-=1
        if direction == "down":
            if currentMap[playerY + 1][playerX] == "*":
                game = False
            if currentMap[playerY + 1][playerX] == "_":
                playerY+=1
           
main()
print("YOU WIN!")
