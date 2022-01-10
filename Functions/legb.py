import builtins
print(dir(builtins))

name = 'MS Dhoni'
def hometown():       
    name = 'Mahi'
    def sis():
        nonlocal name
        name = 'bhai'
        print(name, 'from inner')
    sis()
    print(name, 'from local') 

    print(locals())   
hometown()

print(name) 
   
print(globals())