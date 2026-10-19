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


Kenyan Business Currency Tracker

Overview

A Python command-line application that converts Kenyan Shillings (KES) into multiple currencies using exchange-rate data from an API.

Features

Accepts an amount in Kenyan Shillings (KES).

Converts KES into USD, EUR, GBP, JPY, UGX, TZS, RWF, and ZAR.

Retrieves exchange rates from an external API.

Validates user input.

Handles errors when exchange rates cannot be retrieved.

Technologies Used

Python 3

Requests

ExchangeRate-API

JSON

Requirements

Python 3

Internet connection

requests Python package

How to Run

Install the required package:

python -m pip install requests

Run the application:

python currency_tracker.py

Enter the amount in KES when prompted to view the conversions.

Notes

Exchange rates are updated periodically and may differ from rates offered by banks or money-transfer services.