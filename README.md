# PHANTOM-AI

# Cyber Threat Prediction and Deception System

## Overview
The **Cyber Threat Prediction and Deception System** is an AI-powered platform designed to collect, analyze, and predict potential cyber threats. The system integrates threat intelligence scraping, machine learning-based predictions, and cyber deception techniques to identify and respond to attacks. The platform is capable of:

- Scraping external cyber threat intelligence data.
- Predicting future attack scenarios.
- Profiling attackers based on their behavior.
- Generating automated legal reports.
- Sending reports to authorities.

This project includes both backend and frontend components, providing an easy-to-use interface for interacting with the system and viewing threat intelligence, predictions, and reports.

## Features
- **Data Scraping**: Scrapes threat intelligence data from AlienVault OTX.
- **Threat Prediction**: Predicts potential cyber-attacks using machine learning models.
- **Attacker Profiling**: Profiles attackers based on their behavior and tactics.
- **Automated Report Generation**: Generates legal reports and sends them to authorities.
- **Web Interface**: Simple frontend for triggering backend processes (scraping, predictions, and report generation).

## Technologies Used
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, Pandas
- **Web Scraping**: Playwright (for threat intelligence collection)
- **Frontend**: HTML, JavaScript (for the user interface)
- **Database**: MongoDB (for storing threat intelligence data)
- **Email**: SMTP for sending reports
- **Logging**: Python logging module

## Project Structure

```
cyber-threat-scraper/
│── app.py                          # Flask app for handling user requests
│── main.py                         # Backend logic for scraping, predictions, and reports
│── reports/                        
│   ├── legal_report_generator.py   # Generates legal reports based on predictions
│── scrapers/                       
│   ├── alienvault_otx_scraper.py   # Scraper for collecting data from AlienVault OTX
│── ai_model/                       
│   ├── predict.py                  # Machine learning models for threat prediction and profiling
│── email_sender/                   
│   ├── email_sender.py             # Email logic for sending reports
│── config/                         
│   ├── __init__.py                 # Configuration file for email and MongoDB settings
│── templates/                      
│   ├── index.html                  # Frontend template for user interaction
└── requirements.txt                # List of required Python packages
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/cyber-threat-prediction.git
   cd cyber-threat-prediction
   ```

2. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MongoDB**:
   - Create a MongoDB database and update the `MONGO_URI` in `main.py` with your connection string.

4. **Configure Email Settings**:
   - Update the `config/__init__.py` file with your SMTP email credentials (for sending reports).

5. **Set up Playwright**:
   - Install the necessary browser dependencies for Playwright by running:

     ```bash
     playwright install
     ```

## Usage

### Running the Backend

1. **Start the Flask app** by running:

   ```bash
   python app.py
   ```

2. The app will run locally on `http://127.0.0.1:5000/`. You can access the interface from a web browser.

### Interacting with the Frontend

The web interface allows you to perform the following actions:
- **Start Scraping**: This button triggers the backend to collect threat intelligence data from AlienVault OTX.
- **Generate Predictions**: This triggers the prediction logic on the scraped data, which categorizes threats and predicts future attack scenarios.
- **Generate and Send Reports**: This generates legal reports based on predictions and sends them via email to the configured authorities.

### Scraping Data

- The system scrapes cyber threat intelligence data from AlienVault OTX, and optionally, from threat-related blogs if enabled.

### Making Predictions

- The backend uses machine learning models to predict the category of each threat and to forecast future attack patterns. Predictions are stored in a JSON file (`legal_database.json`).

### Generating Reports

- Legal reports are generated based on the predictions and are sent via email to the configured recipients (e.g., authorities or team members).

### Storing Data

- Threat intelligence data is stored in MongoDB, while predictions are saved in a JSON file for review.

## Example of Use

1. **Scrape Data**:
   - Press the "Start Scraping" button to fetch data from external sources.

2. **Make Predictions**:
   - Press "Generate Predictions" to categorize threats and predict future attacks.

3. **Generate and Send Reports**:
   - Press "Generate and Send Reports" to generate legal reports based on the predictions and send them to the relevant authorities.

## Troubleshooting

- Ensure all environment variables (MongoDB URI and email credentials) are properly configured.
- If using Playwright for scraping, make sure the necessary browser dependencies are installed by running `playwright install`.
- Check the logs (`app.log`) for error details.

## Acknowledgements
- This project leverages **scikit-learn** for machine learning-based threat prediction.
- The web scraping is powered by **Playwright** for efficient, headless browsing.
- **Flask** serves as the web framework for the backend.
