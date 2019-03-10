from yelpapi import YelpAPI
import argparse
from pprint import pprint

API_KEY = 'cA6mUWcXb1zHfyVEKHZVTRCJAlc5rqszTM2VbPMboML-uyA4-KdxN3muANFzqD03XaZBkRJpPVNO-GVNRUEkA8DwcTnqTd3zCF4iC9Oo_bwFtw0ItWYvbFORyLCBXHYx'

argparser =argparse.ArgumentParser(description='coffee research')
arparser.add_argument()
                      type=str, help='Yelp Fusion API Key')
args = argparser.parse_args()

yelp_api = YelpAPI(API_KEY)

response = yelp_api.search_query(term='coffee', location='chicago, IL', sort_by='rating', limit=5)
pprint(response)