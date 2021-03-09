# dsci550-assignment1
Repository for DSCI 550 Group 8 - Assignment 1

### Data

data/fraudulent_emails_orignal.json: Plain parsed fraudulent_emails.txt output directly from Tika (no enrichment)

data/fraudulent_emails_olivia.json: Enriched fraudulent emails dataset. Additional fields include:
* 'embedded_resources'
* 'se_tags'
* 'author_titles'
* 'urgency_score'
* 'GeoLocationParser-data'
* 'IPInfo-data'

### Tasks
[ ] 5.2.1. Attacker title extraction: Increase robustness. Can we add more titles? (the best way to see if this is the case might be manual review)
[ ] 5.2.2. Urgency score: Review. Add/remove words? Word tenses? Change score amounts?
[ ] 5.2.3. Message creation timestamp: Review algorithm, primarily the part where we are choosing to rely on the data from the GeoTopicParser and the GeoTopicParser has parsed multiple geolocations from the message. How do we decipher which location to use?
