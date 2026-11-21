# Password Auditor

A Python-based cybersecurity project designed to analyze password composition and provide detailed character statistics through a command-line interface.

## Project Overview

Password Auditor is a Python application designed to analyze the composition of a password.

The application identifies and counts different character categories, including uppercase letters, lowercase letters, digits, symbols, and whitespace characters.

Its purpose is to provide users with a clear overview of their password composition without displaying the original password.

## Objectives

The main objectives of this project are:

- **Python Fundamentals:** Develop practical programming skills using Python, including variables, loops, conditional statements, string manipulation, and input validation.
- **Password Security Fundamentals:** Understand basic password composition concepts and the importance of character diversity in password construction.
- **Software Architecture Fundamentals:** Gain an initial understanding of code organization, project structure, and separation of responsibilities.

## Features

- **Hidden Password Input:** Requests a password using Python's `getpass` module, preventing the password from being displayed during input.
- **Password Composition Analysis:** Analyzes and counts the total number of characters, uppercase letters, lowercase letters, digits, symbols, and whitespace characters.
- **Analysis Report:** Generates a console-based report displaying password composition statistics without revealing the original password.
- **Input Validation:** Rejects empty passwords and inputs containing only whitespace characters.

## Requirements

To run Password Auditor, the following resources are required:

- A computer capable of running Python.
- Python 3 installed on the system.
- A Python-compatible code editor or IDE (recommended).
- Python Standard Library, including the `getpass` module.

No external Python packages are required.

## How to Run

1. Access the Password Auditor repository on GitHub.
2. Clone the repository or download the project files.
3. Make sure Python 3 is installed on your computer.
4. Open a terminal in the project directory.
5. Execute the application using the following commands:

    python src/main.py

6. Enter a valid password when prompted.
7. View the password composition analysis displayed in the terminal.

**Note:** The password input is hidden during typing through Python's `getpass` module.

## Technical Concepts

The project applies the following Python programming concepts:

- **Module Import:** Importing the `getpass` module for hidden password input.
- **String Variables:** Storing and manipulating password data using string variables.
- **Loops:** Using `for` to iterate through password characters and `while` to validate user input.
- **Counters:** Using integer variables to count characters belonging to different categories.
- **Conditional Statements:** Using `if`, `elif`, and `else` to classify individual characters.
- **String Methods:** Applying methods such as `isupper()`, `islower()`, `isdigit()`, and `isspace()`.
- **String Formatting:** Using f-strings to display the analysis report.
- **Input Validation:** Checking whether the submitted password is empty or contains only whitespace characters.
- **Built-in Functions:** Using `len()` to calculate password length.

## Limitations

The current version of Password Auditor has the following limitations:

- **No Strength Assessment:** The application does not determine the actual strength or resistance of a password against attacks.
- **No Cracking Time Estimation:** It does not estimate how long an attacker might take to crack a password.
- **No Password Reuse Detection:** It cannot determine whether the user reuses the same password across multiple services.
- **No Breach Detection:** It does not check whether a password has appeared in known data breaches or leaked password databases.

The application focuses exclusively on password composition analysis and character statistics.

## Future Improvements

The following features are planned for future versions of Password Auditor:

1. **Password Predictability Analysis:** Identify predictable patterns and weak character combinations.
2. **Password Reuse Detection:** Implement mechanisms to identify password reuse using user-provided data.
3. **Data Breach Detection:** Integrate with external services to check whether passwords have appeared in known data breaches.
4. **Password Cracking Time Estimation:** Estimate password cracking time under different attack scenarios.
5. **Password Strength Classification:** Classify passwords according to multiple security factors.
6. **Common Password Detection:** Identify passwords found in common password dictionaries.
7. **Password Entropy Calculation:** Estimate password entropy and theoretical search space.
8. **Exportable Security Report:** Generate TXT, JSON, or PDF reports without exposing the original password.
9. **Custom Password Policy:** Allow users to define password requirements and validation rules.

## Project Status

**Version:** 1.0

**Status:** Initial implementation completed.

This project is part of a personal Cybersecurity Project Lab focused on developing practical cybersecurity and programming skills through hands-on projects.

## Disclaimer

Password Auditor is an educational project intended for learning purposes. It analyzes password composition but does not guarantee password security or resistance against cyberattacks.

The application does not store or transmit passwords.
