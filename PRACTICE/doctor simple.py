# Main program to handle Doctor and Hospital information

# Reading number of doctors
n = int(input())

# Initializing an empty dictionary to store doctor objects
doctorDB = {}

# Reading Doctor details and adding them to the doctorDB dictionary
for i in range(1, n + 1):
    doctorId = int(input())
    doctorName = input()
    specialization = input()
    consultationFee = float(input())
    
    doctorDB[i] = {
        'doctorId': doctorId,
        'doctorName': doctorName,
        'specialization': specialization,
        'consultationFee': consultationFee
    }

# Creating a Hospital object and passing the doctorDB
hospital = doctorDB

# Function to search doctors by name
def searchByDoctorName(doctorName):
    result = []
    for key, doctor in hospital.items():
        if doctor['doctorName'] == doctorName:
            result.append(doctor)
    
    return result if result else None

# Function to calculate total consultation fee by specialization
def calculateConsultationFeeBySpecialization(specialization):
    total_fee = 0
    for key, doctor in hospital.items():
        if doctor['specialization'] == specialization:
            total_fee += doctor['consultationFee']
    
    return total_fee if total_fee > 0 else 0

# Main logic to execute the search and fee calculation
doctor_name_to_search = input()
specialization_to_search = input()

# Search for doctors by name
doctors_found = searchByDoctorName(doctor_name_to_search)

# Display result for searchByDoctorName
if doctors_found:
    for doctor in doctors_found:
        print(doctor['doctorId'])
        print(doctor['doctorName'])
        print(doctor['specialization'])
        print(int(doctor['consultationFee']))
else:
    print("No Doctor Exists with the given DoctorName")

# Calculate consultation fee for the specialization
total_fee = calculateConsultationFeeBySpecialization(specialization_to_search)

# Display result for calculateConsultationFeeBySpecialization
if total_fee == 0:
    print("No Doctor with the given specialization")
else:
    print(total_fee)
