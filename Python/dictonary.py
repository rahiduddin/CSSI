students = {"10001578":"Jonathan",
            "10005776":"Elvis",
            "10007543":"Abigail",
            "10008712":"Nusrath",
            "10005151":"Olawale",
            "10006570":"Olivia",
            "10003570":"Rayona",
            "10002576":"Egide",
            "10005789":"Zanif",
            "10002213":"Rahid",
            "10003207":"Imran",}

def studentLookUp(list,name):
    for key in list:
        if name == list[key]:
            return key
    return "Invalid Student Name"

##print studentLookUp (students,"Rahid")




#10001578








#input('Enter Student Name')
#if 'raw_input'in students:
#    print "He's in the system"







#studentLookUp (students,"Jonathan")
# 10001578
#studentLookUp (students,"elvis")
# Invalid Student Name
