# 🔐 Random Password Generator — Version 1 (V1)

> **Important:** This repository contains **Version 1 (V1)** of the Random Password Generator.  
> The improved **Version 2.0** (with persistence, multi-user support, and better architecture) is available here: **[➡️ View Version 2.0 on GitHub](https://github.com/MrHacker2006/advanced-random-password-generator.git)**

---

## Overview
A small, interactive Python script that generates strong random passwords based on user-selected constraints and copies the result to your clipboard. V1 focuses on a minimal, easy-to-run experience — perfect for learning and quick usage.

---

## Features (V1)
- ✅ Interactive prompts for password length and character types (numbers, lowercase, uppercase, punctuation)  
- ✅ Option to **guarantee at least one character from each selected type**  
- ✅ Final shuffle for unpredictability  
- ✅ Automatic copy to clipboard via `pyperclip`  
- ✅ Lightweight, dependency-minimal, beginner-friendly

> **Note:** Persistent storage, multi-user support, CSV export, and encryption are part of V2.0.

---

## Quick Start

### Requirements
- Python 3.7+  
- `pyperclip` (used to copy generated password to the clipboard)

---

### Install dependency
```bash
pip install pyperclip
```
---

### Run the script
```bash
python v1_random_password_generator.py
```

---

### Usage Example (sample interaction)

Welcome to the Random Password Generator!

Enter the length of the password (in integers), which you want to generate : 12

What things you want in your password? Answer below👇

Do you want to include Numbers ? (Y/N): y
Do you want to include Lowercase Letters ? (Y/N): y
Do you want to include Uppercase letters ? (Y/N): y
Do you want to include Punctuations ? (Y/N): n

Do You want one character from each type you have selected? (Y/N) : y

The Final Password is : 9AbxDqlmPj2r
This password is copied in your clipboard automatically.

---

## Project structure

random-password-generator-v1/
├─ random_password_generator.py    # Main interactive script (this V1 code)
├─ README.md                       # This file

---

## Limitations (V1) & Next Steps

🔒 No persistent credential storage — V1 does not save passwords. (V2.0 adds CSV-backed multi-user storage.)

🔐 No encryption at rest — passwords are generated and copied to clipboard only. Plan: encryption option in V2.0.

⚙️ Interactive only — no CLI flags for automation. Consider argparse-based flags for scripting.

📦 Input handling — script can exit on invalid inputs; improve by re-prompting and better validation.

Planned / available in V2.0: persistent storage (local CSV), multi-user support, modular architecture, better error handling, optional encryption, and CLI flags.

---

## Contributing

Thanks for considering contributing! To contribute:

1. Fork the repo.

2. Create a branch: git checkout -b feature/your-feature

3. Implement changes and add tests/examples where applicable.

4. Open a Pull Request explaining the change and rationale.

If you’re aiming to help with V2.0 features (CSV migration, multi-user, encryption), mention that in the PR so we can coordinate.

---

## Versioning & Where to find V2.0

- This repository is V1 — a compact, interactive generator.

- V2.0 (recommended for production-like workflows) includes storage, multi-user features, and architecture improvements.

- V2.0 repo link : https://github.com/MrHacker2006/advanced-random-password-generator.git

---

## Contact

Questions, ideas, or collaboration?

GitHub: https://github.com/MrHacker2006

Email: guptagautam908@gmail.com




