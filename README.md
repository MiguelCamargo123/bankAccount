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

- **Financial Operations:**
  - **Deposit (`depositar`):** Adds funds to the logged-in account.
  - **Withdraw (`sacar`):** Removes funds, validating if the user has a sufficient balance (no overdraft).
  - **Check Balance (`verSaldo`):** Displays the current balance.
- **Transaction History (`verHistorico`):** Displays a detailed history of all account movements.

## 🛠️ Prerequisites 
You need to have Python installed on your machine. 
- **Python 3.x** No external libraries required. The project relies purely on Python's built-in modules (`json` and `hashlib`).

## 💻 How to Run 
1. Clone this repository or download the source files.
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is located.
4. Run the script:
```bash
python main.py
```

5. Follow the on-screen prompts to register a new account or log in to an existing one.

## 📁 Code Structure
The architecture is divided into two main classes:

### Banco (Bank Manager)
• __init__(self): Initializes the bank and loads the user database.

• __carregar_json_banco(self): Loads accounts from contas.json.

• __salvar_json_banco(self): Saves the current state of all accounts to JSON.

• registrar_pessoa_banco(self, titular: str, senha: str): Creates a new account, encrypts the password, and updates the database.

• verificar_se_conta_certa(self, nome_titular: str, senha_digitada: str) -> tuple[bool, Conta | None]: Authenticates a user by comparing the hashed input with the stored hash.

### Conta (Individual Account)
• __init__(self, titular: str, senha: str): Initializes a new account instance.

• depositar(self, valor: float) -> None: Handles deposits and updates history.

• sacar(self, valor: float) -> None: Handles withdrawals with balance validation.

• verSaldo(self) -> None: Displays the current balance.

• verHistorico(self) -> None: Displays recorded transactions.

## 📜 Version History

### v1.3.0 (*current version*)
- **[Feature]** Added `Banco` class to manage multiple accounts.
- **[Security]** Implemented SHA-256 password hashing for user authentication.
- **[Architecture]** Added strict Type Hints (`Pylance/Pyright` strict mode compliant).
- **[Refactor]** JSON persistence now handles a list of complex dictionary objects (`contas.json`).
- Added complete authentication flow (`verificar_se_conta_certa`).

### v1.2.0
- Added JSON persistence for a single account (`historico.json`).
- Added `__carregar()` and `__salvar()` private methods to handle data persistence.

### v1.1.0
- Added transaction history tracking.
- Improved method design (input separated from business logic).
- Added structured transaction records (dictionary-based).
- Improved menu flow and validation.
- Better separation between system logic and user interface.

### v1.0.0
- Initial release.
- Basic deposit and withdrawal functionality.
- Balance checking.
- Encapsulation with private `__saldo` attribute.
