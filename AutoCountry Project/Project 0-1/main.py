AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ] # Program dataset

# Function that is run upon execution of the program
def onLoad():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit\n")
    user_input = input()

    match user_input:

        case "1":
            printVehicles()

        case "2":
            searchVehicles()

        case "3":
            exitProgram()

def printVehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    # Iterate over AllowedVehiclesList and print each item
    for vehicle in AllowedVehiclesList:
        print(vehicle)
    print("")
    onLoad()

def searchVehicles():
    vehicle_name = input("Please Enter the full Vehicle name: ")
    vehicle_is_allowed = False
    for vehicle in AllowedVehiclesList:
        if vehicle == vehicle_name:
            vehicle_is_allowed = True

    if vehicle_is_allowed:
        pass
    else:
        pass
    

def exitProgram():
    # Print thank-you message
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")

onLoad()
