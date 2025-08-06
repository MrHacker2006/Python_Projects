# 🔐 Random Password Generator

A simple, self-built Python tool to create strong passwords on demand—no tutorials followed, just pure problem-solving (with tiny AI nudges when I got stuck).

---

## 🚀 Features

- Choose password length (any positive integer)  
- Include or exclude:
  - Numbers (0–9)  
  - Lowercase letters (a–z)  
  - Uppercase letters (A–Z)  
  - Punctuation symbols (!@#$…)
- Optionally enforce at least one character from each selected set  
- Final password is auto-shuffled for extra randomness  
- Automatically copied to your clipboard for easy pasting

---

## ⚙️ How to Use

1. Clone this folder and open a terminal.  
2. Run with Python 3.10+:  
   
       python password_generator.py

3. Follow the prompts—answer Y/N questions to customize your password.  
4. Your new password appears on screen and is ready to paste!

---

## 🛠️ Requirements

- Python 3.10 or higher  
- Built-in modules: `random`, `string`, `sys`  
- Third-party: `pyperclip` (install via `pip install pyperclip`)

---

## 📝 Notes

- Invalid inputs (non-integers, negative lengths) are caught and re-prompted.  
- If you choose no character sets, the program exits with an error message.  

---

## 🤝 Attribution

Made from scratch by Gautam Gupta— no step-by-step video tutorials followed, just iterative thinking and a few AI hints.  
Feel free to fork, tweak, and build on it!

---

## 📜 License

This project is released under the [MIT License](https://github.com/MrHacker2006/Python_Projects/blob/39fb5e74de23894dadee69847c9738acef73b410/LICENSE).  
See the LICENSE file in the repo root for full details.
