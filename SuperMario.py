from __future__ import annotations
import msvcrt 
# Todo:  Need input specific for unix and mac 
 

#data = input() 
#charSequence =[]

#for x in data : 
#    charSequence.append(x)

#print(charSequence)
 
#os.system("start /wait cmd  {command}")



#Game Loop 
#def display_pressed_key(key):
#    print(f'You Pressed the {key} key')

print("SuperBario")

letterList = ["x"]
printCharacter = ""

while True:   
    #movingSideways=input() 
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

   



    #if keyboard.is_pressed('a'):
    #    display_pressed_key("a")
    #if keyboard.is_pressed('s'):
    #        display_pressed_key("s")
    #if keyboard.is_pressed('d'):
    #        display_pressed_key("d")
    #if keyboard.is_pressed('w'):
    #        display_pressed_key("w")     
#if __name__ == "__main__":