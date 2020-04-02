“ApartmentFinder” is a Python program for a small property management company to steam line their apartment rental process and keep track of available and leased apartments.

At program start, data from the file apartment_data.txt is populated into the database. The user is then prompted to enter an option from the following menu items below.

MENU OPTIONS

1.)	Rent/Lease Apartment
The user is prompted to enter a minimum number of bedrooms required, a minimum number of baths required, and maximum amount of rent the user is willing to pay.  The program searches the apartments database and display apartments that meet the user’s requirements. 

If the user decides to continue with the lease, the program will prompt the user for the following information: first name and last name.  Once the user’s entry is complete, the program will create a tenant and add the tenant to the Tenants database.  The selected apartment status must be changed to rented (‘R’)

2.)	Search Available Apartments
The user is prompted to enter a minimum number of bedrooms required, a minimum number of baths required, and maximum rent amount the user is willing to pay.  The program displays a list of available apartments that meet the user’s requirements. If the search result is 0, display an appropriate message

3.)	Make Apartment Available
The user is prompted for the apartment number.  The program searches for the corresponding apartment.  If the apartment is currently under lease, the program changes the apartment status to available and deletes the current tenant from the Tenants database.  If the apartment is not currently under lease, the program displays a message informing the user that the apartment is already available.  If no apartment is found with the apartment number entered, the program displays an appropriate message

4.) List Available Apartments
Searches the apartments database and displays all available apartments

5.)	List Rented/Leased Apartments
Search the apartments and tenants databases and displays details about each rented apartment (apartment number, number of  
bedrooms, number of baths, rent amount, tenant id, and tenant name)

6.)	Display Tenant Information
Prompts the user for the apartment number.  If the apartment is found and under lease, details about the current tenant are displayed.  If the apartment is not currently under rent, the program displays message indicating that the apartment is available for rent.  If the apartment was not found with that number, an error is displayed.

7.)	Add New Apartment
The program prompsts the user for the apartment details (apartment number, number of bed rooms, number of baths, rent amount) and adds the apartment to the apartments database as an available apartment.

8.	Exit
Displays a summary report (total number of apartments, total number of apartments under lease, total number of apartments available, total number of tenants) and exits the program

MODULE DEFINITIONS:

Client module (client.py)
This module is the gateway to the program.  The logic in this module allows the user to interact with the program and perform all required operations.  All menu options are accessible in this module.  Classes created in other modules are mainly instantiated in this module.  Selection of a menu option initiates call(s) to various class methods.

Tenant Module (tenant.py)
This module contains class Tenant which contains attributes and methods for a tenant: tenant id (tenant_id), tenant first name (tenant_fName), tenant last name (tenant_lName), and apartment number (tanant_aptNum).  This class only gets methods for the attributes; the constructor in this class allows the first and last names and the apartment number to be passed as arguments.  The values passed to the constructor initialize the class attributes: tenant_fName, tenant_lName, and tenant_aptNum.  Tenant id is a 5-digit integer generated in the class when the class constructor is called. 

Tenants database module (tenant_database.py)
This module contains class Tenant_db used to store all tenants.  The class includes a list (tenants) as the tenants database.  Each item in the list is a Tenant object.  The constructor for this class takes no arguments; once an instance of the class is created, tenants is initialized as an instance variable containing an empty list.  The following methods are included in the class:
1.) addTenant: This method takes one parameter.  When this method is called it is passed a Tenant object.  This method adds a tenant to the Tenant database.  This method does not return a value
2.) getTenant: This method takes an apartment number as parameter and returns the tenant associated with the apartment.  If no tenant is found, the method returns a blank string
3.) countTenants:  This method takes no parameters.  It returns the number of tenants in the Tenants database
4.) removeTenant: This method takes the apartment number as a parameter.  It deletes the tenant associated with the apartment number and returns the tenant.  If no tenant is found, the method returns an empty string
5.) getAllTenants: This method takes no parameters.  It returns all tenant in the Tenants database

Apartment module (apartment.py)
This module contains the class Apartment used to create apartments. The class includes the following attributes: apartment number (apt_num), number of bedrooms (apt_bedrm), number of baths (apt_baths), rent amount (apt_rent), and apartment status (apt_status).  Each attribute includes a get and set method. The arguments passed to the class constructor should be used to initialize the class attributes.  The apartment class is used in the client module and the apartment database module.

Apartment database module (apartment_db.py)
This module includes class Apartment_db used to store and retrieve apartments and also perform rental operations.  This class contains instance variable, apartments (list), which stores the apartments details.  The constructor of this class takes no arguments.  Once an instance of the class is created, the apartments variable will be created as an empty list.  The following methods are included in this class:
1.) addApartment: This method takes an apartment object as argument and add the apartment to the apartments list.  Once the apartment is added, the method with print a message indicating the apartment was successfully added.  This method does not return a value
2.) getApartment: This method takes an apartment number as parameter and returns the apartment associated with the apartment number
3.)	getAvailApartments: This method takes no parameters.  It returns all apartments with ‘A’ status
4.)	getRentedApartements: This method takes no parameters.  It returns all apartments with status equal to ‘R’ 
5.)	changeApartmentStatus: This method takes an apartment number and status value (‘R’ or ‘A’) as parameters.  If the apartment is found, this method changes the status of the corresponding apartment.  Status should be set to ‘R’ if the apartment needs to be status as rented or ‘A’ if the apartment needs to be made available.  If the current status of the apartment is the same as the value passed, display a message indicating that the apartment status was not changed.  If the apartment was not found, display a message that the apartment number is not valid.  This method does not return a value  
6.)	getTotalApartments: This method takes no parameters.  It returns a count of the apartments in the database
7.)	getTotalAvailable: This method takes no parameters. It returns a count of the available apartments
8.)	getTotalRented: This method takes no parameters. It returns a count of rented apartments
9.)	loadApartments: This method takes a file as parameter.  It loads apartments into the apartments database from a file.  Each apartment will have a status of ‘A’.  This method does not return a value





