"""
time as numbers so 9:30 would be 9.5.
Two appointments conflict if:
start_a < end_b AND start_b < end_a both would have to be true

1. Detect overlappinng appointments
2. Only compare appointments belonging to the same doctor
3. Return a flat list of tuples containing conflicting appointment IDs
Result should be a tuple, containing only IDs
no conflicts, return []


iterate through the appointments dictionary
if start_a < end_b AND start_b < end_a then append both id's to a result list
return the tuple

appointments = [
    {"id": 1, "doctor_id": "D1", "patient_id": "P1", "start": 9, "end": 10},
    {"id": 2, "doctor_id": "D1", "patient_id": "P2", "start": 9.5, "end": 10.5},
    {"id": 3, "doctor_id": "D1", "patient_id": "P3", "start": 11, "end": 12},
    {"id": 4, "doctor_id": "D2", "patient_id": "P4", "start": 9, "end": 10},
    {"id": 5, "doctor_id": "D2", "patient_id": "P5", "start": 10, "end": 11},
    {"id": 6, "doctor_id": "D2", "patient_id": "P6", "start": 10.5, "end": 11.5},
    {"id": 7, "doctor_id": "D3", "patient_id": "P7", "start": 8, "end": 9},
    {"id": 8, "doctor_id": "D3", "patient_id": "P8", "start": 9, "end": 10},
]

Expected output:
[(1, 2), (5, 6)]



"""

"""

"""
def find_conflicts(appointments):
    result = []
    
    for i in range(len(appointments)):
        for j in range(i+1, len(appointments)):
            #doctor ids are same + given condition. is true
            if appointments[i]["doctor_id"]==appointments[j]["doctor_id"] and appointments[i]["start"] < appointments[j]["end"] and appointments[j]["start"] < appointments[i]["end"]:
                #just add the ordered pair of the ids in the result
                result.append((appointments[i]["id"], appointments[j]["id"]))

                #it also returned same ids 


    return result




if __name__ == "__main__":
    # You can test using the datasets below
    appointments = [
    {"id": 1, "doctor_id": "D1", "patient_id": "P1", "start": 9, "end": 10},
    {"id": 2, "doctor_id": "D1", "patient_id": "P2", "start": 9.5, "end": 10.5},
    {"id": 3, "doctor_id": "D1", "patient_id": "P3", "start": 11, "end": 12},
    {"id": 4, "doctor_id": "D2", "patient_id": "P4", "start": 9, "end": 10},
    {"id": 5, "doctor_id": "D2", "patient_id": "P5", "start": 10, "end": 11},
    {"id": 6, "doctor_id": "D2", "patient_id": "P6", "start": 10.5, "end": 11.5},
    {"id": 7, "doctor_id": "D3", "patient_id": "P7", "start": 8, "end": 9},
    {"id": 8, "doctor_id": "D3", "patient_id": "P8", "start": 9, "end": 10},
    ]
    #print(find_conflicts(appointments))

    test_a = [
    {"id": 1, "doctor_id": "D1", "patient_id": "P1", "start": 9, "end": 10},
    {"id": 2, "doctor_id": "D1", "patient_id": "P2", "start": 10, "end": 11},
    ]

    #print(find_conflicts(test_a))

    test_b = [
    {"id": 1, "doctor_id": "D1", "patient_id": "P1", "start": 9, "end": 11},
    {"id": 2, "doctor_id": "D1", "patient_id": "P2", "start": 10, "end": 12},
    {"id": 3, "doctor_id": "D1", "patient_id": "P3", "start": 10.5, "end": 11.5},
    ]
    print(find_conflicts(test_b))



