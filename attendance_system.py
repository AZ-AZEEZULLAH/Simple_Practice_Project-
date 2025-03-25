#Students Attendance & Marked


# import os 

# from datetime import datetime

# class Attendance:
#     def __init__(self):
#         self.students ={}
#         self.attendance_records = {}
#         self.students_file = "students.json"
#         self.attendance_file = "attendance.json"
#         self.load_data()

#     def load_data(self):
#         try:
#             # Load data for students
#             # use conditions

#             if os.path.exists(self.students_file):
#                 with open(self.students_file,"r") as f:
#                     content = f.read()
#                     if content.strip():
#                         self.students = json.loads(content) # type: ignore

#                     else:
#                         self.students={}


#             # load attendance data


#             if os.path.exists(self.attendance_file):
#                 with open(self.attendance_file,"r") as f:
#                     content = f.read()
#                     if content.strip():
#                         self.attendance_records = json.loads(content) # type: ignore

#                     else:

#                         self.attendance_records = {}

#             else:
#                 self.attendance_records={}

#         except json.JSONDeccodeError: # type: ignore
#             print("Error:Data files are corrupted Initializing with empty data")
#             self.students={}
#             self.attendance_records={}
#             self.save_data()



#     def save_data(self):
#         try:
#             with open(self.students_file,"w") as f:
#                 json.dump(self.students,f,indent=4)

#             with open(self.attendance_file,"w") as f :
#                 json.dump(self.attendance_records,f,indent=4)

#         except Exception as e :
#             print(f"Error Saving Data:{e}")


#     def add_student(self, Student_Id, Name):
#         if Student_Id in self.students:
#             return False, "Student ID Already Exists"



#         self.students[Student_Id] = Name
#         self.save_data()
#         return True, "Student Added Successfully"



#     def mark_attendance(self, Student_Id):
#         if Student_Id not in self.students:
#             return False, "Student Are not Found"

#         date = datetime.now().strftime("%d-%m-%Y")
#         if date not in self.attendance_records:
#             self.attendance_records[date] = {}


#         self.attendance_records[date][Student_Id] =True
#         self.save_data()
#         return True, f"Attendance Marked for {self.students[Student_Id]}"


#     def  view_attendance(self,date=None):
#         if date is None:
#             date = datetime.now().strftime("%d-%m-%Y")

#         if date not in self.attendance_records:
#             return "No Attendance Record Found for this data:" 


#         result = f"\nAttendance for {date}:\n"
#         result += "_" * 50 + "\n"
#         result += f"{"Student_ID":<15} {'Name'<30} {"Status":<10}\n"
#         result += "_" * 90 + "\n"



#         for Student_Id in self.students:
#             present = self.attendance_records[date].get(Student_Id, False)
#             status = "Present" if present else "Absent"
#             result += f"{Student_Id:<15} {self.students[Student_Id]}:<30 { status:<10}\n"

#             return result



#     def main():
#         system = Attendance()


#         while True:

#             print("\n=== Student Attendance ")
#             print("01: Add New Student.")
#             print("02: Mark Attendance.")
#             print("03: View Attendance")
#             print("04: Exit")


#             try:
#                 choice = input("\nEnter Your Choice (1-4)").strip()


#                 if choice == "1":
#                     Student_Id = input("Enter Student ID:").strip()
#                     name= input("Error Student Name :").strip()
#                     if not Student_Id or not name :
#                         print("Error: Student Name Cannot be Empty!")
#                         continue

#                 success, message = system.add_student(Student_Id,name)
#                 print(message)




#             elif choice == "2":
#                 Student_Id = input("Enter Student ID:").strip()
#                 if not Student_Id:
#                     print("Error:Student ID Cannot be Empty:")
#                     continue
#                 success, message = system.mark_attendance(Student_Id)
#                 print(message)



#             elif choice = "3":
#                 date = input("Enter date (DD-MM-YYYY) or press for Today:").strip()

#                 if date:
#                     try:
#                         datetime.strptime(date, %d-%m-%Y)
#                     except ValueError:
#                         print("Error : Invalid date format ! Please use DD-MM-YYYY")
#                         continue
#                     print(system.view_attendance(date if date else None))


#             elif choice = "4":
#                 print("Thank you for using Attendance !")
#                     break
#               else:
#                 print("Invalid Choice ! Please Try Again.")

#             except Exception as e :
#                 print(f"An Error Occurred: {e}")
#                 print(f"Please Try Again")

#     if __name__ == " _main_":
#         main()




import os
import json
from datetime import datetime

class Attendance:
    def __init__(self):
        self.students = {}
        self.attendance_records = {}
        self.students_file = "students.json"
        self.attendance_file = "attendance.json"
        self.load_data()

    def load_data(self):
        try:
            # Load student data
            if os.path.exists(self.students_file):
                with open(self.students_file, "r") as f:
                    content = f.read()
                    self.students = json.loads(content) if content.strip() else {}

            # Load attendance data
            if os.path.exists(self.attendance_file):
                with open(self.attendance_file, "r") as f:
                    content = f.read()
                    self.attendance_records = json.loads(content) if content.strip() else {}
            else:
                self.attendance_records = {}

        except json.JSONDecodeError:
            print("Error: Data files are corrupted. Initializing with empty data.")
            self.students = {}
            self.attendance_records = {}
            self.save_data()

    def save_data(self):
        try:
            with open(self.students_file, "w") as f:
                json.dump(self.students, f, indent=4)

            with open(self.attendance_file, "w") as f:
                json.dump(self.attendance_records, f, indent=4)
        except Exception as e:
            print(f"Error Saving Data: {e}")

    def add_student(self, Student_Id, Name):
        if Student_Id in self.students:
            return False, "Student ID Already Exists"

        self.students[Student_Id] = Name
        self.save_data()
        return True, "Student Added Successfully"

    def mark_attendance(self, Student_Id):
        if Student_Id not in self.students:
            return False, "Student Not Found"

        date = datetime.now().strftime("%d-%m-%Y")
        if date not in self.attendance_records:
            self.attendance_records[date] = {}

        self.attendance_records[date][Student_Id] = True
        self.save_data()
        return True, f"Attendance Marked for {self.students[Student_Id]}"

    def view_attendance(self, date=None):
        if date is None:
            date = datetime.now().strftime("%d-%m-%Y")

        if date not in self.attendance_records:
            return "No Attendance Record Found for this date."

        result = f"\nAttendance for {date}:\n"
        result += "_" * 50 + "\n"
        result += f"{'Student_ID':<15} {'Name':<30} {'Status':<10}\n"
        result += "_" * 50 + "\n"

        for Student_Id in self.students:
            present = self.attendance_records[date].get(Student_Id, False)
            status = "Present" if present else "Absent"
            result += f"{Student_Id:<15} {self.students[Student_Id]:<30} {status:<10}\n"

        return result

def main():
    system = Attendance()

    while True:
        print("\n=== Student Attendance ===")
        print("1: Add New Student.")
        print("2: Mark Attendance.")
        print("3: View Attendance")
        print("4: Exit")

        try:
            choice = input("\nEnter Your Choice (1-4): ").strip()

            if choice == "1":
                Student_Id = input("Enter Student ID: ").strip()
                name = input("Enter Student Name: ").strip()
                if not Student_Id or not name:
                    print("Error: Student ID and Name Cannot be Empty!")
                    continue

                success, message = system.add_student(Student_Id, name)
                print(message)

            elif choice == "2":
                Student_Id = input("Enter Student ID: ").strip()
                if not Student_Id:
                    print("Error: Student ID Cannot be Empty.")
                    continue

                success, message = system.mark_attendance(Student_Id)
                print(message)

            elif choice == "3":
                date = input("Enter date (DD-MM-YYYY) or press Enter for Today: ").strip()
                if date:
                    try:
                        datetime.strptime(date, "%d-%m-%Y")
                    except ValueError:
                        print("Error: Invalid date format! Please use DD-MM-YYYY")
                        continue

                print(system.view_attendance(date if date else None))

            elif choice == "4":
                print("Thank you for using Attendance!")
                break

            else:
                print("Invalid Choice! Please Try Again.")

        except Exception as e:
            print(f"An Error Occurred: {e}")
            print("Please Try Again")

if __name__ == "__main__":
    main()
