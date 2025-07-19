# 📰 News Fetcher with Python and NewsAPI

### 🤝Project Type: Made with Help

This is a simple Python script that lets you **search for the most popular news articles** on any topic using the [NewsAPI](https://newsapi.org/). You enter a topic, and it returns a list of headlines along with their URLs — clean and straight from the command line.

---

## 🌐 What It Does

- Prompts you to enter a topic of interest (e.g., "AI", "SpaceX", "Elections")  
- Sends a request to NewsAPI to fetch the most **popular** news articles from **July 17, 2025**  
- Parses the response and neatly displays the titles and URLs of the articles  

---

## 💻 Code Overview

Here’s what the script does, step-by-step:

1. Takes a topic as input from the user  
2. Forms a NewsAPI request URL using your API key  
3. Sends a GET request to NewsAPI  
4. Parses the returned JSON response  
5. Iterates over the articles and prints each article's title and link  

---

## 🧠 How to Use

1. ✅ Make sure you have Python installed (preferably Python 3.7+).
2. ✅ Install the `requests` module if you haven’t already:
   ```
   pip install requests
   ```
3. 🧾 Replace the API key (`4959237c1b0d42e780524462f8c0cb59`) with your own from [newsapi.org](https://newsapi.org/register) (it's free!).
4. 🏃‍♀️ Run the script:
   ```
   python news_fetcher.py
   ```

5. 📥 When prompted, type a topic you're interested in:
   ```
   Enter the topic, in which you are interested today: climate change
   ```

6. 📰 You'll see a list of article titles and URLs.

---

## 🛡️ Disclaimer

- This script is for **educational purposes** only.
- The API key provided in the code above has **usage limits**, so you may need to get your own at [newsapi.org](https://newsapi.org).
- Always handle API data responsibly and abide by API provider’s terms of service.

## 📜 License

This project is for educational and personal use only. For commercial use of NewsAPI, check their official terms and pricing.

