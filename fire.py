from datetime import date, datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
import ryan

# Use a service account.
cred = credentials.Certificate('fire_creds.json')

# app = firebase_admin.initialize_app(cred)
# Check if the default app is already initialized
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

def dateDiffCheck(theDate: str):
    dateDiff = date.today() - datetime.strptime(theDate, '%Y%m%d').date()
    return dateDiff.days

def getKnownAirports(AirportCode: str):
    airportInfo = db.collection('Airports').document(AirportCode.upper()).get().to_dict()
    return airportInfo

def writeDirectDestinations(destinationList, AirportCode: str):
    doc_ref = db.collection('Airports').document(AirportCode.upper()).collection('Destinations').document('Direct')
    doc_ref.set({
        'Destinations': destinationList,
        'UpdateDate': date.today().strftime('%Y%m%d')
        })
    
def getDirectDestinations(AirportCode: str):
    directs = db.collection('Airports').document(AirportCode.upper()).collection('Destinations').document('Direct').get().to_dict()
    try:
        updateDate = directs['UpdateDate']
    except TypeError:
        updateDate = '19010101'
    if dateDiffCheck(updateDate) > 14:
        destinations = requests.get(ryan.getDestinations(AirportCode.upper()), headers=ryan.headers).json()
        directDestinations = ryan.destinationAirports(destinations)
        writeDirectDestinations(directDestinations, AirportCode)
    else:
        directDestinations = directs['Destinations']
    return directDestinations

