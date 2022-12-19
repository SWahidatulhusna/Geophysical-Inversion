# Program    : Data model bola (G) dan Data sintetik (d) weighted minimum length
# Spesifikasi: Inverse Modelling
# Versi      : 1.0
# Last Edited: 2020-10-12
# Programmer : Sabda Wahidatulhusna

import numpy as np
import matplotlib.pyplot as plt
import statistics
#pembuatan Data sintetik
lebar = 100
tinggi = 100

r=5

lokasi_model1 = [[5,5],[15,5],[25,5],[35,5],[45,5],[55,5],[65,5],[75,5],[85,5],[95,5]]
rho1=1.9
lokasi_model2 = [[5,15],[15,15],[25,15],[35,15],[45,15],[55,15],[65,15],[75,15],[85,15],[95,15]]
rho2=2.3
lokasi_model3=[[5,25],[15,25],[25,25],[35,25],[45,25],[55,25],[65,25],[75,25],[85,25],[95,25]]
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

d = np.array([0,5,15,25,35,45,55,65,75,86,95,100])
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
noise = 0.1 * np.random.randint(0,10,12)
dnoise = di + noise
dnoise = dnoise.ravel()
dnoise=np.array(dnoise)
m = np.dot(np.dot(np.linalg.inv(np.dot(Gkernel.transpose(), Gkernel)), Gkernel.transpose()), dnoise)
print('Model(p) hasil inversi',m)
dinversi=np.dot(Gkernel,m)
m0=[0.3,0.4,0.7]
m_=[1.9,2.3,2.5]
cv=[]
for i in range(len(m0)):
    cov= (m_[i]-statistics.mean(m_)*m0[i]-statistics.mean(m0))/3
    cv.append(cov)
cv=np.array(cv)
cv=cv.transpose()
print(cv)
I=np.eye(3)
covar=I*cv
wi=np.linalg.inv(covar)
# wii=np.linalg.inv(wi)
A=np.dot(wi,Gkernel.transpose())
B=np.linalg.inv(np.dot(Gkernel, A))
C=np.dot(A,B)
Mwl=np.dot(C,dnoise)
dwieght=np.dot(Gkernel,Mwl)
print(Mwl)
print(dwieght)
print(dnoise)
ax[0].plot(d,dinversi,'-b')
ax[0].plot(d,dnoise ,'ro')
ax[0].plot(d,dwieght,'-r',label='weighted')
ax[0].set_xlim(0,100)
ax[0].set_xlabel('lintasan')
ax[0].set_ylabel('mGal')
plt.show()




