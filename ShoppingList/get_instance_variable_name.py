import os
os.system("cls")


class InstanceVariable(object):    
    def __init__(self):
        pass
        
    def get_instance_variable_name(self):
        ivn = [k for k,v in globals().items() if v is self][0]
        return ivn

hello = InstanceVariable()
world = InstanceVariable()

print(hello.get_instance_variable_name())
print(world.get_instance_variable_name())
print()