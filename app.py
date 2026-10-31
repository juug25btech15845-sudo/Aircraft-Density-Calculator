import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AeroDensity | Aircraft Atmosphere Simulator",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS - AEROSPACE DASHBOARD THEME
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Orbitron:wght@500;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #07111f 0%, #0b1729 50%, #101f35 100%);
    color: #e5edf8;
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1500px;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: #0b1627;
    border-right: 1px solid #1d3553;
}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #dbeafe;
}

/* Main title */

.hero-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.5rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 1px;
}

.hero-subtitle {
    color: #94a3b8;
    font-size: 1rem;
    margin-top: -10px;
}

.section-title {
    font-family: 'Orbitron', sans-serif;
    color: #dbeafe;
    font-size: 1.15rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

/* Metric cards */

div[data-testid="stMetric"] {
    background: linear-gradient(145deg, #13243a, #0e1c2f);
    border: 1px solid #263e5c;
    border-radius: 14px;
    padding: 20px 22px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
}

div[data-testid="stMetricLabel"] {
    color: #94a3b8;
    font-size: 0.9rem;
}

div[data-testid="stMetricValue"] {
    color: #38bdf8;
    font-family: 'Orbitron', sans-serif;
    font-size: 1.6rem;
}

/* Information cards */

.info-card {
    background: linear-gradient(145deg, #13243a, #0e1c2f);
    border: 1px solid #263e5c;
    border-radius: 14px;
    padding: 22px;
    margin-bottom: 12px;
}

.info-label {
    color: #94a3b8;
    font-size: 0.85rem;
}

.info-value {
    color: #38bdf8;
    font-size: 1.5rem;
    font-weight: 700;
    margin-top: 6px;
}

/* Status */

.status-pill {
    display: inline-block;
    background: rgba(34, 197, 94, 0.12);
    border: 1px solid rgba(34, 197, 94, 0.4);
    color: #4ade80;
    padding: 6px 14px;
    border-radius: 30px;
    font-size: 0.8rem;
    font-weight: 600;
}

/* Buttons */

.stDownloadButton button {
    background: linear-gradient(90deg, #0284c7, #2563eb);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
}

.stDownloadButton button:hover {
    background: linear-gradient(90deg, #0369a1, #1d4ed8);
    color: white;
}

/* Divider */

hr {
    border-color: #263e5c;
}

/* Dataframe */

div[data-testid="stDataFrame"] {
    border: 1px solid #263e5c;
    border-radius: 12px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# INTERNATIONAL STANDARD ATMOSPHERE CONSTANTS
# =========================================================

T0 = 288.15          # Sea-level temperature (K)
P0 = 101325.0        # Sea-level pressure (Pa)
R = 287.05287        # Specific gas constant for dry air (J/kg/K)
G0 = 9.80665         # Standard gravity (m/s²)
L = 0.0065           # Temperature lapse rate (K/m)

# ISA tropopause
T11 = T0 - L * 11000


# =========================================================
# ATMOSPHERIC CALCULATION FUNCTION
# =========================================================

def calculate_atmosphere(altitude):

    """
    Calculates ISA temperature, pressure and density.

    Valid range:
    0 to 20,000 metres.

    0-11,000 m: Troposphere
    11,000-20,000 m: Isothermal lower stratosphere
    """

    if altitude < 0 or altitude > 20000:
        raise ValueError("Altitude must be between 0 and 20,000 m.")

    # -----------------------------------------------------
    # TROPOSPHERE: 0 TO 11,000 METRES
    # -----------------------------------------------------

    if altitude <= 11000:

        temperature = T0 - L * altitude

        pressure = P0 * (
            temperature / T0
        ) ** (G0 / (R * L))

    # -----------------------------------------------------
    # LOWER STRATOSPHERE: 11,000 TO 20,000 METRES
    # -----------------------------------------------------

    else:

        temperature = T11

        pressure_11 = P0 * (
            T11 / T0
        ) ** (G0 / (R * L))

        pressure = pressure_11 * np.exp(
            -G0 * (altitude - 11000) / (R * T11)
        )

    # -----------------------------------------------------
    # IDEAL GAS LAW
    # -----------------------------------------------------

    density = pressure / (R * temperature)

    # Speed of sound
    speed_of_sound = np.sqrt(1.4 * R * temperature)

    # Return atmospheric properties
    return temperature, pressure, density, speed_of_sound


# =========================================================
# PLOTLY CHART THEME
# =========================================================

def style_chart(fig, height=420):

    fig.update_layout(
        height=height,
        paper_bgcolor="#0b1729",
        plot_bgcolor="#0b1729",
        font=dict(
            family="Inter",
            color="#cbd5e1",
            size=12
        ),
        title_font=dict(
            family="Orbitron",
            size=16,
            color="#e2e8f0"
        ),
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=30
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="#cbd5e1")
        ),
        xaxis=dict(
            gridcolor="#20344d",
            zerolinecolor="#20344d"
        ),
        yaxis=dict(
            gridcolor="#20344d",
            zerolinecolor="#20344d"
        ),
        hoverlabel=dict(
            bgcolor="#13243a",
            font_color="#ffffff"
        )
    )

    return fig


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div style="text-align:center; padding:15px 0;">
        <div style="font-size:3rem;">✈️</div>
        <div style="font-family:Orbitron; font-size:1.2rem;
                    color:#38bdf8; font-weight:700;">
            AERODENSITY
        </div>
        <div style="color:#64748b; font-size:0.75rem;">
            ATMOSPHERIC SIMULATION
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("### ⚙️ Simulation Controls")

    altitude = st.slider(
        "Aircraft Altitude",
        min_value=0,
        max_value=20000,
        value=5000,
        step=100,
        format="%d m"
    )

    custom_altitude = st.number_input(
        "Enter precise altitude (m)",
        min_value=0,
        max_value=20000,
        value=altitude,
        step=100
    )

    altitude = float(custom_altitude)

    st.markdown("### 🌍 Atmospheric Model")

    st.selectbox(
        "Standard atmosphere",
        ["ISA - International Standard Atmosphere"],
        disabled=True
    )

    st.info(
        "This model assumes standard atmospheric "
        "conditions and dry air."
    )

    st.divider()

    st.markdown("""
    <div style="color:#64748b; font-size:0.75rem;">
        MODEL RANGE<br>
        0 – 20,000 metres<br><br>
        MODEL VERSION<br>
        ISA Troposphere + Lower Stratosphere
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# MAIN HEADER
# =========================================================

st.markdown("""
<div style="display:flex; align-items:center; gap:15px;">
    <div style="font-size:2.5rem;">🛰️</div>
    <div>
        <div class="hero-title">AEROSPACE ANALYTICS</div>
        <div class="hero-subtitle">
            Aircraft Atmospheric Density & Performance Simulator
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<span class="status-pill">● SIMULATION ACTIVE</span>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# CALCULATE SELECTED ALTITUDE
# =========================================================

temperature, pressure, density, speed_of_sound = (
    calculate_atmosphere(altitude)
)

temperature_celsius = temperature - 273.15
pressure_kpa = pressure / 1000
pressure_hpa = pressure / 100


# =========================================================
# KPI CARDS
# =========================================================

st.markdown(
    '<div class="section-title">LIVE ATMOSPHERIC CONDITIONS</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "✈️ Aircraft Altitude",
        f"{altitude:,.0f} m"
    )

with col2:
    st.metric(
        "🌡️ Temperature",
        f"{temperature_celsius:.2f} °C"
    )

with col3:
    st.metric(
        "🌬️ Air Density",
        f"{density:.4f} kg/m³"
    )

with col4:
    st.metric(
        "📡 Pressure",
        f"{pressure_kpa:.2f} kPa"
    )

st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# AIRCRAFT ALTITUDE INDICATOR
# =========================================================

sea_level_density = calculate_atmosphere(0)[2]

density_ratio = density / sea_level_density

st.markdown(
    '<div class="section-title">AIR DENSITY RATIO</div>',
    unsafe_allow_html=True
)

gauge_col1, gauge_col2 = st.columns([2, 1])

with gauge_col1:

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=density_ratio * 100,
            number={
                "suffix": "%",
                "font": {
                    "size": 32,
                    "color": "#38bdf8"
                }
            },
            title={
                "text": "Density Relative to Sea Level",
                "font": {
                    "size": 15,
                    "color": "#cbd5e1"
                }
            },
            gauge={
                "axis": {
                    "range": [0, 110],
                    "tickcolor": "#94a3b8"
                },
                "bar": {
                    "color": "#38bdf8",
                    "thickness": 0.25
                },
                "bgcolor": "#13243a",
                "bordercolor": "#263e5c",
                "steps": [
                    {
                        "range": [0, 40],
                        "color": "#162b42"
                    },
                    {
                        "range": [40, 70],
                        "color": "#183652"
                    },
                    {
                        "range": [70, 100],
                        "color": "#164e63"
                    }
                ],
                "threshold": {
                    "line": {
                        "color": "#f97316",
                        "width": 4
                    },
                    "thickness": 0.8,
                    "value": 100
                }
            }
        )
    )

    style_chart(gauge, 280)

    st.plotly_chart(
        gauge,
        use_container_width=True,
        config={"displayModeBar": False}
    )

with gauge_col2:

    st.markdown("""
    <div class="info-card">
        <div class="info-label">STANDARD DENSITY</div>
        <div class="info-value">1.225 kg/m³</div>
        <br>
        <div class="info-label">CURRENT DENSITY</div>
        <div class="info-value">
            """ + f"{density:.4f} kg/m³" + """</div>
        <br>
        <div class="info-label">DENSITY REDUCTION</div>
        <div class="info-value">
            """ + f"{(1-density_ratio)*100:.1f}%" + """</div>
    </div>
    """, unsafe_allow_html=True)


st.divider()


# =========================================================
# GENERATE ATMOSPHERIC PROFILE
# =========================================================

altitudes = np.linspace(0, 20000, 300)

profile = [
    calculate_atmosphere(h)
    for h in altitudes
]

temperatures = np.array([p[0] - 273.15 for p in profile])
pressures = np.array([p[1] / 1000 for p in profile])
densities = np.array([p[2] for p in profile])
speeds = np.array([p[3] for p in profile])


# =========================================================
# GRAPH 1: AIR DENSITY VS ALTITUDE
# =========================================================

st.markdown(
    '<div class="section-title">01 — AIR DENSITY PROFILE</div>',
    unsafe_allow_html=True
)

density_fig = go.Figure()

density_fig.add_trace(
    go.Scatter(
        x=densities,
        y=altitudes,
        mode="lines",
        name="Air Density",
        line=dict(
            color="#38bdf8",
            width=3
        ),
        fill="tozerox",
        fillcolor="rgba(56,189,248,0.08)",
        hovertemplate=(
            "Density: %{x:.4f} kg/m³"
            "<br>Altitude: %{y:,.0f} m"
            "<extra></extra>"
        )
    )
)

density_fig.add_trace(
    go.Scatter(
        x=[density],
        y=[altitude],
        mode="markers",
        name="Selected Aircraft",
        marker=dict(
            color="#fb7185",
            size=13,
            symbol="diamond",
            line=dict(
                color="#ffffff",
                width=1
            )
        ),
        hovertemplate=(
            "Selected Altitude"
            "<br>Density: %{x:.4f} kg/m³"
            "<br>Altitude: %{y:,.0f} m"
            "<extra></extra>"
        )
    )
)

density_fig.update_layout(
    title="Atmospheric Density vs Altitude",
    xaxis_title="Air Density (kg/m³)",
    yaxis_title="Altitude (m)",
    hovermode="closest"
)

density_fig.update_yaxes(
    range=[0, 20000]
)

style_chart(density_fig)

st.plotly_chart(
    density_fig,
    use_container_width=True
)


# =========================================================
# GRAPH 2: TEMPERATURE VS ALTITUDE
# =========================================================

st.markdown(
    '<div class="section-title">02 — TEMPERATURE PROFILE</div>',
    unsafe_allow_html=True
)

temp_fig = go.Figure()

temp_fig.add_trace(
    go.Scatter(
        x=temperatures,
        y=altitudes,
        mode="lines",
        name="Temperature",
        line=dict(
            color="#fbbf24",
            width=3
        ),
        hovertemplate=(
            "Temperature: %{x:.2f} °C"
            "<br>Altitude: %{y:,.0f} m"
            "<extra></extra>"
        )
    )
)

temp_fig.add_trace(
    go.Scatter(
        x=[temperature_celsius],
        y=[altitude],
        mode="markers",
        name="Selected Aircraft",
        marker=dict(
            color="#fb7185",
            size=12,
            symbol="diamond"
        )
    )
)

temp_fig.update_layout(
    title="Temperature Variation with Altitude",
    xaxis_title="Temperature (°C)",
    yaxis_title="Altitude (m)"
)

style_chart(temp_fig)

st.plotly_chart(
    temp_fig,
    use_container_width=True
)


# =========================================================
# GRAPH 3: ATMOSPHERIC PRESSURE VS ALTITUDE
# =========================================================

st.markdown(
    '<div class="section-title">03 — PRESSURE PROFILE</div>',
    unsafe_allow_html=True
)

pressure_fig = go.Figure()

pressure_fig.add_trace(
    go.Scatter(
        x=pressures,
        y=altitudes,
        mode="lines",
        name="Atmospheric Pressure",
        line=dict(
            color="#a78bfa",
            width=3
        ),
        fill="tozerox",
        fillcolor="rgba(167,139,250,0.08)",
        hovertemplate=(
            "Pressure: %{x:.3f} kPa"
            "<br>Altitude: %{y:,.0f} m"
            "<extra></extra>"
        )
    )
)

pressure_fig.add_trace(
    go.Scatter(
        x=[pressure_kpa],
        y=[altitude],
        mode="markers",
        name="Selected Aircraft",
        marker=dict(
            color="#fb7185",
            size=12,
            symbol="diamond"
        )
    )
)

pressure_fig.update_layout(
    title="Atmospheric Pressure vs Altitude",
    xaxis_title="Pressure (kPa)",
    yaxis_title="Altitude (m)"
)

style_chart(pressure_fig)

st.plotly_chart(
    pressure_fig,
    use_container_width=True
)


# =========================================================
# GRAPH 4: ATMOSPHERIC PROPERTY COMPARISON
# =========================================================

st.markdown(
    '<div class="section-title">04 — ATMOSPHERIC OVERVIEW</div>',
    unsafe_allow_html=True
)

overview_fig = go.Figure()

overview_fig.add_trace(
    go.Scatter(
        x=altitudes,
        y=densities,
        mode="lines",
        name="Density",
        line=dict(
            color="#38bdf8",
            width=3
        )
    )
)

overview_fig.add_trace(
    go.Scatter(
        x=altitudes,
        y=pressures,
        mode="lines",
        name="Pressure",
        line=dict(
            color="#a78bfa",
            width=3,
            dash="dash"
        ),
        yaxis="y2"
    )
)

overview_fig.update_layout(
    title="Density and Pressure Comparison",
    xaxis_title="Altitude (m)",
    yaxis=dict(
        title="Density (kg/m³)",
        gridcolor="#20344d"
    ),
    yaxis2=dict(
        title="Pressure (kPa)",
        overlaying="y",
        side="right",
        showgrid=False
    ),
    legend=dict(
        orientation="h",
        y=1.12
    )
)

style_chart(overview_fig)

st.plotly_chart(
    overview_fig,
    use_container_width=True
)


# =========================================================
# ATMOSPHERIC DATA TABLE
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">ATMOSPHERIC DATA EXPLORER</div>',
    unsafe_allow_html=True
)

st.write(
    "Explore the calculated atmospheric properties "
    "at different altitudes."
)

table_df = pd.DataFrame({
    "Altitude (m)": altitudes,
    "Temperature (°C)": temperatures,
    "Pressure (kPa)": pressures,
    "Density (kg/m³)": densities,
    "Speed of Sound (m/s)": speeds
})

table_df = table_df.round(4)

st.dataframe(
    table_df,
    use_container_width=True,
    hide_index=True
)

csv_data = table_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Atmospheric Data (CSV)",
    data=csv_data,
    file_name="aircraft_atmospheric_data.csv",
    mime="text/csv"
)


# =========================================================
# ATMOSPHERIC MODEL INFORMATION
# =========================================================

st.divider()

with st.expander("📘 About the Atmospheric Model"):

    st.markdown("""
    ### International Standard Atmosphere (ISA)

    The simulation uses the ISA model for dry air.

    **Troposphere (0–11,000 m)**

    Temperature decreases linearly with altitude.

    **Lower Stratosphere (11,000–20,000 m)**

    Temperature remains constant at 216.65 K.

    ### Governing Equations

    **Temperature**

    T = T₀ − L × h

    **Pressure in the troposphere**

    P = P₀ × (T / T₀) ^ (g / (R × L))

    **Pressure in the isothermal layer**

    P = P₁₁ × exp(−g × (h − 11000) / (R × T₁₁))

    **Air Density**

    ρ = P / (R × T)

    **Speed of Sound**

    a = √(γ × R × T)

    ### Constants

    - Sea-level temperature: 288.15 K
    - Sea-level pressure: 101325 Pa
    - Gas constant: 287.05287 J/(kg·K)
    - Gravity: 9.80665 m/s²
    - Temperature lapse rate: 0.0065 K/m
    - Specific heat ratio: 1.4
    """)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div style="text-align:center; padding:30px 0 10px 0;
            color:#64748b; font-size:0.8rem;">

    ✈️ AERODENSITY | Aircraft Atmospheric Simulator

    Developed using Python, Streamlit, NumPy, Pandas & Plotly

    Educational simulation based on the International Standard Atmosphere.

</div>
""", unsafe_allow_html=True)
