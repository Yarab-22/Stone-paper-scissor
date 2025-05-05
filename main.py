'''
-1 = stone
1= paper
0 = scissor
'''
import random


print("""
      Hello,
      Welcome to stone,paper & scissor game.

      Your options are - stone,paper & scissor
      """)

computer = random.choice([1, 0, -1])
youCH = input ("Enter your choice: ")

you_dir = {
    "stone":-1,
    "paper":1,
    "scissor":0
}
reverse_dir = {
    -1:"stone",
    1:"paper",
    0:"scissor"
}

you = you_dir[youCH]

print("")
print(f"You chose {reverse_dir[you]} \nComputer chose {reverse_dir[computer]}")
print("")

if(computer == you):
    print("DRAW!!!")

else:
    if(computer == -1 and you == 1):
        print("YOU WIN!!!")
        
    elif(computer == -1 and you == 0):
        print("YOU LOSE!!!")

    elif(computer == 1 and you == -1):
        print("YOU LOSE!!!")

    elif(computer == 1 and you == 0):
        print("YOU WIN!!!")

    elif(computer == 0 and you == 1):
        print("YOU LOSE!!!")

    elif(computer == 0 and you == -1):
        print("YOU WIN!!!")
   