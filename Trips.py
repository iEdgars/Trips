import streamlit as st
import pandas as pd
import json
from datetime import date, datetime
import requests
import fire
import ryan
import time
import random

# Set the page config
st.set_page_config(
  page_title="Trip",
  page_icon="✈️",
  layout="wide"
)

st.title('To help with travel search')

col1, col2 = st.columns(2)

origin = col1.text_input('✈️ From').upper()
destination = col2.text_input('✈️ To').upper()

outboundDate = col1.date_input('✈️ Outbound Date', format='YYYY-MM-DD')
returnDate = col2.date_input('✈️ Retun by', format='YYYY-MM-DD')

layoverMin = col1.number_input('✈️ Layover MIN', step=1)
layoverMax = col2.number_input('✈️ Layover MAX', step=1)

locations = [origin, destination]

if len(origin) == 3 and len(destination) == 3 and layoverMin > 0 and layoverMax > 0:

    try:
        with open('searchedLocations.json', 'r') as f:
            known_locations = json.load(f)
    except FileNotFoundError:
        known_locations = []

    for loc in locations:
        location = loc

        if location not in known_locations:
            st.write(f'new location: {location}')
            known_locations.append(location)
            with open('searchedLocations.json', 'w') as f:
                json.dump(known_locations, f)

    originFire = fire.getKnownAirports(origin)
    destinationFire = fire.getKnownAirports(destination)

    st.write(f"Looking for trip from {originFire['AirportName']}, {originFire['AirportCountryName']} " \
             f"to {destinationFire['AirportName']}, {destinationFire['AirportCountryName']}")
    
    directDestinations = fire.getDirectDestinations(origin)

    if destination in directDestinations:
        directExist = 'y'
        st.write(f"There is a direct flight to {destinationFire['AirportName']}, {destinationFire['AirportCountryName']}")
    else:
        directExist = 'n'
        st.write(f"There is no direct flight to {destinationFire['AirportName']}, {destinationFire['AirportCountryName']}")
    
    directOrigins = fire.getDirectDestinations(destination)

    stops = ryan.mathingAirports(directDestinations, directOrigins)

    # if directExist == 'y':
    #     stops.append(destination)

    fly1 = ryan.initialflightsDF()
    fly2 = ryan.initialflightsDF()

    sleepTime = 0
    setLen = len(stops)

    # st.write(stops)

    for stop in stops:
       
        if sleepTime > 14:
            sleepTime = random.randint(1, 5)
        elif sleepTime > 9:
            sleepTime = random.randint(2, 10)
        else:
            sleepTime = random.randint(2, 20)

        if stop in ['HHN', 'STN']:
            st.write(setLen, 'Skipping:', stop)
            setLen = setLen - 1
        else:
            st.write(setLen, stop, 'sleeping for:', sleepTime)

            fly1df = ryan.flightsDF(f'{origin}-{destination}', origin, stop, outboundDate, returnDate)
            fly1 = pd.concat([fly1, fly1df], ignore_index=True)
            time.sleep(random.randint(0, 2))

            fly2df = ryan.flightsDF(f'{origin}-{destination}', stop, destination, outboundDate, returnDate)
            fly2 = pd.concat([fly2, fly2df], ignore_index=True)

            time.sleep(sleepTime)
            setLen = setLen - 1



    # fly1 = ryan.flightsDF(f'{origin}-{destination}', 'VNO', 'BGY', outboundDate, returnDate)
    # fly2 = ryan.flightsDF(f'{origin}-{destination}', 'BGY', 'PSR', outboundDate, returnDate)

    
    # fly1 = requests.get(ryan.getFlights('VNO', 'BGY', outboundDate, returnDate), headers=ryan.headers).json()
    # fly2 = requests.get(ryan.getFlights('BGY', 'PSR', outboundDate, returnDate), headers=ryan.headers).json()

#limiting datasets to one way
    fly1 = fly1[fly1['From'] == origin]
    fly2 = fly2[fly2['To'] == destination]

    # Merge df1 and df2
    merged_df = pd.merge(fly1, fly2, left_on='To', right_on='From', suffixes=('_fly1', '_fly2'))

# Calculate time difference
    merged_df['time_diff'] = (merged_df['Depart_fly2'] - merged_df['Land_fly1']).dt.total_seconds() / 3600

# Filter rows where time difference is more than 2 hours and less than 12 hours
    filtered_flys = merged_df[(merged_df['time_diff'] > layoverMin) & (merged_df['time_diff'] < layoverMax)]
    
    filtered_flys = filtered_flys.rename(columns={'Trip_fly1': 'Trip', 'From_fly1': 'From', 'From_fly2': 'Stop', 'To_fly2': 'To', 'From Name_fly1':'From Name', 'From Name_fly2':'Stop Name', 'To Name_fly2': 'To Name', 'Depart_fly1':'Depart', 'Land_fly1':'Land Stop', 'Duration_fly1':'Duration 1', 'Depart_fly2':'Depart Stop', 'Land_fly2':'Land', 'Duration_fly2':'Duration 2', 'time_diff':'Layover', 'Price_fly1':'Price 1', 'Price_fly2':'Price 2'})
        # Assuming df is your DataFrame
    filtered_flys['Price 1'] = pd.to_numeric(filtered_flys['Price 1'], errors='coerce')
    filtered_flys['Price 2'] = pd.to_numeric(filtered_flys['Price 2'], errors='coerce')

    # Now, you can calculate the total
    filtered_flys['Total'] = filtered_flys['Price 1'] + filtered_flys['Price 2']

    filtered_flys = filtered_flys.reindex(columns=['Trip', 'From', 'Stop', 'To', 'Depart', 'Duration 1', 'Land Stop', 'Layover', 'Depart Stop', 'Duration 2', 'Land', 'Price 1', 'Price 2', 'Total', 'From Name', 'Stop Name', 'To Name'])


    st.dataframe(filtered_flys)

    st.write('Raw flight data:')

    st.dataframe(fly1)
    st.dataframe(fly2)

