from tenant import Tenant

class Tenant_DB:
    def __init__(self):
        self.tenants = list()

    def addTenant(self,tenant):
        self.tenants.append(tenant)

    def getTenant(self,apt_id):
        found_apt = ''
        for tenant in self.tenants:
            if tenant.tenant_aptNum == apt_id:
                found_apt = tenant
                break
        return found_apt

    def countTenants(self):
        count_tenants = 0
        for tenant in self.tenants:
            count_tenants += 1
        return count_tenants

    def removeTenant(self,apt_num):
        for tenant in self.tenants:
            if tenant.tenant_aptNum == apt_num:
                self.tenants.remove(tenant)
        print('Tenant ' + tenant.tenant_fName + ' ' + tenant.tenant_lName + ' has been removed.')
        return tenant
    
    def getAllTenants(self):
        return self.tenants

tenant_db = Tenant_DB() # Create tenant_db