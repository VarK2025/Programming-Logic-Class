from pathlib import Path

# Create Program Data
script_location = Path(__file__).absolute().parent
data_file_location = script_location / "data_file.txt"
AllowedVehiclesList = []

# Define function onLoad that displays menu and gets user input
# In onLoad: if input is 1 run printVehicles, if input is 2 run exitProgram
def onLoad():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.5")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit\n")
    user_input = input()

    match user_input:

        case "1":
            printVehicles()

        case "2":
            searchVehicles()

        case "3":
            addVehicle()

        case "4":
            deleteVehicle()

        case "5":
            exitProgram()

        case _:
            print("Please enter a valid number\n")
            onLoad()

# Define function printVehicles which prints out each item from the Program Data array
# In printVehicles: run onLoad again
def printVehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
    print("")
    onLoad()

# Define function searchVehicles:
# Gets input from user
# Sets vehicle_is_allowed to False
# Iterates over AllowedVehiclesList, if input is in the list sets vehicle_is_allowed to True
# Outputs different messages based on value of vehicle_is_allowed
def searchVehicles():
    vehicle_name = input("Please Enter the full Vehicle name: ")
    vehicle_is_allowed = False
    for vehicle in AllowedVehiclesList:
        if vehicle == vehicle_name:
            vehicle_is_allowed = True

    if vehicle_is_allowed:
        print(vehicle_name + " is an authorized vehicle\n")
    else:
        print(vehicle_name + " is not an authorized vehicle, if you received this in error please check the spelling and try again\n")

    onLoad()

# Define function addVehicle:
# Gets input from user
# Appends input to AllowedVehiclesList
# Restates user's input
# Saves the updated AllowedVehiclesList to the data file
def addVehicle():
    vehicle_name = input("Please Enter the full Vehicle name you would like to add: ")
    AllowedVehiclesList.append(vehicle_name)
    writeDataToFile(AllowedVehiclesList, data_file_location)
    print("You have added \"" + vehicle_name + "\" as an authorized vehicle\n")


    onLoad()

# Define function deleteVehicle
# Gets vehicle name from user
# Gets confirmation of deletion from user
# If user confirms deletion, vehicle inputted is removed from AllowedVehiclesList
# Restates deletion of vehicle
# Saves the updated AllowedVehiclesList to the data file
def deleteVehicle():
    vehicle_name = input("Please Enter the full Vehicle name you would like to REMOVE: ")
    if vehicle_name in AllowedVehiclesList:
        confirmation = input("Are you sure you want to remove \"" + vehicle_name + "\" from the Authorized Vehicles List?\n")
        if confirmation.lower() == "yes":
            AllowedVehiclesList.remove(vehicle_name)
            writeDataToFile(AllowedVehiclesList, data_file_location)
            print("You have REMOVED \"" + vehicle_name + "\" as an authorized vehicle")

    print("\n")
    onLoad()


# Define function exitProgram which prints out Good-bye message
# In exitProgram: Don’t run onLoad again, thereby ending the program
def exitProgram():
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")

# Define function getDataFromFile
# Reads specified file and returns the lines of the file as an array
def getDataFromFile(file_path):
    new_data_array = []
    data_file = open(file_path, "r")
    #for line in data_file:
    #    new_data_array.append(line)
    new_data_array = data_file.read().splitlines()
    data_file.close()
    #print("New data:")
    #print(new_data_array)
    return new_data_array

# Define function writeDataToFile
# Takes an array and writes each item as a separate line into a specified file
def writeDataToFile(data_arr, file_path):
    data_string = ""
    for item in data_arr:
        data_string += str(item) + "\n"
    data_file = open(file_path, "w")
    data_file.write(data_string)
    data_file.close()

# On execution of program: Populate AllowedVehiclesList with data from the file, run onLoad
AllowedVehiclesList = getDataFromFile(data_file_location)
onLoad()
