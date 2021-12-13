import json
import os
import sys

from suds.client import Client
from Utils.to_dict import recursive_dict
from Utils.console import clear_console

def create_appointment(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print("\n")
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory and assign the values
        print("\n"+"Creating factory: AppointmentStatus ...", end="", flush=True)
        AppointmentStatus = client.factory.create('AppointmentStatus')
        print('\033[32m', "(Ok)", '\033[0m')
        #print("\n", AppointmentStatus)
        #print("\n"+"Assigning the values to: AppointmentStatus ...", end="", flush=True)
        #AppointmentStatus = {
        #    "value" : AppointmentStatus['Scheduled']
        #}
        #print('\033[32m', "(Ok)", '\033[0m')
        #print("\n", AppointmentStatus)
        #print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Create a factory and assign the values
        print("\n"+"Creating factory: AppointmentType ...", end="", flush=True)
        AppointmentType = client.factory.create('AppointmentType')
        print('\033[32m', "(Ok)", '\033[0m')
        #print("\n", AppointmentType)
        #print("\n"+"Assigning the values to: AppointmentType ...", end="", flush=True)
        #AppointmentType = {
        #    "value" : AppointmentType['P']
        #}
        #print('\033[32m', "(Ok)", '\033[0m')
        #print("\n", AppointmentType)
        #print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Create a factory and assign the values
        print("\n"+"Creating factory: ArrayOfGroupPatientSummary ...", end="", flush=True)
        ArrayOfGroupPatientSummary = client.factory.create('ArrayOfGroupPatientSummary')
        print('\033[32m', "(Ok)", '\033[0m')

        #   Create a factory and assign the values
        print("\n"+"Creating factory: PatientSummary ...", end="", flush=True)
        PatientSummary = client.factory.create('PatientSummary')
        print('\033[32m', "(Ok)", '\033[0m')
        #print("\n", PatientSummary)
        print("\n"+"Assigning the values to: PatientSummary ...", end="", flush=True)
        PatientSummary = {
            "DateOfBirth" : "1998-07-20 03:00:00+00:00",    #YYYY-MM-DD HH:mm:ss
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
        #print("\n", PatientSummary)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #print("\n"+"Creating factory: AppointmentCreate ...", end="", flush=True)
        #AppointmentCreate = client.factory.create('AppointmentCreate')
        #print('\033[32m', "(Ok)", '\033[0m')
        #print("\n", AppointmentCreate)
        #print('\033[33m'+'=' * term_size.columns + '\033[0m')

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
        CreateAppointmentReq.Appointment = {
            #"AppointmentId" : "",
            #"AppointmentName" : "Test Create Appointment",
            #"AppointmentReasonId" : None,
            "AppointmentStatus" : AppointmentStatus['Scheduled'],
            "AppointmentType" : AppointmentType['P'],
            #"AppointmentUUID" : None,
            #"AttendeesCount" : None,
            #"CreatedAt" : None,
            #"CreatedBy" : None,
            #"CustomerId" : None,
            "EndTime" : "2021-12-03 13:30:00 PM",
            #"ForRecare" : False,
            #"InsurancePolicyAuthorizationId" : None,
            #"IsDeleted" : False,
            #"IsGroupAppointment" : False,
            #"IsRecurring" : False,
            #"MaxAttendees" : "1",
            "Notes" : "This is a test note for the Doctor",
            #"OccurrenceId" : None,
            #"PatientCaseId" : None,
            "PatientSummaries" : "None", #ArrayOfGroupPatientSummary,
            "PatientSummary" : PatientSummary,
            "PracticeId" : 1,
            "ProviderId" : 1,
            #"RecurrenceRule" : None,
            #"ResourceId" : None,
            #"ResourceIds" : None,
            "ServiceLocationId" : 1,
            "StartTime" : "2021-12-03 13:00:00 PM",
            #"UpdatedAt" : None,
            #"UpdatedBy" : None,
            #"WasCreatedOnline" : True
        }
        print('\033[32m', "(Ok)", '\033[0m')

        #   Factory ready for use
        print("\n", CreateAppointmentReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service CreateAppointment with the param CreateAppointmentReq
        print("\n"+"Starting request: CreateAppointment ...", end="", flush=True)
        response = client.service.CreateAppointment(CreateAppointmentReq)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", response)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')
    except Exception as error:
        return error

def create_patient(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print("\n")
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: CreatePatientReq ...", end="", flush=True)
        CreatePatientReq = client.factory.create('CreatePatientReq')
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", CreatePatientReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        CreatePatientReq.RequestHeader = {
            "CustomerKey" : CustomerKey,
            "Password" : Password,
            "User" : User
        }
        print('\033[32m', "(Ok)", '\033[0m')
    except Exception as error:
        return error