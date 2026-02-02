import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

st.set_page_config(page_title="Boitu's Pathogen Research Profile", layout="wide", page_icon="🦠")

# Set Seaborn style
sns.set_style("whitegrid")

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Explore:",
    ["Home", "TB", "HIV/AIDS", "Malaria"]
)

# Define DataFrames with realistic data + numeric conversion
# TB (WHO estimates: incident cases ~10M, deaths ~1.2-1.6M; spike 2020-21)
tb_stats = pd.DataFrame({
    "Year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Est_Cases": [11800000, 11700000, 11600000, 11400000, 11300000, 11100000, 10900000, 10700000, 10600000, 10400000, 10300000, 10500000, 10700000, 10800000, 10700000],
    "Est_Deaths": [1200000, 1300000, 1200000, 1300000, 1400000, 1400000, 1300000, 1300000, 1300000, 1270000, 1300000, 1600000, 1320000, 1250000, 1230000]
})
tb_stats["Est_Cases"] = pd.to_numeric(tb_stats["Est_Cases"])
tb_stats["Est_Deaths"] = pd.to_numeric(tb_stats["Est_Deaths"])

# HIV/AIDS (UNAIDS: new infections declining, deaths ~630k recent; prevalence separate)
hiv_stats = pd.DataFrame({
    "Year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Est_New_Infections": [2200000, 2100000, 2000000, 1900000, 1800000, 1900000, 1600000, 1600000, 1500000, 1500000, 1500000, 1500000, 1400000, 1400000, 1300000],
    "Est_Deaths": [1400000, 1400000, 1300000, 1200000, 1100000, 1000000, 1000000, 940000, 820000, 690000, 680000, 650000, 630000, 630000, 630000],
    "Living_with_HIV": [32000000, 32900000, 33600000, 34300000, 35000000, 36700000, 36400000, 37100000, 37800000, 38400000, 38900000, 39500000, 39900000, 40400000, 40800000]
})
hiv_stats["Est_New_Infections"] = pd.to_numeric(hiv_stats["Est_New_Infections"])
hiv_stats["Est_Deaths"] = pd.to_numeric(hiv_stats["Est_Deaths"])
hiv_stats["Living_with_HIV"] = pd.to_numeric(hiv_stats["Living_with_HIV"])

# Malaria (WHO: cases rising slowly, deaths ~600k)
malaria_stats = pd.DataFrame({
    "Year": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Est_Cases": [244506717, 237796199, 233131290, 227922326, 225053154, 229741247, 231997173, 239684173, 238083200, 239500520, 251140747, 254322591, 258841993, 272878620, 281741573],
    "Est_Deaths": [692678, 654715, 610323, 583041, 579066, 578270, 576477, 574421, 574784, 567186, 621344, 600935, 598407, 598446, 609930]
})
malaria_stats["Est_Cases"] = pd.to_numeric(malaria_stats["Est_Cases"])
malaria_stats["Est_Deaths"] = pd.to_numeric(malaria_stats["Est_Deaths"])

# Home page
if menu == "Home":
    st.title("🦠 Boitu's Top Infectious Diseases Board")
    st.markdown("""
    **Welcome! Wamukelekile! Vho tanganedzwa! O amogetswe! Welkom! Bem-Vindo! Bienvenu! Willkommen!** 
    \nMy name is Boitumelo, a disease-causing agents' researcher at Rhodes University, South Africa.  
    This app explores priority infectious diseases using Python (pandas for data, matplotlib and seaborn for visuals).  
    Focus: SA/global infectious diseases (data from OurWorldinData, World Medical Association, NICD, WHO, 2025-2026 reports).
    """)
    
    # Create two columns for images
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://media.baamboozle.com/uploads/images/445684/1647955483_57254_gif-url.gif", 
                 caption="Infectious Diseases (Baamboozle)", use_container_width=True)
    
    with col2:
        st.image("https://www.verywellhealth.com/thmb/iL0FXU2GLj4M7YpgHiavt-POs_g=/900x0/filters:no_upscale():max_bytes(150000):strip_icc()/infection-5096014-Final-eaf7a90b39fd4eb69b3a1776b721d975.gif", 
                 caption="Infection: Overview and more (verywell health)", use_container_width=True)
    
    st.markdown("""
    Infectious diseases are caused by pathogenic microorganisms ("germs") that get into your body from the outside, such as bacteria, viruses, parasites, fungi or prions(very rare type of infectious diseases). 
    The diseases can be spread, directly or indirectly. Some infectious diseases can pass from person to person. Some spread through insects or other animals. 
    You may get others by eating contaminated food or water. Or get exposed to them through contaminated surfaces.
    """)

    st.subheader("Impact of Infectious Diseases")
    st.markdown("""
    Globally, infectious diseases persist as a major threat to public health. For instance, HIV/AIDS and malaria, are deadly diseases that predominantly impact people in developing nations including African countries.
    Infectious organisms are responsible for about one-quarter of deaths globally, much of which involve children. Furthermore, the threat posed by infectious diseases has expanded due to the rapid progression of microbial resistance. 
    Preventive and control strategies for communicable diseases must be granted priority in light of this harsh reality.
    """)

    # Priority Pathogens Overview table
    overview = pd.DataFrame({
        "Infectious Disease": ["TB", "HIV/AIDS", "Malaria", "Influenza", "COVID-19"],
        "Global deaths (2024 est.)": ["1,23M", "630K (40,8M living with)", "610k", "290K - 650k", "1,8K"],
        "SA Burden (2025 est.)": ["High", "53k (7.8M living with)", "Regional threat", "Seasonal + avian risk", "Ongoing (few to no cases)"]
    })
    overview.index = overview.index + 1

    st.subheader("Priority Pathogens Overview")
    st.dataframe(overview)

    # Create bar chart data
    data = {
        "Infectious_Disease": ["TB", "HIV/AIDS", "Malaria", "Influenza", "COVID-19"],
        "Deaths_2024": [1230000, 630000, 610000, 470000, 1800]   
    }
    df = pd.DataFrame(data)

    st.subheader("Infectious Diseases Global Deaths Comparison (2024 Estimates)")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    df_sorted = df.sort_values("Deaths_2024")
    
    # Create horizontal bar plot
    colors = plt.cm.Blues_r([0.2, 0.4, 0.6, 0.8, 1.0])
    bars = ax.barh(df_sorted["Infectious_Disease"], df_sorted["Deaths_2024"], color=colors)
    
    # Format x-axis
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{x:,.0f}'))
    ax.set_xlabel("Estimated Global Deaths (2024)")
    
    # Add value labels
    for bar in bars:
        width = bar.get_width()
        ax.text(width + width*0.01, bar.get_y() + bar.get_height()/2, 
                f'{width:,.0f}', ha='left', va='center')
    
    plt.tight_layout()
    st.pyplot(fig)

# Disease pages
elif menu == "TB":
    st.title("TB (Tuberculosis)")
    st.subheader("Global Trends Table")
    st.dataframe(tb_stats)
    
    st.subheader("Trends Plot (Cases & Deaths over Years)")
    
    # Create figure with two y-axes
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Plot cases on left y-axis
    color1 = 'tab:blue'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Estimated Cases', color=color1)
    line1 = ax1.plot(tb_stats["Year"], tb_stats["Est_Cases"], color=color1, 
                     marker='o', label='Cases', linewidth=2)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{x/1e6:.1f}M'))
    
    # Create second y-axis for deaths
    ax2 = ax1.twinx()
    color2 = 'tab:red'
    ax2.set_ylabel('Estimated Deaths', color=color2)
    line2 = ax2.plot(tb_stats["Year"], tb_stats["Est_Deaths"], color=color2, 
                     marker='s', label='Deaths', linewidth=2)
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{x/1e3:.0f}K'))
    
    # Add title and grid
    plt.title('TB Trends: Cases vs Deaths Over Time', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Combine legends
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left')
    
    plt.tight_layout()
    st.pyplot(fig)

elif menu == "HIV/AIDS":
    st.title("HIV/AIDS")
    st.subheader("Global Trends Table")
    st.dataframe(hiv_stats)

    st.subheader("People Living with HIV (Prevalence)")
    
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    
    ax1.plot(hiv_stats["Year"], hiv_stats["Living_with_HIV"], 
             marker='o', linewidth=2, color='purple')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('People Living with HIV')
    ax1.set_title('HIV Prevalence Over Time', fontweight='bold')
    ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{x/1e6:.1f}M'))
    ax1.grid(True, alpha=0.3)
    ax1.fill_between(hiv_stats["Year"], hiv_stats["Living_with_HIV"], 
                     alpha=0.2, color='purple')
    
    plt.tight_layout()
    st.pyplot(fig1)

    st.subheader("New HIV Infections & AIDS-related Deaths")
    
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    
    ax2.plot(hiv_stats["Year"], hiv_stats["Est_New_Infections"], 
             marker='o', linewidth=2, label='New Infections', color='green')
    ax2.plot(hiv_stats["Year"], hiv_stats["Est_Deaths"], 
             marker='s', linewidth=2, label='Deaths', color='red')
    
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Count')
    ax2.set_title('New HIV Infections vs AIDS-related Deaths', fontweight='bold')
    ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{x/1e3:.0f}K'))
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    st.pyplot(fig2)

elif menu == "Malaria":
    st.title("Malaria")
    st.subheader("Global Trends Table")
    st.dataframe(malaria_stats)
    
    st.subheader("Trends Plot (Logarithmic Scale)")
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(malaria_stats["Year"], malaria_stats["Est_Cases"], 
            marker='o', linewidth=2, label='Cases', color='blue')
    ax.plot(malaria_stats["Year"], malaria_stats["Est_Deaths"], 
            marker='s', linewidth=2, label='Deaths', color='red')
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Count (Log Scale)')
    ax.set_title('Malaria Trends: Cases vs Deaths (Logarithmic Scale)', fontweight='bold')
    ax.set_yscale('log')
    ax.grid(True, alpha=0.3, which='both')
    ax.legend()
    
    # Format y-axis for log scale
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f'{y:,.0f}'))
    
    plt.tight_layout()
    st.pyplot(fig)

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.info("Data: OurWorldinData/NICD/WHO 2025-2026 | Built with Streamlit, pandas & matplotlib")
