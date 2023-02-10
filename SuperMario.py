from __future__ import annotations
import msvcrt 
# Todo:  Need input specific for unix and mac 
 

print("SuperBario")

letterList = ["x"]
printCharacter = ""

while True:    
    movementInput = msvcrt.getch() 
    if  movementInput == b'd':  
        letterList.insert(0,"") 
        #print("Inserting value")
        #If list is NOT empty
    if  movementInput == b'a' and letterList:
        #print("Popping value")
        letterList.pop(0)
        #If list IS empty
    elif movementInput == b'a' and not letterList:
        print("Not Full")
     
    for x in letterList:
        printCharacter += x
        #"Letters in charlist"
        print(printCharacter, end="") 
         
    printCharacter = "" 