from controller import *
from TestDataLoading import DataLoad

dataload=DataLoad()


def listAdminOptions():
    print("--------------Welcome to User Access Management---------------------\n")
    print("1. List all users")
    print("2. List all resources")
    print("3. List all roles")
    print("4. List all permissions of a role")
    print("5. Assign roles to users")
    print("6. Remove a role from users")
    print("7. Access a resource")
    print("8. Exit")

def mainmenu():
    print("--------------Welcome to Role Based Access Control System---------------------\n")
    print("1. Login as Admin")
    print("2. Login as Regular user")
    print("3. Exit")
def regularmenu():
    print("1. Access a resource")
    print("2. View my Access Rights")
    print("3. Exit")

def regularops(user):
    while(True):
        regularmenu()
        print("Please select an option from above: ")
        userinput = int(input())
        if (userinput == 1):
            listResources()
            print("Type id of resource you want to access: ")
            resourceidinput = int(input())
            if(resourceidinput not in resources):
                print("Such Resource does not Exist.Press enter to continue")
                input()
                continue
            listActions()
            print("id of action you want to access: ")
            actioninput = int(input())
            if (actioninput not in actions):
                print("Such Action does not Exist.Press enter to continue")
                input()
                continue
            checkAccess(user, getResourceById(resourceidinput), getActionbyId(actioninput))
        elif(userinput==2):
            for role in user.roles:
                list_Role_Permissions(role)
        elif (userinput == 3):
            main()
            break
        else:
            print("Please enter a valid input")

        print("Press Enter to continue")
        input()

def main():
    while (True):
        mainmenu()
        print("Please select an option from above: ")
        userinput = int(input())
        if(userinput==1):
            adminops()
            break
        elif(userinput==2):
            listUsers()
            print("Please type id of user you would like to login as: ")
            useridinput=int(input())
            if (useridinput not in users):
                print("Such User does not Exist.Press enter to continue")
                input()
                continue
            regularops(getUserbyId(useridinput))
        elif(userinput==3):
            exit()
        else:
            print("Please enter a valid input")

        print("Press Enter to continue")
        input()





def adminops():

    while(True):
        listAdminOptions()
        print("Please select an option from above: ")
        userinput = int(input())
        if(userinput==1):
            listUsers()
        elif(userinput==2):
            listResources()
        elif(userinput==3):
            listRoles()
        elif(userinput==4):
            listRoles()
            print("Type role id for which you want to view permissions: ")
            roleinput=int(input())
            if (roleinput not in roles):
                print("Such Role does not Exist.Press enter to continue")
                input()
                continue
            list_Role_Permissions(getRolebyId(roleinput))
        elif(userinput==5):
            listUsers()
            print("Type user id to which you want to assign roles: ")
            useridinput=int(input())
            if (useridinput not in users):
                print("Such User does not Exist.Press enter to continue")
                input()
                continue
            listRoles()
            print("Type role id to which you want to assign to "+getUserbyId(useridinput).name+": ")
            roleinput=int(input())
            if (roleinput not in roles):
                print("Such Role does not Exist.Press enter to continue")
                input()
                continue
            getUserbyId(useridinput).assign_role(getRolebyId(roleinput))
            getUserbyId(useridinput).list_roles()
        elif(userinput==6):
            listUsers()
            print("Type user id for which you want to remove roles: ")
            useridinput = int(input())
            if (useridinput not in users):
                print("Such User does not Exist.Press enter to continue")
                input()
                continue
            listRoles()
            print("Type role id to which you want to remove for " + getUserbyId(useridinput).name)
            roleinput = int(input())
            if (roleinput not in roles):
                print("Such Role does not Exist.Press enter to continue")
                input()
                continue
            getUserbyId(useridinput).remove_role(getRolebyId(roleinput))
            getUserbyId(useridinput).list_roles()
        elif(userinput==7):
            listResources()
            print("Type id of resource you want to access: ")
            resourceidinput=int(input())
            listActions()
            print("id of action you want to access: ")
            actioninput=int(input())
            if (actioninput not in actions):
                print("Such Action does not Exist.Press enter to continue")
                input()
                continue
            checkAccess(getUserbyId(1),getResourceById(resourceidinput),getActionbyId(actioninput))
        elif(userinput==8):
            main()
            break
        else:
            print("Please enter a valid input")

        print("Press Enter to continue")
        input()


main()






