def check_data_type (kata,tebakan):
    tebakan = tebakan.lower()
    
    if (type(kata) == str and (tebakan) == "str"):
        print("Jawaban Anda benar")
        return True
        
    elif (type(kata) ==  int and (tebakan) == "int"):
        print("Jawaban Anda benar")
        return True

    elif (type(kata) == int and (tebakan) == "str"):
        print("Jawaban Anda salah, seharusnya adalah : int")
        return False

    elif (type(kata) == str and (tebakan) == "int"):
        print("Jawaban Anda salah, seharusnya adalah : str")
        return False
    else :
        print ("error")
        return False

print(check_data_type("Kevin","STr")) 
print(check_data_type("Kevin","str")) 
print(check_data_type(12345,"str")) 
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))