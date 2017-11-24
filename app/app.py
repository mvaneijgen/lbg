#/usr/bin/env python
# -*- coding: utf-8 -*-
import csv, codecs, cStringIO
import locale
import os
import re
from collections import defaultdict
from decimal import *
from flask import Flask, render_template, request

app = Flask(__name__)

locale.setlocale(locale.LC_NUMERIC, 'nl_NL.UTF-8')


class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")


class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self


@app.route("/")
def main():
    return render_template('lbg.html')

if __name__ == "__main__":
    app.run(threaded=True)
