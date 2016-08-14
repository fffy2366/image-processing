# -*- coding: utf-8 -*-

"""Evaluate m-file and collect the results.  A simple MATLAB script is
located in my_script.m

"""
from __future__ import division, print_function, absolute_import
from __future__ import unicode_literals

import matlab_wrapper

IMAGE_DIR = "public/uploads/api/"
def main():
    matlab = matlab_wrapper.MatlabSession()

    matlab.put('filename', "f078bf00-4bf3-11e6-aefd-4f827560e966.png")
    matlab.put('IMAGE_DIR', IMAGE_DIR)
    matlab.eval('face')

    print("And the winner is:")
    count = matlab.get('count')

    has_crop = matlab.get('has_crop')
    print(count)
    print(has_crop)


if __name__ == "__main__":
    main()
