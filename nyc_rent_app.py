from requests import get
from zipfile import ZipFile
from io import BytesIO
import pandas as pd
import streamlit as st
import altair as alt

# page title and description
st.title("NYC Median Rent by Borough")
st.markdown(
    """
- Source: StreetEasy’s public database
- Built with: `Python` using `requests`, `zipfile`, `io`, `pandas`, `altair`, and `streamlit`
"""
)
st.header("")

# pull data from StreetEasy
@st.cache  # optimize performance of load_data via streamlist's caching mechanism
def load_data(url):
    request = get(url)  # request the median rent data as a zip file from StreetEasy
    zip_file = ZipFile(
        BytesIO(request.content)
    )  # load the zip file's content as bytes in an in-memory buffer
    files = zip_file.namelist()  # get a list of file names within the zip file
    with zip_file.open(files[0], "r") as csvfile:
        rent_stats_df = pd.read_csv(csvfile)  # read file into a dataframe
    return rent_stats_df


# simplify the above df into a data table for charting
def load_borough_df(df, borough):
    borough_df = df[df["Borough"] == borough]
    borough_df = borough_df.drop(columns="areaType")
    borough_df = borough_df.drop(columns="Borough")
    borough_df = borough_df.melt(
        id_vars="areaName", var_name="Month", value_name="Median Rent"
    )  # pivot the monthly columns into a column of months for charting
    return borough_df


# set up the borough df for charting
def filtered_df(borough_df, starting_month, selected_area):
    borough_df = borough_df[borough_df["areaName"] == selected_area]
    borough_df = borough_df[borough_df["Month"] >= starting_month]
    borough_df = borough_df.drop(columns="areaName")
    return borough_df


# input
url = "https://streeteasy-market-data-download.s3.amazonaws.com/rentals/All/medianAskingRent_All.zip"
rent_stats_df = load_data(url)
starting_month = "2020-01"

# create df for each borough
manhattan_df = load_borough_df(rent_stats_df, "Manhattan")
brooklyn_df = load_borough_df(rent_stats_df, "Brooklyn")
queens_df = load_borough_df(rent_stats_df, "Queens")
bronx_df = load_borough_df(rent_stats_df, "Bronx")
staten_island_df = load_borough_df(rent_stats_df, "Staten Island")

# MANHATTAN SECTION
st.header("Manhattan")
manhattan_area_list = (
    manhattan_df.areaName.unique()
)  # extract unique areas in a given borough
# filter box and default value
manhattan_container = st.container()
manhattan_default_area = list(manhattan_area_list).index("East Village")
manhattan_selected_area = manhattan_container.selectbox(
    "FILTER BY AREA:", manhattan_area_list, index=manhattan_default_area
)
manhattan_df = filtered_df(manhattan_df, starting_month, manhattan_selected_area)
# chart setting
manhattan_chart = alt.Chart(manhattan_df).mark_line().encode(x="Month", y="Median Rent")
st.altair_chart(manhattan_chart, use_container_width=True)

# BROOKLYN SECTION
st.header("Brooklyn")
brooklyn_area_list = (
    brooklyn_df.areaName.unique()
)  # extract unique areas in a given borough
# filter box and default value
brooklyn_container = st.container()
brooklyn_default_area = list(brooklyn_area_list).index("Williamsburg")
brooklyn_selected_area = brooklyn_container.selectbox(
    "FILTER BY AREA:", brooklyn_area_list, index=brooklyn_default_area
)
brooklyn_df = filtered_df(brooklyn_df, starting_month, brooklyn_selected_area)
# chart setting
brooklyn_chart = alt.Chart(brooklyn_df).mark_line().encode(x="Month", y="Median Rent")
st.altair_chart(brooklyn_chart, use_container_width=True)

# QUEENS SECTION
st.header("Queens")
queens_area_list = (
    queens_df.areaName.unique()
)  # extract unique areas in a given borough
# filter box and default value
queens_container = st.container()
queens_default_area = list(queens_area_list).index("Astoria")
queens_selected_area = queens_container.selectbox(
    "FILTER BY AREA:", queens_area_list, index=queens_default_area
)
queens_df = filtered_df(queens_df, starting_month, queens_selected_area)
# chart setting
queens_chart = alt.Chart(queens_df).mark_line().encode(x="Month", y="Median Rent")
st.altair_chart(queens_chart, use_container_width=True)

# THE BRONX SECTION
st.header("The Bronx")
bronx_area_list = bronx_df.areaName.unique()  # extract unique areas in a given borough
# filter box and default value
bronx_container = st.container()
bronx_default_area = list(bronx_area_list).index("Riverdale")
bronx_selected_area = bronx_container.selectbox(
    "FILTER BY AREA:", bronx_area_list, index=bronx_default_area
)
bronx_df = filtered_df(bronx_df, starting_month, bronx_selected_area)
# chart setting
bronx_chart = alt.Chart(bronx_df).mark_line().encode(x="Month", y="Median Rent")
st.altair_chart(bronx_chart, use_container_width=True)

# STATEN ISLAND SECTION
st.header("Staten Island")
staten_island_df = filtered_df(staten_island_df, starting_month, "Staten Island")
# chart setting
staten_island_chart = (
    alt.Chart(staten_island_df).mark_line().encode(x="Month", y="Median Rent")
)
st.altair_chart(staten_island_chart, use_container_width=True)


# hide streamlit's default hamburger menu and footer for a clean look
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
