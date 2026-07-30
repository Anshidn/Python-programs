def show_details(**kwarks):
    for key , value in kwarks.items():
        print(f"{key} : {value}")

show_details(name = "Anshid" , age = 18 , city = "malappuram")
