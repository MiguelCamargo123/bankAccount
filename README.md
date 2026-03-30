# Advanced Banking System 🏦

A robust command-line banking application written in Python. This project demonstrates advanced Object-Oriented Programming (OOP) concepts, multi-user management, security (password hashing), static typing, and JSON-based data persistence.

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [How to Run](#how-to-run)
- [Code Structure](#code-structure)
- [Example Usage](#example-usage)
- [Version History](#version-history)

## 🤔 About

This application simulates a complete bank system. Going beyond a single-account script, this version introduces a Central Bank (`Banco`) that manages multiple User Accounts (`Conta`). It was built to practice strict Python typing (Type Hints), data encapsulation, and security principles by ensuring no passwords are saved in plain text. All user data, balances, and histories are persistently saved to a JSON file.

## 🚀 Features

- **Multi-User Management:** The system can register and manage multiple accounts simultaneously through the `Banco` class.
- **Security & Authentication:** Passwords are encrypted using SHA-256 (`hashlib`) before being stored. Users must authenticate to access their accounts.
- **Strict Static Typing:** The codebase utilizes Python Type Hints (e.g., `-> None`, `tuple[bool, Conta | None]`) to ensure code reliability and catch errors during development (Strict Mode ready).
- **JSON Persistence:** All accounts, encrypted passwords, balances, and transaction histories are automatically saved to `contas.json` and loaded on startup.
- **Financial Operations:** - **Deposit (`depositar`):** Adds funds to the logged-in account.
  - **Withdraw (`sacar`):** Removes funds, validating if the user has a sufficient balance (no overdraft).
  - **Check Balance (`verSaldo`):** Displays the current balance.
  - **Transaction History (`verHistorico`):** Displays a detailed history of all account movements.

## 🛠️ Prerequisites

You need to have Python installed on your machine.

- **Python 3.x**

No external libraries required. The project relies purely on Python's built-in modules (`json` and `hashlib`).

## 💻 How to Run

1. Clone this repository or download the source files.
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script:

```bash
python bankAccount.py
```
