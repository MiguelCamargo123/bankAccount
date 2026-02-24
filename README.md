# Simple Banking System 🏦

A simple command-line banking application written in Python. This project demonstrates basic Object-Oriented Programming (OOP) concepts such as classes, methods, and encapsulation.

## 📋 Table of Contents
* [About](#-about)
* [Features](#-features)
* [Prerequisites](#-prerequisites)
* [How to Run](#-how-to-run)
* [Code Structure](#-code-structure)

## 🧐 About
This script simulates a basic bank account system. It allows a user to interact with their account via the terminal to perform standard financial operations. It is designed to practice Python syntax and OOP logic, specifically protecting attributes (encapsulation) using private variables.

## 🚀 Features
* **Account Creation:** Initializes an account with a specific holder name (`titular`).
* **Deposit (`depositar`):** Adds funds to the account. Includes validation to ensure the deposit amount is positive.
* **Withdraw (`sacar`):** Removes funds from the account. Includes validation to ensure:
  * The amount is positive.
  * The user has sufficient balance (no overdraft allowed).
* **Check Balance (`verSaldo`):** Displays the current available balance formatted in an f-string.
* **Encapsulation:** Uses private attributes (e.g., `__saldo`) to prevent direct modification of the balance outside of the class methods.

## 🛠 Prerequisites
You need to have Python installed on your machine.
* **Python 3.x**

## 💻 How to Run

1. Clone this repository or download the `bankAccount.py` file.
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script:

```bash
  python bankAccount.py
```


-  Follow the on-screen prompts to enter your name, make a deposit, and make a withdrawal.

## 📂 Code Structure
The main class contaBancaria contains the following methods:

- __init__(self, titular, saldo): Constructor method.

- depositar(self): Handles input logic for adding money.

- sacar(self): Handles logic and validation for removing money.

- verSaldo(self): Prints the current status of the account.

## 📝 Example Usage
```Plaintext
  Digite seu nome: John Doe
  Digite um valor: 100
  Digite um valor para sacar: 30
  Valor sacado com sucesso
  O seu saldo atual é de 70
```

Created for study purposes.
