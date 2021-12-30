import json
import os
import sys

from suds.client import Client
from Utils.to_dict import recursive_dict
from Utils.console import clear_console

def delete_appointment(client, CustomerKey, User, Password):
    AppointmentId = input("Enter the appointment id: ")
    term_size = os.get_terminal_size()
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: DeleteAppointmentReq ...", end="", flush=True)
        DeleteAppointmentReq = client.factory.create('DeleteAppointmentReq')
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: Appointment ...", end="", flush=True)
        DeleteAppointmentReq.RequestHeader['CustomerKey'] = CustomerKey
        DeleteAppointmentReq.RequestHeader['Password'] = Password
        DeleteAppointmentReq.RequestHeader['User'] = User
        DeleteAppointmentReq.Appointment['AppointmentId'] = AppointmentId
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service DeleteAppointment with the param DeleteAppointmentReq
        print("\n"+"Starting request: DeleteAppointment ...", end="", flush=True)
        try:
            response = client.service.DeleteAppointment(DeleteAppointmentReq)
            if (response['ErrorResponse']['IsError']):
                print('\033[31m', "(Fail)", '\033[0m')
                print("\n\033[31mError:\033[0m", response['ErrorResponse']['ErrorMessage'])
                print("\n\033[35mStackTrace:\033[0m\n", response['ErrorResponse']['StackTrace'])
            else:
                print('\033[32m', "(Ok)", '\033[0m')
        except Exception as error:
            return error

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = recursive_dict(response)
        print('\033[32m', "(Ok)", '\033[0m')
        if result['ErrorResponse']['IsError'] == "True":

            result['ErrorResponse']['ErrorMessage'] = "Not exist appointment with id " + AppointmentId
            result['ErrorResponse']['StackTrace'] = ""
            result['AppointmentId'] = AppointmentId
        else:
            result = json.dumps(result, indent=4)

        print("\n", result)
        return result
    except Exception as error:
        return error
