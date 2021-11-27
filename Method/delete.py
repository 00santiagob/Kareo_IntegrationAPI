import json
import os
import sys

from suds.client import Client
from Utils.to_dict import recursive_dict
from Utils.console import clear_console

def delete_appointment(client, CustomerKey, User, Password):
    try:
        print('\033[43m', '\033[30m', '\033[01m', "Service temporarily unavailable", '\033[0m')
    except Exception as error:
        return error
