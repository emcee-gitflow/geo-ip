#!/usr/bin/env python3.8

""" Geo-locate IP (w/ optional IPv4 CLI argument) """

import re
import requests
import sys
from xml.etree import ElementTree

url = "https://freegeoip.app/xml/"
ip4 = re.compile(r"\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}"
                 r"(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b")

if ip := ip4.match(sys.argv[-1]):
    url += ip.group()

xml = ElementTree.fromstring(requests.get(url).content)

for cell in xml:
    print(f"{cell.tag}: {cell.text}")
