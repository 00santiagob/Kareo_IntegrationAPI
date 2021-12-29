import json
import os
import sys
from datetime import datetime

from suds.client import Client
from Utils.to_dict import recursive_dict
from Utils.console import clear_console
import ipdb

def create_appointment(client, CustomerKey, User, Password):
    """
    create_appointment() does NOT check if the requested doctor is available 
    nor if there already are scheduled appointments in the given time.

    this endpoint must include the following information as described in its respective documentation:
        CustomerKey...........(ok)
        User..................(ok)
        Password..............(ok)
        PracticeId............(ok)
        ServiceLocationId ....(ok)
        AppointmentStatus.....(ok)
        StartTime.............(ok)
        EndTime...............(ok)
        PatientSummary........(ok)
        AppointmentType.......(ok)
        WasCreatedOnline......(ok)
        PatientId.............(ok)
    """

    term_size = os.get_terminal_size()
    print("\n")
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory and assign the values
        print("\n"+"Creating factory: AppointmentStatus ...", end="", flush=True)
        AppointmentStatus = client.factory.create('AppointmentStatus')
        print('\033[32m', "(Ok)", '\033[0m')

        #   Create a factory and assign the values
        print("\n"+"Creating factory: AppointmentType ...", end="", flush=True)
        AppointmentType = client.factory.create('AppointmentType')
        print('\033[32m', "(Ok)", '\033[0m')

        #   Create a factory and assign the values
        print("\n"+"Creating factory: PatientSummary ...", end="", flush=True)
        PatientSummary = client.factory.create('PatientSummary')
        print('\033[32m', "(Ok)", '\033[0m')
        #print("\n", PatientSummary)
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
        print("\n", PatientSummary)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Create a factory
        print("\n"+"Creating factory: CreateAppointmentReq ...", end="", flush=True)
        CreateAppointmentReq = client.factory.create('CreateAppointmentReq')
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", CreateAppointmentReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        CreateAppointmentReq.RequestHeader = {
                "CustomerKey" : CustomerKey,
                "Password" : Password,
                "User" : User
        }
        print('\033[32m', "(Ok)", '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: Appointment ...", end="", flush=True)
        startTime = datetime(2021, 12, 16, 14, 30, 00)
        endTime = datetime(2021, 12, 16, 15, 00, 00)
        CreateAppointmentReq.Appointment = {
                #"AppointmentId" : "",
                #"AppointmentName" : "Test Create Appointment",
                #"AppointmentReasonId" : None,
                "AppointmentStatus" : AppointmentStatus['Scheduled'],
                #"AppointmentStatus" : "Confirmed",
                "AppointmentType" : AppointmentType['P'],
                #"AppointmentUUID" : None,
                #"AttendeesCount" : None,
                #"CreatedAt" : None,
                #"CreatedBy" : None,
                #"CustomerId" : None,
                "EndTime" : endTime,
                "ForRecare" : False,
                "InsurancePolicyAuthorizationId" : 1,
                "IsDeleted" : False,
                "IsGroupAppointment" : False,
                "IsRecurring" : False,
                #"MaxAttendees" : "1",
                "Notes" : "This is an example note from your doctor",
                #"OccurrenceId" : None,
                #"PatientCaseId" : None,
                "PatientSummaries" : None, #ArrayOfGroupPatientSummary,
                "PatientSummary" : PatientSummary,
                "PracticeId" : 1,
                "ProviderId" : 1,
                #"RecurrenceRule" : None,
                #"ResourceId" : None,
                #"ResourceIds" : None,
                "ServiceLocationId" : 1,
                "StartTime" : startTime,
                #"UpdatedAt" : None,
                #"UpdatedBy" : None,
                "WasCreatedOnline" : True
        }
        print('\033[32m', "(Ok)", '\033[0m')

        #   Factory ready for use
        print("\n", CreateAppointmentReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')
        #   Call the service CreateAppointment with the param CreateAppointmentReq
        print("\n"+"Starting request: CreateAppointment ...", end="", flush=True)
        try:
            response = client.service.CreateAppointment(CreateAppointmentReq)
            print('\033[32m', "(Ok)", '\033[0m')
            print("\n", response)
            print('\033[33m'+'=' * term_size.columns + '\033[0m')
        except Exception as error:
            print("error:",error)

        #   Create result of the response
        print("\n"+"Createting result of the response ...", end="", flush=True)
        result = json.dumps(recursive_dict(response), indent=4)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\nResult:", result)

        return result
    except Exception as error:
        return error

def create_patient(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    try:
        # Create a factory
        print("\n"+"Creating factory: CreatePatientReq ...", end="", flush=True)
        CreatePatientReq = client.factory.create('CreatePatientReq')
        print('\033[32m', "(Ok)", '\033[0m')

        # Assign values to factory
        print("\n"+"Assigning the values to: CreatePatientReq ...", end="", flush=True)
        CreatePatientReq.RequestHeader = {
            "CustomerKey" : CustomerKey,
            "Password" : Password,
            "User" : User
        }

        CreatePatientReq.Patient['FirstName'] = "Leonardo"
        CreatePatientReq.Patient['LastName'] = "Amato"
        CreatePatientReq.Patient['EmailAddress'] = "lamato@liricus.com.ar"
        CreatePatientReq.Patient['Guarantor']['RelationshiptoGuarantor']['value'] = "Other"
        CreatePatientReq.Patient['Gender']['value'] = "Male"
        CreatePatientReq.Patient['Practice']['PracticeID'] = 1
        CreatePatientReq.Patient['Practice']['PracticeName'] = "DEV" 

        print('\033[32m', "(Ok)", '\033[0m')

        # Start request
        print("\n"+"Starting request: CreatePatientReq ...", end="", flush=True)
        CreatePatientRes = client.service.CreatePatient(CreatePatientReq)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\nResult:", CreatePatientRes)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

    except Exception as error:
        print("\nerror:\n",error)
        response = {"ERROR": "CHAOS AND DESTRUCTION"}
        print(response['ERROR'])
