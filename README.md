# Email News API Application

## Description
The Email News API Application is a Python-based project that fetches the latest news from a news API and automatically sends curated news updates to users via email.

## Features
- Fetches real-time news using a News API (newsdata.io).
- Formats news content for email delivery.
- Sends news updates automatically via email.
- Supports secure email authentication using App Passwords from Google.

## Technologies Used
- Python
- Requests
- smtplib
- email 
- News API(newsdata.io)

## Project Structure
- `email_news_app.py` – Main application file
- `send_email.py` – Handles email sending logic

## How It Works
1. The app requests news data from a News API.
2. News headlines and descriptions are processed.
3. The formatted news content is sent to the user’s email.

## How to Run 
1. Install required dependencies  
   ```bash
   pip install requests


