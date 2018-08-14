from tenant import Tenant

class Tenant_DB:
    def __init__(self):
        self.tenants = list()

    def addTenant(self,tenant):
        self.tenants.append(tenant)
        print('Tenant added successfully.')

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
        print('There are ' + str(count_tenants) + ' tenants.')
        return count_tenants

    #def removeTenant(self,apt_id):
        #for tenant in self.tenants:
            #if tenants.getId() == apt_id:
                #found_apt = tenant
                #break
        #return found_apt
    
    def getAllTenants(self):
        return self.tenants

tenant_db = Tenant_DB() # Create tenant_db
tenant = Tenant('John', 'Doe', '123') # Create tenant
tenant_db.addTenant(tenant) # Test add Tenant to tenant_db

get_tenant = tenant_db.getTenant('123') # Test get Tenant method
print(get_tenant.tenant_fName, get_tenant.tenant_lName)

# count_tenants = tenant_db.countTenants() # Test countTenants method
# print('Count Tenants returned: ' + str(count_tenants))

# tenant_db.removeTenant('123') # Test removeTenant method
# count_tenants = tenant_db.countTenants() # Test countTenants method
# print('Count Tenants returned: ', count_tenants)

# tenant = Tenant('John', 'Doe', '123') # Create new tenant
# tenant_two = Tenant('Jane', 'Doe', '124') # Create new tenant
# tenant_db.addTenant(tenant)
# tenant_db.addTenant(tenant_two)
# count_tenants = tenant_db.countTenants() # Test countTenants method
# print('Count Tenants returned: ', count_tenants)

# all_tenants = tenant_db.getAllTenants() # Test getAllTenants method
# print(all_tenants)