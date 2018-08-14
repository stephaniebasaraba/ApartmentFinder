from random import randint

class Apartment:
    def __init__(self, apt_num, apt_bedrm, apt_baths, apt_rent, apt_status):
        self.apt_num = apt_num
        self.apt_bedrm = apt_bedrm
        self.apt_baths = apt_baths
        self.apt_rent = apt_rent
        self.apt_status = apt_status

    def set_apt_num(self,aptNum):
        self.apt_num = aptNum

    def get_apt_num(self):
        return self.apt_num
    
    def set_apt_bedrm(self,aptBedrm):
        self.apt_bedrm = aptBedrm

    def get_apt_bedrm(self):
        return self.apt_bedrm

    def set_apt_baths(self,aptBath):
        self.apt_baths = aptBath

    def get_apt_baths(self):
        return self.apt_baths

    def set_apt_rent(self,aptRent):
        self.apt_rent = aptRent

    def get_apt_rent(self):
        return self.apt_rent

    def set_apt_status(self,aptStatus):
        self.apt_status = aptRent

    def get_apt_status(self):
        return self.apt_status

