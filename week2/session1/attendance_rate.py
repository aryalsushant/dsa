def attendance_rate(attendance_list):
    total = len(attendance_list.values())
    present = 0
    for key, value in attendance_list.items():
        if value == "Present":
            present += 1
    return (present/total)*100



#test case
attendance_list = {
    "Bluey": "Present", 
    "Bingo": "Absent", 
    "Snickers": "Present", 
    "Winton": "Absent"
}

print(attendance_rate(attendance_list))
