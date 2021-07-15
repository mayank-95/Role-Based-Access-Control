from Models import *
from globals import *
def listUsers():
    print("id     username")
    for user in users.values():
        print(str(user.id)+"     "+user.name)

def listRoles():
    print("id     rolename")
    for role in roles.values():
        print(str(role.id) + "      " + role.name)

def listResources():
    print("id     resourcename")
    for resource in resources.values():
        print(str(resource.id)+"     "+resource.name)

def listActions():
    print("id     actionname")
    for action in actions.values():
        print(str(action.id)+"      "+action.name)

def list_Role_Permissions(role):
    print("\n"+role.name +" access permissions as are follows:\n" )
    print("Resource"+"  "+"access permission")
    for access in role_permissions.get(role,None):
        print(access[0].name+"         "+access[1].name)

def assign_role_to_user(user,role):
    user.assign_role(role)

def checkAccess(user,resource,action):
    if(user.is_admin):
        print(action.name + " performed on " + resource.name)
        return
    for role in user.roles:
        accessmatrix=role_permissions.get(role)
        if(accessmatrix is not None):
            for access in accessmatrix:
                if(access[0]==resource and access[1]==action):
                    print(action.name +" performed on "+resource.name)
                    return
    print("You do not have sufficient permission to perform "+action.name+" on "+resource.name)

def getUserbyId(id):
    return users.get(id)

def getRolebyId(id):
    return roles.get(id)

def getActionbyId(id):
    return actions.get(id)

def getResourceById(id):
    return resources.get(id)


