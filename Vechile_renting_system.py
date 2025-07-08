#Car rental program
print("------WELCOME TO VEHICLE RENTING SYSTEM------")
name = input("Enter your full name: ")
print("Select the type of vehicle you want to rent:")
print("1. Car")
print("2. Bike")
print("3. Scooter")
vehicle_type = int(input("Enter the number corresponding to your choice: "))

if vehicle_type == 1:
    vehicle = "Car"
    print("\n------AVAILABLE CAR MODELS------")
    print("1. Mercedes Benz  -	5000")
    print("2. BMW X5         -  4800")
    print("3. Toyota Innova	 -  3000")
    print("4. Honda City	 -  2500")
    car_type=int(input("\nEnter the number corresponding to your choice: "))
    days =int(input("Enter the number of days you want to rent: "))
    
    if car_type==1:
        rent = days*5000
        vehicle_model = "Mercedes Benz"
        rent_perday = 5000
    elif car_type==2:
        rent = days*4800
        vehicle_model = "BMW X5"
        rent_perday = 4800
    elif car_type==3:
        rent = days*3000
        rent_perday = 3000
        vehicle_model = "Toyota Innova"
    elif car_type==4:
        rent = days*2500
        rent_perday = 2500
        vehicle_model = "Honda City"
    else:
        print("Invalid option number !")
        exit()
    
elif vehicle_type==2:
    vehicle = "Bike"
    print("\n------AVAILABLE BIKE MODELS------")
    print("1. Royal Enfield	 -  1200")
    print("2. Yamaha R15     -  1000")
    print("3. KTM Duke	     -  1300")
    print("4. Honda Activa	 -  600")    
    bike_type=int(input("\nEnter the number corresponding to your choice: "))
    days =int(input("Enter the number of days you want to rent: "))

    if bike_type==1:
        rent = days*1200
        rent_perday = 1200
        vehicle_model = "Royal Enfield"
    elif bike_type==2:
        rent = days*1000
        rent_perday = 1000
        vehicle_model = "Yamaha R15"
    elif bike_type==3:
        rent = days*1300
        rent_perday = 1300
        vehicle_model = "KTM Duke"
    elif bike_type==4:
        rent = days*600
        rent_perday = 600
        vehicle_model = "Honda Activa"
    else:
        print("Invalid Option number!")
        exit()

elif vehicle_type==3:
    vehicle = "Scooter"
    print("\n------AVAILABLE SCOOTER MODELS------")
    print("1. Vespa	         -  800")
    print("2. Honda Dio      -  700")
    print("3. Suzuki Access	 -  650")  
    scooter_type=int(input("\nEnter the number corresponding to your choice: "))
    days =int(input("Enter the number of days you want to rent: "))   

    if scooter_type==1:
        rent = days*800
        rent_perday = 800
        vehicle_model="Vespa" 
    elif scooter_type==2:
        rent = days*700
        rent_perday = 700
        vehicle_model="Honda Dio"
    elif scooter_type==3:
        rent = days* 650
        rent_perday = 650
        vehicle_model = "Suzuki Access"
    else:
        print("Invalid Option Number!")
        exit()
    
else:
    print("Invalid Option Number!")
    exit()

print("\n\n================= VEHICLE RENTAL BILL =================")
print(f"Customer Name          :  {name}")
print(f"Vehicle Type           :  {vehicle}")
print(f"Model Selected         :  {vehicle_model}")
print(f"Rent Per Day           :  ₹{rent_perday}")
print(f"Number of Days Rented  :  {days}")
print("\n-------------------------------------------------------")
print(f"Total Amount           :  {rent}")
print("=======================================================")
print("Thank you for choosing Umehani's Rental Service! 💖")
print("Drive safe and see you again soon! 🚗✨")

