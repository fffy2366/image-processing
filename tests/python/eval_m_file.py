# -*- coding: utf-8 -*-

"""Evaluate m-file and collect the results.  A simple MATLAB script is
located in my_script.m

"""
from __future__ import division, print_function, absolute_import
from __future__ import unicode_literals

import matlab_wrapper


def main():
    matlab = matlab_wrapper.MatlabSession()

    matlab.put('x', 2.)
    matlab.eval('face')
    y = matlab.get('y')

    print("And the winner is:", y)
    for i in y:
        print(int(i))


if __name__ == "__main__":
    main()
