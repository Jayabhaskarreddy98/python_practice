class company:
    comp_name='jsp'


    def __init__(self,name,id,desg):
        self.name=name
        self.id=id
        self.desg=desg

    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_desg(self):
        return self.desg
    
    def set_emp_name(self,name):
        n=self.name
        self.name=name
        print(f'{n} has been updated to {self.name}')
    
    def set_emp_id(self,id):
        i=self.id
        self.id=id
        print(f'{i} has been updated to {self.id}')
    
    def set_emp_desg(self,desg):
        d=self.desg
        self.desg=desg
        print(f'{d} has been updated to {self.desg}')   

    @classmethod
    def set_comp_name(cls,comp_name):
        c=cls.comp_name
        cls.comp_name=comp_name
        print(f'{c} has been updated to {cls.comp_name}')

if __name__=="__main__":
        print(f'employee details')
        name=input('enter the employe name->')
        id=int(input('enter employee id->'))
        desg=input('enter the employe desg->')   

object=company(name,id,desg)

object.get_name()
object.get_id()
object.get_desg()
object.set_emp_name(input('enter employe name->'))
object.set_emp_id(input('enter employe id->'))
object.set_emp_desg(input('enter employe desg->'))


emp1=company
emp2=company
print(emp1.comp_name,'from emp1')
print(emp2.comp_name,'from emp2')
emp1.set_comp_name('icc')
print(emp1.comp_name,'from emp1')
print(emp2.comp_name,'from emp2')          