# Online Price Alert App

A Flask web application that tracks product prices on online stores and notifies the user when an item drops below a target price. Users register stores (with the HTML tag/CSS selector that contains the price), add product URLs with a price limit, and a separate updater script periodically scrapes the current prices and triggers alerts.

## Tech stack

- Python 3 / Flask (blueprints for `alerts`, `stores`, `users`)
- MongoDB (via `pymongo`) for persistence
- `requests` + `BeautifulSoup` for scraping product pages
- Jinja2 / HTML templates for the UI

## Project structure

- `app.py` — Flask entry point, registers blueprints under `/alerts`, `/stores`, `/users`
- `alert_updater.py` — standalone script that loads every saved alert, refreshes its scraped price, and prints a notification when the price is at or below the limit
- `flipkart_price.py` — early standalone scraper used as a prototype against a Flipkart product page
- `models/` — `Model` base (Mongo CRUD), plus `Item`, `Alert`, `Store`, and `User`
- `views/` — Flask blueprints with the routes for alerts, stores, and users
- `common/database.py` — thin `pymongo` wrapper; expects MongoDB at `mongodb://127.0.0.1:27017/pricing`
- `common/utils.py` — email validation helper
- `templates/` — Jinja templates for each blueprint

## How to run

1. Install and start MongoDB locally on the default port (`27017`); the app uses the `pricing` database.
2. Install dependencies:
   ```
   pip install flask pymongo requests beautifulsoup4
   ```
3. Start the web app:
   ```
   python app.py
   ```
   It runs in debug mode on Flask's default port (`http://127.0.0.1:5000`).
4. In the UI, first create a Store (name, URL prefix, the HTML tag and a JSON query that selects the price element on that store's product pages), then add an Alert with a product URL and a price limit.
5. To check prices and trigger notifications, run the updater script (e.g. on a schedule):
   ```
   python alert_updater.py
   ```

## Notifications

The current updater prints a console message when an item's scraped price drops below the configured limit; no email/SMS/Telegram channel is wired up in this version.

## Status

Work in progress — a learning project for combining Flask, MongoDB, and web scraping.
