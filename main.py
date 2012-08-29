#!/usr/bin/env python
import matplotlib.pyplot as plt 
import matplotlib
import data
c=[]
m=[]
d=[]

def main():
    print 'NO.	CPU	MEMORY	DISK'
    plt.subplot(211)
    i=0
    while True:
        i+=1
        plt.ylim(0,100)
        plt.xlim(0,60)
        cc=data.cpu()
        mm=data.mem()
        dd=data.dsk()
        print i,'\t',cc,'\t',mm,'\t',dd
        c.append(cc)
        m.append(mm)
        d.append(dd)
        plt.grid(True)
        plt.xlabel('TIME')
        plt.ylabel('USAGE IN %')
        
        plt.title(' - - SYSTEM MONITOR - - ')
        ds='DISK ('+dd+'%)' 
        ms='RAM  ('+mm+'%)' 
        cs='CPU  ('+cc+'%)' 
        plt.plot(d[-60:-1],'g', label=ds)
        plt.plot(m[-60:-1],'r', label=ms)
        plt.plot(c[-60:-1],'b', label=cs)
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.06,0,0.04), ncol=3)
        if len(c)>60:
	    del c[0]
	    del m[0]
	    del d[0]
        plt.draw()
        matplotlib.interactive(True)
        plt.show()
        plt.clf()
        
main()