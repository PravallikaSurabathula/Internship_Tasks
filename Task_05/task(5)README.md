# 🔐 Task 05 – Secure Password Generator (Python)

## 📌 Description

This project is a **secure password generator** built using Python. It creates cryptographically strong passwords and calculates their **entropy** (a measure of password strength in bits). The tool helps users generate passwords that are both random and secure by combining uppercase, lowercase, digits, and symbols.

---

## 🔑 Features

- Generates strong, random passwords using `secrets` for cryptographic randomness.
- Supports custom password length.
- Calculates **entropy** (bits of security) to evaluate password strength.
- Provides feedback on whether the password is weak, moderate, or strong.
- Interactive loop lets the user regenerate passwords until satisfied.

---

## 🧮 Entropy Explanation

Password entropy is calculated using the formula:

Where:
- `pool_size` is the number of unique characters used (e.g., uppercase, lowercase, digits, punctuation).
- Higher entropy = more secure password.
- **< 50 bits**: Weak  
- **50–80 bits**: Moderate  
- **80+ bits**: Strong

---

## 💻 Sample Output

```bash
===== Secure Password Generator =====
Enter desired password length: 12

Generated Password: @kC8dLqW&h#z
Password Entropy: 85.54 bits
Strong password! Very secure.

Are you happy with this password? (yes/no): yes
Password finalized.
