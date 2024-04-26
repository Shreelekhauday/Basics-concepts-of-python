def get_student_details(student_id):
    studentdatabase = {
        21:{"name": "shifa", "sem": 4, "roll no": "21","grade":"A!"},
        22:{"name": "shree", "sem": 4, "roll no": "22","grade":"A@"},
        23:{"name": "shobha", "sem":4, "roll no": "23","grade":"A#"},
        24:{"name":"shabana", "sem":4,  "roll no":"24","grade":"A+"}
    }

    if student_id in studentdatabase:
        return studentdatabase[student_id]
    else:
        return None
def display_studentdetails(student_id):
    student_details = get_student_details(student_id)
    if student_details:
        print("Student ID:", student_id)
        print("Name:", student_details["name"])
        print("Sem:", student_details["sem"])
        print("Roll no:", student_details["roll no"])
        print("Grade:",student_details["grade"])
    else:
        print("Student ID not found.")
student_id = int(input("enter student ID: "))
display_studentdetails(student_id)