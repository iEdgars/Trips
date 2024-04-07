from datetime import date
import pandas as pd
import requests

baseURL = 'https://www.ryanair.com/api'

# ryanCookie = 'rid=3931c16d-5c6f-4ccb-97b9-db61df784bcb; mkt=/gb/en/; STORAGE_PREFERENCES={"STRICTLY_NECESSARY":true,"PERFORMANCE":false,"FUNCTIONAL":false,"TARGETING":false,"SOCIAL_MEDIA":false,"PIXEL":false,"GANALYTICS":false,"__VERSION":2}; RY_COOKIE_CONSENT=true; fr-correlation-id=67ff7eb7-edf7-4389-a0d1-e93c8ed6fef6; fr-correlation-id.sig=xP7xRs50ztq-uw9_xW8cr5c6MJo; tj_seed=008eccc46545ddf02fe76cece7df000000; agsd=LMfiKZXi7rCTdlkxXOLjnnMqFXnxpiCAUlY9wfOn3HqzPFCK; _cc=AYiH8%2BxwGp86%2Br6JvSUceNPQ; _cid_cc=AYiH8%2BxwGp86%2Br6JvSUceNPQ; AMCV_64456A9C54FA26ED0A4C98A5%40AdobeOrg=-715282455%7CMCIDTS%7C19786%7CMCMID%7C79414081869209830472658947344781096292%7CMCAAMLH-1710079325%7C6%7CMCAAMB-1710079325%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1709481725s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-265859108%7CMCSYNCSOP%7C411-19793%7CvVersion%7C4.2.0; __zlcmid=1KbmXdmsAtQsLYF; myRyanairID=; .AspNetCore.Session=CfDJ8NWtdMbBsIBNuIq3PW%2BkRJTP9mHxeKEH3M0XqvgicdwP0Rok6inpSJpCl6MVVEBG51wk9IpL3p4tLq7NNg4mnCW7%2BnmcAvsS6dx8ht5PlzrCJZLxdpENKI2mUXajO3rRAI%2B5NxdUZU%2FdA6VC%2FvYGu6S0atbFyCbhOY8aVDJtVSRV; rid.sig=jyna6R42wntYgoTpqvxHMK7H+KyM6xLed+9I3KsvYZaVt7P36AL6zp9dGFPu5uVxaIiFpNXrszr+LfNCdY3IT3oCSYLeNv/ujtjsDqOzkY5JmUFsCdAEz3kpPbhCUwiArp5oaa75tpJtO3kFwYQ8l0DbH67AtcN/PMbniLsiM5qn+2AjrrtoNJicE3ZQwFHVipe4lWPSRfq2OIyUrlFhwEDt20+wCX7l1mCubNXtG6nZrUA07sFUFhn4RUxnjwjJ6d9qjjBasXLvYSqyYN7UadcxLyXgua2mbG5A40mHEBkzO1uFZu26ijA0o1sfCWdS+ghbVEA8SXbleW+z4G9gykK62+T+vG2NCISDbiB5lLO6eslHn8xugrLbUqDpK6eI9RHZC/bL1jV/54UVDGDKgVpoZjgFZNTDTACAiplVp8adufPcE324vLtWttgDLi3Nx+uMxkz3zC6lIM3WboAa/fj2t009Ks/EewfFhlaO3qrF1qudgtP9o/Pjj9XevwZ1d7t4p0/Q+qEWzB/uHy5EYzOUoYpSN5JKojBkWSCIWW87FnUdg/gMdISPOlsNy7JrLh/ywgPfZLxUH5t4LrlTjAbDkH09ymoix/pi+becivJR0TfZibH7nJ+8KbYwDbDbRHi7vuxPogMF0wT18w/L/m3dRFGOLshTYwovD0H9UByXXkm11vXDBeuUWuZ4ULYoXg2yBwKWhx4dt5WoOyrS+RoH+f72fk7JxqZgAEbCoo9s0UFIa5Ac5JjxI/ScUafSfVeXNF0BfDbqtB7hPQ7uR2+A48Vw8q2wL0+27otJyXyQzhGf1jsaRDTeWhU5Wd7F/GNX9vYMqYfA451kVS1cdO8GsQlPRGKRBqTeyh5hHnw0NRXoMqM2i40hKobY1dtOXYIfvGm5hkdwpm+cfwQynQzWmKdGFaROJRlUOAxKGqziXq+qDt6kgTcgRbb9bm37NAPi/HsnJmHQ2AKzfAyCb0WIET2L6aFUK3Lg3ixWr7/tlAZeW23zQ9jKLhwf3HcFNDLesUCYu5KxBaBln8E6BYrb7TK7AL3yEuXndH2pVL+NvTl7OxQMeaeY2vUTjjevxofqV8vCVXz6Xc5y+LBPYj99vI6ZuhzkJIonFwfE/L3bVsQ2MHpGoBRvAbvZYS7MiaAihfZxNbdE1gbqsPPDtzrqFm7nmHBustXdKTKRXTBxOcz8VdC9O0AQnRGz91RWt8eHo5OmHkliLBYJzda1iw=='
ryanCookie = 'fr-correlation-id=bda8f3c7-1db4-4198-af55-c6e0cccb3a00; rid=ad512ba8-c416-4ec4-91c3-30419db8c8f5; mkt=/gb/en/; STORAGE_PREFERENCES={"STRICTLY_NECESSARY":true,"PERFORMANCE":false,"FUNCTIONAL":false,"TARGETING":false,"SOCIAL_MEDIA":false,"PIXEL":false,"__VERSION":2}; myRyanairID=; RY_COOKIE_CONSENT=true; rid.sig=jyna6R42wntYgoTpqvxHMK7H+KyM6xLed+9I3KsvYZaVt7P36AL6zp9dGFPu5uVxaIiFpNXrszr+LfNCdY3IT3oCSYLeNv/ujtjsDqOzkY5JmUFsCdAEz3kpPbhCUwiArp5oaa75tpJtO3kFwYQ8l0DbH67AtcN/PMbniLsiM5qn+2AjrrtoNJicE3ZQwFHVipe4lWPSRfq2OIyUrlFhwEDt20+wCX7l1mCubNXtG6nZrUA07sFUFhn4RUxnjwjJ6d9qjjBasXLvYSqyYN7UaY8s+X70korZyaicZWcWTvOuJpS/t0mQO55YWPA3Vd5qNkkutAl0IbtjKtk9L5isdm6o5090yxOrU109eu/hef4iUEykcVo0hFOWqRELbSvZUJBAjU8DHdgjAT9BMKUDwBLwOMAT1Z7+7tKkjbAhIEyEHjAnSFbnHDDCTFOKdVDRcuRbZY8N+o0C7I6bykVyiVCceJkLF/+7YWqWKAynaytefLR4B5pL76RqscTghrl/bnpV0l71loApUhkJf737P3b5DcLE3I8OrsX0GTv0kOhHVXclYPFH2DKSC/GV3TWA/yiQKFtX8INUT8z7Urhslln2lPLn7XVt0vfXcgeXKk28NpEwP3w64JjJM42lkqsyzmOGnidR8MQriyJxHh3sghBE445XbiZ9/8U6iJ8bn4+ep1etSXys2bELIbjemMUvfRj1rxqZsZAPYOPNjfIohGIxL8/Unp4f6DAnQVeSAn8GO5S/e79ZG5bjsycU9gAp3gEE08QCcMpOxXsC1YYJEhvPDGICP6JUhCzaTRBpR+CP2Iihu73VO43vVGFfgXo2z5McPja2HvumWQgoHbTPdky/PbDlsf7uubPPm1ev8EPzzbk2c6w26z1G0nJBOm2R/96hVqe0R1JsHODzT3cxvpM3l0nQ7RmUILxzlqblEq4=; .AspNetCore.Session=CfDJ8AId49pjtGVHoprbzNbFymZeMk%2BJ16nA8WSCH%2B%2FT%2BDu%2F0%2F9VhE1NZ13acX71naH3%2BRXpVHjleMHaAxKc2XbE4osGQo7Pjp9m8hxmZv%2BgCP%2BJkfZp2GYP2cGHC64khZRbJ2b%2B3jWZwB%2Ft%2FU0HS2Ic3mYNPqZjSKZgtvzcOLyJhNdz'
headers = {'Cookie': ryanCookie, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


def dateAvailabilities(origin: str, destination: str):
    return f'https://www.ryanair.com/api/farfnd/3/oneWayFares/{origin}/{destination}/availabilities'

def getDestinations(airportFrom: str):
    base = f'{baseURL}/views/locate/searchWidget/routes/en/airport/'
    fullURL = f'{base}{airportFrom.upper()}'
    return fullURL

def getFlights(origin: str, destination: str, Outbound: str, Return: str):
    base = f'{baseURL}/booking/v4/en-en/availability'
    fullURL = f'{base}?ADT=2&CHD=0&Destination={destination}&INF=0&Origin={origin}&TEEN=0&IncludeConnectingFlights=false&DateOut={Outbound}&FlexDaysOut=6&DateIn={Return}&FlexDaysIn=6&RoundTrip=true&ToUs=AGREED'
    
    return fullURL

def destinationAirports(destinations):
    destAirports = []
    for dest in destinations:
        destAirports.append(dest['arrivalAirport']['code'])
    return destAirports

def mathingAirports(originDestinations: list, destinationOrigins: list):
    # Convert the lists to sets
    destinationSet = set(originDestinations)
    originSet = set(destinationOrigins)
    # Find the intersection of the two sets
    matchedAirportSet = destinationSet & originSet
    # Convert the result back to a list (if needed)
    matchedAirportList = list(matchedAirportSet)
    return matchedAirportList

#date / time formatting:
def ryanDateTime(dateTime: str, returnFormat: str='date'):
    #dateTime should be in format YYYY-MM-DDTHH:MM:SS.sss ['2023-01-17T15:55:00.000']
    #returnFormat should be: 
        #date ['2023-01-17'], 
        #dateid ['20230117'], 
        #hour ['15'], 
        #minute ['55'], 
        #time ['15:55'], 
        #datetime ['20230117_15:55'], 
        #dateid:int [20230117], 
        #hour:int [15], 
        #minute:int [55]
    simpleDate = dateTime.split('T')[0]
    dateid = simpleDate.replace('-','')
    hour = dateTime.split('T')[1].split(':')[0]
    minute = dateTime.split('T')[1].split(':')[1]
    time = f"{hour}:{minute}"
    datetime = f"{dateid}_{time}"

    if returnFormat == 'date':
        return simpleDate
    if returnFormat == 'dateid':
        return dateid
    if returnFormat == 'dateid:int':
        return int(dateid)
    if returnFormat == 'hour':
        return hour
    if returnFormat == 'hour:int':
        return int(hour)
    if returnFormat == 'minute':
        return minute
    if returnFormat == 'minute:int':
        return int(minute)
    if returnFormat == 'time':
        return time
    if returnFormat == 'datetime':
        return datetime
    
def initialflightsDF():
    # columns = ['Trip', 'From', 'From Name', 'To', 'To Name', 'Fly Date', 'Depart', 'Land', 'Depart UTC', 'Land UTC', 'Price', 'Duration', 'flightKey']
    columns = ['Trip', 'From', 'From Name', 'To', 'To Name', 'Fly Date', 'Depart', 'Land', 'Price', 'Duration']
    df = pd.DataFrame(columns=columns)

    return df

def flightsDF(trip: str, origin: str, destination: str, Outbound: str, Return: str):
    columns = ['Trip', 'From', 'From Name', 'To', 'To Name', 'Fly Date', 'Depart', 'Land', 'Depart UTC', 'Land UTC', 'Price', 'Duration', 'flightKey']
    df = pd.DataFrame(columns=columns)

    fly = requests.get(getFlights(origin, destination, Outbound, Return), headers=headers).json()

    for f in fly['trips']:
        for d in f['dates']:
            if d['flights'] != []:
                for flight in d['flights']:
                    df.loc[len(df)] = [trip, f['origin'], f['originName'], f['destination'], f['destinationName'], d['dateOut'][:10], flight['time'][0], flight['time'][1], flight['timeUTC'][0], flight['timeUTC'][1], flight['regularFare']['fares'][0]['amount'], flight['duration'], flight['flightKey']]

    df = df.drop(['Depart UTC', 'Land UTC', 'flightKey'], axis=1)
    df['Depart'] = pd.to_datetime(df['Depart'])
    df['Land'] = pd.to_datetime(df['Land'])
    # df['Depart UTC'] = pd.to_datetime(df['Depart UTC'])
    # df['Land UTC'] = pd.to_datetime(df['Land UTC'])

    return df