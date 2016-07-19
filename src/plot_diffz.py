
#execfile('/home/xiaodongli/software/pythonlib/stdA.py')
from stdA import *

i1, i2 = 5, 50
sfact = 1
logY=False

nowdir = '../105thick/'
fig = plt.figure(figsize=(18,7))
ax1, ax2, ax3 = fig.add_subplot(131), fig.add_subplot(132), fig.add_subplot(133)
for nowzstr in ['0', '0.5', '1', '1.5', '2']:
	nowfile = nowdir+'J08.dat.z_'+nowzstr+'.mge3.000e11.slice1.1.rmax50.50rbins.2pcf'
	#print isfile(nowfile)
	R1, R2, DD, DR, RR, XiN, XiD, XiLS = Xsfromdata(np.loadtxt(nowfile,skiprows=1), range(8))
	Rmid = [((R1[row]**3.0+R2[row]**3.0)*0.5)**(1.0/3.0) for row in range(len(R1))]
	Y1 = XmultY(Rmid, XiLS,a=sfact);
	ax1.plot(Rmid, Y1, label = 'z='+nowzstr, lw=2)
	ax1.set_ylabel('$\\xi \\times s^{'+str(sfact)+'}$', fontsize=26)
	Y2 = normto1(Y1)
	ax2.plot(Rmid, Y2, label = 'z='+nowzstr, lw=2)
	ax2.set_ylabel('$\\xi \\times s^{'+str(sfact)+'}$ (normalized)', fontsize=26)
	X3, Y3 = Rmid[i1-1:i2], normto1(Y1[i1-1:i2])
	ax3.plot(X3, Y3, label = 'z='+nowzstr, lw=2)
	ax3.set_ylabel('$\\xi \\times s^{'+str(sfact)+'}$ (normalized in range of ('+str(i1-1)+','+str(i2)+')', fontsize=26)
for ax in [ax1,ax2,ax3]:
	ax.grid()
	ax.set_xlabel('$r$', fontsize=20)
	if logY:
		ax.set_yscale("log")
ax1.legend(loc='best',frameon=False)
ax2.legend(loc='best',frameon=False)
ax3.legend(loc='best',frameon=False)
fig.tight_layout()
fig.savefig('Diffz_sfact'+str(sfact)+'.eps', format='eps')
plt.show()
