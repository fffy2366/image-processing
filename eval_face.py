# -*- coding: utf-8 -*-

"""Evaluate m-file and collect the results.  A simple MATLAB script is
located in my_script.m

"""
from __future__ import division, print_function, absolute_import
from __future__ import unicode_literals

import matlab_wrapper
import sys

IMAGE_DIR = "public/uploads/api/"
def main():
    matlab = matlab_wrapper.MatlabSession()

    matlab.put('filename', sys.argv[1])
    matlab.put('IMAGE_DIR', IMAGE_DIR)
    matlab.eval('face')

    print("And the winner is:")
    count = matlab.get('count')

    has_crop = matlab.get('has_crop')
    print(int(count))
    print(int(has_crop)==1)


if __name__ == "__main__":
    main()
