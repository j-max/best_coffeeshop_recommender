import pandas as pd
import re

def make_block_dict(census_blocks_df = pd.read_csv('../block_shapes/CensusBlockTIGER2010.csv')):
    block_dict = {}
    for index, row in census_blocks_df.iterrows():
        block_coord = row['the_geom'].split(" ")
        lat_pat = re.compile('[^-\d][\d]+[.][\d]+')
        lats = lat_pat.findall(str(block_coord))
        long_pat = re.compile('[-][\d]+[.][\d]+')
        longs = long_pat.findall(str(block_coord))
        float_lats = [float(x[1:]) for x in lats]
        avg_lat = sum(float_lats)/len(float_lats)
        float_longs = [float(x) for x in longs]
        avg_long = sum(float_longs)/len(float_longs)

        block_dict[row['TRACT_BLOC']] = [avg_lat, avg_long]

    return block_dict