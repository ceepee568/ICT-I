students_list=[]
students_set=()
students_dict={}

students_list.append("Sangay Phuntsho")
students_set=("age:18 and grade:12" )
students_dict["Sangay Phuntsho"]="age:18 and grade:12" 

students_list.append("Wangchuk Dema")
students_set=("age:18 and grade:12" )
students_dict["Wangchuk Dema"]="age:18 and grade:12" 

students_list.append("Dorji Seldon")
students_set=("age:18 and grade:12" )
students_dict["Dorji Seldon"]="age:18 and grade:12" 

students_list.append("Namdrel Zangpo")
students_set=("age:18 and grade:12" )
students_dict["Sangay Phuntsho"]="age:18 and grade:12" 

search_name=input("Enter the name to search: ")
if search_name in students_list:
    print(f"Name has been found! The name of the book {search_name} is {students_dict[search_name]}")
else:
    print("Name not found!")

