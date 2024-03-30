from datetime import date

baseURL = 'https://www.ryanair.com/api'

ryanCookie = 'rid=3931c16d-5c6f-4ccb-97b9-db61df784bcb; mkt=/gb/en/; STORAGE_PREFERENCES={"STRICTLY_NECESSARY":true,"PERFORMANCE":false,"FUNCTIONAL":false,"TARGETING":false,"SOCIAL_MEDIA":false,"PIXEL":false,"GANALYTICS":false,"__VERSION":2}; RY_COOKIE_CONSENT=true; fr-correlation-id=67ff7eb7-edf7-4389-a0d1-e93c8ed6fef6; fr-correlation-id.sig=xP7xRs50ztq-uw9_xW8cr5c6MJo; tj_seed=008eccc46545ddf02fe76cece7df000000; agsd=LMfiKZXi7rCTdlkxXOLjnnMqFXnxpiCAUlY9wfOn3HqzPFCK; _cc=AYiH8%2BxwGp86%2Br6JvSUceNPQ; _cid_cc=AYiH8%2BxwGp86%2Br6JvSUceNPQ; AMCV_64456A9C54FA26ED0A4C98A5%40AdobeOrg=-715282455%7CMCIDTS%7C19786%7CMCMID%7C79414081869209830472658947344781096292%7CMCAAMLH-1710079325%7C6%7CMCAAMB-1710079325%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1709481725s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C-265859108%7CMCSYNCSOP%7C411-19793%7CvVersion%7C4.2.0; __zlcmid=1KbmXdmsAtQsLYF; myRyanairID=; .AspNetCore.Session=CfDJ8NWtdMbBsIBNuIq3PW%2BkRJTP9mHxeKEH3M0XqvgicdwP0Rok6inpSJpCl6MVVEBG51wk9IpL3p4tLq7NNg4mnCW7%2BnmcAvsS6dx8ht5PlzrCJZLxdpENKI2mUXajO3rRAI%2B5NxdUZU%2FdA6VC%2FvYGu6S0atbFyCbhOY8aVDJtVSRV; rid.sig=jyna6R42wntYgoTpqvxHMK7H+KyM6xLed+9I3KsvYZaVt7P36AL6zp9dGFPu5uVxaIiFpNXrszr+LfNCdY3IT3oCSYLeNv/ujtjsDqOzkY5JmUFsCdAEz3kpPbhCUwiArp5oaa75tpJtO3kFwYQ8l0DbH67AtcN/PMbniLsiM5qn+2AjrrtoNJicE3ZQwFHVipe4lWPSRfq2OIyUrlFhwEDt20+wCX7l1mCubNXtG6nZrUA07sFUFhn4RUxnjwjJ6d9qjjBasXLvYSqyYN7UadcxLyXgua2mbG5A40mHEBkzO1uFZu26ijA0o1sfCWdS+ghbVEA8SXbleW+z4G9gykK62+T+vG2NCISDbiB5lLO6eslHn8xugrLbUqDpK6eI9RHZC/bL1jV/54UVDGDKgVpoZjgFZNTDTACAiplVp8adufPcE324vLtWttgDLi3Nx+uMxkz3zC6lIM3WboAa/fj2t009Ks/EewfFhlaO3qrF1qudgtP9o/Pjj9XevwZ1d7t4p0/Q+qEWzB/uHy5EYzOUoYpSN5JKojBkWSCIWW87FnUdg/gMdISPOlsNy7JrLh/ywgPfZLxUH5t4LrlTjAbDkH09ymoix/pi+becivJR0TfZibH7nJ+8KbYwDbDbRHi7vuxPogMF0wT18w/L/m3dRFGOLshTYwovD0H9UByXXkm11vXDBeuUWuZ4ULYoXg2yBwKWhx4dt5WoOyrS+RoH+f72fk7JxqZgAEbCoo9s0UFIa5Ac5JjxI/ScUafSfVeXNF0BfDbqtB7hPQ7uR2+A48Vw8q2wL0+27otJyXyQzhGf1jsaRDTeWhU5Wd7F/GNX9vYMqYfA451kVS1cdO8GsQlPRGKRBqTeyh5hHnw0NRXoMqM2i40hKobY1dtOXYIfvGm5hkdwpm+cfwQynQzWmKdGFaROJRlUOAxKGqziXq+qDt6kgTcgRbb9bm37NAPi/HsnJmHQ2AKzfAyCb0WIET2L6aFUK3Lg3ixWr7/tlAZeW23zQ9jKLhwf3HcFNDLesUCYu5KxBaBln8E6BYrb7TK7AL3yEuXndH2pVL+NvTl7OxQMeaeY2vUTjjevxofqV8vCVXz6Xc5y+LBPYj99vI6ZuhzkJIonFwfE/L3bVsQ2MHpGoBRvAbvZYS7MiaAihfZxNbdE1gbqsPPDtzrqFm7nmHBustXdKTKRXTBxOcz8VdC9O0AQnRGz91RWt8eHo5OmHkliLBYJzda1iw=='
headers = {'Cookie': ryanCookie, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

def getDestinations(airportFrom: str):
    base = f'{baseURL}/views/locate/searchWidget/routes/en/airport/'
    fullURL = f'{base}{airportFrom.upper()}'
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
    
