# NYC's Median Rent by Borough
## Background
This web application extracts the latest data from StreetEasy’s public database and produces charts of NYC's median rent since January 2020 to date.

I built this app in 2021 to look back at the changes in median rent before, at the peak of, and after COVID. 

This app was written in Python and used the following Python libraries:
- `requests`, for making HTTP requests and downloading data from StreetEasy
- `zipfile` and `io`, for processing the zipped data file from StreetEasy
- `pandas`, for analyzing the unzipped CSV data file
- `altair`, for creating beautiful visualizations from the data

The backbone of this app is [Streamlit](https://streamlit.io/), an open-source app framework for machine learning and data science projects. It allows developers to quickly create beautiful web apps in minutes.

## Quick Demo
View the app live [here](https://share.streamlit.io/quandollar/nyc_rent_app/main/nyc_rent_app.py). Note that you may need to wait a few minutes for the app to wake up. You can also checkout the GIF below.

Visualizations are categorized by NYC borough: Manhattan, Brooklyn, Queens, The Bronx, and Staten Island. Each borough can be filtered by sub-area, except for Staten Island.
![demo](https://github.com/quandollar/nyc_rent_app/blob/main/demo%20assets/demo.gif)

A quick glance shows trends across areas in Manhattan and Brooklyn following a similar behavior. Take downtown Manhattan for example:
![analysis](https://github.com/quandollar/nyc_rent_app/blob/main/demo%20assets/analysis.png)