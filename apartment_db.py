from apartment import Apartment

class Apartment_DB:
    def __init__(self):
        self.apartments = list()

    def addApartment(self,apartment):
        self.apartments.append(apartment)
        print('Apartment added successfully.')

    def getApartment(self,apt_id):
        found_apt = ''
        for apartment in self.apartments:
            if apartment.apt_num == apt_id:
                found_apt = apartment
                break
        return found_apt

    def getAvailApartments(self):
        avail_apts = []
        for apartment in self.apartments:
            if apartment.apt_status == 'A':
                avail_apts.append(apartment.apt_num)
        return avail_apts

    def getRentedApartments(self):
        rented_apts = []
        for apartment in self.apartments:
            if apartment.apt_status == 'R':
                rented_apts.append(apartment.apt_num)
        return rented_apts

    def changeApartmentStatus(self, aptNum, aptStatus):
        for apartment in self.apartments:
            if apartment.apt_num == aptNum:
                if (apartment.apt_status == 'R' and aptStatus == 'A'):
                    apartment.set_apt_status('A')
                    break
                elif (apartment.apt_status == 'A' and aptStatus == 'R'):
                    apartment.set_apt_status('R')
                    break
                else:
                    print(aptStatus + ' is already the apartment status.')
                    break
        return apartment

    def getTotalApartments(self):
        count_apts = 0
        for apartment in self.apartments:
            count_apts += 1
        print('There are a total of ' + str(count_apts) + ' apartments.')
        return count_apts

    def getTotalAvailable(self):
        count_avail = 0
        for apartment in self.apartments:
            if apartment.apt_status == 'A':
                count_avail += 1
        return count_avail

    def getTotalRented(self):
        count_rented = 0
        for apartment in self.apartments:
            if apartment.apt_status == 'R':
                count_rented += 1
        return count_rented

    def loadApartments(self, file):
        apartment_data = open(file)
        for object in apartment_data:
            item = object.split(' ')
            apt_num = item[0]
            apt_bedrm = int(item[1])
            apt_baths = int(item[2])
            apt_rent = int(item[3])
            apt_status = 'A'
            apt_status = apt_status.replace('\n','')
            self.apartments.append(Apartment(apt_num, apt_bedrm, apt_baths, apt_rent, apt_status))
        apartment_data.close()
        

apartment_db = Apartment_DB() # Create apartment_db
apartment_db.loadApartments('apartment_data.txt')
# apartment = Apartment('16F', '1 Bdr', '1 Bath', '$1,500', 'A')
# apartment_two = Apartment('16B', '1 Bdr', '1 Bath', '$1,600', 'R')
# apartment_db.addApartment(apartment)
# apartment_db.addApartment(apartment_two)

# get_apartment = apartment_db.getApartment('16F')
# print(get_apartment.apt_num, get_apartment.apt_rent)

# find available apartments
# avail_apt = apartment_db.getAvailApartments()
# print(avail_apt)

# find rented apartments
# rented_apt = apartment_db.getRentedApartments()
# print(rented_apt)

# change apartment status
# change_status = apartment_db.changeApartmentStatus('101', 'A')
# print(change_status.apt_num, change_status.apt_status)

# count all apartments
# count_apts = apartment_db.getTotalApartments() # Test countTenants method
# print('Total count of apartments: ' + str(count_apts))

# count available apartments
# count_avail = apartment_db.getTotalAvailable() # Test countTenants method
# print('Total count of available apartments: ' + str(count_avail))

# count rented apartments
# count_rented = apartment_db.getTotalRented() # Test countTenants method
# print('Total count of rented apartments: ' + str(count_rented))

# apartment_db.loadApartments('apartment_data.txt')
# print(load_apartments)