import ast
# select = int(input(bright.BLUE + "\nSelect Course Number : " + bright.RESET))

# if select in ug:
#     print(select, " : ",ug[select])


# for k,v in pg_course.items():
#                         print(bright.MAGNETA + f"{k:<5}{v['course']:<40}{v['duration']:<14}{v['fees']:<25}" + bright.RESET)
     

with open("faculty.txt","r") as file:
    for line in file:
        data = ast.literal_eval(line)
        if data['Faculty Name'] == "kumar" and data['Faculty Phone No.'] == 654321:
            if data['Faculty Password'] == "kumarsanu":
                print(f"\n\tFaculty Name : {data['Faculty Name']}")
                print(f"\n\tFaculty Phone No. : {data['Faculty Phone No.']}")
                print(f"\n\tFaculty Email ID. : {data['Faculty Email ID']}")
                print(f"\n\tFaculty Graduation : {data['Faculty Graduation']}")
                print(f"\n\tFaculty Experince : {data['Faculty Experince']}")
                break
            else:
                print("not match")
        