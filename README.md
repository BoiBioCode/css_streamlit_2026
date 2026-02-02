# Boitu's Pathogen Research Dashboard 🦠

An interactive Streamlit web app exploring priority infectious diseases with global trends and visualizations.

Built by **Boitumelo (BoiBioCode)** — Researcher at Rhodes University, South Africa.

## What this app shows

Quick overview and time-series trends (2010–2024) for key infectious diseases:

- **TB (Tuberculosis)**
- **HIV/AIDS** (new infections, AIDS-related deaths, people living with HIV)
- **Malaria**
- **Influenza** (Only on the Home page)
- **COVID-19** (Only on the Home page)

Data sources: WHO, UNAIDS, Our World in Data, NICD, and latest global reports (2024–2026 estimates).

## Features

- Interactive sidebar navigation
- Global trends tables (pandas DataFrames)
- Simple line charts showing cases/incidence vs deaths over time
- Priority pathogens overview table
- 2024 global deaths comparison horizontal bar chart (Plotly)
- Welcome section with multilingual greeting & educational content

## 🛠️ Tech Stack

- Python 3
- Streamlit (web app framework)
- pandas (data handling & tables)
- Plotly Express (interactive bar chart)
- Matplotlib & NumPy (imported, ready for future extensions)