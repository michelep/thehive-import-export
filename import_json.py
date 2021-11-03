#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
import datetime

from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CaseTask, CustomFieldHelper

### variables ###
api_key = ""
url = "http://[URL]:9000"

json_path="incidents.json"

def main():
    api = TheHiveApi(url, api_key)

    with open(json_path, 'r', encoding='utf-8') as f:
        cases = json.load(f)

    for case in cases:
        print('Create Case')
        print('-----------------------------')
        new_case = Case(
            title=case['title'],
            tlp=case['tlp'],
            pap=case['pap'],
            flag=case['flag'],
            tags=case['tags'],
            description=case['description'],
            startDate=case['startDate']
        )

        id = None
        response = api.create_case(new_case)
        if response.status_code == 201:
            print(json.dumps(response.json(), indent=4, sort_keys=True))
            print('')
            id = response.json()['id']
        else:
            print('ko: {}/{}'.format(response.status_code, response.text))
            sys.exit(0)

if __name__ == "__main__":
    main()
