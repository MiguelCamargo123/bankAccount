# Simple Banking System 🏦

A simple command-line banking application written in Python. This project demonstrates Object-Oriented Programming (OOP) concepts such as classes, methods, encapsulation, and JSON-based data persistence.

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [How to Run](#how-to-run)
- [Code Structure](#code-structure)
- [Example Usage](#example-usage)
- [Version History](#version-history)

## 🤔 About

This script simulates a basic bank account system. It allows a user to interact with their account via the terminal to perform standard financial operations. It is designed to practice Python syntax and OOP logic, specifically protecting attributes (encapsulation) using private variables. Starting from v1.2.0, all transactions are now persisted to a JSON file, so your history is saved between sessions.

## 🚀 Features

- **Account Creation:** Initializes an account with a specific holder name (`titular`).
- **Deposit (`depositar`):** Adds funds to the account. Includes validation to ensure the deposit amount is positive.
- **Withdraw (`sacar`):** Removes funds from the account. Includes validation to ensure:
  - The amount is positive.
  - The user has sufficient balance (no overdraft allowed).
- **Check Balance (`verSaldo`):** Displays the current available balance formatted in an f-string.
- **Transaction History (`verHistorico`):** Displays all past deposits and withdrawals with the balance after each operation.
- **JSON Persistence:** Transaction history is automatically saved to `historico.json` and reloaded on startup.
- **Encapsulation:** Uses private attributes (e.g., `__saldo`) to prevent direct modification of the balance outside of the class methods.

## 🛠️ Prerequisites

You need to have Python installed on your machine.

- **Python 3.x**

No external libraries required — only the built-in `json` module is used.

## 💻 How to Run

1. Clone this repository or download the `bankAccount.py` file.
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script:

```
python bankAccount.py
```

5. Follow the on-screen prompts to interact with your account.

## 📁 Code Structure

The main class `contaBancaria` contains the following methods:

- **`__init__(self, titular, saldo)`:** Constructor method. Initializes the account and loads existing history from JSON.
- **`__carregar(self)`:** Private method. Loads transaction history from `historico.json` on startup. Creates an empty history if the file doesn't exist yet.
- **`__salvar(self)`:** Private method. Saves the current transaction history to `historico.json`. Called automatically after every deposit or withdrawal.
- **`depositar(self, valor)`:** Handles logic for adding money to the account.
- **`sacar(self, valor)`:** Handles logic and validation for removing money from the account.
- **`verSaldo(self)`:** Prints the current balance.
- **`verHistorico(self)`:** Prints all recorded transactions.

## 📌 Example Usage

```
Digite seu nome: Miguel
Olá Miguel, voce deseja [S]acar, [D]epositar, dar uma olhada no [H]istórico de transações ou [V]seu saldo? D
Digite um valor para depositar: 500
Olá Miguel, voce deseja [S]acar, [D]epositar, dar uma olhada no [H]istórico de transações ou [V]seu saldo? S
Digite um valor para sacar: 200
Valor sacado com sucesso
Olá Miguel, voce deseja [S]acar, [D]epositar, dar uma olhada no [H]istórico de transações ou [V]seu saldo? V
O seu saldo atual é de 300.0
```

## 📜 Version History

### v1.2.0 (*current version*)
- Added JSON persistence — transaction history is now saved between sessions
- Added `__carregar()` private method to load data on startup
- Added `__salvar()` private method to persist data after every transaction

### v1.1.0
- Added transaction history tracking
- Improved method design (input separated from business logic)
- Added structured transaction records (dictionary-based)
- Improved menu flow and validation
- Better separation between system logic and user interface

### v1.0.0
- Initial release
- Basic deposit and withdrawal functionality
- Balance checking
- Encapsulation with private `__saldo` attribute

---

*Created for study purposes.*
