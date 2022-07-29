
'''creating class with method(config)'''
# class computer:
#     def config(self):
#         print('i5,16gd,1tb')
# com1=computer()
# com1.config()#i5,16gd,1tb
# computer.config(com1)

''' object (com1) is also a argument without (self) argument  any method(my) will not excected
every method will have the one argument default that is object name that is the reason we need to mention the  self argument defalt '''


'''__init__  is a method to def]ine the varibles it automaticalli excecuted without creating object'''
# class computer:
#     def __init__(self):
#         print('1TB,16GB,i5')
#     def my(self):
#         print('this is my computer config')
# com1=computer()
# com1.my()

'''output'''
# 1TB,16GB,i5
# this is my computer config

# class computer:
#     def __init__(self,cpu,ram) :
#         self.cpu=cpu
#         self.ram=ram
#         # print(self.cpu,self.ram)
#     def config(self):
#         print('config of my pc',self.cpu,self.ram)
#         # print('my computer')
# c1=computer('i5',16)
# c2=computer('ryzen',8)
# c1.config()
# c2.config()

'''output'''
# config of my pc i5 16  
# config of my pc ryzen 8
'''==========='''

# class computer:
    # def __init__(self,cpu,ram) :
    #     self.cpu=cpu
    #     self.ram=ram
    #     # print(self.cpu,self.ram)
    # def config(self):
    #     print('config of my pc',self.cpu,self.ram)
    #     # print('my computer')
    # def config1(self,user):
    #     print('it not my pc configaration')
    #     print('name of user',user)

# c1=computer('i5',16)
# c2=computer('ryzen',8)

# c1.config()
# c2.config()
# c1.config1('gggg')
# c2.config1('goutham')

'''output'''
# name of user gggg
# it not my pc configaration
# name of user goutham      
'''==================='''
# class computer:
#     def __init__(self,cpu,ram,user) :
#         self.cpu=cpu
#         self.ram=ram
#         self.name=user
#         # print(self.cpu,self.ram)

#     def config(self):
#         print('config of my pc',self.cpu,self.ram,self.name)
#         # print('my computer')

#     def config1(self):
#         print('it not my pc configaration')
#         print('name of user',self.name)
#         print('name of user',self.cpu)
#         print('name of user',self.ram)

#     def config2(self,user,sys):
#         print(self.ram)
#         print('user name is',user)
#         print('system name is',sys)

# c1=computer('i5',16,'babu')
# c2=computer('ryzen',8,'ravi')

# # c1.config()   #config of my pc i5 16 babu

# # c1.config1()    #it not my pc configaration
#                 #name of user babu 
#                 #name of user i5   
#                 #name of user 16 
# c2.config2('goutham','dell')    #8
#                                 # user name is goutham
                                # system name is dell
 
