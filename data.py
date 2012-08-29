import psutil
def cpu():
    '''This method returns the current CPU usage'''
    a=psutil.cpu_percent(interval =0.1, percpu=False)
    return "%4.2f" %a
def mem():
    '''This method returns the current RAM usage'''
    a=psutil.phymem_usage().percent
    return "%2.2f" %a
def dsk():
    '''This method returns the current DISK usage'''
    a=psutil.disk_partitions()
    b=[]
    x=0
    y=0
    for i in range (0,len(a)):
        b.append(a[i][1])
        x+=psutil.disk_usage(b[i])[0]
        y+=psutil.disk_usage(b[i])[1]
        z=float(y)/float(x)*100         
    return "%2.2f" %z
