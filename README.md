# Binance Futures Trading Bot

## Project Overview

This project is a simple **Python-based trading bot** that interacts with the **Binance Futures Testnet API** to place cryptocurrency orders.

The bot allows users to place **Market** and **Limit orders** through a **Command Line Interface (CLI)**. It also includes logging, input validation, and error handling to ensure reliability.

The bot connects to the **Binance Futures Testnet** instead of the live exchange, allowing safe testing without real money.

---

## Features

* Place **Market Orders**
* Place **Limit Orders**
* Command Line Interface (CLI)
* Input validation
* Logging of order activity
* Error handling
* Modular project structure

---

## Technologies Used

* Python
* Binance Futures API
* python-binance library
* dotenv for environment variables
* logging module

---

## Project Structure

```
trading_bot
│
├── bot
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

Clone the repository

```
git clone https://github.com/yourusername/binance-trading-bot.git
cd binance-trading-bot
```

Install required libraries

```
pip install -r requirements.txt
```

---

## Setup API Keys

Create a `.env` file in the root folder and add your **Binance Futures Testnet API keys**.

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

You can generate API keys from the Binance Futures Testnet dashboard.

---

## Running the Bot

### Market Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01
```

### Limit Order

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.01 --price 30000
```

---

## Example Output

```
Order Summary
-------------
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01

Order Response
--------------
Order ID: 12345678
Status: NEW
Executed Qty: 0.000
```

---

## Logs

All trading activity is recorded in a log file.

```
logs/trading.log
```

Example log entry:

```
2026-03-15 INFO Market order placed BTCUSDT BUY
```

---

## Assumptions

* The bot only supports **USDT futures pairs**.
* Minimum order value must meet Binance Futures requirements (~100 USDT).
* The project is designed for **testnet usage only**.

---

## Future Improvements

* Add Stop-Limit Orders
* Add Web UI dashboard
* Add automated trading strategies
* Add position management

---

## Disclaimer

This project is for **educational purposes only**.
It uses the Binance Futures Testnet and does not involve real trading.

---

## Author

Developed by: Sntosh Gautam
