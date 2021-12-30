import json
import os
import sys
from datetime import datetime

from suds.client import Client
from Utils.to_dict import recursive_dict
from Utils.console import clear_console
import ipdb

def create_appointment(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
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
        print("\n"+"Creating factory: CreateAppointmentReq ...", end="", flush=True)
        CreateAppointmentReq = client.factory.create('CreateAppointmentReq')
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        CreateAppointmentReq.RequestHeader['CustomerKey'] = CustomerKey
        CreateAppointmentReq.RequestHeader['Password'] = Password
        CreateAppointmentReq.RequestHeader['User'] = User
        print('\033[32m', "(Ok)", '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: Appointment ...", end="", flush=True)
        CreateAppointmentReq.Appointment['AppointmentStatus'] = AppointmentStatus['Scheduled']
        CreateAppointmentReq.Appointment['AppointmentType'] = AppointmentType['P']
        CreateAppointmentReq.Appointment['EndTime'] = datetime(2021, 12, 16, 15, 00, 00)
        CreateAppointmentReq.Appointment['ForRecare'] = False
        CreateAppointmentReq.Appointment['InsurancePolicyAuthorizationId'] = 1
        CreateAppointmentReq.Appointment['IsDeleted'] = False
        CreateAppointmentReq.Appointment['IsGroupAppointment'] = False
        CreateAppointmentReq.Appointment['IsRecurring'] = False
        CreateAppointmentReq.Appointment['Notes'] = "This is an example note from your doctor",
        CreateAppointmentReq.Appointment['PatientSummaries'] = None
        CreateAppointmentReq.Appointment['PracticeId'] = 1
        CreateAppointmentReq.Appointment['ProviderId'] = 1
        CreateAppointmentReq.Appointment['ServiceLocationId'] = 1
        CreateAppointmentReq.Appointment['StartTime'] = datetime(2021, 12, 16, 14, 30, 00)
        CreateAppointmentReq.Appointment['WasCreatedOnline'] = True
        CreateAppointmentReq.Appointment['PatientSummary']['PatientId'] = 5
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service CreateAppointment with the param CreateAppointmentReq
        print("\n"+"Starting request: CreateAppointment ...", end="", flush=True)
        try:
            response = client.service.CreateAppointment(CreateAppointmentReq)
            print('\033[32m', "(Ok)", '\033[0m')
            if (response['ErrorResponse']['IsError']):
                print(response['ErrorResponse']['ErrorMessage'])
            else:
                print("\n", response['Appointment'])
        except Exception as error:
            print("error:",error)

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Create result of the response
        print("\n"+"Createting result of the response ...", end="", flush=True)
        result = json.dumps(recursive_dict(response), indent=4)
        print('\033[32m', "(Ok)", '\033[0m')

        return result
    except Exception as error:
        return error

def create_patient(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        # Create a factory
        print("\n"+"Creating factory: CreatePatientReq ...", end="", flush=True)
        CreatePatientReq = client.factory.create('CreatePatientReq')
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        # Assign values to factory
        print("\n"+"Assigning the values to: CreatePatientReq ...", end="", flush=True)
        CreatePatientReq.RequestHeader['CustomerKey'] = CustomerKey
        CreatePatientReq.RequestHeader['Password'] = Password
        CreatePatientReq.RequestHeader['User'] = User

        CreatePatientReq.Patient['FirstName'] = "Leonardo"
        CreatePatientReq.Patient['LastName'] = "Amato"
        CreatePatientReq.Patient['EmailAddress'] = "lamato@liricus.com.ar"
        CreatePatientReq.Patient['Guarantor']['RelationshiptoGuarantor']['value'] = "Other"
        CreatePatientReq.Patient['Gender']['value'] = "Male"
        CreatePatientReq.Patient['Practice']['PracticeID'] = 1
        CreatePatientReq.Patient['Practice']['PracticeName'] = "DEV" 
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        # Start request
        print("\n"+"Starting request: CreatePatientReq ...", end="", flush=True)
        try:
            response = client.service.CreatePatient(CreatePatientReq)
            print('\033[32m', "(Ok)", '\033[0m')
            if (response['ErrorResponse']['IsError']):
                print(response['ErrorResponse']['ErrorMessage'])
            else:
                print("\n", response['SecurityResponse'])
            print('\033[33m'+'=' * term_size.columns + '\033[0m')
        except Exception as error:
            print("\nerror:\n",error)        
    except Exception as error:
        print("\nerror:\n",error)
        response = {"ERROR": "CHAOS AND DESTRUCTION"}
        print(response['ERROR'])
