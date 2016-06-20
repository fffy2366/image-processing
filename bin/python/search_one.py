# author: Adrian Rosebrock
# date: 27 January 2014
# website: http://www.pyimagesearch.com

# USAGE
# python search_external.py --dataset ../../public/uploads/similar --index ../../public/uploads/similar.cpickle --query 1464317727202AD22DC2.jpg

# import the necessary packages
from pyimagesearch.rgbhistogram import RGBHistogram
from pyimagesearch.searcher import Searcher
import numpy as np
import argparse
import cPickle
import cv2
import time
from pyimagesearch import logger
from models.similar_images import SimilarImages
import sys

conf = logger.Logger()

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
                help="Path to the directory that contains the images we just indexed")
ap.add_argument("-i", "--index", required=True,
                help="Path to where we stored our index")
ap.add_argument("-q", "--query", required=True,
                help="Path to query image")
args = vars(ap.parse_args())
# print 'start waiting:', time.strftime('%H:%M:%S'),'\n<br/>'

# load the query image and show it
queryImage = cv2.imread(args["dataset"]+"/"+args["query"])
# cv2.imshow("Query", queryImage)

# print "query: %s" % (args["query"]),'\n<br/>'

# describe the query in the same way that we did in
# index.py -- a 3D RGB histogram with 8 bins per
# channel
desc = RGBHistogram([8, 8, 8])
queryFeatures = desc.describe(queryImage)

# load the index perform the search
#index = cPickle.loads(open(args["index"]).read())
s = SimilarImages()

_index = s.findAll()
index = {}
for i in _index:
    features =  i.get('features')
    # print cPickle.loads(features)
    # print cPickle.load(i.get('features'))
    index[i.get('name')] = cPickle.loads(features)
# sys.exit(0) ;
searcher = Searcher(index)
results = searcher.search(queryFeatures)

# initialize the two montages to display our results --
# we have a total of 25 images in the index, but let's only
# display the top 10 results; 5 images per montage, with
# images that are 400x166 pixels


# loop over the top ten results
for j in xrange(0, 50):
    # grab the result (we are using row-major order) and
    # load the result image
    (score, imageName) = results[j]
    if(score>0.01):
        break
    if(imageName==args["query"]):
        continue
    path = args["dataset"] + "/%s" % (imageName)


    print "\t%d. %s : %.3f" % (j + 1, imageName, score),'\n<br/>'  # check to see if the first montage should be used


# print 'stop waiting', time.strftime('%H:%M:%S'),'\n<br/>'
