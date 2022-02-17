import json
import os
import sys

from suds.client import Client
from Utils.to_dict import recursive_dict
from Utils.console import clear_console

def get_appointment(client, CustomerKey, User, Password):
    AppointmentId = input("Enter the appointment id: ")
    term_size = os.get_terminal_size()
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetAppointmentReq ...", end="", flush=True)
        GetAppointmentReq = client.factory.create('GetAppointmentReq')
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: Appointment ...", end="", flush=True)
        GetAppointmentReq.RequestHeader['CustomerKey'] = CustomerKey
        GetAppointmentReq.RequestHeader['Password'] = Password
        GetAppointmentReq.RequestHeader['User'] = User
        GetAppointmentReq.Appointment['AppointmentId'] = 14
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service GetAppointment with the param GetAppointmentReq
        print("\n"+"Starting request: GetAppointment ...", end="", flush=True)
        try:
            response = client.service.GetAppointment(GetAppointmentReq)
            if (response['ErrorResponse']['IsError']):
                print('\033[31m', "(Fail)", '\033[0m')
                print("\n\033[31mError:\033[0m", response['ErrorResponse']['ErrorMessage'])
                print("\n\033[35mStackTrace:\033[0m\n", response['ErrorResponse']['StackTrace'])
            else:
                print('\033[32m', "(Ok)", '\033[0m')
                print("\n", response['Appointment'])
        except Exception as error:
            return error

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = json.loads(json.dumps(recursive_dict(response), indent=4))
        print('\033[32m', "(Ok)", '\033[0m')

        return result
    except Exception as error:
        return error

def get_appointments(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetAppointmentsReq ...", end="", flush=True)
        GetAppointmentsReq = client.factory.create('GetAppointmentsReq')
        print('\033[32m', "(Ok)", '\033[0m')

        print(GetAppointmentsReq)

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        GetAppointmentsReq.RequestHeader['CustomerKey'] = CustomerKey
        GetAppointmentsReq.RequestHeader['Password'] = Password
        GetAppointmentsReq.RequestHeader['User'] = User
        print('\033[32m', "(Ok)", '\033[0m')

        print("\n"+"Assigning the values to: Filter ...", end="", flush=True)
        GetAppointmentsReq.Filter['EndDate'] = "12/31/2021 8:30:00 PM"
        GetAppointmentsReq.Filter['PracticeName'] = "Intelligent Sleep with Renuma"
        GetAppointmentsReq.Filter['StartDate'] = "12/01/2021 4:00:00 AM"
        GetAppointmentsReq.Filter['TimeZoneOffsetFromGMT'] = "0"
        GetAppointmentsReq.Filter['Type'] = "Patient"
        print('\033[32m', "(Ok)", '\033[0m')

        print("\n"+"Assigning the values to: Fields ...", end="", flush=True)
        GetAppointmentsReq.Fields['AllDay'] = True
        GetAppointmentsReq.Fields['AppointmentReason1'] = True
        GetAppointmentsReq.Fields['ConfirmationStatus'] = True
        GetAppointmentsReq.Fields['CreatedDate'] = True
        GetAppointmentsReq.Fields['EndDate'] = True
        GetAppointmentsReq.Fields['ID'] = True
        GetAppointmentsReq.Fields['LastModifiedDate'] = True
        GetAppointmentsReq.Fields['Notes'] = True
        GetAppointmentsReq.Fields['PatientFullName'] = True
        GetAppointmentsReq.Fields['PatientID'] = True
        GetAppointmentsReq.Fields['PracticeID'] = True
        GetAppointmentsReq.Fields['PracticeName'] = True
        GetAppointmentsReq.Fields['Recurring'] = True
        GetAppointmentsReq.Fields['ResourceName1'] = True
        GetAppointmentsReq.Fields['ServiceLocationName'] = True
        GetAppointmentsReq.Fields['StartDate'] = True
        GetAppointmentsReq.Fields['Type'] = True
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service GetAppointments with the param GetAppointmentsReq
        print("\n"+"Starting request: GetAppointments ...", end="", flush=True)
        try:
            response = client.service.GetAppointments(GetAppointmentsReq)
            if (response['ErrorResponse']['IsError']):
                print('\033[31m', "(Fail)", '\033[0m')
                print("\n\033[31mError:\033[0m", response['ErrorResponse']['ErrorMessage'])
                print("\n\033[35mStackTrace:\033[0m\n", response['ErrorResponse']['StackTrace'])
            else:
                print('\033[32m', "(Ok)", '\033[0m')
                print("\n", response['Appointments'])
        except Exception as error:
            return error

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = json.loads(json.dumps(recursive_dict(response), indent=4))
        print('\033[32m', "(Ok)", '\033[0m')
        return result
    except Exception as error:
        return error

def get_patient(client, CustomerKey, User, Password):
    PatientId = input("Enter the patient id: ")
    term_size = os.get_terminal_size()
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetPatientReq ...", end="", flush=True)
        GetPatientReq = client.factory.create('GetPatientReq')
        print('\033[32m', "(Ok)", '\033[0m')

        print("GetPatientReq:", GetPatientReq)

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        GetPatientReq.RequestHeader['CustomerKey'] = CustomerKey
        GetPatientReq.RequestHeader['Password'] = Password
        GetPatientReq.RequestHeader['User'] = User        
        print('\033[32m', "(Ok)", '\033[0m')

        print("\n"+"Assigning the values to: Filter ...", end="", flush=True)
        GetPatientReq.Filter['PatientID'] = PatientId
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service GetPatient with the param GetPatientReq
        print("\n"+"Starting request: GetPatient ...", end="", flush=True)
        try:
            response = client.service.GetPatient(GetPatientReq)
            if (response['ErrorResponse']['IsError']):
                print('\033[31m', "(Fail)", '\033[0m')
                print("\n\033[31mError:\033[0m", response['ErrorResponse']['ErrorMessage'])
                print("\n\033[35mStackTrace:\033[0m\n", response['ErrorResponse']['StackTrace'])
            else:
                print('\033[32m', "(Ok)", '\033[0m')
                # print("\n", response)
        except Exception as error:
            return error

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = {}
        if response['Patient'] == None:
            print('\033[31m', "(Patient not exist)", '\033[0m')
        else:
            result = json.loads(json.dumps(recursive_dict(response), indent=4))
            print('\033[32m', "(Ok)", '\033[0m')
            print('\n', result)
        return result

    except Exception as error:
        return error

def get_patients(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetPatientsReq ...", end="", flush=True)
        GetPatientsReq = client.factory.create('GetPatientsReq')
        print('\033[32m', "(Ok)", '\033[0m')

        print("GetPatientsReq:", GetPatientsReq)

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        GetPatientsReq.RequestHeader['CustomerKey'] = CustomerKey
        GetPatientsReq.RequestHeader['Password'] = Password
        GetPatientsReq.RequestHeader['User'] = User        
        print('\033[32m', "(Ok)", '\033[0m')

        print("\n"+"Assigning the values to: Filter ...", end="", flush=True)
        GetPatientsReq.Filter['PracticeID'] = "1"
        print('\033[32m', "(Ok)", '\033[0m')

        print("\n"+"Assigning the values to: Fields ...", end="", flush=True)
        GetPatientsReq.Fields['EmailAddress'] = True
        GetPatientsReq.Fields['ID'] = True
        GetPatientsReq.Fields['PatientFullName'] = True
        GetPatientsReq.Fields['PracticeId'] = True
        GetPatientsReq.Fields['PracticeName'] = True
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service GetPatients with the param GetPatientsReq
        print("\n"+"Starting request: GetPatients ...", end="", flush=True)
        try:
            response = client.service.GetPatients(GetPatientsReq)
            if (response['ErrorResponse']['IsError']):
                print('\033[31m', "(Fail)", '\033[0m')
                print("\n\033[31mError:\033[0m", response['ErrorResponse']['ErrorMessage'])
                print("\n\033[35mStackTrace:\033[0m\n", response['ErrorResponse']['StackTrace'])
            else:
                print('\033[32m', "(Ok)", '\033[0m')
                # print("\n", response['Patients'])
        except Exception as error:
            return error

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = json.loads(json.dumps(recursive_dict(response), indent=4))
        print('\033[32m', "(Ok)", '\033[0m')
        return result

    except Exception as error:
        return error

def get_all_patients(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetAllPatientsReq ...", end="", flush=True)
        GetAllPatientsReq = client.factory.create('GetAllPatientsReq')
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        GetAllPatientsReq.RequestHeader['CustomerKey'] = CustomerKey
        GetAllPatientsReq.RequestHeader['Password'] = Password
        GetAllPatientsReq.RequestHeader['User'] = User
        print('\033[32m', "(Ok)", '\033[0m')

        print("\n"+"Assigning the values to: Filter ...", end="", flush=True)
        GetAllPatientsReq.Filter['PracticeID'] = "1"
        GetAllPatientsReq.Filter['StartKey'] = "0"
        print('\033[32m', "(Ok)", '\033[0m')

        print("\n"+"Assigning the values to: Fields ...", end="", flush=True)
        GetAllPatientsReq.Fields['EmailAddress'] = True
        GetAllPatientsReq.Fields['ID'] = True
        GetAllPatientsReq.Fields['PatientFullName'] = True
        GetAllPatientsReq.Fields['PracticeId'] = True
        GetAllPatientsReq.Fields['PracticeName'] = True
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service GetAllPatients with the param GetPatientsReq
        print("\n"+"Starting request: GetAllPatients ...", end="", flush=True)
        try:
            response = client.service.GetAllPatients(GetAllPatientsReq)
            if (response['ErrorResponse']['IsError']):
                print('\033[31m', "(Fail)", '\033[0m')
                print("\n\033[31mError:\033[0m", response['ErrorResponse']['ErrorMessage'])
                print("\n\033[35mStackTrace:\033[0m\n", response['ErrorResponse']['StackTrace'])
            else:
                print('\033[32m', "(Ok)", '\033[0m')
                print("\n", response['Patients'])
        except Exception as error:
            return error  

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = json.loads(json.dumps(recursive_dict(response), indent=4))
        print('\033[32m', "(Ok)", '\033[0m')
        return result
    except Exception as error:
        return error

def get_providers(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetProvidersReq ...", end="", flush=True)
        GetProvidersReq = client.factory.create('GetProvidersReq')
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        print(GetProvidersReq)

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        GetProvidersReq.RequestHeader['CustomerKey'] = CustomerKey
        GetProvidersReq.RequestHeader['Password'] = Password
        GetProvidersReq.RequestHeader['User'] = User
        print('\033[32m', "(Ok)", '\033[0m')

        print("\n"+"Assigning the values to: Filter ...", end="", flush=True)
        GetProvidersReq.Filter['PracticeID'] = "1"
        print('\033[32m', "(Ok)", '\033[0m')

        print("\n"+"Assigning the values to: Fields ...", end="", flush=True)
        GetProvidersReq.Fields['Active'] = True
        GetProvidersReq.Fields['EmailAddress'] = True
        GetProvidersReq.Fields['FullName'] = True
        GetProvidersReq.Fields['ID'] = True
        GetProvidersReq.Fields['PracticeID'] = True
        GetProvidersReq.Fields['PracticeName'] = True
        GetProvidersReq.Fields['Prefix'] = True
        GetProvidersReq.Fields['SpecialtyName'] = True
        GetProvidersReq.Fields['State'] = True
        GetProvidersReq.Fields['Type'] = True
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service GetProviders with the param GetPatientsReq
        print("\n"+"Starting request: GetProviders ...", end="", flush=True)
        try:
            response = client.service.GetProviders(GetProvidersReq)
            if (response['ErrorResponse']['IsError']):
                print('\033[31m', "(Fail)", '\033[0m')
                print("\n\033[31mError:\033[0m", response['ErrorResponse']['ErrorMessage'])
                print("\n\033[35mStackTrace:\033[0m\n", response['ErrorResponse']['StackTrace'])
            else:
                print('\033[32m', "(Ok)", '\033[0m')
                print("\n", response['Providers'])
        except Exception as error:
            return error  

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = json.loads(json.dumps(recursive_dict(response), indent=4))
        print('\033[32m', "(Ok)", '\033[0m')
        return result
    except Exception as error:
        return error
