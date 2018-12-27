#context Manager-----> 1)Setup(K.W-Try) 2)Handoff(K.W-Yield) 3)Wrap-Up(K.W-Finally)
#basic conext Manager framework
#@contextmanager
#def simple_context_manager(obj):
#    try:
#         yield
#    finally:  

#Increments some property by one
from contextlib import contextmanager
@contextmanager
def simple_context_manager(obj):
    try:
        obj.some_property +=1
        yield
    finally:
        obj.some_property -=1

class Some_obj(object):
    def __init__(self, arg):
        self.some_property = arg


obj = Some_obj(5)
print(obj.some_property)
with simple_context_manager(obj):
                                    print(obj.some_property)

print(obj.some_property)    
