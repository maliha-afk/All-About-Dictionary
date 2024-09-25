#dictionary
Atiya={
    "age":12 ,
    "school":"H.A.K.Academy",
    "city":"Mawna",
    "Marks":90.5
}

HAKAcademy_school_details={
    "established":2003,
    "student number": 2000,
    "total teachers":50
}

Bangladesh={
    "National river":"Padma/Jamuna",
    "National anthem":"Amar Sonar Bangla"

}

fruits={
    "bangladesh's national fruit":"Jackfruit",
    "India's national fruit ":"Mango",
    "most expensieve fruit":"Yubari King Melon",
    "most expensieve fruit in bangladesh":"Miyazaki mango"
}


#accesing an element
print(HAKAcademy_school_details("student number"))
print(HAKAcademy_school_details.get("established"))
print(HAKAcademy_school_details["total teachers"])
print(fruits.get["bangladesh's national fruit"])
print(fruits["India's national fruit"])
print(fruits.get["most expensieve fruit"])
print(fruits["most expensieve fruit in bangladesh"])
print(fruits)


#add an element
Atiya["Roll"]=22
print(Atiya)


#update an element
Atiya["Class"]=6
print(Atiya)

#remove
Atiya.pop("age")
print(Atiya)

#key
for key in Bangladesh:
    print(Bangladesh)

#value
for value in Bangladesh.values():
    print(Bangladesh)

    
