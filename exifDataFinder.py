'''
program rips exif data from jpegs
'''

import string,sys,os
from PIL import Image
from PIL.ExifTags import TAGS

path_to_jpegs = '/Users/antigen/Pictures/'

for root, dir, files in os.walk('path_to_jpegs'):
    print root
    print dir
    print files
    for targets in files:
        if ".JPG" in targets.upper():
            fn = root + targets
            try:
                i = Image.open(fn)
                info = i._getexif()
                exif = {}
                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    exif[decoded] = value

                exifGPS = exif['GPSInfo']
                latData = exifGPS[2]
                lonData = exifGPS[4]

                latDeg = latData[0][0] / float(latData[0][1])
                latMin = latData[1][0] / float(latData[1][1])
                latSec = latData[2][0] / float(latData[2][1])
                                
                lonDeg = lonData[0][0] / float(lonData[0][1])
                lonMin = latData[2][0] / float(latData[1][1])
                lonSec = lonData[2][0] / float(lonData[2][1])

                lat_final = (latDeg + (latMin + latSec/60.0)/60.0)
                lon_final = (lonDeg + (lonMin + lonSec/60.0)/60.0)

            except:
                pass
