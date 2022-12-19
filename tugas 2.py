# Program    : Data model bola (G) dan Data sintetik (d)
# Spesifikasi: Inverse Modelling
# Versi      : 1.0
# Last Edited: 2020-10-12
# Programmer : Sabda Wahidatulhusna

import numpy as np
import matplotlib.pyplot as plt

#pembuatan Data sintetik
lebar = 100
tinggi = 100

r=5

lokasi_model1 = [[25,5]]
rho1=1.9
lokasi_model2 = [[45,15]]
rho2=2.3
lokasi_model3=[[95,25]]
rho3= 2.5
fig,ax = plt.subplots(2,figsize=(lebar,tinggi))
fig.suptitle('Gravity Model Sphere')
for i in range(5,lebar+10,10):
    for k in range(5,tinggi,10):
        bulat = plt.Circle((i,k),r,color='b', fill=False)
        ax[1].add_artist(bulat)

ax[1].set_xlim(0,100)
ax[1].set_ylim(60,0)
ax[1].set_xlabel('lintasan')
ax[1].set_ylabel('kedalaman')

for lingkaran1 in lokasi_model1:
    bulat = plt.Circle((lingkaran1[0],lingkaran1[1]),r,color='g')
    ax[1].add_artist(bulat)
for lingkaran2 in lokasi_model2:
    bulat = plt.Circle((lingkaran2[0],lingkaran2[1]),r,color='r')
    ax[1].add_artist(bulat)
for lingkaran2 in lokasi_model3:
    bulat = plt.Circle((lingkaran2[0],lingkaran2[1]),r,color='orange')
    ax[1].add_artist(bulat)
def gravz(rho,x,b,h):
    G = 6.67 * 10 ** -11; rho0 = 0
    return ((4*np.pi/3)*G*(rho-rho0)*(h*b**3)/(x**2+h**2)**1.5)*10**9


rho0 = 0

d = np.arange(0,100,0.1)
gtotal = np.linspace(rho0,rho0,len(d))
delta_G = []
# print(d)
for i in lokasi_model1:
    gcal = gravz(rho1,abs(d-i[0]),r,i[1])
    delta_G.append(gcal)
for i in lokasi_model2:
    gcal = gravz(rho2,abs(d-i[0]),r,i[1])
    delta_G.append(gcal)
for i in lokasi_model3:
    gcal = gravz(rho2,abs(d-i[0]),r,i[1])
    delta_G.append(gcal)
for g in delta_G:
    gtotal += g

#memulai Inversi

gsatu=[]
gdua=[]
gtiga=[]

def gravg(x,b,h):
    G = 6.67 * 10 ** -11
    return ((4*np.pi/3)*G*(h*b**3)/(x**2+h**2)**1.5)*10**9

for i in lokasi_model1:
    gcal1 = gravg(abs(d-i[0]),r,i[1])
for i in lokasi_model2:
    gcal2 = gravg(abs(d-i[0]),r,i[1])
for i in lokasi_model3:
    gcal3 = gravg(abs(d-i[0]),r,i[1])


matriks=[]
for j in range(len(d)):
    matr=[gcal1[j],gcal2[j],gcal3[j]]
    matriks.append(matr)

Gkernel = np.array(matriks)


di=list(gtotal.flatten())
noise = 0.1 * np.random.randint(0,6,1000)
dnoise = di + noise
dnoise = dnoise.ravel()
dnoise=np.array(dnoise)
m = np.dot(np.dot(np.linalg.inv(np.dot(Gkernel.transpose(), Gkernel)), Gkernel.transpose()), dnoise)
print('Model(p) hasil inversi',m)
dinversi=np.dot(Gkernel,m)
ax[0].plot(d,dinversi,'-b')
ax[0].plot(d,dnoise ,'ro')
ax[0].set_xlim(0,100)
ax[0].set_xlabel('lintasan')
ax[0].set_ylabel('mGal')
plt.show()




