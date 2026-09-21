from course import ug_course, pg_course, ug, pg
from colors import basic, bright
import ast

def studentAddmission():

      print("\n\t" + bright.YELLOW + "-"*42 + bright.RESET)
      print("\t\t" + bright.YELLOW + "Student Addmission Page" + bright.RESET)
      print("\t" + bright.YELLOW + "-"*42 + bright.RESET + "\n")

      name = input(bright.BLUE + "Enter Person Name : " + bright.RESET)
      address = input(bright.BLUE + "Enter Person Address : " + bright.RESET)
      phone = int(input(bright.BLUE + "Enter Person Phone No. : " + bright.RESET))
      email = input(bright.BLUE + "Enter Person Email ID : " + bright.RESET)
      while True:
        graduation = input(bright.BLUE + "Choose UG/PG : " + bright.RESET)
            
        if graduation.lower() == "ug":
                print(bright.MAGNETA + "-"*80 + bright.RESET)
                print(bright.MAGNETA + f"{'No':<5}{'Course':<40}{'Duration':<14}{'Fees':<25}" + bright.RESET)
                print(bright.MAGNETA + "-"*80 + bright.RESET)
                for k,v in ug_course.items():
                  print(bright.MAGNETA + f"{k:<5}{v['course']:<40}{v['duration']:<14}{v['fees']:<25}" + bright.RESET)

                select = int(input(bright.BLUE + "\nSelect Course Number : " + bright.RESET))

                if select in ug_course:
                      print("\n")
                      print(bright.GREEN + "-"*50 + bright.RESET)
                      print(bright.GREEN + f"{'Course':<25}{'Duration':<14}{'Fees':<25}" + bright.RESET)
                      print(bright.GREEN + "-"*50 + bright.RESET)
                      print(bright.GREEN + f"{ug_course[select]['course']:<25}{ug_course[select]['duration']:<14}{ug_course[select]['fees']:<25}" + bright.RESET)
                      
                      while True:
                        feesPay = int(input(bright.BLUE + "\nHow Much You Pay Now : " + bright.RESET))
                            
                        if feesPay >= 5000 and feesPay <= ug_course[select]['fees']:
                              while True:
                                password = input("\n" + bright.BLUE + "Create Password for Student Login : " + bright.RESET)                                                        
                                comfirm_password = input("\n" + bright.BLUE + "Comfirm Password : " + bright.RESET)                                                        

                                if password == comfirm_password:
                                        print("\n\t" + bright.CYAN + "-"*35 + bright.RESET)
                                        print(bright.CYAN + "\t\tStudent Information" + bright.RESET)
                                        print("\t" + bright.CYAN + "-"*35 + bright.RESET)
                                        print(bright.CYAN + f"\n\tStudent Account Password : {password}" + bright.RESET)
                                        print(bright.CYAN + f"\n\tStudent Name : {name}" + bright.RESET)
                                        print(bright.CYAN + f"\tStudent Address : {address}" + bright.RESET)
                                        print(bright.CYAN + f"\tStudent Phone no. : {phone}" + bright.RESET)
                                        print(bright.CYAN + f"\tStudent Email ID : {email}" + bright.RESET)
                                        print(bright.CYAN + f"\tDegree Type : {graduation.upper()}" + bright.RESET)
                                        print(bright.CYAN + f"\tCourse Name : {ug_course[select]['course']}" + bright.RESET)
                                        print(bright.CYAN + f"\tPending Fees : {ug_course[select]['fees'] - feesPay}" + bright.RESET)
                                        print(bright.GREEN + "\nAddmission Book Successfully..." + bright.RESET)
                                        studentAdd = {
                                                "Student Password" : password,
                                                "Student Name" : name.lower(),
                                                "Student Address" : address,
                                                "Student Phone no." : phone,
                                                "Student Email ID" : email,
                                                "Degree Type" : graduation.upper(),
                                                "Course Name" : ug_course[select]['course'],
                                                "Fees" : ug_course[select]['fees'],
                                                "Pending Fees" : ug_course[select]['fees'] - feesPay, 
                                        }
                                        studentFile = open("ug_student.txt","a")
                                        studentFile.write(str(studentAdd) + "\n")
                                        studentFile.close()
                                        break
                                else:
                                      print(bright.RED + "Error : Password not matchh!!" + bright.RESET)
                                      break

                              break
                        else:
                              print(bright.RED + "Minimmum 5000 Pay for confirm addmission." + bright.RESET)

                else:
                              print(bright.RED + "\nError : Input not matchh!!" + bright.RESET)

                break

        elif graduation.lower() == "pg":
                print(bright.MAGNETA + "-"*80 + bright.RESET)
                print(bright.MAGNETA + f"{'No':<5}{'Course':<40}{'Duration':<14}{'Fees':<25}" + bright.RESET)
                print(bright.MAGNETA + "-"*80 + bright.RESET)
                for k,v in pg_course.items():
                        print(bright.MAGNETA + f"{k:<5}{v['course']:<40}{v['duration']:<14}{v['fees']:<25}" + bright.RESET)
                
                select = int(input(bright.BLUE + "\nSelect Course Number : " + bright.RESET))
                
                if select in pg_course:
                              print("\n")
                              print(bright.GREEN + "-"*50 + bright.RESET)
                              print(bright.GREEN + f"{'Course':<25}{'Duration':<14}{'Fees':<25}" + bright.RESET)
                              print(bright.GREEN + "-"*50 + bright.RESET)
                              print(bright.GREEN + f"{pg_course[select]['course']:<25}{pg_course[select]['duration']:<14}{pg_course[select]['fees']:<25}" + bright.RESET)
                                      
                              while True:
                                feesPay = int(input(bright.BLUE + "\nHow Much You Pay Now : " + bright.RESET))
                                            
                                if feesPay >= 5000 and feesPay <= pg_course[select]['fees']:    
                                      while True:
                                        password = input("\n" + bright.BLUE + "Create Password for Student Login : " + bright.RESET)                                                        
                                        comfirm_password = input("\n" + bright.BLUE + "Comfirm Password : " + bright.RESET)                                                        
                                        
                                        if password == comfirm_password:                                                    
                                                print("\n\t" + bright.CYAN + "-"*35 + bright.RESET)
                                                print(bright.CYAN + "\t\tStudent Information" + bright.RESET)
                                                print("\t" + bright.CYAN + "-"*35 + bright.RESET)
                                                print(bright.CYAN + f"\n\tStudent Name : {name}" + bright.RESET)
                                                print(bright.CYAN + f"\tDegree Type : {graduation.upper()}" + bright.RESET)
                                                print(bright.CYAN + f"\tCourse Name : {pg_course[select]['course']}" + bright.RESET)
                                                print(bright.CYAN + f"\tPayed Fees : {feesPay}" + bright.RESET)
                                                print(bright.GREEN + "\nAddmission Book Successfully..." + bright.RESET)
                                                studentAdd = {
                                                        "Student Password" : password,
                                                        "Student Name" : name.lower(),
                                                        "Student Address" : address,
                                                        "Student Phone no." : phone,
                                                        "Student Email ID" : email,
                                                        "Degree Type" : graduation.upper(),
                                                        "Course Name" : pg_course[select]['course'],
                                                        "Fees" : pg_course[select]['fees'],
                                                        "Pending Fees" : pg_course[select]['fees'] - feesPay, 
                                                        }
                                                studentFile = open("pg_student.txt","a")
                                                studentFile.write(str(studentAdd) + "\n")
                                                studentFile.close()
                                                break
                                        else:
                                                print(bright.RED + "Error : Password not matchh!!" + bright.RESET)
                                                break

                                        

                                      break
                                        
                                             
                                else:
                                      print(bright.RED + "Error : Minimmum 5000 Pay for confirm addmission." + bright.RESET)
        
                else:
                                      print(bright.RED + "\nError : Input not matchh!!" + bright.RESET)
                
                break
        else:
                print(bright.RED + "\nError : choose only UG/PG..." + bright.RESET)

def studentPage():
        print("\n\t" + bright.YELLOW + "-"*35 + bright.RESET)
        print("\t\t" + bright.YELLOW + "Student Page" + bright.RESET)
        print("\t" + bright.YELLOW + "-"*35 + bright.RESET + "\n")
        while True:

                print("\t\t" + bright.MAGNETA + "1. Student Login" + bright.RESET)
                print("\t\t" + bright.MAGNETA + "2. Exit" + bright.RESET + "\n")

                select = int(input(bright.BLUE + "Select Number : " + bright.RESET))

                if select == 1:
                        name = input(bright.BLUE + "Enter Student Name : " + bright.RESET)
                        phone = int(input(bright.BLUE + "Enter Student Phone No. : " + bright.RESET))
                        graduation = input(bright.BLUE + "Select UG/PG : " + bright.RESET)
                        password = input(bright.BLUE + "Enter Student Password : " + bright.RESET)

                        if graduation.lower() == "ug":
                                with open("ug_student.txt","r") as file:
                                        for line in file:
                                                data = ast.literal_eval(line)
                                                if data['Student Name'] == name.lower() and data['Student Phone no.'] == phone:
                                                        if data['Student Password'] == password:
                                                                print("\n\t" + bright.CYAN + "-"*35 + bright.RESET)
                                                                print(bright.CYAN + "\t\tStudent Information" + bright.RESET)
                                                                print("\t" + bright.CYAN + "-"*35 + bright.RESET)
                                                                print(bright.CYAN + f"\n\tStudent Password : {data['Student Password']}" + bright.RESET)
                                                                print(bright.CYAN + f"\n\tStudent Name : {data['Student Name']}" + bright.RESET)
                                                                print(bright.CYAN + f"\tStudent Address : {data['Student Address']}" + bright.RESET)
                                                                print(bright.CYAN + f"\tStudent Phone no. : {data['Student Phone no.']}" + bright.RESET)
                                                                print(bright.CYAN + f"\tStudent Email ID : {data['Student Email ID']}" + bright.RESET)
                                                                print(bright.CYAN + f"\tDegree Type : {data['Degree Type']}" + bright.RESET)
                                                                print(bright.CYAN + f"\tCourse Name : {data['Course Name']}" + bright.RESET)
                                                                print(bright.CYAN + f"\tPending Fees : {data['Pending Fees']}" + bright.RESET + "\n")
                                                                break
                                                        else:
                                                                print("\n" + bright.RED + "Error : Password not matchh!!" + bright.RESET)
                                                else:
                                                                print("\n" + bright.RED + "Error : Student not exits in data...." + bright.RESET)

                        elif graduation.lower() == "pg":
                                with open("pg_student.txt","r") as file:
                                        for line in file:
                                                data = ast.literal_eval(line)
                                                if data['Student Name'] == name.lower() and data['Student Phone no.'] == phone:
                                                        if data['Student Password'] == password:
                                                                print("\n\t" + bright.CYAN + "-"*35 + bright.RESET)
                                                                print(bright.CYAN + "\t\tStudent Information" + bright.RESET)
                                                                print("\t" + bright.CYAN + "-"*35 + bright.RESET)
                                                                print(bright.CYAN + f"\n\tStudent Password : {data['Student Password']}" + bright.RESET)
                                                                print(bright.CYAN + f"\n\tStudent Name : {data['Student Name']}" + bright.RESET)
                                                                print(bright.CYAN + f"\tStudent Address : {data['Student Address']}" + bright.RESET)
                                                                print(bright.CYAN + f"\tStudent Phone no. : {data['Student Phone no.']}" + bright.RESET)
                                                                print(bright.CYAN + f"\tStudent Email ID : {data['Student Email ID']}" + bright.RESET)
                                                                print(bright.CYAN + f"\tDegree Type : {data['Degree Type']}" + bright.RESET)
                                                                print(bright.CYAN + f"\tCourse Name : {data['Course Name']}" + bright.RESET)
                                                                print(bright.CYAN + f"\tPending Fees : {data['Pending Fees']}" + bright.RESET + "\n")
                                                                break
                                                        else:
                                                                print("\n" + bright.RED + "Error : Password not matchh!!" + bright.RESET)
                                                else:
                                                                print("\n" + bright.RED + "Error : Student not exits in data...." + bright.RESET)
                elif select == 2:
                       print("\n" + bright.CYAN + "Exit from student page..." + bright.RESET)
                       break
                else:
                       print("\n" + bright.RED + "Error : invlid number selected..." + bright.RESET)
                                                   

def facultyPage():
        print("\n\t" + bright.YELLOW + "-"*35 + bright.RESET)
        print("\t\t" + bright.YELLOW + "Faculty Page" + bright.RESET)
        print("\t" + bright.YELLOW + "-"*35 + bright.RESET + "\n")

        while True:
                print("\n")
                print("\t\t" + bright.MAGNETA + "1. Faculty Register" + bright.RESET)
                print("\t\t" + bright.MAGNETA + "2. Faculty Login" + bright.RESET)
                print("\t\t" + bright.MAGNETA + "3. Exit" + bright.RESET + "\n")
        
                select = int(input(bright.BLUE + "Select Number : " + bright.RESET))
        
                if select == 1:
                        print("\n")
                        name = input(bright.BLUE + "Enter Your Name : " + bright.RESET)
                        phone = int(input(bright.BLUE + "Enter Your Phone no. : " + bright.RESET))
                        email = input(bright.BLUE + "Enter Your Email ID : " + bright.RESET)
                        graduation = input(bright.BLUE + "Enter Your Graduation : " + bright.RESET)
                        experince = int(input(bright.BLUE + "Enter Your Experince : " + bright.RESET))
                        password = input(bright.BLUE + "Create Password : " + bright.RESET)
                        cmfirmPass = input(bright.BLUE + "Confirm Password : " + bright.RESET)

                        if password == cmfirmPass:
                               facultyInfo = {
                                      "Faculty Password" : password,
                                      "Faculty Name" : name,
                                      "Faculty Phone No." : phone,
                                      "Faculty Email ID" : email,
                                      "Faculty Graduation" : graduation,
                                      "Faculty Experince" : experince,
                               }

                               facultyFile = open("faculty.txt","a")
                               facultyFile.write(str(facultyInfo) + "\n")
                               facultyFile.close()

                               print("\n" + bright.GREEN + "Faculty Register Successfully..." + bright.RESET)
                               break

                        else:
                               print("\n" + bright.RED + "Error : Password not matchh!!" + bright.RESET)
                               break

                elif select == 2:
                     while True:  
                        print("\n") 
                        name = input(bright.BLUE + "Enter Faculty Name : " + bright.RESET)
                        phone = int(input(bright.BLUE + "Enter Your Phone no. : " + bright.RESET))
                        password = input(bright.BLUE + "Create Password : " + bright.RESET)

                        with open("faculty.txt","r") as file:
                               for line in file:
                                   data = ast.literal_eval(line)
                                   if data['Faculty Name'] == name and data['Faculty Phone No.'] == phone:
                                        if data['Faculty Password'] == password:
                                                print("\n\t" + bright.CYAN + "-"*35 + bright.RESET)
                                                print(bright.CYAN + "\t\tFaculty Information" + bright.RESET)
                                                print("\t" + bright.CYAN + "-"*35 + bright.RESET)
                                                print(bright.CYAN + f"\n\tFaculty Name : {data['Faculty Name']}" + bright.RESET)
                                                print(bright.CYAN + f"\n\tFaculty Phone No. : {data['Faculty Phone No.']}" + bright.RESET)
                                                print(bright.CYAN + f"\n\tFaculty Email ID. : {data['Faculty Email ID']}" + bright.RESET)
                                                print(bright.CYAN + f"\n\tFaculty Graduation : {data['Faculty Graduation']}" + bright.RESET)
                                                print(bright.CYAN + f"\n\tFaculty Experince : {data['Faculty Experince']}" + bright.RESET)

                                                break
                                        else:
                                                print(bright.RED + f"\nError : Password not matchh!!" + bright.RESET)
                                                break
                                         

                        break
                elif select == 3:
                       print("\n" + bright.CYAN + "Exit from faculty page..." + bright.RESET)
                       break
                else:
                       print("\n" + bright.RED + "Error : Invalid number seleted..." + bright.RESET)               
                                          

def main():
    print("\n\t" + bright.YELLOW + "-"*42 + bright.RESET)
    print("\t\t" + bright.YELLOW + "Sanatana Dhrma University" + bright.RESET)
    print("\t" + bright.YELLOW + "-"*42 + bright.RESET)

    while True:
        menu = """
                1. Student Addmission
                2. Student Login/SignUp
                3. Faculty Login/SignUp
                4. Exit
                """
        print(bright.MAGNETA + menu + bright.RESET)
        choice = int(input(bright.BLUE + "Enter Your Choice : " + bright.RESET))
        
        if choice == 1:
                studentAddmission()
        elif choice == 2:
                studentPage()
        elif choice == 3:
                facultyPage()
        elif choice == 4:
                print("\n" + bright.CYAN + "Thanks for visit university" + bright.RESET + "\n")
                break
        else:
            print("\n" + bright.RED + "Error : Press Invalid Input..." + bright.RESET + "\n")



if __name__ == "__main__":
    main()