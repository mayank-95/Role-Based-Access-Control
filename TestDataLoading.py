from Models import *
import datetime
class DataLoad():
    def __init__(self):
        self.s3=Resource(1,datetime.datetime.now(),datetime.datetime.now(),"s3")
        self.ec2=Resource(2,datetime.datetime.now(),datetime.datetime.now(),"EC2")

        self.user1=User(1,datetime.datetime.now(),datetime.datetime.now(),"Raj",1)
        self.user2=User(2,datetime.datetime.now(),datetime.datetime.now(),"Bob",0)
        self.user3=User(3,datetime.datetime.now(),datetime.datetime.now(),"Tom",0)
        self.user4=User(4,datetime.datetime.now(),datetime.datetime.now(),"Bill",0)

        self.readonly=Role(1,datetime.datetime.now(),datetime.datetime.now(),"All readonly")
        self.ec2manager=Role(3,datetime.datetime.now(),datetime.datetime.now(),"EC2 Manager")
        self.s3admin=Role(4,datetime.datetime.now(),datetime.datetime.now(),"s3 admin")

        self.action_create=Action(1,datetime.datetime.now(),datetime.datetime.now(),"Create")
        self.action_read=Action(2,datetime.datetime.now(),datetime.datetime.now(),"Read")
        self.action_update=Action(3,datetime.datetime.now(),datetime.datetime.now(),"Update")
        self.action_delete=Action(4,datetime.datetime.now(),datetime.datetime.now(),"Delete")

        self.role_permission1=Resource_Action_Role_Mapping(1,datetime.datetime.now(),datetime.datetime.now(),self.s3,self.action_create,self.s3admin)
        self.role_permission2=Resource_Action_Role_Mapping(2,datetime.datetime.now(),datetime.datetime.now(),self.s3,self.action_read,self.readonly)
        self.role_permission2=Resource_Action_Role_Mapping(3,datetime.datetime.now(),datetime.datetime.now(),self.ec2,self.action_read,self.readonly)
        self.role_permission3=Resource_Action_Role_Mapping(4,datetime.datetime.now(),datetime.datetime.now(),self.s3,self.action_update,self.s3admin)
        self.role_permission4=Resource_Action_Role_Mapping(5,datetime.datetime.now(),datetime.datetime.now(),self.s3,self.action_delete,self.s3admin)
        self.role_permission5=Resource_Action_Role_Mapping(6,datetime.datetime.now(),datetime.datetime.now(),self.s3,self.action_read,self.s3admin)
        self.role_permission6 = Resource_Action_Role_Mapping(6, datetime.datetime.now(), datetime.datetime.now(),self.ec2, self.action_read, self.ec2manager)
        self.role_permission7 = Resource_Action_Role_Mapping(8, datetime.datetime.now(), datetime.datetime.now(),self.ec2, self.action_update, self.ec2manager)

        self.user2.assign_role(self.ec2manager)
        self.user3.assign_role(self.readonly)
        self.user4.assign_role(self.s3admin)