import os
import json
import logging
from json import JSONDecodeError
import datetime
import requests
from sqlalchemy import create_engine


def get_referral_info_from_qb(qb_user_token):
    appointments = []

    api_base_url = 'https://api.quickbase.com/v1/records/query'

    today = datetime.datetime.now()

    time_diff = datetime.timedelta(days=-14)

    two_weeks_ago = today - time_diff

    print(two_weeks_ago)

    params = {
        "from": "bck7gp3q2",
        "select": [
                88,
                89,
                90
            ],
        "where": "{87.GTE." + two_weeks_ago + "}OR{2.GTE." + two_weeks_ago + "}",
        "options": {
                "skip": 0
            }
    }

    headers = {
        'QB-Realm-Hostname': 'scs.quickbase.com',
        'Authorization': 'QB-USER-TOKEN ' + os.getenv('TESTINGAPIUSERTOKEN')
    }

    response = requests.post(api_base_url, headers=headers, json=params)
    print(response)

    return appointments

def main():
    get_referral_info_from_qb(os.getenv('TESTINGAPIUSERTOKEN'))

if __name__ == '__main__':
    get_referral_info_from_qb()




