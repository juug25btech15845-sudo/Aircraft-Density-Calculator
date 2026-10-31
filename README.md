✈️ AeroDensity – Aircraft Atmospheric Density & Performance Simulator

<p align="center">
<b>An Interactive Aircraft Atmospheric Density and Performance Simulation Dashboard</b>
<br>
Developed using Python, Streamlit, NumPy, Pandas, and Plotly.
</p>

<p align="center">
<a href="https://aircraft-density-calculator-szszzzchvwdaqdcesk5mjm.streamlit.app/">
🚀 VIEW LIVE APPLICATION
</a>
</p>

🌐 Live Application

Explore the deployed application:

🔗 https://aircraft-density-calculator-szszzzchvwdaqdcesk5mjm.streamlit.app/

The application is deployed using Streamlit Community Cloud.

📌 Project Overview

AeroDensity is an interactive web-based aircraft atmospheric simulation application designed to calculate and visualize atmospheric properties at different aircraft altitudes.

The application implements the International Standard Atmosphere (ISA) model to calculate:

Air temperature
Atmospheric pressure
Air density
Speed of sound

The simulation covers altitudes from sea level up to 20,000 metres.

Users can interactively select aircraft altitude and observe how atmospheric conditions change with increasing altitude through real-time calculations, interactive graphs, and a data visualization dashboard.

The project is developed using Python and Streamlit, with Plotly providing interactive data visualizations.

🎯 Project Objectives
Calculate atmospheric air density at different aircraft altitudes.
Analyze temperature variations with altitude.
Calculate atmospheric pressure under standard atmospheric conditions.
Determine the speed of sound at different altitudes.
Visualize atmospheric properties through interactive graphs.
Develop an interactive dashboard for exploring aircraft atmospheric conditions.
Export calculated atmospheric data in CSV format.
🚀 Key Features
1. Interactive Altitude Simulation
Adjustable aircraft altitude from 0 to 20,000 metres.
Interactive altitude slider.
Precise altitude input.
Real-time atmospheric calculations.
2. Atmospheric Parameter Calculations

The application calculates the following atmospheric parameters:

Parameter	Unit
Aircraft Altitude	metres (m)
Temperature	Celsius (°C)
Atmospheric Pressure	kilopascals (kPa)
Air Density	kg/m³
Speed of Sound	m/s
3. Air Density Ratio Gauge
Displays the percentage of air density relative to standard sea-level air density.
Dynamically updates according to the selected aircraft altitude.
Provides a visual representation of atmospheric density reduction.
4. Interactive Graphs

The dashboard includes four interactive Plotly visualizations:

Air Density vs Altitude
Temperature vs Altitude
Atmospheric Pressure vs Altitude
Atmospheric Density and Pressure Comparison
5. Atmospheric Data Explorer

Provides a calculated atmospheric data table containing:

Altitude
Temperature
Atmospheric Pressure
Air Density
Speed of Sound
6. CSV Data Export

Users can download the generated atmospheric dataset in CSV format for further analysis and documentation.

7. Aerospace Dashboard Interface
Dark aerospace-themed interface.
Interactive Plotly charts.
Real-time simulation results.
Responsive Streamlit layout.
Dedicated simulation controls.
🧮 Mathematical Model

The application uses the International Standard Atmosphere (ISA) model for dry air.

The simulation covers two atmospheric regions.

1. Troposphere (0–11,000 m)

Temperature calculation:

𝑇
=
𝑇
0
−
𝐿
×
ℎ

Pressure calculation:

𝑃
=
𝑃
0
(
𝑇
𝑇
0
)
𝑔
0
𝑅
𝐿
2. Lower Stratosphere (11,000–20,000 m)

In this region, temperature remains constant at 216.65 K.

Pressure calculation:

𝑃
=
𝑃
11
exp
⁡
(
−
𝑔
0
(
ℎ
−
11000
)
𝑅
𝑇
11
)
3. Air Density Calculation

Using the Ideal Gas Law:

𝜌
=
𝑃
𝑅
𝑇
4. Speed of Sound Calculation
𝑎
=
𝛾
𝑅
𝑇
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
Streamlit Community Cloud	Application deployment
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


Replace YOUR_GITHUB_REPOSITORY_URL with your actual GitHub repository URL.

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

The project requires the following Python libraries:

text
streamlit
numpy
pandas
plotly


Install all dependencies using:

bash
python -m pip install -r requirements.txt

☁️ Deployment

The application is deployed using Streamlit Community Cloud.

Deployment Process
Upload the project files to a GitHub repository.
Connect the GitHub repository to Streamlit Community Cloud.
Select the appropriate GitHub branch.
Set app.py as the main application file.
Deploy the application.
Access the application using the generated Streamlit URL.
Live Deployment Link

🚀 https://aircraft-density-calculator-szszzzchvwdaqdcesk5mjm.streamlit.app/

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
The simulation is intended for educational and analytical purposes and is not certified for aircraft flight operations.
🔮 Future Enhancements

Possible future developments include:

Real-time weather data integration.
Humidity and temperature corrections.
Aircraft performance estimation.
Mach number and dynamic pressure calculations.
Aircraft fuel consumption analysis.
Extended atmospheric simulation.
Additional interactive aerospace visualizations.
👨‍💻 Project Information
Category	Details
Project Name	AeroDensity
Project Type	Aircraft Atmospheric Simulator
Domain	Aerospace Engineering
Programming Language	Python
Framework	Streamlit
Deployment	Streamlit Community Cloud
Simulation Model	International Standard Atmosphere (ISA)
⭐ Acknowledgement

This project is based on the International Standard Atmosphere (ISA) model and uses Python-based scientific computing and visualization libraries.

Special acknowledgement to the developers and contributors of Python, Streamlit, NumPy, Pandas, and Plotly for providing the tools used to develop this application.

If you find this project useful, consider giving the GitHub repository a ⭐ star!

<p align="center">
<b>✈️ AeroDensity – Exploring Atmospheric Conditions for Aerospace Applications</b>
<br><br>
<a href="https://aircraft-density-calculator-szszzzchvwdaqdcesk5mjm.streamlit.app/">
Open Live Application 🚀
</a>
</p>
