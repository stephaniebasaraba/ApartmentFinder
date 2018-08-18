from tenant import Tenant
from tenant_database import Tenant_DB
from apartment import Apartment
from apartment_db import Apartment_DB

apartment_db = Apartment_DB() # Create apartment_db
apartment_db.loadApartments('apartment_data.txt')

tenant_db = Tenant_DB() # Create tenant_db

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
            if apartment.apt_bedrm >= num_bed and apartment.apt_baths >= num_bath and apartment.apt_rent <= max_rent and apartment.apt_status == 'A':
                apartment_list.append(apartment.apt_num)
                print('Apartment number: {}, Beds: {}, Bath: {}, Rent: ${}'.format(apartment.apt_num, apartment.apt_bedrm, apartment.apt_baths, apartment.apt_rent))

        if apartment_list == []:
            print('No apartments match your search criteria.')

        if apartment_list != []:
            lease_option = input('Enter apartment number to lease apartment or -1 to return to the menu: ')
            if lease_option != '-1':
                first_name = input('Enter your first name: ')
                last_name = input('Enter your last name: ')
                new_tenant = Tenant(first_name, last_name, lease_option)
                tenant_db.addTenant(new_tenant)
                for apartment in apartment_db.apartments:
                    if lease_option == apartment.apt_num:
                        apartment.apt_status = 'R'
                print('Tenant added successfully.')

    elif choice == 2:
        apartment_list = []
        num_bed = int(input('Minimum number of bedrooms: '))
        num_bath = int(input('Minimum number of bathrooms: '))
        max_rent = int(input('Maximum rent: '))

        for apartment in apartment_db.apartments:
            if apartment.apt_bedrm >= num_bed and apartment.apt_baths >= num_bath and apartment.apt_rent <= max_rent and apartment.apt_status =='A':
                apartment_list.append(apartment.apt_num)
                print('Apartment number: {}, Beds: {}, Bath: {}, Rent: ${}'.format(apartment.apt_num, apartment.apt_bedrm, apartment.apt_baths, apartment.apt_rent))
        if apartment_list == []:
            print('No apartments match your search criteria.')

    elif choice == 3:
        aptNum = input('Enter apartment number: ')
        avail_apt = apartment_db.getAvailApartments()
        rented_apt = apartment_db.getRentedApartments()
        all_apt = avail_apt + rented_apt
        apt_num_list = []
        avail_num_list = []
        rented_num_list = [[]]
        tenants = tenant_db.getAllTenants()
        for apartment in all_apt:
            apt_num_list.append(apartment.apt_num)
        for apartment in avail_apt:
            avail_num_list.append(apartment.apt_num)
        for apartment in rented_apt:
            rented_num_list.append(apartment.apt_num)

        for apartment in rented_apt:
            if aptNum == apartment.apt_num:
                apartment.apt_status = 'A'
                for tenant in tenant_db.tenants:
                    if tenant.tenant_aptNum == aptNum:
                        tenant_db.removeTenant(aptNum)

        if aptNum in avail_num_list:
            print('This apartment is available.')

        if aptNum not in apt_num_list:
            print('This apartment does not exist.')

    elif choice == 4:
        apartments = apartment_db.getAvailApartments()
        for apartment in apartments:
            print('Apartment Status: {}, Apartment number: {}, Beds: {}, Bath: {}, Rent: ${}'.format(apartment.apt_status, apartment.apt_num, apartment.apt_bedrm, apartment.apt_baths, apartment.apt_rent))

    elif choice == 5:
        apartments = apartment_db.getRentedApartments()
        tenants = tenant_db.getAllTenants()
        for apartment in apartments:
            for tenant in tenants:
                if apartment.apt_num == tenant.tenant_aptNum:
                    print('Apartment Status: {}, Apartment Number: {}, Beds: {}, Bath: {}, Rent: ${}, Tenant Name: {} {}'.format(apartment.apt_status, apartment.apt_num, apartment.apt_bedrm, apartment.apt_baths, apartment.apt_rent, tenant.tenant_fName, tenant.tenant_lName))

    elif choice == 6:
        aptNum = input('Enter apartment number: ')
        avail_apt = apartment_db.getAvailApartments()
        rented_apt = apartment_db.getRentedApartments()
        all_apt = avail_apt + rented_apt
        apt_num_list = []
        avail_num_list = []
        rented_num_list = []
        tenants = tenant_db.getAllTenants()
        for apartment in all_apt:
            apt_num_list.append(apartment.apt_num)
        for apartment in avail_apt:
            avail_num_list.append(apartment.apt_num)
        for apartment in rented_apt:
            rented_num_list.append(apartment.apt_num)

        if aptNum in rented_num_list:
            for tenant in tenants:
                if tenant.tenant_aptNum == aptNum:
                    print('Tenant Name: ' + tenant.tenant_fName + ' ' + tenant.tenant_lName)

        if aptNum not in apt_num_list:
            print('This apartment does not exist.')
        
        if aptNum in avail_num_list:
            print('This apartment is available.')

    elif choice == 7:
        apt_num = int(input('Enter apartment number: '))
        apt_bedrm = int(input('Enter number of bedrooms: '))
        apt_baths = int(input('Enter number of bathrooms: '))
        apt_rent = int(input('Enter apartment rent: '))

        new_apartment = Apartment(apt_num, apt_bedrm, apt_baths, apt_rent, 'A')
        apartment_db.addApartment(new_apartment)
   
    elif choice == 8:
        total_apartments = apartment_db.getTotalApartments()
        available_apartments = len(apartment_db.getAvailApartments())
        rented_apartments = len(apartment_db.getRentedApartments())
        total_tenants = tenant_db.countTenants()

        print('Total Apartments: {}'.format(total_apartments))
        print('Available Apartments: {}'.format(available_apartments))
        print('Rented Apartments: {}'.format(rented_apartments))
        print('Total Tenants: {}'.format(total_tenants))
        done = True
