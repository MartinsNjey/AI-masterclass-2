# Travel Weather Tool

## Overview
A Python command-line tool that retrieves live weather information for a city and combines it with country information.

## Features
- Accepts a city name from the user.
- Fetches weather data from an API.
- Retrieves country information, including region and population.
- Combines data from multiple API calls.
- Saves the weather response to a JSON file.
- Displays information in a readable format.
- Handles errors when data cannot be retrieved.

## Requirements
- Python 3
- `requests`
- `python-dotenv`
- An OpenWeather API key stored in a `.env` file.

## Installation
Install the required packages:

```
pip install requests python-dotenv
```

Create a `.env` file in the project folder and add your API key:

```
OPENWEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key. Do not upload your API key to GitHub.

## How to Run

Open the terminal in the project folder and run:

```
python day3_travel_info.py
```

Enter a city name when prompted.

## Output
The tool displays the current weather and country information and saves the weather response in a JSON file.

## Project Purpose
This project demonstrates Python functions, API requests, JSON file handling, environment variables, user input, and error handling.

---

# AI Masterclass Projects

A collection of Python and data projects built during the AI Masterclass Foundation program.

---

## 1. Kenyan Business Currency Tracker

### Overview

A Python command-line application that converts Kenyan Shillings (KES) into multiple foreign currencies using live exchange-rate data from an online API.

### Features

- Converts KES into USD, EUR, GBP, JPY, UGX, TZS, RWF, and ZAR.
- Retrieves exchange rates online.
- Displays conversion results to two decimal places.
- Handles invalid amounts, unsupported currencies, and connection errors.

### Technologies

- Python 3
- Requests
- python-dotenv
- Exchange-rate API

### Setup

**1. Install the required packages**

```bash
python -m pip install requests python-dotenv
```

**2. Run the application**

```bash
python currency_tracker.py
```

**3. Use the tracker**

Enter an amount in Kenyan Shillings when prompted to display the conversions.

### Important Notes

- Exchange rates change and may differ from rates offered by banks or money-transfer services.
- Conversion results are estimates and should be checked before financial decisions.