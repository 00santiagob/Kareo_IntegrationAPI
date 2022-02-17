import json
import os
import sys
from datetime import datetime

from suds.client import Client
from Utils.to_dict import recursive_dict
from Utils.console import clear_console

#   UpdateAppointment( npdateAppointmentReq )
def update_appointment(client, CustomerKey, User, Password):
    AppointmentId = int(input("Enter the appointment id: "))
    term_size = os.get_terminal_size()
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #   Create a factory
        print("\n"+"Creating factory: GetCustomerIdFromKeyRequest ...", end="", flush=True)
        GetCustomerIdFromKeyRequest = client.factory.create('GetCustomerIdFromKeyRequest')
        print('\033[32m', "(Ok)", '\033[0m')

        print(GetCustomerIdFromKeyRequest)

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: GetCustomerIdFromKeyRequest ...", end="", flush=True)
        GetCustomerIdFromKeyRequest['CustomerKey'] = CustomerKey
        GetCustomerIdFromKeyRequest['User'] = User
        GetCustomerIdFromKeyRequest['Password'] = Password
        print('\033[32m', "(Ok)", '\033[0m')

        print(GetCustomerIdFromKeyRequest)

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Call the service CreateAppointment with the param CreateAppointmentReq
        response = None
        print("\n"+"Starting request: GetCustomerIdFromKeyRequest ...", end="", flush=True)
        response = client.service.GetCustomerIdFromKey(GetCustomerIdFromKeyRequest)
        print('\033[32m', "(Ok)", '\033[0m')

        print("GetCustomerIdFromKey (RESPONSE):", response)

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Create a factory
        print("\n"+"Creating factory: AppointmentStatus ...", end="", flush=True)
        AppointmentStatus = client.factory.create('AppointmentStatus')
        print('\033[32m', "(Ok)", '\033[0m')

        print(AppointmentStatus)

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Create a factory
        print("\n"+"Creating factory: UpdateAppointmentReq ...", end="", flush=True)
        UpdateAppointmentReq = client.factory.create('UpdateAppointmentReq')
        print('\033[32m', "(Ok)", '\033[0m')

        print(UpdateAppointmentReq)

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Assign the values
        print("\n"+"Assigning the values to: RequestHeader ...", end="", flush=True)
        UpdateAppointmentReq.RequestHeader['CustomerKey'] = CustomerKey
        UpdateAppointmentReq.RequestHeader['User'] = User
        UpdateAppointmentReq.RequestHeader['Password'] = Password
        print('\033[32m', "(Ok)", '\033[0m')

        print(UpdateAppointmentReq)

        #   Assign the values
        print("\n"+"Assigning the values to: Appointment ...", end="", flush=True)
        UpdateAppointmentReq.Appointment['AppointmentId'] = AppointmentId   # Required
        UpdateAppointmentReq.Appointment['AppointmentName'] = "Appointment for Renuma"  # Required
        UpdateAppointmentReq.Appointment['AppointmentReasonId'] = 0 # Required
        UpdateAppointmentReq.Appointment['AppointmentStatus'] = AppointmentStatus['Rescheduled']    # Required
        UpdateAppointmentReq.Appointment['EndTime'] = datetime(2022, 1, 16, 15, 00, 00)    # Required
        # UpdateAppointmentReq.Appointment['InsurancePolicyAuthorizationId'] = None   # Optional
        # UpdateAppointmentReq.Appointment['IsGroupAppointment'] = None   # Optional
        # UpdateAppointmentReq.Appointment['IsRecurring'] = None  # Optional
        UpdateAppointmentReq.Appointment['MaxAttendees'] = 0    # Required
        UpdateAppointmentReq.Appointment['Notes'] = "This is other description for update"  # Optional
        # UpdateAppointmentReq.Appointment['OccurrenceId'] = None # Optional
        # UpdateAppointmentReq.Appointment['PatientCaseId'] = None    # Optional
        UpdateAppointmentReq.Appointment['PatientId'] = 3   # Required
        UpdateAppointmentReq.Appointment['ProviderId'] = 1  # Optional
        UpdateAppointmentReq.Appointment['ResourceId'] = 0  # Required
        UpdateAppointmentReq.Appointment['ResourceIds'] = None  # Optional
        UpdateAppointmentReq.Appointment['ServiceLocationId'] = 1   # Required
        UpdateAppointmentReq.Appointment['StartTime'] = datetime(2022, 1, 16, 14, 30, 00)  # Required
        UpdateAppointmentReq.Appointment['UpdatedAt'] = datetime.now()  # Optional

        print('\033[32m', "(Ok)", '\033[0m')

        print(UpdateAppointmentReq)

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #ipdb.set_trace()

        print("\n"+"Starting request: UpdateAppointment ...", end="", flush=True)
        try:
            response = None
            response = client.service.UpdateAppointment(UpdateAppointmentReq)
            if (response['ErrorResponse']['IsError']):
                print('\033[31m', "(Fail)", '\033[0m')
                print("\n\033[31mError:\033[0m", response['ErrorResponse']['ErrorMessage'])
                print("\n\033[35mStackTrace:\033[0m\n", response['ErrorResponse']['StackTrace'])
            else:
                print('\033[32m', "(Ok)", '\033[0m')
                print("\n", response)
        except Exception as error:
            return error

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #   Create result of the response
        print("\n"+"Createting result of the response ...", end="", flush=True)
        result = json.loads(json.dumps(recursive_dict(response), indent=4))
        print('\033[32m', "(Ok)", '\033[0m')
    except Exception as error:
        return error

def update_patient(client, CustomerKey, User, Password):
    PatientId = input("Enter the patient id: ")
    term_size = os.get_terminal_size()
    print('\033[33m'+'=' * term_size.columns + '\033[0m')

    try:
        #Create a factory
        print("\n"+"Creating factory: UpdatePatientReq ...", end="", flush=True)
        UpdatePatientReq = client.factory.create('UpdatePatientReq')
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        #Assign the values
        print("\n"+"Assigning the values to: UpdatePatientReq.RequestHeader ...", end="", flush=True)
        UpdatePatientReq.RequestHeader['CustomerKey'] = CustomerKey
        UpdatePatientReq.RequestHeader['Password'] = Password
        UpdatePatientReq.RequestHeader['User'] = User
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        print("\n"+"Assigning the values to: UpdatePatientReq.Patient ...", end="", flush=True)
        UpdatePatientReq.Patient['PatientID'] = PatientId
        UpdatePatientReq.Patient['FirstName'] = "Leonardo"
        UpdatePatientReq.Patient['LastName'] = "Amato"
        UpdatePatientReq.Patient['EmailAddress'] = "amato979@gmail.com"
        UpdatePatientReq.Patient['Guarantor']['RelationshiptoGuarantor']['value'] = "Other"
        UpdatePatientReq.Patient['Gender']['value'] = "Male"
        UpdatePatientReq.Patient['Practice']['PracticeID'] = 1
        UpdatePatientReq.Patient['Practice']['PracticeName'] = "DEV" 
        print('\033[32m', "(Ok)", '\033[0m')

        print('\033[33m'+'=' * term_size.columns + '\033[0m')

        print("\n"+"Starting request: UpdatePatient ...", end="", flush=True)
        try:
            response = client.service.UpdatePatient(UpdatePatientReq)
            if (response['ErrorResponse']['IsError']):
                print('\033[31m', "(Fail)", '\033[0m')
                print("\n\033[31mError:\033[0m", response['ErrorResponse']['ErrorMessage'])
                print("\n\033[35mStackTrace:\033[0m\n", response['ErrorResponse']['StackTrace'])
            else:
                print('\033[32m', "(Ok)", '\033[0m')
                to_print = {
                    "PatientExternalID" : response['PatientExternalID'],
                    "PatientID" : response['PatientExternalID'],
                    "PracticeExternalID" : response['PracticeExternalID'],
                    "PracticeID" : response['PracticeID'],
                    "PracticeName" : response['PracticeName']
                }
                print("\n", to_print)
        except Exception as error:
            return error

        #   Create result of the response
        print("\n"+"Createting result of the response ...", end="", flush=True)
        result = json.loads(json.dumps(recursive_dict(response), indent=4))
        print('\033[32m', "(Ok)", '\033[0m')
        return result
    except Exception as error:
        return error
