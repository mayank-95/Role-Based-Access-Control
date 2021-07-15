import datetime

import globals
class Basemodel:
    def __init__(self,id,created_date,modified_date):
        self.id=id
        self.created_date=created_date
        self.modified_date=modified_date

class Resource(Basemodel):
    def __init__(self,id,created_date,modified_date,name):
        Basemodel.__init__(self,id,created_date,modified_date)
        self.name=name
        globals.resources[self.id]=self

class Role(Basemodel):
    def __init__(self,id,created_date,modified_date,name):
        Basemodel.__init__(self,id,created_date,modified_date)
        self.name=name
        globals.roles[self.id]=self

class User(Basemodel):
    def __init__(self,id,created_date,modified_date,name,is_admin):
        Basemodel.__init__(self,id,created_date,modified_date)
        self.name=name
        self.is_admin=is_admin
        self.roles = set()  #contains all roles assigned to user
        globals.users[self.id]=self
    def list_roles(self):
        print("RoleId    RoleName")
        for role in self.roles:
            print(str(role.id)+"       "+role.name)
    def assign_role(self,role):
        self.roles.add(role)
        self.modified_date=datetime.datetime.now()
        print("Assigned role "+role.name+" to"+self.name)
    def remove_role(self,role):
        self.roles.remove(role)
        self.modified_date = datetime.datetime.now()
        print("Removed role " + role.name + " to" + self.name)

class Action(Basemodel):
    def __init__(self,id,created_date,modified_date,name):
        Basemodel.__init__(self,id,created_date,modified_date)
        self.name=name
        globals.actions[self.id]=self

class Resource_Action_Role_Mapping(Basemodel):
    def __init__(self,id,created_date,modified_date,resource,action,role):
        Basemodel.__init__(self,id,created_date,modified_date)
        self.resource=resource
        self.action=action
        self.role=role
        if(role in globals.role_permissions):
            globals.role_permissions[role].append([resource,action])
        else:
            globals.role_permissions[role]=[[resource,action]]





