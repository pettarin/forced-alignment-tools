#!/usr/bin/env python
# coding=utf-8

"""
Format data from JSON to GitHub Markdown.
"""

from __future__ import absolute_import
from __future__ import print_function
import io
import json
import os
import sys

__author__ = "Alberto Pettarin"
__email__ = "alberto@albertopettarin.it"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__status__ = "Production"
__version__ = "1.0.0"


def read_data(data_file_path):
    """ Read data from JSON file """
    with io.open(data_file_path, "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    return data


def patch_template(template_file_path, pairs, output_file_path):
    """ Inject data into a Markdown template """
    with io.open(template_file_path, "r", encoding="utf-8") as f:
        template = f.read()
    for key, contents in pairs:
        template = template.replace(u"{{ %s }}" % key, contents)
    with io.open(output_file_path, "w", encoding="utf-8") as f:
        f.write(template)


def format_data(d):
    """ Format data into string """
    def format_table(d):
        """ Format table """
        # string accumulator
        acc = []

        # from JSON we have a list, not a tuple
        fields = [tuple(h) for h in d["header"] if h[0] != u"url"]
        fields_keys = [f[0] for f in fields]

        # create header
        h1 = u"|"
        h2 = u"|"
        for k, n in fields:
            h1 += " %s |" % n
            h2 += " %s |" % (u"-" * len(n))
        acc.append(h1)
        acc.append(h2)

        # create rows
        for r in d["rows"]:
            s = u"|"
            for k in fields_keys:
                v = u""
                if k == "name":
                    v = u"[%s](%s)" % (r[k], r["url"])
                else:
                    v = r[k]
                s += u" %s |" % v
            acc.append(s)

        # return string
        s = u"\n".join(acc)
        return s

    def format_list(d):
        """ Format list """
        acc = []
        for r in d["rows"]:
            s = u""
            if ("abbr" in r) and (len(r["abbr"]) > 0):
                s += u"%s: " % r["abbr"]
            if ("text" in r) and (len(r["text"]) > 0):
                if ("url" in r) and (len(r["url"]) > 0):
                    s += u"[%s](%s)" % (r["text"], r["url"])
                else:
                    s += r["text"]
            if ("notes" in r) and (len(r["notes"]) > 0):
                s += u" (%s)" % r["notes"]
            if len(s) > 0:
                acc.append("* %s" % s)
        acc = sorted(acc)
        return u"\n".join(acc)

    if "type" not in d:
        raise TypeError(u"Unable to determine the type of data")
    if d["type"] == "table":
        return format_table(d)
    if d["type"] == "list":
        return format_list(d)
    raise ValueError(u"Unable to process type '%s'" % d["type"])


def main():
    """ Replace data from JSON file into template and output to Markdown file """
    data_file_path = "data.json"
    template_file_path = "README.template"
    output_file_path = "README.md"

    data = read_data(data_file_path)
    pairs = [(k, format_data(v)) for k, v in data.items()]
    patch_template(template_file_path, pairs, output_file_path)


if __name__ == "__main__":
    main()
