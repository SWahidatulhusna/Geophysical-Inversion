# Program    : Inversi Soal UTS no.1
# Versi      : 1.0
# Last Edited: 2020-10-26
# Programmer : Sabda Wahidatulhusna
import numpy as np
import matplotlib.pyplot as plt
x1=[-2.2,-0.25,0.0, 1.0,1.25,5.25]
x2=[-2.25,-1.2,0.0,-1,4.25,5]
y=[1.8625,-0.275,0.25,-2,1.5,-3.875]

xnol=[]
xsatu=[]
xdua=[]

for i in range(len(y)):
    f0= i*0+1
    f1= x1[i]
    f2= x2[i]
    xnol.append(f0)
    xsatu.append(f1)
    xdua.append(f2)

matriks=[]
for j in range(len(y)):
    kernel=[xnol[j],xsatu[j],xdua[j]]
    matriks.append(kernel)
# print(matriks)

Gkernel = np.array(matriks)
m = np.dot(np.dot(np.linalg.inv(np.dot(Gkernel.transpose(), Gkernel)), Gkernel.transpose()), y)
#mencari koefisien keofisien dan memnuculkan gambar
print('Koefisien hasil inversi',m)

d = np.dot(Gkernel,m)
print ('Data calculated hasil inversi',d)
di=list(d.flatten())
# hitung nilai missfit
missfitin=[]
for i in range(len(y)):
    Missfitt= (y[i]-d[i])/6
    missfitin.append(Missfitt)
total=missfitin[0]+missfitin[1]+missfitin[2]+missfitin[3]+missfitin[4]+missfitin[5]
Missfit=(total)**0.5
print('nilai missfit pernilai',Missfit)

#laju perubahan data terhadap sumbu sumbu x1 dan x2
print("laju perubahan data terhadap sumbu sumbu x2",m[2])
print("laju perubahan data terhadap sumbu sumbu x1",m[1])
#perkiraan nilai y pada koordinat
x11=[-1.5,-2,3.5]
x22=[-1.5,0.5,4]
xnol1=[]
xsatu1=[]
xdua1=[]
for i in range(len(x11)):
    f0= i*0+1
    f1= x11[i]
    f2= x22[i]
    xnol1.append(f0)
    xsatu1.append(f1)
    xdua1.append(f2)

matriks1=[]
for j in range(len(x11)):
    kernel1=[xnol1[j],xsatu1[j],xdua1[j]]
    matriks1.append(kernel1)
Gkernel1 = np.array(matriks1)
perkiraanY= np.dot(Gkernel,m)
print('nilai perkiraan Y',perkiraanY)
fig, ax = plt.subplots(figsize=(16,9))
ax.plot(x1, y, 'b', label='Data observasi x1')
ax.plot(x2, y, 'g', label=' Data observasi x2')
ax.plot(x1, d, 'r', linewidth=1,label='Data Calculated x1')
ax.plot(x2, d, 'k',linewidth=1, label='Data calculated x2')
ax.legend()
plt.show()

