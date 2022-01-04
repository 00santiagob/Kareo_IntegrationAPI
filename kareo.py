import json
import os
import sys

#from suds.client import Client
from Utils.to_dict import recursive_dict
from Utils.console import clear_console
from Method.create import *
from Method.delete import *
from Method.get import *
from Method.update import *
import suds

if __name__ == "__main__":

    CustomerKey = None
    User = None
    Password = None

    for arg in sys.argv[1:]:
        if "Key" in arg:
            CustomerKey = arg[4:]
        elif "User" in arg:
            User = arg[5:]
        elif "Pass" in arg:
            Password = arg[5:]
        else:
            pass

    if CustomerKey is None or User is None or Password is None:
        print("Some or all of the parameters are incorrect")
        exit()

    # Base URL for API requests
    wsdl = "https://webservice.kareo.com/services/soap/2.1/KareoServices.svc?singleWsdl"

    # Conect to Kareo API
    clear_console()
    print("Conecting to Kareo Service API ...", end="", flush=True)
    client = suds.client.Client(wsdl)
    print('\033[32m'+'\033[01m'+'\033[05m'+"(Success)", '\033[0m')
    #print(client)

    print('\033[01m', '\033[33m') # Color font ORANGE
    print("      %%%%                                                                                                              ")
    print("     %%%%%$                                                                                                             ")
    print("    $$$$$$%                                                                                                             ")
    print("   *$$$$$$                                                                                                              ")
    print("  :$$$$$$!     :%%%:                                                                                                    ")
    print("  %@@@@@@     %%%%%%                                                                                                    ")
    print("  %@@@@@@    %%%%%%%!        %%%%                                                                                       ")
    print(" *%$@@@@%   :%%%%%%%       %%%%%%                                                                                       ")
    print(" %%%&&&&%    %%%%%%      :%%%%%%                                                                                        ")
    print(" %%%%&&&&     %%*      :%%%%%%%                                                                                         ")
    print(":%%%%%$&&!           %%%%%%%%                                                                                           ")
    print("*%%%%%%%$##       %%%%%%%%%%:                                                                                           ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%            %%%%                                                                            ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%             %%%%                                                                            ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%             %%%%    !%%%%:  !%%%%%%%%%%%%%%  %%%%%%%%%%: %%%%%%%%%%%      *%%%%%%%%%%%      ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%             %%%%  !%%%%%   %%%%%:   *%%%%%%  %%%%%%!   !%%%%!   *%%%%:   %%%%%:   !%%%%:    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%             %%%%!%%%%*    %%%%        !%%%%  %%%%:    %%%%:       %%%%  %%%%        !%%%    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%            %%%%%%%%      %%%!         %%%%  %%%*     %%%%%%%%%%%%%%%%! %%%!         %%%*   ")
    print("%%%%%%%%%%%%%%%%########$%%%*           %%%%%%%%%:    %%%!         %%%%  %%%!     %%%%***********   %%%!         %%%*   ")
    print("%%%%%%%%%%%%%      &&&&&&&&&%:          %%%%  !%%%%   %%%%        !%%%%  %%%!     %%%%:             %%%%        !%%%    ")
    print("*%%%%%%%%%%%         &&&&&&&&&%         %%%%    %%%%%  %%%%%    !%%%%%%  %%%!      *%%%%:   :%%%%!   %%%%%:   !%%%%:    ")
    print(":%%%%%%%%%%:          !&&&&&&&&%        %%%%     *%%%%  %%%%%%%%%%%%%%%  %%%!        %%%%%%%%%%%:     *%%%%%%%%%%%      ")
    print(" %%%%%%%%%%             %@@@@@@@@                                                                                       ")
    print(" %%%%%%%%%               :@@@@@@@@                                                                                      ")
    print("  %%%%%%%%                 $$$$$$$$                                                                                     ")
    print("  %%%%%%%                   $$$$$$$$                                                                                    ")
    print("   *%%%%%                     $$$$$$                                                                                    ")
    print("     %%:                        %%%                                                                                     ")
    print('\033[0m') # Reset config of print
    print("Service (", '\033[33m'+"KareoServices"+'\033[0m', ") tns=", '\033[34m'+'\033[01m'+'\033[04m'+"\"http://www.kareo.com/api/schemas/\""+'\033[0m')

    """
    Methods (25):
        CreateAppointment( CreateAppointmentReq )
        CreateEncounter( CreateEncounterReq )
        CreatePatient( CreatePatientReq )
        CreatePayment( CreatePaymentRequest )
        DeleteAppointment( DeleteAppointmentReq )
        GetAllPatients( GetAllPatientsReq )
        GetAppointment( GetAppointmentReq )
        GetAppointments( GetAppointmentsReq )
        GetCharges( GetChargesReq )
        GetCustomerIdFromKey( GetCustomerIdFromKeyRequest )
        GetEncounterDetails( GetEncounterDetailsReq )
        GetExternalVendors( GetExternalVendorsReq )
        GetPatient( GetPatientReq )
        GetPatients( GetPatientsReq )
        GetPayments( GetPaymentsReq )
        GetPractices( GetPracticesReq )
        GetProcedureCodes( ns4:GetProcedureCodesReq )
        GetProviders( GetProvidersReq )
        GetServiceLocations( ns4:GetServiceLocationsReq )
        GetTransactions( GetTransactionsReq )
        RegisterExternalVendor(RegisterExternalVendorReq )
        UpdateAppointment( npdateAppointmentReq )           #not working with npdateAppointmentReq. Use UpdateAppointmentReq instead
        UpdateEncounterStatus( npdateEncounterStatusReq )
        UpdatePatient( npdatePatientReq UpdatePatientReq, )
        UpdatePatientsExternalID( npdatePatientsExternalIDReq )
    """
    print("Methods:")
    print("\t 0", '\033[05m'+"==>"+'\033[0m', '\033[03m'+"Create Appointment"+'\033[0m')
    print("\t 1", '\033[05m'+"==>"+'\033[0m', '\033[03m'+"Create Patient"+'\033[0m')
    print("\t 2", '\033[05m'+"==>"+'\033[0m', '\033[03m'+"Delete Appointment"+'\033[0m')
    print("\t 3", '\033[05m'+"==>"+'\033[0m', '\033[03m'+"Get Appointment"+'\033[0m')
    print("\t 4", '\033[05m'+"==>"+'\033[0m', '\033[03m'+"Get Appointments"+'\033[0m')
    print("\t 5", '\033[05m'+"==>"+'\033[0m', '\033[03m'+"Get Patient"+'\033[0m')
    print("\t 6", '\033[05m'+"==>"+'\033[0m', '\033[03m'+"Get Patients"+'\033[0m')
    print("\t 7", '\033[05m'+"==>"+'\033[0m', '\033[03m'+"Get All Patients"+'\033[0m')
    print("\t 8", '\033[05m'+"==>"+'\033[0m', '\033[03m'+"Get Providers"+'\033[0m')
    print("\t 9", '\033[05m'+"==>"+'\033[0m', '\033[03m'+"Update Appointment"+'\033[0m')
    print("\t10", '\033[05m'+"==>"+'\033[0m', '\033[03m'+"Update Patient"+'\033[0m')

    method = input("Select the number of a method: ")

    if method == '0':
        Appointment = None
        Appointment = create_appointment(client, CustomerKey, User, Password)
    elif method == '1':
        Patient = None
        Patient = create_patient(client, CustomerKey, User, Password)
    elif method == '2':
        Appointment = None
        Appointment = delete_appointment(client, CustomerKey, User, Password)
    elif method == '3':
        Appointment = None
        Appointment = get_appointment(client, CustomerKey, User, Password)
    elif method == '4':
        Appointments = None
        Appointments = get_appointments(client, CustomerKey, User, Password)
    elif method == '5':
        Patient = None
        Patient = get_patient(client, CustomerKey, User, Password)
    elif method == '6':
        Patients = None
        Patients = get_patients(client, CustomerKey, User, Password)
    elif method == '7':
        AllPatients = None
        AllPatients = get_all_patients(client, CustomerKey, User, Password)
    elif method == '8':
        Providers = None
        Providers = get_providers(client, CustomerKey, User, Password)
    elif method == '9':
        Appointment = None
        Appointment = update_appointment(client, CustomerKey, User, Password)
    elif method == '10':
        Patient = None
        Patient = update_patient(client, CustomerKey, User, Password)
    else:
        print('\033[41m', '\033[30m', "Method incorrect!!", '\033[0m')

    """
    Types (197):
        AppointmentCreate
        AppointmentData
        AppointmentDelete
        AppointmentFieldsToReturn
        AppointmentFilter
        AppointmentIdentifierReq
        AppointmentRead
        AppointmentStatus
        AppointmentType
        AppointmentUpdate
        ArrayOfAppointmentData
        ArrayOfChargeData
        ns1:ArrayOfDayOfWeek
        ArrayOfEncounterDetailsData
        ArrayOfExternalVendorData
        ArrayOfGroupPatientSummary
        ArrayOfInsurancePolicyAuthorizationCreateReq
        ArrayOfInsurancePolicyAuthorizationRes
        ArrayOfInsurancePolicyAuthorizationUpdateReq
        ArrayOfInsurancePolicyCreateReq
        ArrayOfInsurancePolicyRes
        ArrayOfInsurancePolicyUpdateReq
        ArrayOfOrdinal
        ArrayOfPatientBatchData
        ArrayOfPatientCaseCreateReq
        ArrayOfPatientCaseData
        ArrayOfPatientCaseRes
        ArrayOfPatientCaseUpdateReq
        ArrayOfPatientData
        ArrayOfPatientExternalIDSetting
        ArrayOfPatientInsurancePolicyAuthorizationData
        ArrayOfPatientInsurancePolicyData
        ArrayOfPaymentData
        ArrayOfPracticeData
        ns4:ArrayOfProcedureCodeData
        ArrayOfProviderData
        ArrayOfServiceLineReq
        ArrayOfServiceLineRes
        ns4:ArrayOfServiceLocationData
        ArrayOfTransactionData
        ns3:ArrayOfint
        ns3:ArrayOflong
        ns3:ArrayOfstring
        AttendeeStatus
        ChargeData
        ChargeFieldsToReturn
        ChargeFilter
        CreateAppointmentReq
        CreateAppointmentResp
        CreateEncounterReq
        CreateEncounterResp
        CreatePatientReq
        CreatePaymentRequest
        CreatePaymentResp
        ns1:DayOfWeek
        DeleteAppointmentReq
        DeleteAppointmentResp
        ns0:EPSDTReasonCode
        EmployerReq
        ns0:EmploymentStatusCode
        EncounterCreate
        EncounterDetailsData
        EncounterDetailsFieldsToReturn
        EncounterDetailsFilter
        EncounterDetailsPractice
        EncounterHospitalization
        EncounterMiscellaneous
        EncounterPayment
        EncounterPlaceOfService
        EncounterServiceLocation
        ns0:EncounterStatusCode
        EncounterUpdateStatus
        EncounterUpdateStatusPractice
        ErrorResponse
        ExternalVendorData
        ExternalVendorReq
        ns0:GenderCode
        GetAllPatientsReq
        GetAllPatientsResp
        GetAppointmentReq
        GetAppointmentResp
        GetAppointmentsReq
        GetAppointmentsResp
        GetChargesReq
        GetChargesResp
        GetCustomerIdFromKeyRequest
        GetCustomerIdFromKeyResp
        GetEncounterDetailsReq
        GetEncounterDetailsResp
        GetExternalVendorsReq
        GetExternalVendorsResp
        GetPatientReq
        GetPatientResp
        GetPatientsReq
        GetPatientsResp
        GetPaymentsReq
        GetPaymentsResp
        GetPracticesReq
        GetPracticesResp
        ns4:GetProcedureCodesReq
        ns4:GetProcedureCodesResp
        GetProvidersReq
        GetProvidersResp
        ns4:GetServiceLocationsReq
        ns4:GetServiceLocationsResp
        GetTransactionsReq
        GetTransactionsResp
        GroupPatientSummary
        InsurancePolicyAdjusterReq
        InsurancePolicyAuthorizationCreateReq
        InsurancePolicyAuthorizationRes
        InsurancePolicyAuthorizationUpdateReq
        InsurancePolicyCreateReq
        InsurancePolicyInsuredReq
        InsurancePolicyRes
        InsurancePolicyUpdateReq
        ModifyPatientResp
        Ordinal
        OrphanDiagnosisCodes
        PatientAlertReq
        PatientBatchData
        PatientBatchFieldsToReturn
        PatientBatchGetFilter
        PatientBatchKey
        PatientCaseConditionReq
        PatientCaseCreateReq
        PatientCaseData
        PatientCaseDatesReq
        PatientCaseIdentifierReq
        PatientCaseRes
        PatientCaseUpdateReq
        PatientCreate
        PatientData
        PatientEmployerReq
        PatientExternalIDSetting
        PatientExternalIDSettingBatch
        PatientFieldsToReturn
        PatientFilter
        PatientGuarantorReq
        PatientIdentifierReq
        PatientInsurancePolicyAuthorizationData
        PatientInsurancePolicyData
        PatientSummary
        PatientUpdate
        PaymentAppointmentCreate
        PaymentCreate
        PaymentData
        PaymentFieldsToReturn
        PaymentFilter
        PaymentInsuranceCreate
        ns0:PaymentMethodCode
        PaymentPatientCreate
        PaymentPaymentCreate
        PaymentPracticeCreate
        PermissionsMissing
        PhysicianIdentifierReq
        PracticeData
        PracticeFieldsToReturn
        PracticeFilter
        PracticeIdentifierReq
        PracticiesAuthorized
        ns4:ProcedureCodeData
        ns4:ProcedureCodeFieldsToReturn
        ns4:ProcedureCodeFilter
        ProviderData
        ProviderFieldsToReturn
        ProviderFilter
        ProviderIdentifierDetailedReq
        ProviderIdentifierReq
        RecurrenceRule
        RegisterExternalVendorReq
        RegisterExternalVendorResp
        ns0:Relationship
        RequestBase
        RequestHeader
        ResponseBase
        SecurityResponse
        ServiceLineReq
        ServiceLineRes
        ns4:ServiceLocationData
        ns4:ServiceLocationFieldsToReturn
        ns4:ServiceLocationFilter
        ServiceLocationReq
        SinglePatientFilter
        TransactionData
        TransactionFieldsToReturn
        TransactionFilter
        TypeOfDay
        UpdateAppointmentReq
        UpdateAppointmentResp
        UpdateEncounterStatusReq
        UpdatePatientReq
        UpdatePatientsExternalIDReq
        UpdatePatientsExternalIDResp
        ns2:char
        ns2:duration
        ns2:guid
    """
