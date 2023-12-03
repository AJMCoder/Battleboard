![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# Battleboard

Project 3 is a battleship based game, with the players objective being to destroy the ships located on the board. In this version of the game, the location of the ships has been pre-selected, so the user must guess where the ships are through trial and error. This is a Python terminal game that runs through the Code Institute mock terminal via Heroku. 

## Purpose

The objective of the game is to destroy the battleships that have been placed in random locations on the board, by the developer. Through trial and error, the user must guess where these hidden ships are located and destroy them. However, there are only a limited amount of tries before the user loses, and the developer wins!

## How to play

Battleships is a classic strategy game whereby the users end goal, is to destroy the hidden ships on the board. This project is based on this classic board game and is made purely in Python. This version of the game is soley played against the developer, and so the ships placements have been predetermined before the user starts. 

## Features

### Existing Features

### Future Developments

**Coming Soon**
- In the future, this game will be played against the computer with randomly generated coordinates for the ships. This feature would enable replayability and allow the user to repeatably play the game over and over with different result each time potentially.
- The game will also in the future allow the user to place ships and play alongside the computer, in an all out battle, head-to-head. This will create an even more engaging dynamic with the user having to think strategically about their placement, as well as battling the computer in sinking theirs.
- A score board would also be a useful feature that would support replayability, as through this the user could keep a track of who has won the most games, or even a scoring system that counted the turns to see the quickest win.
- An additional feature that I would like to add, is that ability to change the size of the board for which the game is played on. This could increase or decrease the time of the game depending on size. This could be good in allowing people in the same room to play and take it in turns with a larger board available, rather than just increasing the amount of ships which could overcrowd the board and make the game too easy.
- The game is in its simplest form and in future, the overall design and look of the game could be improved visually to make it more appealing to users.

## Testing

### Validator Testing

- [PEP8 Linter]()

### General Continuous Testing

Having passed my code through the PEP8 Linter, which returned no errors, i have continuously tested my game throughout its build. Some of the methods and tests used, are as followed:
- At numerous development points, I have input code to test the outcome, this included knowingly inputting invalid commands to see what the outcome would be and to ensure that the intended comment from the terminal was executed ("Invalid entry"). 
- My mentor and friends have both tested the game and played it.
- 


### De-bugging:

- Corrected an error in the code where 'chr' was written, rather than 'ch' resulting in the code not running correctly and not printing the table or content.
- When testing the code to see if inputting coordinates was working, i discovered that the grid wasnt being displayed at all. I tried re-writing the 'check shot' function to see if it was interfering with the results, but that didnt fix it. However, this did help me discover another issue, as the original code for this section was not functioning properly and didn't allow the user to enter another guess. By 
- In order to fix my original error above, i scanned through the written code and could see that the the 'show_board' and surrounding code at the bottom had not been grouped into a function, so by moving the code into a for loop fucntion, the list then became workable.
- When adding a new boat, i realised that when writing the second check_shot function that it wasn't as simple as re-writing it the same as boat 1. I needed to add an 'elif' statement so that if there is a miss for both, the code can understand that it has missed both boats not just 1 of them. 

### Deployment:

This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:

- Clone this repository.
- Create a new Heroku app.
- Set the buildbacks to Python and NodeJs in that order.
- In the settings, add the KEY/Value pairs: PORT. Set this to 8000.
- Link the Heroku app to the repository.
- Click Deploy.

### Credits




