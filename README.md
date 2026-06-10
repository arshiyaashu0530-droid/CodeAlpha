# Python Mini Projects Collection

A collection of beginner-friendly Python projects that demonstrate fundamental programming concepts such as loops, conditionals, functions, file handling, dictionaries, and randomization. These projects are designed to help learners strengthen their Python programming skills through practical implementation.

---

## Table of Contents

1. Hangman Game
2. Stock Portfolio Tracker
3. Simple Chatbot
4. Requirements
5. Project Structure
6. Learning Outcomes
7. Future Enhancements
8. License

---

# 1. Hangman Game

A console-based word guessing game where players attempt to reveal a hidden word by guessing one letter at a time.

## Features

- Random word selection
- Tracks guessed letters
- Prevents duplicate guesses
- Limited incorrect attempts
- Win/Loss detection
- Beginner-friendly game logic

## How to Run

bash
python hangman.py


## Sample Output

text
Word: _ _ _ _ _ _

Enter a letter: a

Word: a _ _ _ _ _


### Game Rules

- Guess one letter at a time.
- You have 6 incorrect attempts.
- Reveal all letters before running out of chances.
- The game ends when you either guess the word or lose all attempts.

---

# 2. Stock Portfolio Tracker

A simple command-line application that calculates the total investment value of a stock portfolio based on predefined stock prices and user-entered quantities.

## Features

- Supports multiple stock entries
- Calculates total portfolio value
- Handles invalid stock symbols
- Saves results to a text file
- Demonstrates dictionary and file handling concepts

## Supported Stocks

| Stock Symbol | Price |
|-------------|--------|
| AAPL | 180 |
| TSLA | 250 |
| GOOG | 150 |
| MSFT | 300 |

## How to Run

bash
python stockPortfolio.py


## Sample Output

text
Enter stock name (or 'done' to finish): AAPL
Enter quantity: 10

Enter stock name (or 'done' to finish): TSLA
Enter quantity: 5

Enter stock name (or 'done' to finish): done

Total Investment Value = 3050
Result saved in investment.txt


### Output File

The calculated investment value is stored in:

text
investment.txt


Example:

text
Total Investment Value = 825810


---

# 3. Simple Chatbot

A basic rule-based chatbot that responds to predefined user inputs and demonstrates conditional logic and function implementation.

## Features

- Interactive conversation
- Predefined responses
- Exit command support
- Easy to understand and extend

## Supported Commands

| User Input | Response |
|------------|----------|
| hello | Hi! |
| how are you | I'm fine, thanks! |
| bye | Goodbye! |

## How to Run

bash
python chatbot.py


## Sample Interaction

text
Chatbot: Hello! Type 'bye' to exit.

You: hello
Chatbot: Hi!

You: how are you
Chatbot: I'm fine, thanks!

You: bye
Chatbot: Goodbye!


---

# Requirements

- Python 3.x
- No external libraries required

---

# Project Structure

text
Python-Mini-Projects/
│
├── hangman.py
├── stockPortfolio.py
├── chatbot.py
└── investment.txt


---

# Learning Outcomes

These projects cover the following Python concepts:

- Variables and Data Types
- Conditional Statements
- Loops
- Functions
- Dictionaries
- User Input Handling
- File Operations
- Random Module
- Basic Game Development
- Problem Solving Techniques

---

# Future Enhancements

## Hangman Game
- Difficulty levels
- Score tracking
- Word categories
- ASCII art visualization
- Multiplayer mode

## Stock Portfolio Tracker
- Real-time stock prices using APIs
- Portfolio history tracking
- CSV export support
- Graphical user interface (GUI)

## Chatbot
- Natural Language Processing (NLP)
- AI-powered responses
- Voice interaction
- GUI implementation

---

# License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Author

Developed as beginner-friendly Python projects to practice programming fundamentals, problem-solving, and application development using Python.