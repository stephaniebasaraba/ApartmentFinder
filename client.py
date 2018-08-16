from tenant import Tenant
from tenant_database import Tenant_DB
import apartment
from apartment_db import Apartment_DB

apartment_db = Apartment_DB() # Create apartment_db
apartment_db.loadApartments('apartment_data.txt')

tenant_db = Tenant_DB() # Create tenant_db
tenant = Tenant('John', 'Doe', 123) # Create tenant
tenant_db.addTenant(tenant) # Test add Tenant to tenant_db

def labMenu():
    print('Enter 1 to rent or lease apartment')
    print('Enter 2 to search available apartments')
    print('Enter 3 to make apartment available')
    print('Enter 4 to list available apartments')
    print('Enter 5 to list rented apartments')
    print('Enter 6 to display tenant information')
    print('Enter 7 to add new apartment')
    print('Enter 8 to exit the program')

done = False

while not done:
    labMenu()
    choice = int(input('Please make an entry: '))

    if choice == 1:
        apartment_list = []
        num_bed = int(input('Minimum number of bedrooms: '))
        num_bath = int(input('Minimum number of bathrooms: '))
        max_rent = int(input('Maximum rent: '))

        for apartment in apartment_db.apartments:
            if apartment.apt_bedrm >= num_bed and apartment.apt_baths >= num_bath and apartment.apt_rent <= max_rent:
                apartment_list.append(apartment.apt_num)
                print('Apartment number: {}, Beds: {}, Bath: {}, Rent: ${}').format(apartment.apt_num, apartment.apt_bedrm, apartment.apt_baths, apartment.apt_rent)

        if apartment_list == []:
            print('No apartments match your search criteria.')

        if apartment_list != []:
            lease_option = int(input('Enter apartment number to lease apartment or -1 to exit: '))
            if lease_option != -1:
                first_name = input('Enter your first name: ')

        pass

    elif choice == 2:
        apartment_list = []
        num_bed = int(input('Minimum number of bedrooms: '))
        num_bath = int(input('Minimum number of bathrooms: '))
        max_rent = int(input('Maximum rent: '))

        for apartment in apartment_db.apartments:
            if apartment.apt_bedrm >= num_bed and apartment.apt_baths >= num_bath and apartment.apt_rent <= max_rent:
                apartment_list.append(apartment.apt_num)
                print('Apartment number: {}, Beds: {}, Bath: {}, Rent: ${}').format(apartment.apt_num, apartment.apt_bedrm, apartment.apt_baths, apartment.apt_rent)
        if apartment_list == []:
            print('No apartments match your search criteria.')
        pass

    elif choice == 3:
       
       pass
    elif choice == 4:
        apartments = apartment_db.getAvailApartments()
        for apartment in apartments:
            print('Apartment Status: {}, Apartment number: {}, Beds: {}, Bath: {}, Rent: ${}').format(apartment.apt_status, apartment.apt_num, apartment.apt_bedrm, apartment.apt_baths, apartment.apt_rent)

        # pass
    elif choice == 5:

        pass
    elif choice == 6:

        aptNum = int(input('Enter apartment number: '))
        if tenant.tenant_aptNum == aptNum:
            print('Tenant name: ' + tenant.tenant_fName)

        pass
    elif choice == 7:
        apt_num = int(input('Enter apartment number: '))
        apt_bedrm = int(input('Enter number of bedrooms: '))
        apt_baths = int(input('Enter number of bathrooms: '))
        apt_rent = int(input('Enter apartment rent: '))

        new_apartment = apartment.Apartment(apt_num, apt_bedrm, apt_baths, apt_rent, 'A')
        apartment_db.addApartment(new_apartment)

        pass    
    elif choice == 8:
        num_apt_total
        num_apt_rented
        num_apt_avail
        total_num_tenants

        done = True
    
