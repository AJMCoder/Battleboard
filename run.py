# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("Battleships")
print("Welcome to Battleships!")
print("You will be playing against the computer.")
print("The aim of the game is to sink all of the computer's ships before it sinks yours.")
print("You will be asked to enter the coordinates of where you want to fire your shot.")
print("The computer will then fire a shot at a random location.")
print("If you hit a ship, you will be told that you have hit a ship.")
print("If you miss, you will be told that you have missed.")
print("If you sink a ship, you will be told that you have sunk a ship.")
print("If the computer sinks one of your ships, you will be told that the computer has sunk one of your ships.")
print("The game will end when either you or the computer has sunk all of the other's ships.")
print("Good luck!")

print("You will now be asked to place your ships.")
print("You will be asked to enter the coordinates of where you want to place your ships.")
print("You will be asked to enter the coordinates of the front of the ship.")
print("You will then be asked to enter the coordinates of the back of the ship.")
print("The computer will then place its ships.")
print("The computer will randomly generate the coordinates of the front of the ship.")
print("The computer will then randomly generate the coordinates of the back of the ship.")
print("The computer will then check if the ship is in a valid position.")
print("If the ship is in a valid position, it will be placed.")
print("     0  1  2  3  4  5  6  7  8  9")

#outside for loop prints each row, number of row and the string of dashes.
for x in range(10):
    row = ""
#inside for loop creates the row of dashes.
    for y in range(10):
        chr = " _ "
        row = row + chr
    print(x, " ",row)