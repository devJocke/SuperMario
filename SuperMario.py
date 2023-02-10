from __future__ import annotations
import msvcrt 
# Todo:  Need input specific for unix and mac 
 

print("SuperBario")

letterList = ["x"]
printCharacter = ""

while True:    
    if  msvcrt.getwche() == "d":  
        letterList.insert(0," ") 
        print("\nInserting value")
        #If list is NOT empty
    if  msvcrt.getwche() == "a" and letterList:
        letterList.pop(0)
        print("\nPopping value")
        #If list IS empty
    elif msvcrt.getwche() == "a" and not letterList:
        print("\nNot Full")
     
    for x in letterList:
        printCharacter += x
        print("\nLetters in charlist" + printCharacter) 
         
    printCharacter = "" 