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
        print("\n"+"Assigning the values to: Appointment ...", end="", flush=True)
        AppointmentCreate = client.factory.create('AppointmentCreate')
        CreateAppointmentReq.Appointment = {
            "AppointmentId" : ""
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

        #   Create result of the response
        print("\n"+"Createting result of the response ...", end="", flush=True)
        result = json.dumps(recursive_dict(response), indent=4)
        print('\033[32m', "(Ok)", '\033[0m')
        print("\nResult:", result)

        return result
    except Exception as error:
        return error

    """
    Appointment =
      (AppointmentCreate){
         AppointmentId = None
         AppointmentName = None
         AppointmentReasonId = None
         AppointmentStatus =
            (AppointmentStatus){
               value = None
            }
         AppointmentType =
            (AppointmentType){
               value = None
            }
         AppointmentUUID = None
         AttendeesCount = None
         CreatedAt = None
         CreatedBy = None
         CustomerId = None
         EndTime = None
         ForRecare = None
         InsurancePolicyAuthorizationId = None
         IsDeleted = None
         IsGroupAppointment = None
         IsRecurring = None
         MaxAttendees = None
         Notes = None
         OccurrenceId = None
         PatientCaseId = None
         PatientSummaries =
            (ArrayOfGroupPatientSummary){
               GroupPatientSummary[] = <empty>
            }
         PatientSummary =
            (PatientSummary){
               DateOfBirth = None
               Email = None
               FirstName = None
               GenderId = None
               Guid = None
               HomePhone = None
               LastName = None
               MiddleName = None
               MobilePhone = None
               OtherEmail = None
               OtherPhone = None
               PatientId = None
               PracticeId = None
               PreferredEmailType = None
               PreferredPhoneType = None
               WorkEmail = None
               WorkPhone = None
            }
         PracticeId = None
         ProviderId = None
         RecurrenceRule =
            (RecurrenceRule){
               AppointmentId = None
               DayInterval = None
               DayOfMonth = None
               DayOfWeek =
                  (ArrayOfDayOfWeek){
                     DayOfWeek[] = <empty>
                  }
               DayOfWeekFlags = None
               DayOfWeekMonthlyOrdinal =
                  (ArrayOfOrdinal){
                     Ordinal[] = <empty>
                  }
               DayOfWeekMonthlyOrdinalFlags = None
               EndDate = None
               MonthInterval = None
               MonthOfYear = None
               NumOccurrences = None
               NumberOfTimes = None
               RecurrenceRuleId = None
               StartDate = None
               TypeOfDay =
                  (TypeOfDay){
                     value = None
                  }
               TypeOfDayMonthlyOrdinal =
                  (ArrayOfOrdinal){
                     Ordinal[] = <empty>
                  }
               TypeOfDayMonthlyOrdinalFlags = None
            }
         ResourceId = None
         ResourceIds =
            (ArrayOflong){
               long[] = <empty>
            }
         ServiceLocationId = None
         StartTime = None
         UpdatedAt = None
         UpdatedBy = None
         WasCreatedOnline = None
      }
    """

def create_patient(client, CustomerKey, User, Password):
    try:
        print('\033[43m', '\033[30m', '\033[01m', "Service temporarily unavailable", '\033[0m')
    except Exception as error:
        return error