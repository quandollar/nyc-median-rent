# NYC's Median Rent by Borough
## Background
This web application extracts data from StreetEasy’s public database and produces charts of NYC's median rent over time.

I built this app in 2021 to look back at the changes in median rent before, at the peak of, and after COVID. 

This app was written in Python and the following Python libraries:
- `requests`, for making HTTP requests and downloading data from StreetEasy
- `zipfile` and `io`, for processing the zipped data file from StreetEasy
- `pandas`, for analyzing the unzipped CSV data file
- `altair`, for creating beautiful visualizations from the data

The backbone of this app is [Streamlit](https://streamlit.io/), an open-source app framework for Machine Learning and Data Science projects that allows developers to quickly create beautiful web apps in minutes.

View the app live [here](https://share.streamlit.io/quandollar/nyc_rent_app/main/nyc_rent_app.py). Note that you may need to wait a few minutes for the app to wake up.

## Quick Demo

