import googlemaps

gmaps = googlemaps.Client(api_key='AIzaSyDmTqZUq58tNnz-LsVaE47x4LAvASXR09I')

location = 'New York, NY'
place_type = 'restaurant'

places_result = gmaps.places_nearby(location=location, radius=1000, type=place_type)

for place in places_result['results']:
    name = place['name']
    address = place['vicinity']
    latitude = place['geometry']['location']['lat']
    longitude = place['geometry']['location']['lng']
    
    print(f'{name}, {address}: ({latitude}, {longitude})')
