import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import base64
import schedule, time, logging

logging.basicConfig(filename="report.log", level=logging.INFO,
                    format="%(asctime)s | %(message)s")

def generate_report():
    # 1. Load nutrition programme data
    df = pd.read_csv("data/nutrition_program.csv")

    print(df.head())

    # 2. Generate three charts

    # Chart 1: Beneficiaries by county
    df.groupby("county")["beneficiaries"].sum().plot(kind="bar")
    plt.title("Beneficiaries by County")
    plt.ylabel("Number of Beneficiaries")
    plt.savefig("charts/beneficiaries_by_county.png")
    plt.close()

    # Chart 2: Meals served by county
    df.groupby("county")["meals_served"].sum().plot(kind="bar")
    plt.title("Meals Served by County")
    plt.ylabel("Number of Meals")
    plt.savefig("charts/meals_by_county.png")
    plt.close()

    # Chart 3: Average weight trend
    df.groupby("date")["average_weight_kg"].mean().plot(
        kind="line", marker="o"
    )
    plt.title("Average Weight Trend")
    plt.ylabel("Average Weight (kg)")
    plt.savefig("charts/average_weight_trend.png")
    plt.close()

        # 3. Create a one-paragraph summary
    total_beneficiaries = df["beneficiaries"].sum()
    total_meals = df["meals_served"].sum()
    average_weight = df["average_weight_kg"].mean()

    summary = (
        f"The nutrition programme served {total_beneficiaries} beneficiaries "
        f"and provided {total_meals} meals. The average recorded weight "
        f"across the programme data was {average_weight:.1f} kg."
    )

    print(summary)

        # 4. Convert charts to Base64
    def image_to_base64(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

        # 5. Convert all three charts
    beneficiaries_chart = image_to_base64("charts/beneficiaries_by_county.png")
    meals_chart = image_to_base64("charts/meals_by_county.png")
    weight_chart = image_to_base64("charts/average_weight_trend.png")

        # 6. Build the HTML report
    today = datetime.date.today().strftime("%Y-%m-%d")
    timestamp = datetime.datetime.now().strftime("%A %d %B %Y at %H:%M")

    html = f"""
    <html>
    <head>
        <title>Nutrition Programme Report - {today}</title>
    </head>
    <body>
        <h1>Nutrition Programme Report - {today}</h1>
        <p>Last updated: {timestamp}</p>

        <h2>Summary</h2>
        <p>{summary}</p>

        <h2>Beneficiaries by County</h2>
        <img src="data:image/png;base64,{beneficiaries_chart}">

        <h2>Meals Served by County</h2>
        <img src="data:image/png;base64,{meals_chart}">

        <h2>Average Weight Trend</h2>
        <img src="data:image/png;base64,{weight_chart}">
    </body>
    </html>
    """

    # 7. Save the HTML report
    filename = f"reports/report_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.html"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)

    print(f"Report saved to {filename}")

# 8. Schedule the report every Monday at 7am

def daily_job():
    try:
        generate_report()
        logging.info("Report generated and saved OK")
    except Exception as e:
        logging.error(f"Report failed: {e}")

daily_job()
schedule.every().monday.at("07:00").do(daily_job)

while True:
    schedule.run_pending()
    time.sleep(60)