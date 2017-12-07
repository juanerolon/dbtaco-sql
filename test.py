#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 14:24:01 2017

@author: juanerolon
"""

import os
from classy import Classy

def method(a,b=None):
    
    print('a is {ai} and b is {bi} '.format(ai=a, bi=b))
    
def clean_name(some_var):
    return ''.join(char for char in some_var if char.isalnum())


print(clean_name('%__14_()-414'))
    
    
    
    
method(5)
method(5,7)



nmd = {1:'col1', 2:'col2',3:'col3'}
tpd = {1:'integer', 2:'text',3:'real'}
val = {1:123, 2:'word', 3:5.32}


x = list(nmd.keys())
x.sort()
print(x)


s = ''
for m in x:
    s = s + ' ' +  nmd[m] + ' ' + tpd[m] + ','
    
sfin = s[1:-1]
    
print(sfin)
    


lta = []
ltb = []
for m in x:
    lta.append(nmd[m]) 
    ltb.append(val[m])
                         
                         
sta = str(tuple(lta))
stb = str(tuple(ltb))
    
print(sta)
print(stb)




field = 'bart'
print('field = {f}'.format(f=field))


z = 'abcd'
z = z[1:-1]
print(z)


try:
    
    x = 'ab'
    x.sort()
except:
    print("Error")
        

obj = Classy(3.14)

obj.vox()

print('self.y = ', obj.y)


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)


print(abspath)
print(dname)


specdir = "/Users/juanerolon/Dropbox/_sql/python_sqlite"
os.chdir(specdir)

f = open('test.file', 'w')
f.close()   


    
    
    
"""    
CREATE TABLE database_name.table_name(
   column1 datatype  PRIMARY KEY(one or more columns),
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
);
"""

"""
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=new_field, ft=field_type))

"""