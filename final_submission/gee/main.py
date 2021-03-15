#from datetime import datetime, timedelta, timezone
from IPython.display import Image
from gee import geengine
import dateutil.parser
import time
import json

#  Initialize custom Google Earth Engine object
engine = geengine()

# Read-in fraudulent messages
with open('../data/fraudulent_emails.json','r') as injson:
    messages = json.load(injson)

# Iterate over messages and look for good geolocation matches
for message in messages:
    if 'TIKA-GeoLocationParser' in message:
        # Save parsed geolocation data
        geolocation = message['TIKA-GeoLocationParser'][0]
        # Opting not to filter on timestamp because testing has shown that few images are available within filtered date ranges
        #timestamp = dateutil.parser.parse(message['timestamp']).replace(tzinfo=timezone.utc).astimezone(tz=None)
        if 'Geographic_LONGITUDE' in geolocation:
            # Create new key-value pair in message record
            message['GoogleEarthEngine'] = {
                'name': geolocation['Geographic_NAME'],
                'longitude': geolocation['Geographic_LONGITUDE'],
                'latitude': geolocation['Geographic_LATITUDE']
            }
            # Get population density image bytes
            image = engine.get_population_density_img(float(geolocation['Geographic_LONGITUDE']), float(geolocation['Geographic_LATITUDE']))
            # Convert bytes to base64 encoded string and save
            message['GoogleEarthEngine'][engine.collections['population_density']['name']] = engine.image_to_b64(image)
            # Get population count image bytes
            image = engine.get_population_count_img(float(geolocation['Geographic_LONGITUDE']), float(geolocation['Geographic_LATITUDE']))
            # Convert bytes to base64 encoded string and save
            message['GoogleEarthEngine'][engine.collections['population_count']['name']] = engine.image_to_b64(image)
            # Get raw land image bytes (this can take a while, so skip it if it timesout)
            try:
                image = engine.get_raw_land_img(float(geolocation['Geographic_LONGITUDE']), float(geolocation['Geographic_LATITUDE']))
            except HTTPError:
                print('HTTPError: Request for raw land image (LANDSAT/LE07/C01/T1) timedout')
                image = b''
            # Convert bytes to base64 encoded string and save
            message['GoogleEarthEngine'][engine.collections['raw_land']['name']] = engine.image_to_b64(image)
            # Get country boundaries image bytes
            image = engine.get_country_boundaries_img(float(geolocation['Geographic_LONGITUDE']), float(geolocation['Geographic_LATITUDE']))
            # Convert bytes to base64 encoded string and save
            message['GoogleEarthEngine'][engine.collections['country_boundaries']['name']] = engine.image_to_b64(image)
            # Save an example
            example = message['GoogleEarthEngine']
            # Sleep so we don't blast Google
            time.sleep(3)

# Save enriched fraudulent messages
with open('../data/fraudulent_emails.json','w') as outjson:
    json.dump(messages, outjson, indent=2)
