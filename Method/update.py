import json
import os
import sys
import datetime

from suds.client import Client
from Utils.to_dict import recursive_dict
from Utils.console import clear_console

#         UpdateAppointment( npdateAppointmentReq )
def update_appointment(client, CustomerKey, User, Password):

    """
   this endpoint must include the following information as described in its respective documentation:
      CustomerKey...........(ok)
      User..................(ok)
      Password..............(ok)
      AppointmentId.........
      AppointmentStatus.....(ok)
      ServiceLocationId ....
      StartTime.............
      EndTime...............
      AppointmentReasonId...
      ResourceId............
      PatientId.............(ok)
      AppointmentName.......
      MaxAttendees..........
   """

    term_size = os.get_terminal_size()
    print("\n")
    print('\033[33m'+'=' * term_size.columns + '\033[0m')
 
    try:
                #   Create a factory and assign the values. You can also parse this argument as strings 
        print("\n"+"Creating factory: AppointmentStatus ...", end="", flush=True)
        AppointmentStatus = client.factory.create('AppointmentStatus')
        print('\033[32m', "(Ok)", '\033[0m')

                #   Create a factory and assign the values
        """
        print("\n"+"Creating factory: PatientSummary ...", end="", flush=True)
        PatientSummary = client.factory.create('PatientSummary')
        print('\033[32m', "(Ok)", '\033[0m')

        print("\n"+"Assigning the values to: PatientSummary ...", end="", flush=True)
        dateOfBirth = datetime(1998,7,20) #YYYY-MM-DD HH:mm:ss
        PatientSummary = {
                "DateOfBirth" : dateOfBirth,    
                "Email" : "sbalog@elementoarg.io",
                "FirstName" : "Santiago",
                #"GenderId" : "1",
                #"HomePhone" : None,
                "LastName" : "Balog",
                "MiddleName" : "Alberto",
                #"MobilePhone" : "3518056090",
                #"OtherEmail" : "santiagobalog1998@gmail.com",
                #"OtherPhone" : None,
                "PatientId" : 3,
                "PracticeId" : 1
                #"PreferredEmailType" : "HOME",
                #"PreferredPhoneType" : None,
                #"WorkEmail" : None,
                #"WorkPhone" : None
        }
        print('\033[32m', "(Ok)", '\033[0m')
        """
        #   Create a factory
        print("\n"+"Creating factory: UpdateAppointmentReq ...", end="", flush=True)
        UpdateAppointmentReq = client.factory.create('UpdateAppointmentReq')
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", UpdateAppointmentReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        UpdateAppointmentReq.RequestHeader = {
                "CustomerKey" : CustomerKey,
                "Password" : Password,
                "User" : User
        }
        print('\033[32m', "(Ok)", '\033[0m')

        print("\n", UpdateAppointmentReq)



    except Exception as error:
        return error

def update_patient(client, CustomerKey, User, Password):
    try:
        print('\033[43m', '\033[30m', '\033[01m', "Service temporarily unavailable", '\033[0m')
    except Exception as error:
        return error
