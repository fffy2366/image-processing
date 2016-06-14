#!/usr/bin/env bash
convert $1 -colorspace Gray ocr.tif
tesseract ocr.tif $1
gedit $1.txt