import numpy as np
import math
from numpy import linalg as LA

#print('Enter the vector')
a1=1
a2=1
m1=np.array([a1,a2])
#print(m1)
r1= np.sqrt(a1**2 + a2**2)
#print(r1)
arg1=np.arctan(a2/a1)
arg1_deg=math.degrees(np.arctan(a2/a1))

print('arg1=',arg1)
z1=r1*(np.array([math.cos(arg1),math.sin(arg1)]))
#z2=np.array([math.cos(arg1),math.sin(arg1)])
print('z1=',z1)

a3=1
a4=-1
m2=np.array([a3,a4])
#print(m2)
r2= np.sqrt(a3**2 + a4**2)
#print(r2)
arg2=np.arctan(a4/a3)
arg2_deg=math.degrees(np.arctan(a4/a3))
print('arg2=',arg2)
z2=r2*(np.array([math.cos(arg2),math.sin(arg2)]))
print('z2=',z2)
inv_z2=(1/r2)*(np.array([((-1)**(1+1))*math.cos(arg2),((-1)**(1+2))*math.sin(arg2)]))
inv_arg2=((-1)**(1+2))*arg2
print('inv_arg2',inv_arg2)
print('inv_z2',inv_z2)
z1_inv_z2=(r1/r2)*(np.array([math.cos(arg1+inv_arg2),math.sin(arg1+inv_arg2)]))
print('z1_inv_z2=',z1_inv_z2)


z3=z2
print(z3)

z4=(1/r1)*(np.array([((-1)**(1+1))*math.cos(arg1),((-1)**(1+2))*math.sin(arg1)]))
print('z4=',z4)

inv_arg1=((-1)**(1+2))*arg1
print(inv_arg1)
z3_z4=(r2/r1)*(np.array([math.cos(inv_arg1+arg2),math.sin(inv_arg1+arg2)]))
print('z3_z4=',z3_z4)

sub_z= z1_inv_z2 - z3_z4
print('sub_z=',sub_z)

modulus_value= LA.norm(sub_z)
print('modulus_value',modulus_value)
