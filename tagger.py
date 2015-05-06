#!/usr/bin/env python

import os
import sys
import json
import pprint

from clarifai.client import ClarifaiApi
import clarifai.client.client

def main(argv):
  api = ClarifaiApi()
  pp = pprint.PrettyPrinter(indent=3)
  # terms = ["baseball","basketball","cricket"]
  # terms  =["football","soccer"]
  terms = ["tennis","hockey"]
  for term in terms:
    print("Fetching CNN tags for images of " + term)
    ec = 0
    f = open(term + '_12470504.txt', 'r')
    fo = open(term + '_12470504_out.txt','w')
    f.readline()
    f.readline()
    fo.write("Hashtags\tImage\tCNNTags\tCNNTagProbs\n\n")
    for line in f:
      data = line.split('\t')
      fo.write(data[0] + "\t")
      url = data[1].strip()
      fo.write(url + "\t")
      fo.write("\t")
      try:
        response = api.tag_image_urls(url)
        results = response['results']
        tags = []
        probs = []
        for result in results:
          tags  = result['result']['tag']['classes']
          probs = result['result']['tag']['probs']
        fo.write(','.join(tags) + "\t")
        fo.write(','.join(format(x, "1.5f") for x in probs) + "\n")
      except clarifai.client.client.ApiError:
        ec = ec + 1
        # print(sys.exc_info())
        # pp.pprint(all_info)
    f.close
    fo.close
    print("Completed fetching tags for term " + term + " " + str(ec) + " errors\n")

if __name__ == '__main__':
  main(sys.argv)