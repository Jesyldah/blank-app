import streamlit as st

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

# Creating the charts
fig, ax = plt.subplots(1, 2, figsize=(20, 10))

# Bar chart for cost in Kenyan Shillings
df.set_index('Cost element').T.plot(kind='bar', stacked=True, ax=ax[0], legend=False)
ax[0].set_title('Housing Development Cost Comparisons: Kenyan Shillings', fontsize=16,)
ax[0].set_ylabel('Kenyan shillings (millions)', fontsize=16, fontweight='bold')
ax[0].set_xlabel('')
ax[0].set_xticklabels(df.columns[1:], rotation=0, fontsize=12,)

# Bar chart for percentage cost
df_percentage = df.set_index('Cost element').div(df.set_index('Cost element').sum(axis=0), axis=1) * 100
df_percentage.T.plot(kind='bar', stacked=True, ax=ax[1])
ax[1].set_title('Housing Development Cost Comparisons: Percentage', fontsize=16)
ax[1].set_ylabel('Percentage(%)', fontsize=16, fontweight='bold')
ax[1].set_xlabel('')
ax[1].set_xticklabels(df.columns[1:], rotation=0, fontsize=12)
ax[1].legend(loc='upper left', bbox_to_anchor=(1.05, 1), frameon=False, fontsize=18)

# Adjust layout
plt.tight_layout()

st.set_page_config(layout="wide")

# Displaying in Streamlit
st.title("Housing Development Cost Comparison")

with st.expander("HCCB 22 gragh comparison: CAHF vs Low-rise and High-rise projects"):
    # Create two columns
    col1, col2 = st.columns([1,2])

    with col1:
        st.write(df_lbl.to_html(index=False), unsafe_allow_html=True)

    with col2:
        st.pyplot(fig)




import streamlit as st
import pandas as pd

# Load the data
data = {
    "DESCRIPTION": ["Excavations", "Hardcore & Dust", "DPM", "Surface treatment", "Concrete works", "Reinforcement bars", "BRC", "Formwork", "Waterproofing", "Floor Hardener & Powerfloating", "DPC", "Total"],
    "BQ Price": [389503.69, 26500.00, 10600.00, 7950.00, 16473303.99, 12521909.63, 26000.00, 414943.42, 53048.00, 682773.35, 3090.00, 30608522.25],
    "Materials Cost": [0, 27200.00, 3300.00, 5600.00, 10837000.00, 11156290.00, 25000.00, 267700.00, 40000.00, 387000.00, 1236.00, 22750326.00],
    "Labor, transport and Profits Cost": [389503.69, -700.00, 7300.00, 2350.00, 5636303.99, 1365019.63, 1500.00, 146243.42, 13048.00, 295773.35, 1854.00, 7858196.25],
    "Remarks": ["", "", "", "", "", "", "", "", "", "", "", ""]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df.index = list("ABCDEFGHIJKL")

# Create HTML table
html_table = """
<h5>Sample BQ 1</h5>
<hr>
<p><b>Project Name: </b>Proposed  Residential Development (1A) , Riruta, Off Naivasha Road </p>
<p><b>Cost Analysis Level: </b>Rate Anaylsis <i>(Cost of Materials, Labor, transport and Profits) </i></p>
<p><b>BQ Element/Section:  </b>Section 03 - Structure </p>
<table border="1" class="dataframe" style="width:100%; border: 1px solid black; border-collapse: collapse;">
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
    "BQ Price": [28109707.73, 39546297.23, 13622229.38, 81277234.33],
    "Materials Cost": [18466700.00, 35064852.56, 8858200.00, 62389752.56],
    "Labor, transport and Profits Cost": [9642007.73, 4481444.67, 4764029.38, 18887451.77],
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
    "BQ Price": [2086295.7, 1700452.625, 762300, 90000, 4639048.325],
    "Materials Cost": [3219000, 976912, 539100, 57000, 4792012],
    "Labor, transport and Profits Cost": [-1132704.3, 723540.625, 223200, 33000, -152963.675],
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
    "BQ Price": [204790, 18833521.05, 576034.8, 272255, 19886600.85],
    "Materials Cost": [112500, 12436040, 336100, 359150.8, 13243790.8],
    "Labor, transport and Profits Cost": [92290, 6397481.05, 239934.8, -86895.8, 6642810.05],
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
    "BQ Price": [30608522.2531377, 81277234.328207, 4639048.325, 19886600.85, 136411405.756345],
    "Materials Cost": [22750326, 62389752.56, 4792012, 13243790.8, 103175881.36],
    "Labor, transport and Profits Cost": [7858196.25313774, 18887481.768207, -152963.675, 6642810.05, 33235524.3963448],
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
"""


# Load the data
data2 = {
    "DESCRIPTION": ["Excavations", "Hardcore", "Quarry Dust", "Surface treatment", "Concrete works", "Reinforcement bars", "BRC", "Formwork", "Foundation Walling", "Total"],
    "BQ Price": [2067750, 35000, 20000, 0, 7233850, 3922320, 48000, 439100, 304000, 14070020],
    "Materials Cost": [0, 31500, 6400, 0, 4262400, 3236520, 25000, 283345, 219800, 8064965],
    "Labor, transport and Profits Cost": [2067750, 3500, 13600, 0, 2971450, 685800, 23000, 155755, 84200, 6005055],
    "Remarks": ["", "", "", "", "", "", "", "", "", ""]
}

# Create a DataFrame
df6 = pd.DataFrame(data2)

# Set index to uppercase alphabet letters from A, starting from 'Excavations'
df6.index = list("ABCDEFGHIJ")

# Create HTML table
html_table2 = """
<h5>Sample BQ 2</h5>
<hr>
<p><b>Project Name: </b>Proposed  Elmer Haco Apartments for Elmer One Development Limited </p>
<p><b>Cost Analysis Level: </b>Rate Anaylsis <i>(Cost of Materials, Labor, transport and Profits) </i></p>
<p><b>BQ Element/Section:  </b>Section 03 - Structure </p>
<table border="1" class="dataframe" style="width:100%; border: 1px solid black; border-collapse: collapse;">
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
    "BQ Price": [50915823, 71415600, 16253850, 160600, 138745873],
    "Materials Cost": [30071800, 57790360, 10691490, 96000, 98649650],
    "Labor, transport and Profits Cost": [20844023, 13625240, 5562360, 64600, 40096223],
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
    "BQ Price": [678222,  142920, 191550, 380250, 859800, 2552200,  2043400,  526800, 3160450,  684000, 4335470,  11219592,],
    "Materials Cost": [395600,  121440, 124510, 325500, 593488, 1229000,  1311200,  360000, 2330532,  210000, 2838778,  7001270,],
    "Labor, transport and Profits Cost": [282622, 21480,  67040,  54750,  266312, 1323200,  732200, 166800, 829918, 474000, 1496692,  5715014,],
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
    "BQ Price": [8942868, 8942868],
    "Materials Cost": [6159275,  6159275],
    "Labor, transport and Profits Cost": [2783593, 2783593],
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
    "BQ Price": [1137750, 452200, 17423500, 1647000,  12881970, 799200, 33542420,],
    "Materials Cost": [973350,  266800, 11697020, 1235250,  5341760,  409800, 19514180,],
    "Labor, transport and Profits Cost": [164400, 185400, 5726480,  411750, 7540210,  389400, 14417640,],
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
    "BQ Price": [63586400, 63586400],
    "Materials Cost": [52893471,  52893471],
    "Labor, transport and Profits Cost": [10692929, 10692929],
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
    "BQ Price": [15975500, 15975500],
    "Materials Cost": [10621126,  10621126],
    "Labor, transport and Profits Cost": [5354374, 5354374],
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
    "BQ Price": [27792470, 27792470],
    "Materials Cost": [14784448,  14784448],
    "Labor, transport and Profits Cost": [13008022, 13008022],
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
    "BQ Price": [30715380,  30320670, 14509800, 46350414, 61036050,],
    "Materials Cost": [30715380,  30320670, 14509800, 46350414, 61036050,],
    "Labor, transport and Profits Cost": [18745968, 9724940,  10531285, 11587603.5, 50589796.5,],
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
    "BQ Price": ['14,070,020',  138745873,  15555062, 8942868,  34341620, 63586400, 15975500, 27792470, 121896264,  440906077,],
    "Materials Cost": [8064965, 98649650, 9840048,  6159275,  19923980, 52893471, 10621126, 14784448, 71306467.5, 292243430.5,],
    "Labor, transport and Profits Cost": [6005055,  40096223, 5715014,  2783593,  14417640, 10692929, 5354374,  13008022, 50589796.5, 148662646.5,],
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