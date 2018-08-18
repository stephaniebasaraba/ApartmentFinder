from random import randint

class Tenant:
    def __init__(self,tenant_fName,tenant_lName,tenant_aptNum):
        self.tenant_id = ''.join(["%s" % randint(0, 9) for num in range(0, 5)])
        self.tenant_fName = tenant_fName
        self.tenant_lName = tenant_lName
        self.tenant_aptNum = tenant_aptNum

    def get_fName(self):
        return self.tenant_fName

    def get_lName(self):
        return self.tenant_lName

    def get_tenant_aptNum(self,):
        return self.tenant_aptNum


