# author: Adrian Rosebrock
# date: 27 January 2014
# website: http://www.pyimagesearch.com

# USAGE
# python search_index_one.py --dataset ../../public/uploads/similar --index ../../public/uploads/similar.cpickle --file 1464318452058AFC4E73.jpg

# import the necessary packages
from pyimagesearch.rgbhistogram import RGBHistogram
import argparse
import cPickle
import glob
import cv2
import os
import sys
import datetime
from models.similar_images import SimilarImages

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,
                help="The file to be indexed")
ap.add_argument("-d", "--dataset", required=True,
                help="Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required=True,
                help="Path to where the computed index will be stored")
args = vars(ap.parse_args())




# initialize the index dictionary to store our our quantifed
# images, with the 'key' of the dictionary being the image
# filename and the 'value' our computed features

# if(os.path.isfile(args["index"])):
#
#     index = cPickle.loads(open(args["index"]).read())
#     if(index.has_key(args["file"])):
#         print "has exist"
#         sys.exit(0)
s = SimilarImages()
i = s.findByName(args["file"])
if(i!=None):
    print "has exist"
    sys.exit(0)

index = {}

# initialize our image descriptor -- a 3D RGB histogram with
# 8 bins per channel
desc = RGBHistogram([8, 8, 8])



# load the image, describe it using our RGB histogram
# descriptor, and update the index
image = cv2.imread(args["dataset"] +"/"+ args["file"])
features = desc.describe(image)
index[args["file"]] = features

# we are now done indexing our image -- now we can write our
# index to disk



s.insert({'name':args["file"],'features':cPickle.dumps(features),'created_at':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
# f = open(args["index"], "a")
# f.write(cPickle.dumps(index))
# f.close()

# show how many images we indexed
#index = cPickle.loads(open(args["index"]).read())
print "done...add indexed %d images" % (len(index))
