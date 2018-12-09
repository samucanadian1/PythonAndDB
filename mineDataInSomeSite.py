import requests
import BeautifulSoup

session = requests.session()

req = session.get('https://www.flighthub.com/flight/search?type=roundtrip&seg0_from=YUL&seg0_to=CWB&seg0_date=2018-12-11&seg1_date=2018-12-25&seg1_from_code=YUL&seg2_from_code=YUL&seg3_from_code=YUL&seg4_from_code=YUL&num_adults=1&num_children=0&num_infants=0&num_infants_lap=0&seat_class=Economy&seg1_from=CWB&seg1_to=YUL&campaign=1&search_id=81b68b249dcb5e09a55fea4bedaac660&flexible_search_id=81b68b249dcb5e09a55fea4bedaac660')

doc = BeautifulSoup.BeautifulSoup(req.content)

print (doc)

with open('out.txt', 'w') as f:
    print >> f, 'Filename:', doc


