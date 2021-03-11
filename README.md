# dsci550-assignment1
Repository for DSCI 550 Group 8 - Assignment 1

### Report

https://docs.google.com/document/d/1LHZureAfEl2ty9DPJZv9lSV5RFfpV81gAZhNP5V1YkY/edit?usp=sharing

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
- [x] Pre-5. Evaluate message language with Tika
- [ ] 5.2.1. Attacker title extraction: Increase robustness. Can we add more titles? (the best way to see if this is the case might be manual review)
- [ ] 5.2.2. Urgency score: Review. Add/remove words? Word tenses? Change score amounts? AND account for other languages
- [ ] 5.2.3. Message creation timestamp: Review algorithm, primarily the part where we are choosing to rely on the data from the GeoTopicParser and the GeoTopicParser has parsed multiple geolocations from the message. How do we decipher which location to use?
- [ ] 5.2.4. Categorize (tag) the attacker's offering -- do it
- [ ] 5.2.6. Evaluate attacker's relationship to the recipient -- do it
- [x] 5.2.7. Sentiment analysis -- thanks Claudia!
- [ ] 5.2.8. Attacker's language:
  - [ ] account for misspellings in other languages? -- sync with Katie
  - [ ] ratio of capitalization -- do it (sync with Katie)
- [ ] 5.2.9. Attacker age estimation -- do it (sync with Claudia)
- [X] 5.2.10. Discover if the message was sent from an address previously reported to be phisher: do it
- [ ] 6. Attach other datasets
  - [X] Global Unemployment data - excel (Applications top level type)
  - [X] International Debt Statistics data - csv (text top level type)
  - [ ] Image data - (image top level type) base64 encode image
- [ ] 7. Tika Similarity
- [ ] 8. Package up as TSV
- [ ] Write report
