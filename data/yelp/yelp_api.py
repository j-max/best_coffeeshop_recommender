import requests
import urllib
from yelp import Client

API_KEY = cA6mUWcXb1zHfyVEKHZVTRCJAlc5rqszTM2VbPMboML-uyA4-KdxN3muANFzqD03XaZBkRJpPVNO-GVNRUEkA8DwcTnqTd3zCF4iC9Oo_bwFtw0ItWYvbFORyLCBXHYx

client = Client(MY_API_KEY)
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'

DEFAULT_TERM = 'coffee'
DEFAULT_LOCATION = 'Chicago, IL'
SEARCH_LIMIT = 10
