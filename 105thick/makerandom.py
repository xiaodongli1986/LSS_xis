
import random

nran = 15028085*30

nowf=open('random.xyzw', 'w')
for i in range(nran):
	x,y = random.uniform(0,3150), random.uniform(0,3150)
	nowf.write(str(x)+' '+str(y)+' 0 1\n')
nowf.close()


	
