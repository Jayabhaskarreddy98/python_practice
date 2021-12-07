def order(x):
    print("Method called for value:", x)
    return True if x > 0 else False
      
a = order
b = order
c = order
  
if a(-1) or b(5) or c(10):
    print("Atleast one of the number is positive")