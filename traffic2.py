# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 12:50:27 2017

@author: Tom
"""
from physics import *
import pylab
import timeit
start = timeit.default_timer()
l=500   #number of sites
#n=100    #number of cars
vmax=3  #maximum velocity
#p=0.5
T=8000
#------------------------------------------------------------------------------
def traffic(T,n,l,p,vmax,f):
    y=0
    c1=c2=c3=c4=0.0
    w=0
    x=[-1 for i in range(l)]
    q=0
    while q<n:                  #initial generation
        i=int(uniform(l-1))
        if x[i]==-1:
            x[i]=int(uniform(vmax))
            q+=1
    for t in range(T):
        a=-1
        b=-1
        for i in range(l):        #a def
            if x[i]>-1 and a==-1:
                a=i
        for i in range(l):      #rule 1
            if -1<x[i]<vmax:
                x[i]+=1
        for i in range(l-1,-1,-1): #rule 2
            if x[i]>-1:
                if l-abs(a-i)<=x[i] and i+x[i]<l:
                    x[i]=a-i-1
                elif l-abs(a-i)<=x[i]:
                    x[i]=a-i-1+l
                elif abs(a-i)<=x[i]:        #bug if only 1 car
                    x[i]=a-i-1
                a=i
        for i in range(l):      #rule 3
            if x[i]>0:
                g=uniform(1)
                if g<=p:
                    x[i]-=1
        for i in range(l-1,-1,-1): #rule 4
            if x[i]>0 and i+x[i]<l and i>b:
                if i<=0.25*l<i+x[i] and w>f*T:
                    c1+=1.0                #checkpoint
                elif i<=0.5*l<i+x[i] and w>f*T:
                    c2+=1.0
                elif i<=0.75*l<i+x[i] and w>f*T:
                    c3+=1.0
                x[i+x[i]]=x[i]
                x[i]=-1
            elif x[i]>0 and i>b:
                b=i+x[i]-l
                x[b]=x[i]
                x[i]=-1
                if w>f*T:
                    c4+=1.0                #checkpoint
        w+=1
    return (c1+c2+c3+c4)/(4.0*float(T)*(1.0-f))
    
'''y+=1
        pylab.xlim(0,l)
        pylab.ylim(0,T)
        pylab.xlabel('Road')
        pylab.ylabel('Time')
        for i in range(l):
            if x[i]==0:
                pylab.scatter(i,y,color='0.8',s=0.7)
            elif x[i]==1:
                pylab.scatter(i,y,color='0.6',s=0.7)
            elif x[i]==2:
                pylab.scatter(i,y,color='0.5',s=0.7)
            elif x[i]==3:
                pylab.scatter(i,y,color='0.3',s=0.7)
            elif x[i]==4:
                pylab.scatter(i,y,color='0.1',s=0.7)
            elif x[i]==5:
                pylab.scatter(i,y,color='0.0',s=0.7)
    pylab.show()'''
#------------------------------------------------------------------------------
m1=m2=m3=0.0
#n=100.0
x1=[0 for i in range(0,l-1)]
x2=[0 for i in range(0,l-1)]
x3=[0 for i in range(0,l-1)]
x4=[0 for i in range(0,l-1)]
y1=[0 for i in range(0,l-1)]
y2=[0 for i in range(0,l-1)]
y3=[0 for i in range(0,l-1)]
y4=[0 for i in range(0,l-1)]
i=0
f=0.3
n=2.0
p=0.0
while n<l:
    for a in range(5):
        m1+=traffic(T,n,l,p,vmax,f)
    x1[i]=n/l
    y1[i]=m1/5.0
    n+=3
    i+=1
    m1=0
p=0.25
n=2.0
i=0
while n<l:
    for a in range(5):
        m1+=traffic(T,n,l,p,vmax,f)
    x2[i]=n/l
    y2[i]=m1/5.0
    n+=3
    i+=1
    m1=0
p=0.5
n=2.0
i=0
while n<l:
    for a in range(5):
        m1+=traffic(T,n,l,p,vmax,f)
    x3[i]=n/l
    y3[i]=m1/5.0
    n+=3
    i+=1
    m1=0
p=0.75
n=2.0
i=0
while n<l:
    for a in range(5):
        m1+=traffic(T,n,l,p,vmax,f)
    x4[i]=n/l
    y4[i]=m1/5.0
    n+=3
    i+=1
    m1=0
pylab.plot(x1[:i],y1[:i],label='p=0.0')
pylab.plot(x2[:i],y2[:i],label='p=0.25')
pylab.plot(x3[:i],y3[:i],label='p=0.5')
pylab.plot(x4[:i],y4[:i],label='p=0.75')
pylab.xlabel('Car Density')
pylab.ylabel('Flow')
pylab.legend()
pylab.xlim(0,1.0)
pylab.ylim(0)
pylab.show()
stop = timeit.default_timer()
print( stop - start)
#------------------------------------------------------------------------------
