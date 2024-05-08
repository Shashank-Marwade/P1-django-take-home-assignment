# 🚀 RAKT's "Out-of-the-Box" Engineering Challenge 🌟

Welcome to RAKT's unique and exciting way of discovering new talent. At RAKT, we believe in fun, creativity, and thinking outside the box. This challenge is your playground to showcase your skills in a way that's both enjoyable and insightful.

## 🎉 Why We Do This Differently

- **Enjoy the Process**: We want you to have fun with this challenge. Think of it as a mini-hackathon where your creativity and innovation can shine.
- **Reflect Real-World Scenarios**: Just like our work at RAKT, this challenge mirrors real-world scenarios but with a twist of fun and creativity.
- **No Pressure**: Say goodbye to the traditional, high-pressure coding interviews. We're more interested in how you think and create, not just how you code under stress.

## 🌐 The Problem : World Needs More Food Trucks!

Our team in San Francisco are on a quest to discover the hidden gems of street food, particularly food trucks! Your challenge is to to make it possible for us to find a food truck no matter where our work takes us in the city.

This is a freeform assignment. You can write a web API that returns a set of food trucks (our team is fluent in JSON). You can write a web frontend that visualizes the nearby food trucks. We also spend a lot of time in the shell, so a CLI that gives us a couple of local options would be great. And don't be constrained by these ideas if you have a better one!

The only requirement for the assignment is that it give us at least 5 food trucks to choose from a particular latitude and longitude.

Feel free to tackle this problem in a way that demonstrates your expertise of an area -- or takes you out of your comfort zone. For example, if you build Web APIs by day and want to build a frontend to the problem or a completely different language instead, by all means go for it - learning is a core competency in our group. Let us know this context in your solution's documentation.

San Francisco's food truck open dataset (csv) is included in this [repo](https://raw.githubusercontent.com/RAKT-Innovations/P1-django-take-home-assignment/main/food-truck-data.csv).


## 🕹️ Our Approach
- **Time Commitment:** Dedicate around three hours of focused work to this assignment. Quality matters more to us than quantity, so there's no need to overengineer your solution.
- **Real-World Simulation:** Treat this task as you would a project intended for production. Create a GitHub repository, use git for version control, and document your project in a README.md file.
- **Production-Oriented:** Your solution should reflect what you would deliver in a production environment. We understand this might limit the scope within the given time, but we prefer a production-ready approach over a feature-heavy one.
- **Documentation and Rationale:** Document your technical decisions, trade-offs, and any considerations you had. If you had more time or were to do it again, let us know what you would change or improve.
- **Flexibility in Tools and Languages:** Please use django as your framework but do not limit yourself to vanilla django, feel free to use everything you'd like on top of it.

## 📬 How to Submit Your Work
- **Private Fork:** Instead of forking the public repository, create a copy of it. You can do this by cloning the repository to your local machine and then pushing it as a new **public repository** under your own GitHub account.
- **Document Your Process:** Include a README.md in your submission detailing how to set up and run your script. This should be unique to your implementation and understanding.
- **Comment Your Code:** Ensure your script is well-documented with comments that explain your logic and approach. This documentation should reflect your personal problem-solving process.
- **Email Submission:** Rather than creating a pull request, which is public, send us a link to your public repository via email to developer@rakt.org with the title "[P1-Submission] Your name". Ensure your repo is public so that we can access it.
- **Deadline:** Please submit your assignment within 5 days of receiving these instructions.

# Hidden Gems: Discover Food Trucks Near You

Welcome to "Hidden Gems," a Django-based application designed to help you find food trucks in San Francisco. This application is my response to RAKT's "Out-of-the-Box" Engineering Challenge. It leverages the haversine formula to calculate distances, utilizes pandas for data management, and incorporates a map interface via Leaflet for a user-friendly visualization of food truck locations.

## 🎯 Features

- **Web Interface**: A Leaflet map that visualizes food trucks near a specified location.
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

Ensure you have Python installed on your machine. This application is built using Python 3.8. You can download it from [python.org](https://www.python.org/downloads/).

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

