#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
import datetime

from thehive4py.api import TheHiveApi
from thehive4py.query import *

### variables ###
api_key = ""
url = "http://[URL]:9000"
json_path = "incidents_{}.json".format(str(datetime.date.today()).replace("-", "_"))

query = {}

def main():
    api = TheHiveApi(url, api_key)
    cases = api.find_cases(range="all")
    cases = cases.json()

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(cases, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    print("[INFO] Starting the script...")
    main()
    print("[INFO] No errors found. Output file generated successfully")
    print("[INFO] Program terminated. Exiting...")
