import streamlit as st

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px
import numpy as np

im = Image.open("./openaccess.png")

st.set_page_config(layout="wide", page_title="Kobo Dashboard", page_icon = im)

# Custom CSS to make the expander fill the page width and prevent overlapping
st.markdown(
    """
    <style>
    /* Make the main container full width */
    .main {
        max-width: 100%;
        padding-top: 0;
        padding-bottom: 0;
        margin: 0;
    }

    .css-18e3th9 {
        padding-top: 0rem !important;
    }
    
    .css-1d391kg {
        padding-top: 0rem;
    }

    .header-container {
        display: flex;
        align-items: center;
        justify-content: flex-start; /* Align image to the left */
        background: linear-gradient(to right, #018749, #E5E4E2, #E5E4E2, #E5E4E2, #E5E4E2, #E5E4E2, #E5E4E2, #E5E4E2); /* Green and grey background shades */
        padding: 10px 20px;
        height: 60px; /* Adjust height to fit the content */
        margin: 0;  /* Remove any margin */
        width: 100%;
        box-sizing: border-box;
    }
    .header-image {
        max-height: 60px; /* Smaller header image */
        margin-left: 50px; /* Space between image and title */
        width: 60px;
    }
    .streamlit-expander {
        width: 100%;
    }
    .streamlit-expander > .streamlit-expanderHeader {
        width: 100%;
    }
    .streamlit-expander > .streamlit-expanderContent {
        width: 100%;
    }
    .stApp {
        overflow-x: hidden;
    }
    .column1 {
        flex: 1 !important;
        max-width: 100%;
    }
    .column2 {
        flex: 2 !important;
        max-width: 100%;
    }
    @media (max-width: 1600px) {
        .column1 {
            flex: 1 !important;
            max-width: 100%;
        }
        .column2 {
            flex: 2 !important;
            max-width: 100%;
        }
    }
    @media (max-width: 1200px) {
        .column1, .column2 {
            flex: 100% !important;
            max-width: 100%;
        }
    }
    .fixed-table {
        width: 100%;
        height: 400px;  /* Set a fixed height */
        overflow-y: auto;
        overflow-x: hidden;
        font-size: 10px;  /* Reduced font size */
    }
    .fixed-table table {
        table-layout: fixed;
        width: 100%;
    }

    .fixed-table th {
        background-color: #018749;  /* Green background for headers */
        color: white;
        text-align: right;  /* Align text to the right */
        padding: 5px;
    }
    .fixed-table th, .fixed-table td {
        text-align: left;  /* Align text to the right */
        padding: 5px;
    }
        /* Footer styling */
    .myfooter {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #018749;
        color: white;
        text-align: center;
        padding: 0px 0;
        font-size: 8px;
        z-index: 1000;
        }
    </style>
    """,
    unsafe_allow_html=True
)

hide_default_format = """
       <style>
       #MainMenu, header, footer {visibility: hidden;}
       </style>
       """

st.markdown(hide_default_format, unsafe_allow_html=True)

# Data preparation
data_lbl = {
    'Cost element': ['Land', 'Infrastructure', 'Compliances and approvals', 'Construction',
                     'Professional and project management', 'Other development costs', 'Marketing',
                     'Finance', 'Developer overhead and management'],
    'CAHF House 55m2': ['378,575', '966,150', '57,750', '1,833,013', '64,155', '43,161', '58,102', '475,691', '77,470'],
    'Low-rise blocks 44m2': ['135,226', '139,228', '56,514', '1,711,501', '308,070', '51,345', '43,175', '469,686', '100,742'],
    'High-rise blocks 44m2': ['130,617', '140,461', '56,514', '1,866,445', '335,960', '55,993', '46,936', '543,058', '93,871']
}

df_lbl = pd.DataFrame(data_lbl)

# Data preparation for the graphs
data_num = {
    'Cost element': ['Land', 'Infrastructure', 'Compliances and approvals', 'Construction',
                     'Professional and project management', 'Other development costs', 'Marketing',
                     'Finance', 'Developer overhead and management'],
    'CAHF House 55m2': [378575, 966150, 57750, 1833013, 64155, 43161, 58102, 475691, 77470],
    'Low-rise blocks 44m2': [135226, 139228, 56514, 1711501, 308070, 51345, 43175, 469686, 100742],
    'High-rise blocks 44m2': [130617, 140461, 56514, 1866445, 335960, 55993, 46936, 543058, 93871]
}

df = pd.DataFrame(data_num)

# Interactive stacked bar chart with Housing Type on X-axis and Cost Elements on Y-axis
df_melted = df.melt(id_vars='Cost element', var_name='Housing Type', value_name='Cost')
fig1 = px.bar(df_melted, 
              x='Housing Type', 
              y='Cost', 
              color='Cost element', 
              title='Housing Development Cost Comparisons: Ksh',
              labels={'Cost': 'Kenyan Shillings', 'Housing Type': 'Housing Type'},
              color_discrete_sequence=px.colors.qualitative.D3)

fig1.update_layout(barmode='stack', 
                    margin=dict(t=50,l=0, r=0,), 
                   xaxis_title=None,  # Remove x-axis title
                   yaxis_title=dict(text ='Cost (Kenyan Shillings)', standoff=5),
                   title_x=0.1,
                   title_font=dict(size=10, family='Arial', color='black', weight='bold'),  # Reduce title font size and bolden
                   font=dict(size=10, color='black'),  # Reduce overall font size
                   xaxis=dict(tickfont=dict(size=8, color='black')), 
                   yaxis=dict(tickfont=dict(size=8, color='black')), # Reduce x-axis labels font size
                   showlegend=False)  # Hide legend

fig1.update_yaxes(title_font=dict(size=8, family='Arial Black', color='black', weight='bold'),
        # showline=True,
        #  linewidth=1,
        #  linecolor='green',
        #  mirror=True
         )  # Bolden the y-axis title
fig1.update_xaxes(tickangle=0,
        # showline=True,
        #  linewidth=1,
        #  linecolor='green',
        #  mirror=True
         )  # Make x-axis labels horizontal

# Calculate percentage cost per house type
df_percentage = df.set_index('Cost element').div(df.set_index('Cost element').sum(axis=0), axis=1) * 100
df_percentage = df_percentage.reset_index()
df_percentage_melted = df_percentage.melt(id_vars='Cost element', var_name='Housing Type', value_name='Percentage')

# Interactive stacked bar chart for percentage cost
fig2 = px.bar(df_percentage_melted, 
              x='Housing Type', 
              y='Percentage', 
              color='Cost element', 
              title='Housing Development Cost Comparisons: Percentage',
              labels={'Percentage': 'Percentage (%)', 'Housing Type': 'Housing Type'},
              color_discrete_sequence=px.colors.qualitative.D3)

fig2.update_layout(barmode='stack', 
                    margin=dict(t=50, l=0, r=0,), 
                   xaxis_title=None,  # Remove x-axis title
                   # yaxis_title='Percentage (%)',
                   yaxis_title=dict(text="Percentage (%)", standoff=5),  # Reduce standoff to bring the title closer to the axis
                   title_x=0.05,
                   title_font=dict(size=10, family='Arial', color='black'),  # Reduce title font size and bolden
                   font=dict(size=8, color='black'),  # Reduce overall font size
                   xaxis=dict(tickfont=dict(size=8, color='black')), 
                   yaxis=dict(tickfont=dict(size=8, color='black')), # Reduce x-axis labels font size
                   legend=dict(
                       font=dict(size=8),  # Reduce legend font size
                       title=None,  # Remove the legend title
                       x=1.01, y=1.01, 
                       bgcolor='rgba(255,255,255,0)', 
                       bordercolor='rgba(0,0,0,0)'))

fig2.update_yaxes(title_font=dict(size=8, family='Arial Black', color='black', weight='bold'),
        # showline=True,
        #  linewidth=1,
        #  linecolor='green',
        #  mirror=True
         )  # Bolden the y-axis title
 # Bolden the y-axis title
fig2.update_xaxes(tickangle=0,
        # showline=True,
        #  linewidth=1,
        #  linecolor='green',
        #  mirror=True
         )  # Make x-axis labels horizontal

# Displaying in Streamlit
# st.image('./openaccess.png')

# Load the header image
header_image = Image.open("./openaccess.png")

# Add the header image
# Display the header with the image and background colors
# header_image = "./openaccess.png"  # Use the correct path to your image
# Display the header with the image and background colors
st.markdown(f"""
<div class="header-container">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4XHiiYPE05yXnEX6enp_ETSuVF0-N2u-MVSeypb8sIlAAX5O1", class="header-image"/>
</div>
""", unsafe_allow_html=True)

st.subheader("Housing Development Cost Comparison")

# Add Lorem Ipsum text
st.markdown("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada. Sed congue, metus non scelerisque dignissim, purus nisi pulvinar metus, eget ultricies nisl erat ut mi. Fusce elementum, nulla vel feugiat lacinia, elit purus fermentum lacus, et imperdiet urna metus et ligula. Ut tincidunt, erat eu tincidunt gravida, felis libero tempus lorem, ac sodales mi justo a turpis. Curabitur suscipit, sem quis elementum faucibus, erat orci posuere metus, et ultricies magna risus a purus. Nullam vestibulum ligula et sapien consequat, quis interdum quam cursus.
""")

with st.expander("HCCB 2022 gragh comparison: CAHF vs Low-rise and High-rise projects", expanded=True):
    # Create a container for the columns
    with st.container():
        # Create two columns with custom widths
        col1, col2, col3 = st.columns([1, 1, 1.6], gap="medium")

        with col1:
            st.markdown("  ")
            # st.dataframe(df)
            st.dataframe(df,
                column_config = {
                "CAHF House 55m2": st.column_config.Column(
                        "CAHF 🏡",
                        help="*CAHF House 55m2* :house_with_garden:",
                        width="small"),
                "Low-rise blocks 44m2": st.column_config.Column(
                        "Low-rise🏗️",
                        help="*Low-rise blocks 44m2* :building_construction:",
                        width="small"),
                "High-rise blocks 44m2": st.column_config.Column(
                        "High-rise🏗️",
                        help="*High-rise blocks 44m2* :building_construction:",
                        width="small"),
                "Cost element": st.column_config.Column(
                        "Cost 💰",
                        help="*Cost element* :moneybag:",
                        width="small"),
                },
                height=380,
                hide_index=True,
            )
            # st.markdown(f'<div class="fixed-table">{df_lbl.to_html(index=False)}</div>', unsafe_allow_html=True)

        with col2:
            st.plotly_chart(fig1, use_container_width=True)
          
        with col3:
            st.plotly_chart(fig2, use_container_width=True)


# Load the existing data for each section
substructures_data = {
    "DESCRIPTION": ["Excavations", "Hardcore & Dust", "DPM", "Surface treatment", "Concrete works", "Reinforcement bars", "BRC", "Formwork", "Waterproofing", "Floor Hardener & Powerfloating", "DPC", "Total"],
    "BQ Price": [389503.69, 26500.00, 10600.00, 7950.00, 16473303.99, 12521909.63, 26000.00, 414943.42, 53048.00, 682773.35, 3090.00, 30608522.25],
    "Materials Cost": [0, 27200.00, 3300.00, 5600.00, 10837000.00, 11156290.00, 25000.00, 267700.00, 40000.00, 387000.00, 1236.00, 22750326.00],
    "Labor, transport and Profits Cost": [389503.69, -700.00, 7300.00, 2350.00, 5636303.99, 1365019.63, 1500.00, 146243.42, 13048.00, 295773.35, 1854.00, 7858196.25],
    "Remarks": ["", "", "", "", "", "", "", "", "", "", "", ""]
}

superstructures_data = {
    "DESCRIPTION": ["Concrete works", "Reinforcement bars", "Formwork", "Total"],
    "BQ Price": [28109707.73, 39546297.23, 13622229.38, 81277234.33],
    "Materials Cost": [18466700.00, 35064852.56, 8858200.00, 62389752.56],
    "Labor, transport and Profits Cost": [9642007.73, 4481444.67, 4764029.38, 18887451.77],
    "Remarks": ["", "", "", ""]
}

roofing_data = {
    "DESCRIPTION": ["Roof Covering", "Roof Structure", "Rainwater Goods", "Total"],
    "BQ Price": [1200000.00, 2500000.00, 150000.00, 3850000.00],
    "Materials Cost": [800000.00, 1800000.00, 100000.00, 2700000.00],
    "Labor, transport and Profits Cost": [400000.00, 700000.00, 50000.00, 1150000.00],
    "Remarks": ["", "", "", ""]
}

walling_data = {
    "DESCRIPTION": ["External Walls", "Internal Walls", "Total"],
    "BQ Price": [3000000.00, 1500000.00, 4500000.00],
    "Materials Cost": [2000000.00, 1000000.00, 3000000.00],
    "Labor, transport and Profits Cost": [1000000.00, 500000.00, 1500000.00],
    "Remarks": ["", "", ""]
}

summary_data = {
    "DESCRIPTION": ["Substructures", "Superstructures", "Roofing", "Walling", "Total"],
    "BQ Price": [30608522.25, 81277234.33, 3850000.00, 4500000.00, 124777756.58],
    "Materials Cost": [22750326.00, 62389752.56, 2700000.00, 3000000.00, 90840078.56],
    "Labor, transport and Profits Cost": [7858196.25, 18887451.77, 1150000.00, 1500000.00, 29395648.02],
    "Remarks": ["", "", "", "", ""]
}

# Create DataFrames for each section
substructures_df = pd.DataFrame(substructures_data)
superstructures_df = pd.DataFrame(superstructures_data)
roofing_df = pd.DataFrame(roofing_data)
walling_df = pd.DataFrame(walling_data)
summary_df = pd.DataFrame(summary_data)

# Define indices for each section
substructures_index = list("ABCDEFGHIJKL") + [""]  # 12 rows
superstructures_index = list("MNOP") + [""]        # 4 rows
roofing_index = list("QRST")                       # 4 rows
walling_index = list("UV") + [""]                  # 3 rows
summary_index = list("WXYZ") + [""]                # 5 rows

# Assign the indices to each DataFrame
substructures_df.index = substructures_index[:len(substructures_df)]
superstructures_df.index = superstructures_index[:len(superstructures_df)]
roofing_df.index = roofing_index[:len(roofing_df)]
walling_df.index = walling_index[:len(walling_df)]
summary_df.index = summary_index[:len(summary_df)]


# Define data for each section separately
data_substructures = {
    "DESCRIPTION": ["Excavations", "Hardcore", "Quarry Dust", "Surface treatment", "Concrete works", "Reinforcement bars", "BRC", "Formwork", "Foundation Walling", "Total"],
    "BQ Price": [2067750.00, 35000.00, 20000.00, "", 7233850.00, 3922320.00, 48000.00, 439100.00, 304000.00, 14070020.00],
    "Materials Cost": [0, 31500.00, 6400.00, "", 4262400.00, 3236520.00, 25000.00, 283345.00, 219800.00, 8064965.00],
    "Labor, Transport and Profits Cost": [2067750.00, 3500.00, 13600.00, "-", 2971450.00, 685800.00, 23000.00, 155755.00, 84200.00, 6005055.00],
    "Remarks": ["", "", "", "", "", "", "", "", "", ""]
}

data_superstructures = {
    "DESCRIPTION": ["Concrete works", "Reinforcement bars", "Formwork", "Waterproofing", "Total"],
    "BQ Price": [50915823.00, 71415600.00, 16253850.00, 160600.00, 138745873.00],
    "Materials Cost": [30071800.00, 57790360.00, 10691490.00, 96000.00, 98649650.00],
    "Labor, Transport and Profits Cost": [20844023.00, 13625240.00, 5562360.00, 64600.00, 40096223.00],
    "Remarks": ["", "", "", "", ""]
}

data_roofing = {
    "DESCRIPTION": ["Concrete works", "Reinforcement bars", "Formwork", "Copings", "Masonry walling", "APP waterproofing", "Saflock roofing sheets", "Roof insulation", "Roof steel works", "Polycarbonate", "Finishings", "Total"],
    "BQ Price": [678222.00, 142920.00, 191550.00, 380250.00, 859800.00, 2552200.00, 2043400.00, 526800.00, 3160450.00, 684000.00, 4335470.00, 15555062.00],
    "Materials Cost": [395600.00, 121440.00, 124510.00, 325500.00, 593488.00, 1229000.00, 1311200.00, 360000.00, 2330532.00, 210000.00, 2838778.00, 9840048.00],
    "Labor, Transport and Profits Cost": [282622.00, 21480.00, 67040.00, 54750.00, 266312.00, 1323200.00, 732200.00, 166800.00, 829918.00, 474000.00, 1496692.00, 5715014.00],
    "Remarks": ["", "", "", "", "", "", "", "", "", "", "", ""]
}

data_staircases = {
    "DESCRIPTION": ["Steel staircase complete", "Total"],
    "BQ Price": [8942868.00, 8942868.00],
    "Materials Cost": [6159275.00, 6159275.00],
    "Labor, Transport and Profits Cost": [2783593.00, 2783593.00],
    "Remarks": ["", ""]
}

data_external_walls = {
    "DESCRIPTION": ["Copings", "Clay brick grille", "Masonry walls", "Balustrading", "Finishes", "Fencing", "Total"],
    "BQ Price": [1137750.00, 452200.00, 17423500.00, 1647000.00, 12881970.00, 799200.00, 34341620.00],
    "Materials Cost": [973350.00, 266800.00, 11697020.00, 1235250.00, 5341760.00, 409800.00, 19923980.00],
    "Labor, Transport and Profits Cost": [164400.00, 185400.00, 5726480.00, 411750.00, 7540210.00, 389400.00, 14417640.00],
    "Remarks": ["", "", "", "", "", "", ""]
}

data_windows_external_doors = {
    "DESCRIPTION": ["Windows & Doors", "Total"],
    "BQ Price": [63586400.00, 63586400.00],
    "Materials Cost": [52893471.00, 52893471.00],
    "Labor, Transport and Profits Cost": [10692929.00, 10692929.00],
    "Remarks": ["", ""]
}

data_internal_walling = {
    "DESCRIPTION": ["Stone works", "Total"],
    "BQ Price": [15975500.00, 15975500.00],
    "Materials Cost": [10621126.00, 10621126.00],
    "Labor, Transport and Profits Cost": [5354374.00, 5354374.00],
    "Remarks": ["", ""]
}

data_internal_doors = {
    "DESCRIPTION": ["Doors", "Total"],
    "BQ Price": [27792470.00, 27792470.00],
    "Materials Cost": [14784448.00, 14784448.00],
    "Labor, Transport and Profits Cost": [13008022.00, 13008022.00],
    "Remarks": ["", ""]
}

data_internal_finishes = {
    "DESCRIPTION": ["Internal wall finishes", "Floor finishes", "Ceiling finishes", "Fittings", "Total"],
    "BQ Price": [30715380.00, 30320670.00, 14509800.00, 46350414.00, 121896264.00],
    "Materials Cost": [11969412.00, 20595730.00, 3978515.00, 34762810.50, 71306467.50],
    "Labor, Transport and Profits Cost": [18745968.00, 9724940.00, 10531285.00, 11587603.50, 50589796.50],
    "Remarks": ["", "", "", "", ""]
}

data_summary = {
    "DESCRIPTION": ["Substructures", "Superstructure", "Roofing", "Staircases", "External Walls", "Windows and External Doors", "Internal Walling", "Internal Doors", "Internal Finishes", "Total"],
    "BQ Price": [14070020.00, 138745873.00, 15555062.00, 8942868.00, 34341620.00, 63586400.00, 15975500.00, 27792470.00, 121896264.00, 440906077.00],
    "Materials Cost": [8064965.00, 98649650.00, 9840048.00, 6159275.00, 19923980.00, 52893471.00, 10621126.00, 14784448.00, 71306467.50, 292243430.50],
    "Labor, Transport and Profits Cost": [6005055.00, 40096223.00, 5715014.00, 2783593.00, 14417640.00, 10692929.00, 5354374.00, 13008022.00, 50589796.50, 148662646.50],
    "Remarks": ["", "", "", "", "", "", "", "", "", ""]
}

# Create a DataFrame for each section
df_substructures = pd.DataFrame(data_substructures)
df_superstructures = pd.DataFrame(data_superstructures)
df_roofing = pd.DataFrame(data_roofing)
df_staircases = pd.DataFrame(data_staircases)
df_external_walls = pd.DataFrame(data_external_walls)
df_windows_external_doors = pd.DataFrame(data_windows_external_doors)
df_internal_walling = pd.DataFrame(data_internal_walling)
df_internal_doors = pd.DataFrame(data_internal_doors)
df_internal_finishes = pd.DataFrame(data_internal_finishes)
df_summary = pd.DataFrame(data_summary)

# Start the Streamlit app
st.write("🚧 **Construction Cost Breakdown**")

# Create HTML table
html_BQ1 = """
<h6 style="color:green">Sample BQ 1</h6>
<p style="font-size:12px"><b>Project Name: </b>Proposed  Residential Development (1A) , Riruta, Off Naivasha Road </p>
<p style="font-size:12px"><b>Cost Analysis Level: </b>Rate Anaylsis <i>(Cost of Materials, Labor, transport and Profits) </i></p>
<p style="font-size:12px"><b>BQ Element/Section:  </b>Section 03 - Structure </p>
<hr>
<div style="max-width: 100%; overflow-x: auto;">
"""
# Create HTML table
html_BQ2 = """
<h6 style="color:green">Sample BQ 2</h6>
<p style="font-size:12px"><b>Project Name: </b>Proposed  Elmer Haco Apartments for Elmer One Development Limited </p>
<p style="font-size:12px"><b>Cost Analysis Level: </b>Rate Anaylsis <i>(Cost of Materials, Labor, transport and Profits) </i></p>
<p style="font-size:12px"><b>BQ Element/Section:  </b>Section 03 - Structure </p>
<hr>
<div style="max-width: 100%; overflow-x: auto;">
"""

# Sample data for Summary section (you should replace this with your actual data)
data_summary1 = {
    "DESCRIPTION": ["Substructures", "Superstructure", "Roofing", "Walling"],
    "BQ Price": [30608522.25, 81277234.33, 4639048.33, 19886600.85]
}

data_summary2 = {
    "DESCRIPTION": ["Substructures", "Superstructure", "Roofing", "Staircases", "External Walls", "Windows and External Doors", "Internal Walling", "Internal Doors", "Internal Finishes"],
    "BQ Price": [14070020.00, 138745873.00, 15555062.00, 8942868.00, 34341620.00, 63586400.00, 15975500.00, 27792470.00, 121896264.00]
}

# Create DataFrame for each summary
df_summary1 = pd.DataFrame(data_summary1)
df_summary2 = pd.DataFrame(data_summary2)

# Create pie charts for each summary
fig1 = px.pie(df_summary1, names='DESCRIPTION', values='BQ Price', title='BQ1 Construction Cost Distribution')
fig1.update_traces(hole=0)
fig1.update_layout(
    width=500,  # Set width to 500 pixels
    height=400,  # Set height to 500 pixels
    margin=dict(l=20, r=20, t=20, b=20),
)

fig2 = px.pie(df_summary2, names='DESCRIPTION', values='BQ Price', title='BQ2 Construction Cost Distribution')
fig2.update_traces(hole=0)
fig2.update_layout(
    width=500,  # Set width to 500 pixels
    height=400, # Set height to 500 pixels
    margin=dict(l=20, r=20, t=20, b=20),
)

with st.container():
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown(html_BQ1, unsafe_allow_html=True)
        # Create collapsible sections for each part
        st.plotly_chart(fig1)

        with st.expander("SUBSTRUCTURES"):
            st.dataframe(substructures_df)

        with st.expander("SUPERSTRUCTURES"):
            st.dataframe(superstructures_df)

        with st.expander("ROOFING"):
            st.dataframe(roofing_df)

        with st.expander("WALLING"):
            st.dataframe(walling_df)

        with st.expander("SUMMARY"):
            st.dataframe(summary_df)

    with col2:
        st.markdown(html_BQ2, unsafe_allow_html=True)

        st.plotly_chart(fig2)  
              
        with st.expander("SUBSTRUCTURES"):
            st.dataframe(df_substructures)

        with st.expander("SUPERSTRUCTURES"):
            st.dataframe(df_superstructures)

        with st.expander("ROOFING"):
            st.dataframe(df_roofing)

        with st.expander("STAIRCASES"):
            st.dataframe(df_staircases)

        with st.expander("EXTERNAL WALLS"):
            st.dataframe(df_external_walls)

        with st.expander("WINDOWS AND EXTERNAL DOORS"):
            st.dataframe(df_windows_external_doors)

        with st.expander("INTERNAL WALLING"):
            st.dataframe(df_internal_walling)

        with st.expander("INTERNAL DOORS"):
            st.dataframe(df_internal_doors)

        with st.expander("INTERNAL FINISHES"):
            st.dataframe(df_internal_finishes)

        with st.expander("SUMMARY"):
            st.dataframe(df_summary)

# Create a DataFrame for the table
data = {
    "BQ Item": ["Substructures", "Superstructure", "Roofing", "Staircases", "External Walls", 
                "Windows and External Doors", "Internal Walling", "Internal Doors", "Internal Finishes"],
    "BQ1 Cost": [14070020.00, 138745873.00, 15555062.00, 8942868.00, 34341620.00, 
            63586400.00, 15975500.00, 27792470.00, 121896264.00],
    "BQ2 Cost": [30608522.00, 81277234.00, 4639048.00, 0.00, 0.00, 
            0.00, 0.00, 0.00, 0.00],
    "Your Input": [0.0] * 9  # Initialize "Your Input" with zeros
}

df = pd.DataFrame(data)

with st.expander("**Benchmark Your Cost Estimates**", expanded=True):
    # Create a container for the columns
    with st.container():
        # Create two columns with custom widths
        col1, col2 = st.columns([1.35, 2], gap="small")
            # Editable DataFrame directly on the app

        with col1:
            st.write(":red[:red-background[*Input your cost per BQ item*]]")
            df_editable = st.data_editor(df, num_rows="fixed", use_container_width=True, 
                disabled=("BQ Item", "BQ1 Cost", "BQ2 Cost"), hide_index=True, 
                column_config = {
                "BQ Item": st.column_config.Column(
                        width="small")},)

            # Calculate the total for each column
            total_input = df_editable["Your Input"].sum()
            total_row = pd.DataFrame({
                "BQ Item": ["Total"],
                "BQ1 Cost": [df_editable["BQ1 Cost"].sum()],
                "BQ2 Cost": [df_editable["BQ2 Cost"].sum()],
                "Your Input": [total_input]
            })

            # Append the total row to the editable DataFrame
            df_editable_with_total = pd.concat([df_editable, total_row], ignore_index=True)

            # st.header("Percentage Table")
            # Display the updated Table 1 with totals
            # st.write(df_editable_with_total, hide_index=True)

            # Calculate percentages based on the totals
            # df_percent = df_editable_with_total.copy()
            df_editable_with_total["BQ1 Cost (%)"] = ((df_editable_with_total["BQ1 Cost"] / df_editable_with_total.loc[df_editable_with_total['BQ Item'] == 'Total', 'BQ1 Cost'].values[0]) * 100).replace([np.inf, -np.inf, np.nan], 0).round(0).astype(int).astype(str) + '%'
            df_editable_with_total["BQ2 Cost (%)"] = ((df_editable_with_total["BQ2 Cost"] / df_editable_with_total.loc[df_editable_with_total['BQ Item'] == 'Total', 'BQ2 Cost'].values[0]) * 100).replace([np.inf, -np.inf, np.nan], 0).round(0).astype(int).astype(str) + '%'
            df_editable_with_total["Percentage"] = ((df_editable_with_total["Your Input"] / df_editable_with_total.loc[df_editable_with_total['BQ Item'] == 'Total', 'Your Input'].values[0]) * 100).replace([np.inf, -np.inf, np.nan], 0).round(0).astype(int).astype(str) + '%'

            # Rename columns for clarity
            # df_percent.rename(columns={"BQ1 Cost": "BQ1 Cost (%)", "BQ2 Cost": "BQ2 Cost (%)"}, inplace=True)

            # Drop the 'Your Input' column for the percentage view
            # df_percent = df_percent.drop(columns=["Your Input"])

        with col2:
            # Display the percentages as a separate view
            st.write(" :green[:green-background[*Compare your cost distribution with the Benchmarks*]]")
            df_percent = df_editable_with_total[["BQ Item","BQ1 Cost","BQ1 Cost (%)","BQ2 Cost", "BQ2 Cost (%)", "Your Input","Percentage"]]
            st.dataframe(df_percent, 
                column_config = {
                "BQ Item": st.column_config.Column(width="small")},
                hide_index=True, use_container_width=True)
