import streamlit as st
import pandas as pd
import json
from datetime import date, datetime
import requests
import fire
import ryan

# Set the page config
st.set_page_config(
  page_title="Trip",
  page_icon="✈️",
#   layout="wide"
)

st.title('To help with travel search')

col1, col2 = st.columns(2)

origin = col1.text_input('✈️ From').upper()
destination = col2.text_input('✈️ To').upper()

outboundDate = col1.date_input('✈️ Outbound Date', format='YYYY-MM-DD')
returnDate = col2.date_input('✈️ Retun by', format='YYYY-MM-DD')

locations = [origin, destination]

if len(origin) == 3 and len(destination) == 3:

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
        st.write(f"There is a direct flight to {destinationFire['AirportName']}, {destinationFire['AirportCountryName']}")
    else:
        st.write(f"There is no direct flight to {destinationFire['AirportName']}, {destinationFire['AirportCountryName']}")
    
    directOrigins = fire.getDirectDestinations(destination)



