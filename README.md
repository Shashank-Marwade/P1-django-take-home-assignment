# Hidden Gems: Discover Food Trucks Near You

Welcome to "Hidden Gems," a Django-based application designed to help you find food trucks in San Francisco. This application is my response to RAKT's "Out-of-the-Box" Engineering Challenge. It leverages the haversine formula to calculate distances, utilizes pandas for data management, and incorporates a map interface via Leaflet for a user-friendly visualization of food truck locations.

## 🎯 Features

- **Web Interface**: A Leaflet map that list food trucks near a specified location.
- **Command Line Interface (CLI)**: Provides a quick lookup to find nearby food trucks based on user-input latitude and longitude.
- **Logging**: The application incorporates a robust logging system to capture and record key events and errors. This feature is critical for troubleshooting, maintenance, and ensuring the reliability of the application over time. Logs can help track down issues such as unexpected data values, like NaNs, or operational problems.


## 🛠️ Technology Stack

- **Django**: For the backend and web interface.
- **Pandas**: To handle and process the `food-truck-data.csv`.
- **Leaflet**: For mapping and geographic functionality.
- **Haversine Formula**: To calculate the geographical distance between points.

## ⚙️ Setup and Installation

Follow these steps to get "Hidden Gems" running locally:

### Prerequisites

Ensure you have Python installed on your machine. This application is built using Python 3.9. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/Shashank-Marwade/P1-django-take-home-assignment.git
cd P1-django-take-home-assignment
```

### Step 2: Install Dependencies

Navigate to the project directory and install the required Python libraries:

```bash
cd hidden_gems
pip install -r requirements.txt
```

### Step 3: Run the Application

To start the web application, run:

```bash
cd hidden_gems
python manage.py runserver
```

Then, open your browser and go to http://127.0.0.1:8000 to view the map and search for food trucks.

### Step 4: Using the CLI

To use the CLI tool for finding nearby food trucks, use the following command in the project directory:

```bash
python manage.py querycsv [latitude] [longitude]

```

For example:

```bash
python manage.py querycsv 37.7749 -122.4194

```

This will list at least five nearby food trucks based on the provided geographic coordinates.

## 📖 Documentation

Each part of the application and script is well-commented to explain the functionality and logic. Detailed comments are provided to ensure clarity and ease of understanding.

## 🔄 If I Had More Time

Testing: Implement a full suite of unit and integration tests to ensure reliability and facilitate future updates.
User Authentication: Add user management to save favorite trucks and preferences.
Enhanced UI: More interactive elements and better design practices could be applied to the frontend.

## 📬 Submission

This is a submission for RAKT's "Out-of-the-Box" Engineering Challenge. The repository can be accessed publicly but is intended for evaluation by RAKT's engineering team as part of the job application process.

