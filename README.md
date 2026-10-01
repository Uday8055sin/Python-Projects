# 🐍 Python Projects

A collection of four beginner-friendly Python projects developed to strengthen programming fundamentals, problem-solving skills, automation concepts, data handling, and user interaction.

These projects were created as practical implementations of Python concepts learned during my programming journey.

---

## 👨‍💻 Author

**Uday Pratap Singh**

B.Tech – Computer Science & Engineering (Data Science)

Institute of Technology and Management (ITM), Gida, Gorakhpur

---

## 📌 Projects Included

| # | Project | Description |
|---|---|---|
| 1 | 🎮 Hangman Game | A word-guessing game using Python |
| 2 | 📈 Stock Portfolio Tracker | Calculates stock investment values |
| 3 | 📁 Task Automation | Automatically organizes JPG files |
| 4 | 🤖 Basic Chatbot | A simple rule-based chatbot |

---

# 1. 🎮 Hangman Game

## 📖 About

Hangman is a simple text-based word-guessing game.

The computer randomly selects a word from a predefined list. The user has to guess the word one letter at a time.

The player has a maximum number of incorrect guesses before the game ends.

### Example

```text
Word: _ _ _ _ _ _

Enter a letter: p

Correct!

Word: p _ _ _ _ _# Python-Projects

Features
. Random word selection
. Letter by letter guessing
. Maximum 6 wrong guesses
. Displays guessed letters
. Checks the repeated guesses
. Display win or game over message
. Simple command line interface
Technologies Used
. Python
. random module
Python Concepts Used
. Variables
. Strings
. List
.if-else
.for loop
.while loop
. User input
. Randomization

Stock Portfolio Tracker
About
The Stock Portfolio Tracker is a simple Python application that calculates the total investment value of selected stocks.
The user enters a stock name and quantity. The program uses predefined stock prices to calculate the investment value.
Note: This is an educational project and does not use live stock-market data.
Example
AAPL = $180

Quantity = 5

Investment = $900
Features
Displays available stocks
Accepts stock name from the user
Accepts stock quantity
Calculates individual investment
Calculates total portfolio value
Supports multiple stocks
Optionally saves the portfolio to a text file
Technologies Used
Python
Dictionary
File handling
Python Concepts Used
Dictionaries
Variables
User input
while loop
if-else
Arithmetic operations
File handling
How to Run
python stock_portfolio.py
Example
AAPL | Price: $180 | Quantity: 5 | Investment: $900
TSLA | Price: $250 | Quantity: 2 | Investment: $500
TOTAL INVESTMENT: $1400
Task Automation with Python
About
This project demonstrates how Python can be used to automate repetitive file-management tasks.
The program searches for .jpg files inside a selected folder and automatically moves them into a separate folder named JPG_Files.
Manual Process
Find JPG files
      ↓
Select files
      ↓
Create folder
      ↓
Move files
Automated Process
Python
  ↓
Find JPG files
  ↓
Create JPG_Files folder
  ↓
Move files automatically
Features
Accepts a folder path from the user
Checks whether the folder exists
Creates a JPG_Files folder automatically
Finds JPG files
Moves JPG files automatically
Displays the number of files moved
Technologies Used
Python
os module
shutil module
Python Concepts Used
File handling
Folder management
File paths
os
shutil
for loop
if-else
String operations
How to Run
python file_organizer.py
The program will ask for a folder path.
Example:
Enter the folder path:
C:\Users\Uday\Pictures\Test
The program will then create:
Test
JPG_Files
and move the JPG files into it.
For testing, use a test folder because the program actually moves files.
Basic Chatbot
About
The Basic Chatbot is a simple rule-based chatbot created using Python.
It accepts user input and provides predefined responses based on the entered message.
Example
You: hello
Bot: Hi! Nice to meet you.

You: how are you
Bot: I'm fine, thanks!

You: what is your name
Bot: My name is Python Chatbot.

You: bye
Bot: Goodbye!
Features
Responds to predefined messages
Supports greetings
Answers basic questions
Uses a continuous conversation loop
Provides an exit option
Simple command-line interface
Technologies Used
Python
Python Concepts Used
Functions
Strings
if-elif-else
while loop
User input
Return statements
How to Run
python chatbot.py
Type:
bye
to end the chatbot session.
Note: This is a rule-based chatbot and does not use Machine Learning or Generative AI.

Python
├── Programming Fundamentals
├── Problem Solving
├── Data Structures
├── File Handling
├── Automation
├── User Input Handling
├── Functions
└── Conditional Logic
