from random import randint

class Tenant:
    def __init__(self, tenant_fName, tenant_lName, tenant_aptNum):
        self.tenant_id = ''.join(["%s" % randint(0, 9) for num in range(0, 5)])
        self.tenant_fName = tenant_fName
        self.tenant_lName = tenant_lName
        self.tenant_aptNum = tenant_aptNum

    def set_fName(self,fName):
        self.tenant_fName = fName

    def set_lName(self,lName):
        self.tenant_lName = lName

    def set_tenant_aptNum(self,aptNum):
        self.tenant_aptNum = aptNum


