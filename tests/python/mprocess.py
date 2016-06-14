#!/usr/bin/env python
# encoding: utf-8
'''
python mprocess.py -t 1 /Users/fengxuting/Downloads/test122.jpg

'''
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import time

def test(file):
    time.sleep(3)
    print(file)


def _poolcallback(results):
    fname, result, totaltime, size, message = results
    print(fname, result, sep="\t")


def main():
    import argparse
    import os
    import multiprocessing
    parser = argparse.ArgumentParser(description='Detect nudity in images.')
    parser.add_argument('files', metavar='image', nargs='+',
                        help='Images you wish to test')
    parser.add_argument('-t', '--threads', metavar='int', type=int, required=False, default=0,
                        help='The number of threads to start.')
    args = parser.parse_args()
    threadlist = []
    pool = multiprocessing.Pool(args.threads)
    for fname in args.files:
        if os.path.isfile(fname):
            threadlist.append(pool.apply_async(test, (fname,)))
        else:
            print(fname, "is not a file")
    pool.close()
    try:
        for t in threadlist:
            t.wait()
    except KeyboardInterrupt:
        pool.terminate()
        pool.join()


if __name__ == "__main__":
    main()
