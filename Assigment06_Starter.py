# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# Rachel M Woo, 5. 14 through 16. 2021,Modified code to complete assignment 6
# Rachel M Woo, 5. 16 through 18. 2021, run the script and debugging to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        #list_of_rows.clear()  # clear current data
        objFile = open('ToDoFile.txt', "r")
        for row in objFile:
            lstRow = row.split(",")
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
            lstTable.append(dicRow)
            for dicRow in lstTable:
                print(dicRow["Task"] + " - " + dicRow["Priority"])

        objFile.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        # TODO: Add Code Here!
        print("Type in a 'Task' and 'Priority' for your To Do List")
        objFile = open('ToDoFile.txt', "w")
        strTask = input("Enter a Task: ")
        strPriority = input("Enter a Priority: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        objFile.close()
        print("Your data has been saved to ToDoFile.txt")

        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        # TODO: Add Code Here!
        print("Type in a 'Task' you would like to remove")
        strRemove = input("Enter a Task: ")
        for dicRow in lstTable:
            if strRemove.lower() == dicRow["Task"].lower():
                lstTable.remove(dicRow)

        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # TODO: Add Code Here!
        objFile = open('ToDoFile.txt', "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + ',' + dicRow["Priority"] + '\n')
        objFile.close()

        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for dicRow in lstTable:
            print(dicRow["Task"] + " - " + dicRow["Priority"])

        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        pass  # TODO: Add Code Here!
        print("Type in a new 'Task' and 'Priority' for your To Do List")
        strTask = input("Enter a Task: ")
        strPriority = input("Enter a Priority: ")
        # Add a new item to the List(Table) each time the user makes that choice
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Your data has been saved to ToDoList.txt")

        # return task, priority
        return list_of_rows, 'Success'
    @staticmethod
    def input_task_to_remove():
        pass  # TODO: Add Code Here!
        print("Type in a 'Task' you would like to remove")
        strRemove = input("Enter a Task: ")
        for dicRow in lstTable:
            if strRemove.lower() == dicRow["Task"].lower():
                lstTable.remove(dicRow)

        return list_of_rows, 'Success'

    # return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file('ToDoFile.txt', lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Add Code Here
        print("Type in a 'Task' and 'Priority' for your To Do List")
        strTask = input("Enter a Task: ")
        strPriority = input("Enter a Priority: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)

        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Add Code Here
        print("Type in a 'Task' you would like to remove")
        strRemove = input("Enter a Task: ")
        for dicRow in lstTable:
            if strRemove.lower() == dicRow["Task"].lower():
                lstTable.remove(dicRow)

        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # TODO: Add Code Here!
            strFile = open("ToDoFile.txt", "w")
            for dicRow in lstTable:
                strFile.write(dicRow["Task"] + "," + dicRow["Priority"])
            print("Data - saved!")

            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            # TODO: Add Code Here!
            objFile = open("ToDoFile.txt", "w")
            for row in lstTable:
                objFile.write(strTask[0] + "," + strPriority[1])
            print("Data - saved!")

            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  #  Exit Program
        print("Goodbye!")
        break   # and Exit
