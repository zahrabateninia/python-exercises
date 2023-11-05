READ = 0b1000  # Read permission
WRITE = 0b0100  # Write permission
EXECUTE = 0b0010  # Execute permission
CHANGE_POLICY = 0b0001  # Change Policy permission

person1 = READ  # Read only
person2 = READ | WRITE  # Read and Write
person3 = READ | WRITE | EXECUTE | CHANGE_POLICY  # All permissions
person4 = 0  # No permissions

common_permissions = person1 & person2 & person3 & person4

# common permissions in binary form
print(bin(common_permissions))
