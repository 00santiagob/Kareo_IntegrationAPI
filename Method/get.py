import json
import os
import sys

from suds.client import Client
from Utils.to_dict import recursive_dict
from Utils.console import clear_console

def get_appointment(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print("\n")
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetAppointmentReq ...", end="", flush=True)
        GetAppointmentReq = client.factory.create('GetAppointmentReq')
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", GetAppointmentReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        GetAppointmentReq.RequestHeader = {
            "CustomerKey" : CustomerKey,
            "Password" : Password,
            "User" : User
        }
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n"+"Assigning the values to: Appointment ...", end="", flush=True)
        GetAppointmentReq.Appointment = {
            "AppointmentId" : ""
        }
        print('\033[32m', "(Ok)", '\033[0m')

        #   Factory ready for use
        print("\n", GetAppointmentReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service GetAppointment with the param GetAppointmentReq
        print("\n"+"Starting request: GetAppointment ...", end="", flush=True)
        response = client.service.GetAppointment(GetAppointmentReq)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", response)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = json.dumps(recursive_dict(response), indent=4)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\nResult:", result)

        return result
    except Exception as error:
        return error

def get_appointments(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print("\n")
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetAppointmentsReq ...", end="", flush=True)
        GetAppointmentsReq = client.factory.create('GetAppointmentsReq')
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", GetAppointmentsReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        GetAppointmentsReq.RequestHeader = {
            "CustomerKey" : CustomerKey,
            "Password" : Password,
            "User" : User
        }
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n"+"Assigning the values to: Filter ...", end="", flush=True)
        GetAppointmentsReq.Filter = {
            #"AppointmentReason" : "",
            #"ConfirmationStatus" : "",
            #"EndDate" : "",
            #"FromCreatedDate" : "",
            #"FromLastModifiedDate" : "",
            #"PatientCasePayerScenario" : "",
            #"PatientFullName" : "SANTIAGO BALOG",
            #"PatientID" : "3",
            "PracticeName" : "Intelligent Sleep with Renuma"
            #"ResourceName" : "",
            #"ServiceLocationName" : "",
            #"StartDate" : "",
            #"TimeZoneOffsetFromGMT" : "",
            #"ToCreatedDate" : "",
            #"ToLastModifiedDate" : "",
            #"Type" : ""
        }
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n"+"Assigning the values to: Fields ...", end="", flush=True)
        GetAppointmentsReq.Fields = {
            "AllDay" : True,
            "ConfirmationStatus" : True,
            "CreatedDate" : True,
            "EndDate" : True,
            "ID" : True,
            "LastModifiedDate" : True,
            "PatientFullName" : True,
            "PatientID" : True,
            "PracticeID" : True,
            "PracticeName" : True,
            "Recurring" : True,
            "StartDate" : True,
            "Type" : True
        }
        print('\033[32m', "(Ok)", '\033[0m')

        #   Factory ready for use
        print("\n", GetAppointmentsReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service GetAppointments with the param GetAppointmentsReq
        print("\n"+"Starting request: GetAppointments ...", end="", flush=True)
        response = client.service.GetAppointments(GetAppointmentsReq)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", response)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = json.dumps(recursive_dict(response), indent=4)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\nResult:", result)

        return result

    except Exception as error:
        return error

def get_patient(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print("\n")
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetPatientReq ...", end="", flush=True)
        GetPatientReq = client.factory.create('GetPatientReq')
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", GetPatientReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        GetPatientReq.RequestHeader = {
            "CustomerKey" : CustomerKey,
            "Password" : Password,
            "User" : User
        }
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n"+"Assigning the values to: Filter ...", end="", flush=True)
        GetPatientReq.Filter = {
            #"ExternalID" : "",
            #"ExternalVendorID" : "",
            "PatientID" : "3"
        }
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n"+"Service has no values to set in Fields ...", end="", flush=True)
        print('\033[32m', "(Ok)", '\033[0m')

        #   Factory ready for use
        print("\n", GetPatientReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service GetPatient with the param GetPatientReq
        print("\n"+"Starting request: GetPatient ...", end="", flush=True)
        response = client.service.GetPatient(GetPatientReq)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", response)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = json.dumps(recursive_dict(response), indent=4)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\nResult:", result)

        return result

    except Exception as error:
        return error

def get_patients(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print("\n")
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetPatientsReq ...", end="", flush=True)
        GetPatientsReq = client.factory.create('GetPatientsReq')
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", GetPatientsReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        GetPatientsReq.RequestHeader = {
            "CustomerKey" : CustomerKey,
            "Password" : Password,
            "User" : User
        }
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n"+"Assigning the values to: Filter ...", end="", flush=True)
        GetPatientsReq.Filter = {
            #"FromLastModifiedDate" : "1/10/2021",
            "PracticeID" : "1"
        }
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n"+"Assigning the values to: Fields ...", end="", flush=True)
        GetPatientsReq.Fields = {
            #"Age" : True,
            #"City" : True,
            #"Country" : True,
            #"DOB" : True,
            "EmailAddress" : True,
            #"Gender" : True,
            "ID" : True,
            "PatientFullName" : True,
            "PracticeId" : True,
            "PracticeName" : True,
            #"State" : True,
            #"ZipCode" : True
        }
        print('\033[32m', "(Ok)", '\033[0m')

        #   Factory ready for use
        print("\n", GetPatientsReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service GetPatients with the param GetPatientsReq
        print("\n"+"Starting request: GetPatients ...", end="", flush=True)
        response = client.service.GetPatients(GetPatientsReq)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", response)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = json.dumps(recursive_dict(response), indent=4)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\nResult:", result)

        return result

    except Exception as error:
        return error

def get_all_patients(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print("\n")
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetAllPatientsReq ...", end="", flush=True)
        GetAllPatientsReq = client.factory.create('GetAllPatientsReq')
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", GetAllPatientsReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        GetAllPatientsReq.RequestHeader = {
            "CustomerKey" : CustomerKey,
            "Password" : Password,
            "User" : User
        }
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n"+"Assigning the values to: Filter ...", end="", flush=True)
        GetAllPatientsReq.Filter = {
            #"BatchSize" : "",
            "PracticeID" : "1",
            "StartKey" : "0"
        }
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n"+"Assigning the values to: Fields ...", end="", flush=True)
        GetAllPatientsReq.Fields = {
            #"Age" : True,
            #"City" : True,
            #"Country" : True,
            #"DOB" : True,
            "EmailAddress" : True,
            #"Gender" : True,
            "ID" : True,
            "PatientFullName" : True,
            "PracticeId" : True,
            "PracticeName" : True,
            #"State" : True,
            #"ZipCode" : True
        }
        print('\033[32m', "(Ok)", '\033[0m')

        #   Factory ready for use
        print("\n", GetAllPatientsReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service GetAllPatients with the param GetPatientsReq
        print("\n"+"Starting request: GetAllPatients ...", end="", flush=True)
        response = client.service.GetAllPatients(GetAllPatientsReq)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", response)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = json.dumps(recursive_dict(response), indent=4)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\nResult:", result)

        return result

    except Exception as error:
        return error

def get_providers(client, CustomerKey, User, Password):
    term_size = os.get_terminal_size()
    print("\n")
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetProvidersReq ...", end="", flush=True)
        GetProvidersReq = client.factory.create('GetProvidersReq')
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", GetProvidersReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        GetProvidersReq.RequestHeader = {
            "CustomerKey" : CustomerKey,
            "Password" : Password,
            "User" : User
        }
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n"+"Assigning the values to: Filter ...", end="", flush=True)
        GetProvidersReq.Filter = {
            #"DepartmentName" : "",
            #"FromCreatedDate" : "",
            #"FromLastModifiedDate" : "",
            #"FullName" : "",
            "PracticeID" : "1"
            #"PracticeName" : "",
            #"ToCreatedDate" : "",
            #"ToLastModifiedDate" : "",
            #"Type" : ""
        }
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n"+"Assigning the values to: Fields ...", end="", flush=True)
        GetProvidersReq.Fields = {
            "Active" : True,
            "EmailAddress" : True,
            "FullName" : True,
            "ID" : True,
            "PracticeID" : True,
            "PracticeName" : True,
            "Prefix" : True,
            "SpecialtyName" : True,
            "State" : True,
            "Type" : True
        }
        print('\033[32m', "(Ok)", '\033[0m')

        #   Factory ready for use
        print("\n", GetProvidersReq)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service GetProviders with the param GetPatientsReq
        print("\n"+"Starting request: GetProviders ...", end="", flush=True)
        response = client.service.GetProviders(GetProvidersReq)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\n", response)
        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Get result of the response
        print("\n"+"Getting result of the response ...", end="", flush=True)
        result = json.dumps(recursive_dict(response), indent=4)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\nResult:", result)

        return result
    except Exception as error:
        return error
