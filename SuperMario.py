from __future__ import annotations
import msvcrt 
import LevelDesign
# Todo:  Need input specific for unix and mac 
 

print("SuperBario\n")

playerPositions = ["x"] 
#Prints the first character X then sets the caret at the same position instead of jumping forward 
print(playerPositions[0],end="\r") 

levelOne = LevelDesign.LevelOne

while True:
    movementInput = msvcrt.getch() 

    if  movementInput == b'd':  
        playerPositions.insert(0," ") 

        #If list is NOT empty
    if  movementInput == b'a' and playerPositions: 

        #Make sure position does not include X(that would mean we are at the left edge of the map)
        if playerPositions[0] != "x":
        #In order to move X we add a space to the end and pop the first one
         playerPositions.append(" ")
         playerPositions.pop(0)
        #If list IS empty should never happen
    elif movementInput == b'a' and not playerPositions:
        print("Empty")
   
    for position in playerPositions: 
        print(position, end="")

    print(end="\r")