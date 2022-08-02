'''super() is used to access the parent class  methods in child class'''

class parent:
    def fun(self):
        print('i am a parent class of the programm')
class child(parent):
    def fun1(self):
        print("i am a child class of the parent")
        super().fun()
        print('this is the end of the child class')
p=parent()
c=child()
p.fun()     #i am a parent class of the programm
c.fun1()

'''output'''
# i am a child class of the parent
# i am a parent class of the programm
# this is the end of the child class
