#mehtod1 for calling module
import howtocreateyourownmodule#call module howtocreateyourownmodule

print(howtocreateyourownmodule.sum(10,20))
print(howtocreateyourownmodule.mul(10,20))
print("")

#method 2 for calling module elyas method

import howtocreateyourownmodule as m
print(m.sum(10,30))
print(m.mul(10,10))
print("")

#method 3 for calling module from method

from howtocreateyourownmodule import sum
print(sum(10,20))
print("")

#method 4 for calling module all method

from howtocreateyourownmodule import *# it call all function
print(sum(10,20))
print(mul(10,20))