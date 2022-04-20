#!/usr/bin/env python
# coding: utf-8

# * Define the `Employee` class with an `__init__()` method
# * Define a class attribute `new_id` and set it to `1`
# * Each Employee instance will need its own unique ID. Thus, inside `__init__()`, define `self.id` and set it equal to the class variable `new_id`
# * Lastly, increment `new_id` by `1`
# * Define a `say_id()` method
# * Inside `say_id()`, output the string `"My ID is "` and then the instance id.
# * Create 3 Employee objects and call the `say_id` method for them

# In[ ]:


class Employee:
    new_id=1
    def __init__(self):
        self.id=Employee.new_id
        Employee.new_id+=1
    def say_id(self):
        print("my ID is {}".format(self.id))
        
a1=Employee()
a2=Employee()
a3=Employee()
a1.say_id()
a2.say_id()
a3.say_id()


# In[ ]:





# In[ ]:




