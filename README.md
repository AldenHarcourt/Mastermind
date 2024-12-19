# Mastermind
 
Mastermind Game
Welcome to the Mastermind game! This project implements a version of the classic Mastermind game, where the player either guesses the secret code or allows the computer to guess the code based on feedback.

Overview
Mastermind is a code-breaking game where one player sets a secret code, and the other player tries to guess the code by providing guesses, receiving feedback on how many correct positions (red pins) and how many correct colors in wrong positions (white pins) they have guessed.

This implementation provides two modes:

Human Guessing Mode: The human player tries to guess a secret code generated randomly by the computer. After each guess, the game provides feedback in terms of red and white pins.
Computer Guessing Mode: The computer tries to guess the secret code chosen by the player. After each guess, the player provides feedback on the red and white pins, helping the computer refine its guesses.
Features
Human Guessing Mode: The player inputs guesses, and the game responds with the number of red and white pins.
Computer Guessing Mode: The computer makes its guesses, and the player provides feedback on the accuracy of each guess.
Minimax Strategy: The computer uses a minimax approach to make optimal guesses, minimizing the worst-case number of remaining possibilities for each guess.
Classes
computerGuessing: This class handles the logic for the computer's guesses, including maintaining a list of possible key combinations, calculating red and white pins, and updating the list of valid guesses based on user feedback.
HumanGuessingMasterMind: This class handles the logic for the human player's guesses, including calculating red and white pins based on the player's input.
Game Flow: The game offers an interactive loop that allows the player to choose between guessing the code or having the computer guess it. The game will prompt for feedback after each guess until the game is won or the maximum number of attempts is reached.
How to Play
Human Guessing: If you choose "guess," the computer will generate a random code, and you will try to guess it. After each guess, the game will provide feedback:

Red pins: Correct color in the correct position.
White pins: Correct color in the wrong position.
Computer Guessing: If you choose "key," the game will let you set a secret code. The computer will then try to guess it. After each guess, you will provide feedback on the number of red and white pins.

Play Again: After either the computer or human wins, you will be prompted to play again or quit.

Instructions
Clone or download this repository to your local machine.
Run the script main() to start the game.
Follow the on-screen instructions to either guess the secret code or have the computer guess it.
Example Run
vbnet
Copy code
Would you like to guess or have the key (guess or key or quit): guess
How many guesses do you want (9 is standard): 9
Guess should be in the format: 1111
Your guess is: 1234
RedPins: 2
WhitePins: 1
...
Game Modes
Human Guessing Mode: The player tries to guess the code.
Computer Guessing Mode: The computer guesses the code, and the player provides feedback.
Functions
playHumanGuessing(): Runs the human guessing game.
playComputerGuessing(): Runs the computer guessing game.
main(): Allows the user to choose between guessing the code or setting the code for the computer to guess.
Requirements
Python 3.x