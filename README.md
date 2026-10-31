✈️ AeroDensity – Aircraft Atmospheric Density & Performance Simulator

<p align="center">
<b>An Interactive Aircraft Atmospheric Density and Performance Simulation Dashboard</b>
</p>

<p align="center">
Built using Python, Streamlit, NumPy, Pandas, and Plotly.
</p>

🌐 Live Application

Try the live application here:

🚀 AeroDensity – Open Live Dashboard

The application is deployed using Streamlit Community Cloud.

📌 Project Overview

AeroDensity is an interactive web-based aircraft atmospheric simulation application designed to calculate and visualize atmospheric properties at different aircraft altitudes.

The application implements the International Standard Atmosphere (ISA) model to calculate air temperature, atmospheric pressure, air density, and speed of sound from sea level up to 20,000 metres.

It provides an interactive dashboard where users can select aircraft altitude and observe how atmospheric conditions change with increasing altitude.

The project is developed using Python and Streamlit, with Plotly providing interactive data visualizations.

🎯 Objectives
Calculate atmospheric air density at different aircraft altitudes.
Analyze temperature variations with altitude.
Calculate atmospheric pressure under standard atmospheric conditions.
Determine the speed of sound at different altitudes.
Visualize atmospheric properties through interactive graphs.
Provide an interactive dashboard for exploring aircraft atmospheric conditions.
Export calculated atmospheric data in CSV format.
🚀 Key Features
1. Interactive Altitude Simulation
Adjustable aircraft altitude from 0 to 20,000 metres.
Interactive altitude slider.
Precise altitude input.
Real-time atmospheric calculations.
2. Atmospheric Parameter Calculations

The application calculates:

Parameter	Unit
Aircraft Altitude	metres (m)
Temperature	Celsius (°C)
Atmospheric Pressure	kilopascals (kPa)
Air Density	kg/m³
Speed of Sound	m/s
3. Air Density Ratio Gauge

Displays the percentage of air density relative to standard sea-level air density.

4. Interactive Graphs

The dashboard includes four interactive visualizations:

Air Density vs Altitude
Temperature vs Altitude
Atmospheric Pressure vs Altitude
Atmospheric Density and Pressure Comparison
5. Atmospheric Data Explorer

Provides a calculated atmospheric data table containing:

Altitude
Temperature
Pressure
Density
Speed of Sound
6. CSV Data Export

Users can download the generated atmospheric dataset for further analysis.

7. Aerospace Dashboard Interface
Dark aerospace-themed interface.
Interactive Plotly charts.
Real-time simulation results.
Responsive Streamlit layout.
🧮 Mathematical Model

The application uses the International Standard Atmosphere (ISA) model for dry air.

The simulation covers two atmospheric regions.

1. Troposphere (0–11,000 m)

Temperature:

T = T₀ − L × h

Pressure:

P = P₀ × (T/T₀)^(g₀/(R×L))

2. Lower Stratosphere (11,000–20,000 m)

Temperature remains constant at 216.65 K.

Pressure:

P = P₁₁ × exp[-g₀(h − 11000)/(R × T₁₁)]

3. Air Density Calculation

Using the Ideal Gas Law:

ρ = P/(R × T)

4. Speed of Sound Calculation

a = √(γ × R × T)

⚙️ Constants Used
Parameter	Value
Sea-Level Temperature	288.15 K
Sea-Level Pressure	101325 Pa
Specific Gas Constant	287.05287 J/(kg·K)
Gravitational Acceleration	9.80665 m/s²
Temperature Lapse Rate	0.0065 K/m
Specific Heat Ratio	1.4
Tropopause Altitude	11,000 m
Maximum Simulation Altitude	20,000 m
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Streamlit	Web application development
NumPy	Numerical calculations
Pandas	Data processing and tabulation
Plotly	Interactive graphs and gauge visualization
GitHub	Source code management
Streamlit Cloud	Application deployment
📂 Project Structure
text
Aircraft-Density-Calculator/
│
├── app.py
│
├── requirements.txt
│
└── README.md

💻 Installation and Setup

Follow these steps to run the application locally.

Step 1: Clone the Repository
bash
git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Navigate to the Project Folder
bash
cd Aircraft-Density-Calculator

Step 3: Install Required Dependencies
bash
python -m pip install -r requirements.txt

Step 4: Run the Streamlit Application
bash
python -m streamlit run app.py

Step 5: Open the Application

Open the local URL displayed in your terminal:

text
http://localhost:8501

📦 Requirements

The following Python libraries are required:

text
streamlit
numpy
pandas
plotly

☁️ Deployment

The application is deployed using Streamlit Community Cloud.

Deployment process:

Upload the project files to a GitHub repository.
Connect the GitHub repository to Streamlit Community Cloud.
Select the app.py file as the main application file.
Deploy the application.
Access the application through the generated Streamlit URL.

Live deployment:
https://aircraft-density-calculator-szszzzchvwdaqdcesk5mjm.streamlit.app/

📊 Applications

This project can be useful for:

Aerospace engineering education.
Aircraft atmospheric performance studies.
Understanding atmospheric density variations.
Studying the International Standard Atmosphere.
Aircraft flight environment analysis.
Engineering simulations and academic projects.
⚠️ Limitations
The simulation uses standard atmospheric conditions.
The model assumes dry air.
Atmospheric calculations are limited to 0–20,000 metres.
Weather variations and real-time atmospheric measurements are not included.
The simulation is intended for educational and analytical purposes, not certified aircraft flight operations.
🔮 Future Enhancements

Possible future developments include:

Real-time weather data integration.
Humidity and temperature correction.
Aircraft performance estimation.
Mach number and dynamic pressure calculations.
Aircraft fuel consumption analysis.
Extended atmospheric simulation.
Additional interactive aerospace visualizations.
👨‍💻 Author

Project: AeroDensity – Aircraft Atmospheric Density & Performance Simulator

Domain: Aerospace Engineering / Python-Based Simulation

Framework: Streamlit

⭐ Acknowledgement

This project is based on the International Standard Atmosphere (ISA) model and uses Python-based scientific computing and visualization libraries.

If you find this project useful, consider giving the GitHub repository a ⭐ star!

<p align="center">
<b>✈️ AeroDensity – Exploring Atmospheric Conditions for Aerospace Applications</b>
</p>
