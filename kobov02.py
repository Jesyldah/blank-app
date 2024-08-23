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
                    margin=dict(t=70), 
                   xaxis_title=None,  # Remove x-axis title
                   yaxis_title='Cost (Kenyan Shillings)',
                   title_font=dict(size=10, family='Arial', color='black', weight='bold'),  # Reduce title font size and bolden
                   font=dict(size=10, color='black'),  # Reduce overall font size
                   xaxis=dict(tickfont=dict(size=8, weight='bold')),  # Reduce x-axis labels font size
                   showlegend=False)  # Hide legend

fig1.update_yaxes(title_font=dict(size=8, family='Arial Black', color='black', weight='bold'))  # Bolden the y-axis title
fig1.update_xaxes(tickangle=0)  # Make x-axis labels horizontal

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
                    margin=dict(t=70), 
                   xaxis_title=None,  # Remove x-axis title
                   yaxis_title='Percentage (%)',
                   title_font=dict(size=10, family='Arial', color='black', weight='bold'),  # Reduce title font size and bolden
                   font=dict(size=10, color='black'),  # Reduce overall font size
                   xaxis=dict(tickfont=dict(size=8)),  # Reduce x-axis labels font size
                   legend=dict(
                       font=dict(size=8),  # Reduce legend font size
                       title=None,  # Remove the legend title
                       x=0.99, y=0.97, 
                       bgcolor='rgba(255,255,255,0)', 
                       bordercolor='rgba(0,0,0,0)'))

fig2.update_yaxes(title_font=dict(size=8, family='Arial Black', color='black', weight='bold'))  # Bolden the y-axis title
fig2.update_xaxes(tickangle=0)  # Make x-axis labels horizontal

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
        col1, col2, col3 = st.columns([1, 1.1, 1.7], gap="medium")

        with col1:
            st.markdown("  ")
            # st.dataframe(df)
            st.dataframe(df,
                column_config = {
                "CAHF House 55m2": st.column_config.Column(
                        "CAHF",
                        help="*CAHF House 55m2*",
                        width="small"),
                "Low-rise blocks 44m2": st.column_config.Column(
                        "Low-rise",
                        help="*Low-rise blocks 44m2*",
                        width="small"),
                "High-rise blocks 44m2": st.column_config.Column(
                        "High-rise ",
                        help="*High-rise blocks 44m2*",
                        width="small"),
                "Cost Element": st.column_config.Column(
                        width="small"),
                },
                height=380,
                width=300,
                hide_index=True,
            )
            # st.markdown(f'<div class="fixed-table">{df_lbl.to_html(index=False)}</div>', unsafe_allow_html=True)

        with col2:
            st.plotly_chart(fig1, use_container_width=True)
          
        with col3:
            st.plotly_chart(fig2, use_container_width=True)



import streamlit as st
import pandas as pd

# Load the data
data = {
    "DESCRIPTION": ["Excavations", "Hardcore & Dust", "DPM", "Surface treatment", "Concrete works", "Reinforcement bars", "BRC", "Formwork", "Waterproofing", "Floor Hardener & Powerfloating", "DPC", "Total"],
    "BQ Price": ['389,503.69', '26,500.00', '10,600.00', '7,950.00', '16,473,303.99', '12,521,909.63', '26,000.00', '414,943.42', '53,048.00', '682,773.35', '3,090.00', '30,608,522.25'],
    "Materials Cost": [0, '27,200.00', '3,300.00', '5,600.00', '10,837,000.00', '11,156,290.00', '25,000.00', '267,700.00', '40,000.00', '387,000.00', '1,236.00', '22,750,326.00'],
    "Labor, transport and Profits Cost": ['389,503.69', '-700.00', '7,300.00', '2,350.00', '5,636,303.99', '1,365,019.63', '1,500.00', '146,243.42', '13,048.00', '295,773.35', '1,854.00', '7,858,196.25'],
    "Remarks": ["", "", "", "", "", "", "", "", "", "", "", ""]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df.index = list("ABCDEFGHIJKL")

# Create HTML table
html_table = """
<h6 style="color:green">Sample BQ 1</h6>
<p style="font-size:12px"><b>Project Name: </b>Proposed  Residential Development (1A) , Riruta, Off Naivasha Road </p>
<p style="font-size:12px"><b>Cost Analysis Level: </b>Rate Anaylsis <i>(Cost of Materials, Labor, transport and Profits) </i></p>
<p style="font-size:12px"><b>BQ Element/Section:  </b>Section 03 - Structure </p>
<div style="max-width: 100%; overflow-x: auto;">
<table border="1" class="dataframe" style="width:100%; border: 1px solid black; border-collapse: collapse; font-size: 10px;">
  <thead>
    <tr style="text-align: left;">
      <th></th>
      <th>DESCRIPTION</th>
      <th>BQ Price</th>
      <th>Materials Cost</th>
      <th>Labor, transport and Profits Cost</th>
      <th>Remarks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>SUBSTRUCTURES</b></td>
    </tr>
"""

# Add the rest of the rows with their respective index, except the last row
for index, row in df.iloc[:-1].iterrows():
    html_table += f"<tr><td>{index}</td>"
    for value in row:
        html_table += f"<td>{value}</td>"
    html_table += "</tr>"

# Add the last row without numbering and bolded
total_row = df.iloc[-1]
html_table += "<tr><td></td>"
for value in total_row:
    html_table += f"<td><b>{value}</b></td>"
html_table += "</tr>"

html_table += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>SUPERSTRUCTURES</b></td>
    </tr>
"""

# Load the data
new_data = {
    "DESCRIPTION": ["Concrete works", "Reinforcement bars", "Formwork", "Total"],
    "BQ Price": ['28,109,707.73', '39,546,297.23', '13,622,229.38', '81,277,234.33'],
    "Materials Cost": ['18,466,700.00', '35,064,852.56', '8,858,200.00', '62,389,752.56'],
    "Labor, transport and Profits Cost": ['9,642,007.73', '4,481,444.67', '4,764,029.38', '18,887,451.77'],
    "Remarks": ["", "", "", ""]
}

# Create a DataFrame
df2 = pd.DataFrame(new_data)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df2.index = list("ABCD")

# Add the rest of the rows with their respective index, except the last row
for index, row in df2.iloc[:-1].iterrows():
    html_table += f"<tr><td>{index}</td>"
    for value in row:
        html_table += f"<td>{value}</td>"
    html_table += "</tr>"

# Add the last row without numbering and bolded
total_row = df2.iloc[-1]
html_table += "<tr><td></td>"
for value in total_row:
    html_table += f"<td><b>{value}</b></td>"
html_table += "</tr>"

html_table += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>ROOFING</b></td>
    </tr>
"""


# Load the data
new_data2 = {
    "DESCRIPTION": ["Sikalastic 560 waterproofing", "Floor Finishes", "PCC Interlocking Tiles", "Polycarbonate", "Total"],
    "BQ Price": ['2,086,295.70', '1,700,452.63', '762,300.00', '90,000.00', '4,639,048.33'],
    "Materials Cost": ['3,219,000.00', '976,912.00', '539,100.00', '57,000.00', '4,792,012.00'],
    "Labor, transport and Profits Cost": ['-1,132,704.30', '723,540.63', '223,200.00', '33,000.00', '-152,963.68'],
    "Remarks": ["", "", "", "",""]
}

# Create a DataFrame
df3 = pd.DataFrame(new_data2)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df3.index = list("ABCDE")

# Add the rest of the rows with their respective index, except the last row
for index, row in df3.iloc[:-1].iterrows():
    html_table += f"<tr><td>{index}</td>"
    for value in row:
        html_table += f"<td>{value}</td>"
    html_table += "</tr>"

# Add the last row without numbering and bolded
total_row = df3.iloc[-1]
html_table += "<tr><td></td>"
for value in total_row:
    html_table += f"<td><b>{value}</b></td>"
html_table += "</tr>"

html_table += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>WALLING</b></td>
    </tr>
"""

# Load the data
new_data4 = {
    "DESCRIPTION": ["Copings", "Masonry walls-6'' Thick", "Ditto-4'' Thick", "Lintol", "Total"],
    "BQ Price": ['204,790.00', '18,833,521.05', '576,034.80', '272,255.00', '19,886,600.85'],
    "Materials Cost": ['112,500.00', '12,436,040.00', '336,100.00', '359,150.80', '13,243,790.80'],
    "Labor, transport and Profits Cost": ['92,290.00', '6,397,481.05', '239,934.80', '-86,895.80', '6,642,810.05'],
    "Remarks": ["", "", "", "",""]
}

# Create a DataFrame
df4 = pd.DataFrame(new_data4)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df4.index = list("ABCDE")

# Add the rest of the rows with their respective index, except the last row
for index, row in df4.iloc[:-1].iterrows():
    html_table += f"<tr><td>{index}</td>"
    for value in row:
        html_table += f"<td>{value}</td>"
    html_table += "</tr>"

# Add the last row without numbering and bolded
total_row = df4.iloc[-1]
html_table += "<tr><td></td>"
for value in total_row:
    html_table += f"<td><b>{value}</b></td>"
html_table += "</tr>"

html_table += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>SUMMARY</b></td>
    </tr>
"""

# Load the data
new_data5 = {
    "DESCRIPTION": ["Substructures", "Superstructure", "Roofing", "Walling", "Total"],
    "BQ Price": ['30,608,522.25', '81,277,234.33', '4,639,048.33', '19,886,600.85', '136,411,405.76'],
    "Materials Cost": ['22,750,326.00', '62,389,752.56', '4,792,012.00', '13,243,790.80', '103,175,881.36'],
    "Labor, transport and Profits Cost": ['7,858,196.25', '18,887,481.77', '-152,963.68', '6,642,810.05', '33,235,524.40'],
    "Remarks": ["", "", "", "",""]
}

# Create a DataFrame
df5 = pd.DataFrame(new_data5)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df5.index = list("ABCDE")

# Add the rest of the rows with their respective index, except the last row
for index, row in df5.iloc[:-1].iterrows():
    html_table += f"<tr><td>{index}</td>"
    for value in row:
        html_table += f"<td>{value}</td>"
    html_table += "</tr>"

# Add the last row without numbering and bolded
total_row = df5.iloc[-1]
html_table += "<tr><td></td>"
for value in total_row:
    html_table += f"<td><b>{value}</b></td>"
html_table += "</tr>"

html_table += """
  </tbody>
</table>
<div>
"""


# Load the data
data2 = {
    "DESCRIPTION": ["Excavations", "Hardcore", "Quarry Dust", "Surface treatment", "Concrete works", "Reinforcement bars", "BRC", "Formwork", "Foundation Walling", "Total"],
    "BQ Price": ['2,067,750.00', '35,000.00', '20,000.00', '0.00', '7,233,850.00', '3,922,320.00', '48,000.00', '439,100.00', '304,000.00', '14,070,020.00'],
    "Materials Cost": ['0.00', '31,500.00', '6,400.00', '0.00', '4,262,400.00', '3,236,520.00', '25,000.00', '283,345.00', '219,800.00', '8,064,965.00'],
    "Labor, transport and Profits Cost": ['2,067,750.00', '3,500.00', '13,600.00', '0.00', '2,971,450.00', '685,800.00', '23,000.00', '155,755.00', '84,200.00', '6,005,055.00'],
    "Remarks": ["", "", "", "", "", "", "", "", "", ""]
}

# Create a DataFrame
df6 = pd.DataFrame(data2)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df6.index = list("ABCDEFGHIJ")

# Create HTML table
html_table2 = """
<h6 style="color:green">Sample BQ 2</h6>
<p style="font-size:12px"><b>Project Name: </b>Proposed  Elmer Haco Apartments for Elmer One Development Limited </p>
<p style="font-size:12px"><b>Cost Analysis Level: </b>Rate Anaylsis <i>(Cost of Materials, Labor, transport and Profits) </i></p>
<p style="font-size:12px"><b>BQ Element/Section:  </b>Section 03 - Structure </p>
<div style="max-width: 100%; overflow-x: auto;">
<table border="1" class="dataframe" style="width:100%; border: 1px solid black; border-collapse: collapse; font-size: 10px;">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DESCRIPTION</th>
      <th>BQ Price</th>
      <th>Materials Cost</th>
      <th>Labor, transport and Profits Cost</th>
      <th>Remarks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>SUBSTRUCTURES</b></td>
    </tr>
"""

# Add the rest of the rows with their respective index, except the last row
for index, row in df6.iloc[:-1].iterrows():
    html_table2 += f"<tr><td>{index}</td>"
    for value in row:
        html_table2 += f"<td>{value}</td>"
    html_table2 += "</tr>"

# Add the last row without numbering and bolded
total_row = df.iloc[-1]
html_table2 += "<tr><td></td>"
for value in total_row:
    html_table2 += f"<td><b>{value}</b></td>"
html_table2 += "</tr>"

html_table2 += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>SUPERSTRUCTURES</b></td>
    </tr>
"""

# Load the data
data7 = {
    "DESCRIPTION": ["Concrete works", "Reinforcement bars", "Formwork", "Waterproofing", "Total"],
    "BQ Price": ['50,915,823.00', '71,415,600.00', '16,253,850.00', '160,600.00', '138,745,873.00'],
    "Materials Cost": ['30,071,800.00', '57,790,360.00', '10,691,490.00', '96,000.00', '98,649,650.00'],
    "Labor, transport and Profits Cost": ['20,844,023.00', '13,625,240.00', '5,562,360.00', '64,600.00', '40,096,223.00'],
    "Remarks": ["", "", "", "",""]
}

# Create a DataFrame
df7 = pd.DataFrame(data7)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df7.index = list("ABCDE")

# Add the rest of the rows with their respective index, except the last row
for index, row in df7.iloc[:-1].iterrows():
    html_table2 += f"<tr><td>{index}</td>"
    for value in row:
        html_table2 += f"<td>{value}</td>"
    html_table2 += "</tr>"

# Add the last row without numbering and bolded
total_row = df7.iloc[-1]
html_table2 += "<tr><td></td>"
for value in total_row:
    html_table2 += f"<td><b>{value}</b></td>"
html_table2 += "</tr>"

html_table2 += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>ROOFING</b></td>
    </tr>
"""

# Load the data
data8 = {
    "DESCRIPTION": ["Concrete works","Reinforcement bars", "Formwork", "Copings ", "Masonry walling",  "APP waterproofing",  "Saflock roofing sheets", "Roof insulation",  "Roof steel works", "Polycarbonate",  "Finishings",
"Total"],
    "BQ Price": ['678,222.00',  '142,920.00', '191,550.00', '380,250.00', '859,800.00', '25,522,00.00',  '2,043,400.00',  '526,800.00', '3,160,450.00',  '684,000.00', '4,335,470.00',  '11,219,592.00',],
    "Materials Cost": ['395,600.00',  '121,440.00', '124,510.00', '325,500.00', '593,488.00', '1,229,000.00',  '1,311,200.00',  '360,000.00', '2,330,532.00',  '210,000.00', '2,838,778.00',  '7,001,270.00',],
    "Labor, transport and Profits Cost": ['282,622.00', '21,480.00',  '67,040.00',  '54,750.00',  '266,312.00', '1,323,200.00',  '732,200.00', '166,800.00', '829,918.00', '474,000.00', '1,496,692.00',  '5,715,014.00',],
    "Remarks": ["", "", "", "","", "", "", "","","","",""]
}

# Create a DataFrame
df8 = pd.DataFrame(data8)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df8.index = list("ABCDEFGHIJKL")

# Add the rest of the rows with their respective index, except the last row
for index, row in df8.iloc[:-1].iterrows():
    html_table2 += f"<tr><td>{index}</td>"
    for value in row:
        html_table2 += f"<td>{value}</td>"
    html_table2 += "</tr>"

# Add the last row without numbering and bolded
total_row = df8.iloc[-1]
html_table2 += "<tr><td></td>"
for value in total_row:
    html_table2 += f"<td><b>{value}</b></td>"
html_table2 += "</tr>"

html_table2 += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>STAIRCASES</b></td>
    </tr>
"""

# Load the data
data9 = {
    "DESCRIPTION": ["Steel staircase complete","Total"],
    "BQ Price": ['8,942,868.00', '8,942,868.00'],
    "Materials Cost": ['6,159,275.00',  '6,159,275.00'],
    "Labor, transport and Profits Cost": ['2,783,593.00', '2,783,593.00'],
    "Remarks": ["", ""]
}

# Create a DataFrame
df9 = pd.DataFrame(data9)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df9.index = list("AB")

# Add the rest of the rows with their respective index, except the last row
for index, row in df9.iloc[:-1].iterrows():
    html_table2 += f"<tr><td>{index}</td>"
    for value in row:
        html_table2 += f"<td>{value}</td>"
    html_table2 += "</tr>"

# Add the last row without numbering and bolded
total_row = df9.iloc[-1]
html_table2 += "<tr><td></td>"
for value in total_row:
    html_table2 += f"<td><b>{value}</b></td>"
html_table2 += "</tr>"

html_table2 += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>EXTERNAL WALLS</b></td>
    </tr>
"""

# Load the data
data10 = {
    "DESCRIPTION": ["Copings",  "Clay brick grille",  "Masonry walls",  "Balustrading", "Finishes", "Fencing","Total"],
    "BQ Price": ['1,137,750.00', '452,200.00', '17,423,500.00', '1,647,000.00',  '12,881,970.00', '799,200.00', '33,542,420.00',],
    "Materials Cost": ['973,350.00',  '266,800.00', '11,697,020.00', '1,235,250.00',  '5,341,760.00',  '409,800.00', '19,514,180.00',],
    "Labor, transport and Profits Cost": ['164,400.00', '185,400.00', '5,726,480.00',  '411,750.00', '7,540,210.00',  '389,400.00', '14,417,640.00',],
    "Remarks": ["", "", "", "", "", "", ""]
}

# Create a DataFrame
df10 = pd.DataFrame(data10)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df10.index = list("ABCDEFG")

# Add the rest of the rows with their respective index, except the last row
for index, row in df10.iloc[:-1].iterrows():
    html_table2 += f"<tr><td>{index}</td>"
    for value in row:
        html_table2 += f"<td>{value}</td>"
    html_table2 += "</tr>"

# Add the last row without numbering and bolded
total_row = df10.iloc[-1]
html_table2 += "<tr><td></td>"
for value in total_row:
    html_table2 += f"<td><b>{value}</b></td>"
html_table2 += "</tr>"

html_table2 += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>WINDOWS AND EXTERNAL DOORS</b></td>
    </tr>
"""

# Load the data
data11 = {
    "DESCRIPTION": ["Windows & Doors","Total"],
    "BQ Price": ['63,586,400.00', '63,586,400.00'],
    "Materials Cost": ['52,893,471.00',  '52,893,471.00'],
    "Labor, transport and Profits Cost": ['10,692,929.00', '10,692,929.00'],
    "Remarks": ["", ""]
}

# Create a DataFrame
df11 = pd.DataFrame(data11)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df11.index = list("AB")

# Add the rest of the rows with their respective index, except the last row
for index, row in df11.iloc[:-1].iterrows():
    html_table2 += f"<tr><td>{index}</td>"
    for value in row:
        html_table2 += f"<td>{value}</td>"
    html_table2 += "</tr>"

# Add the last row without numbering and bolded
total_row = df11.iloc[-1]
html_table2 += "<tr><td></td>"
for value in total_row:
    html_table2 += f"<td><b>{value}</b></td>"
html_table2 += "</tr>"

html_table2 += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>INTERNAL WALLING</b></td>
    </tr>
"""

# Load the data
data12 = {
    "DESCRIPTION": ["Stone works","Total"],
    "BQ Price": ['15,975,500.00', '15,975,500.00'],
    "Materials Cost": ['10,621,126.00',  '10,621,126.00'],
    "Labor, transport and Profits Cost": ['5,354,374.00', '5,354,374.00'],
    "Remarks": ["", ""]
}

# Create a DataFrame
df12 = pd.DataFrame(data12)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df12.index = list("AB")

# Add the rest of the rows with their respective index, except the last row
for index, row in df12.iloc[:-1].iterrows():
    html_table2 += f"<tr><td>{index}</td>"
    for value in row:
        html_table2 += f"<td>{value}</td>"
    html_table2 += "</tr>"

# Add the last row without numbering and bolded
total_row = df12.iloc[-1]
html_table2 += "<tr><td></td>"
for value in total_row:
    html_table2 += f"<td><b>{value}</b></td>"
html_table2 += "</tr>"

html_table2 += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>INTERNAL DOORS</b></td>
    </tr>
"""

# Load the data
data13 = {
    "DESCRIPTION": ["Doors","Total"],
    "BQ Price": ['27,792,470.00', '27,792,470.00'],
    "Materials Cost": ['14,784,448.00',  '14,784,448.00'],
    "Labor, transport and Profits Cost": ['13,008,022.00', '13,008,022.00'],
    "Remarks": ["", ""]
}

# Create a DataFrame
df13 = pd.DataFrame(data13)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df13.index = list("AB")

# Add the rest of the rows with their respective index, except the last row
for index, row in df13.iloc[:-1].iterrows():
    html_table2 += f"<tr><td>{index}</td>"
    for value in row:
        html_table2 += f"<td>{value}</td>"
    html_table2 += "</tr>"

# Add the last row without numbering and bolded
total_row = df13.iloc[-1]
html_table2 += "<tr><td></td>"
for value in total_row:
    html_table2 += f"<td><b>{value}</b></td>"
html_table2 += "</tr>"

html_table2 += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>INTERNAL FINISHES</b></td>
    </tr>
"""

# Load the data
data14 = {
    "DESCRIPTION": ["Internal wall finishes", "Floor finishes", "Ceiling finishes", "Fittings","Total"],
    "BQ Price": ['30,715,380.00',  '30,320,670.00', '14,509,800.00', '46,350,414.00', '61,036,050.00',],
    "Materials Cost": ['30,715,380.00',  '30,320,670.00', '14,509,800.00', '46,350,414.00', '61,036,050.00',],
    "Labor, transport and Profits Cost": ['18,745,968.00', '9,724,940.00',  '10,531,285.00', '11,587,603.50', '50,589,796.50',],
    "Remarks": ["", "", "", "", ""]
}

# Create a DataFrame
df14 = pd.DataFrame(data14)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df14.index = list("ABCDE")

# Add the rest of the rows with their respective index, except the last row
for index, row in df14.iloc[:-1].iterrows():
    html_table2 += f"<tr><td>{index}</td>"
    for value in row:
        html_table2 += f"<td>{value}</td>"
    html_table2 += "</tr>"

# Add the last row without numbering and bolded
total_row = df14.iloc[-1]
html_table2 += "<tr><td></td>"
for value in total_row:
    html_table2 += f"<td><b>{value}</b></td>"
html_table2 += "</tr>"

html_table2 += """
  </tbody>
    <tr>
      <td colspan="6" style="text-align:center;"><b>SUMMARY</b></td>
    </tr>
"""

# Load the data
data15 = {
    "DESCRIPTION": ["Substructures",  "Superstructure", "Roofing",  "Staircases", "External Walls", "Windows and External Doors", "Internal Walling", "Internal Doors", "Internal Finishes","Total"],
    "BQ Price": ['14,070,020',  '138,745,873.00',  '15,555,062.00', '8,942,868.00',  '34,341,620.00', '63,586,400.00', '15,975,500.00', '27,792,470.00', '121,896,264.00',  '440,906,077.00',],
    "Materials Cost": ['8,064,965.00', '98,649,650.00', '9,840,048.00',  '6,159,275.00',  '19,923,980.00', '52,893,471.00', '10,621,126.00', '14,784,448.00', '71,306,467.50', '292,243,430.50',],
    "Labor, transport and Profits Cost": ['6,005,055.00',  '40,096,223.00', '5,715,014.00',  '2,783,593.00',  '14,417,640.00', '10,692,929.00', '5,354,374.00',  '13,008,022.00', '50,589,796.50', '148,662,646.50',],
    "Remarks": ["", "", "", "", "", "", "", "", "", ""]
}

# Create a DataFrame
df15 = pd.DataFrame(data15)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df15.index = list("ABCDEFGHIJ")

# Add the rest of the rows with their respective index, except the last row
for index, row in df15.iloc[:-1].iterrows():
    html_table2 += f"<tr><td>{index}</td>"
    for value in row:
        html_table2 += f"<td>{value}</td>"
    html_table2 += "</tr>"

# Add the last row without numbering and bolded
total_row = df15.iloc[-1]
html_table2 += "<tr><td></td>"
for value in total_row:
    html_table2 += f"<td><b>{value}</b></td>"
html_table2 += "</tr>"

html_table2 += """
  </tbody>
  </table>
</div>
"""

# Create a Streamlit app
# st.title("Cost Breakdown")

# Display the table
# st.markdown(html_table, unsafe_allow_html=True)
# st.markdown(html_table2, unsafe_allow_html=True)

# Use the full page instead of a narrow central column
# st.set_page_config(layout="wide")

with st.expander("Explore Bill of Quantities (BQs)"):
  # Create two columns for the tables
  col1, col2 = st.columns([1,1])

  # Add the first table to the first column
  with col1:
      st.markdown(html_table, unsafe_allow_html=True)

  # Add the second table to the second column
  with col2:
      st.markdown(html_table2, unsafe_allow_html=True)

with st.expander("Cost Estimation"):
    st.markdown("Input values")

# Footer
st.markdown("""
<div class="myfooter">
    <p>
        Contact us: info@example.com | All rights reserved © 2024
        <br>
        <a href="https://www.facebook.com" target="_blank" style="color:white">Facebook</a>
        | <a href="https://www.twitter.com" target="_blank" style="color:white">Twitter</a>
        | <a href="https://www.linkedin.com" target="_blank" style="color:white">LinkedIn</a>
    </p>
</div>
""", unsafe_allow_html=True)