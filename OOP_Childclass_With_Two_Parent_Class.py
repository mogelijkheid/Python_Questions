#!/usr/bin/env python
# coding: utf-8

# 1. Create a class `Car` with attributes `name` and `model`
# 2. Add `showName()` and `showModel()` methods to `Car` class
# 3. Create a class `Id` with attribute `carId`
# 4. Add `getId()` method to `Id` class
# 5. Create a class `Main` which inherits from `Car` and `Id` classes
# 6. Create a `Main` object and call existing methods for this object

# In[ ]:



class Car:    
   def __init__(self, name, model):  
       self.name = name  
       self.model = model
 
    
   def showName(self):  
       print(self.name)  
 
   def showModel(self):  
       print(self.model)  
 
    
class Id: 
   
   def __init__(self, carId):  
       self.carId = carId  
 
   def getId(self):  
       return self.carId  
 
 
class Main(Car, Id): 
   
   def __init__(self, name, model, carId):  
       Car.__init__(self,name, model)  
       Id.__init__(self,carId)
 
# Create an object of the subclass  
main = Main('Mercedes', 'X', '500')  
main.showName()  
print(main.getId()) 


# In[ ]:





# In[ ]:




