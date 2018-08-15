import tenant
import tenant_database
import apartment
from apartment_db import Apartment_DB

apartment_db = Apartment_DB() # Create apartment_db
apartment_db.loadApartments('apartment_data.txt')

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
            if apartment.apt_bedrm >= num_bed and apartment.apt_baths >= num_bath:
                # apartment_list.append(apartment)
                print('Apartment number: {}, Beds: {}, Bath: {}, Rent: ${}').format(apartment.apt_num, apartment.apt_bedrm, apartment.apt_baths, apartment.apt_rent)
            
        
        pass
    elif choice == 2:
        
        pass
    elif choice == 3:
       
       pass
    elif choice == 4:

        pass
    elif choice == 5:

        pass
    elif choice == 6:

        pass
    elif choice == 7:

        pass    
    elif choice == 8:
        done = True
    
