#! python3

"""Utils.py: Common helper functions"""
import sys
import json
import string
import time


def check_response(response):
    if response is None:
        print_err("Error! Response is empty")
        return None
    status_code = response["ResponseMetadata"]["HTTPStatusCode"]
    if status_code not in [200, 201, 202, 204]:
        print_err("Error! Unexpected status code %d" % status_code)
        return None
    return response


def print_err(*args):
    print(*args, file=sys.stderr)


def dump_json(obj):
    print(json.dumps(obj, indent=2, default=str))


def poll_state(poll_func, poll_arg, retry_count: int, retry_wait: int, expected_state: string, poll_name="Poll"):
    tries = retry_count
    while tries > 0:
        result = poll_func(poll_arg)
        if result is None:
            print("Error polling %s" % poll_name)
            return False
        if result == expected_state:
            print("%s complete" % poll_name)
            return True
        print("%s is %s. Waiting for %s" % (poll_name, result, expected_state))
        time.sleep(retry_wait)
        tries -= 1
    print("Giving up poll for %s" % poll_name)
    return False
