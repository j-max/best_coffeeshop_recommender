
def add_to_shop_dict(response, coffee_shop_dict):
    for yelp_shop in response['businesses']:
        try:
            try:
                coffee_shop_dict[yelp_shop['id']] = (yelp_shop['alias'],
                                                     yelp_shop['is_closed'],
                                                    (yelp_shop['coordinates']['latitude']),
                                                    (yelp_shop['coordinates']['longitude']),
                                                    (yelp_shop['location']['display_address'][0]+', ' + yelp_shop['location']['display_address'][1]),
                                                    (yelp_shop['location']['address1']),
                                                    (yelp_shop['location']['zip_code']),
                                                    yelp_shop['price'],
                                                    yelp_shop['rating'],
                                                    yelp_shop['review_count'])
            except:
                coffee_shop_dict[yelp_shop['id']] = (yelp_shop['alias'],
                                                     yelp_shop['is_closed'],
                                                    (yelp_shop['coordinates']['latitude']),
                                                    (yelp_shop['coordinates']['longitude']),
                                                    (yelp_shop['location']['display_address'][0]+', ' + yelp_shop['location']['display_address'][1]),
                                                    (yelp_shop['location']['address1']),
                                                    (yelp_shop['location']['zip_code']),
                                                    'no_price',
                                                    yelp_shop['rating'],
                                                    yelp_shop['review_count'])
        except:
            print(yelp_shop['alias'])
            print('did not work')
            pass


