# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <Zhihua Shang>,<06/16/2020>,Modified code to complete assignment 8
# <Zhihua Shang>,<06/17/2020>,Modified code to complete assignment 8
# <Zhihua Shang>,<06/18/2020>,Modified code to complete assignment 8

# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:strFileName

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
        def __str__(self):
        return self.product_name + "," + str(self.product_price)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Zhihua Shang>,<06/16/2020>,Modified code to complete assignment 8
    """
    # -- NO Field in this class--
    # --Constructor--
    def __init__(self,product_name,product_price):
        # --Attributes--
        self.__product_name=product_name
        self.__product_price=product_price
    # --properties--
    # product_name
    @property
    def product_name(self): # getter or accessor
        return str(self.__product_name).title()  # title case
    @product_name.setter # the name must match the property's
    def product_name(self,value): # setter or mutator
        if str(value).isnumeric()==False:  # the product_name is a string and can not use numbers
            self.__product_name=value
        else:
            raise Exception("Name can not be numbers")

    # product_price
    @property
    def product_price(self):# getter or accessor
        return str(self.__product_price).title()   # title case
    @product_price.setter  # the name must match the property's
    def product_price(self,value):
        if str(value).isnumeric()==True: # the product_price is a number and can not use strings.
            self.product_price=value
        else:
            raise Exception("Price has to be numbers only")

    # --Methods--
    def __str__(self):
        return self.product_name + "," + str(self.product_price)
    # --End of class --

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Zhihua Shang>,<6/18/2020>,Modified code to complete assignment 8
    """
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ save data from a file into a list of dictionary rows

         :param file_name: (string) name of file
         :param list_of_product_objects: (list) you want to fill product data with this file
         :return: (bool) whether or not saved sucessfully
         """
        savedStatusSuccessfully = False
        try: # error handling
            datafile=open(file_name,'w') # write the data into a file
            for row in list_of_product_objects:
                datafile.write(row.__str__()+'\n')
            datafile.close()
            savedStatusSuccessfully=True
        except Exception as e:
            print(e)
        return savedStatusSuccessfully

    @staticmethod
    def read_data_from_file(file_name):
        """ Read data from the file into a list
        :param file_name: (string) name of the file
        :return: (list) rows of product
        """

        list=[]
        try: # error handling
            datafile=open(file_name,"r")
            for line in datafile:
                data=line.split(",")
                row=Product(data[0],data[1])
                list.append(row)
            datafile.close()
        except Exception as e:
            print(e)
        return list



# Presentation (Input/Output)  -------------------------------------------- #
class IO:

    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show user current data in the list of product objects
        2) Let user add data to the list of product objects
        3) Let user save current data to file
        4) Exit program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_data_in_list(list_of_rows):
        """ Shows the current product and price in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print('The current products are: ')
        for row in list_of_rows:
            print(row.product_name + ':' + row.product_price)
        print()  # Add an extra line for looks

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product_and_price():
        # use variables to capture users' input
        productName = str(input('Enter product name that you want to add: '))
        productPrice = float(input('Enter product price: '))
        return Product(product_name=productName,product_price=productPrice)



# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
try: # error handling
    lstOfProductObjects=FileProcessor.read_data_from_file(strFileName)

    while True:
        # Show user a menu of options
        IO.print_menu()
        # Get user's menu option choice
        userchoice=IO.input_menu_choice()
        if userchoice=='1':
             # Show user current data in the list of product objects
            IO.print_current_data_in_list(lstOfProductObjects)
            continue
        elif userchoice=='2':
            # Let user add data to the list of product objects
            lstOfProductObjects.append(IO.input_new_product_and_price())
            continue
        elif userchoice=='3':
            # let user save current data
            FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
            continue
        elif userchoice=='4':
            # to file exit program
            break
except Exception as e:
    print('There is an error!')
    print(e)








