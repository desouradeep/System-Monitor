#!/usr/bin/env python
import gtk
import data
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
import gobject


def main():
    win = gtk.Window()
    win.connect("destroy", lambda x: sys.exit())
    win.set_default_size(700,350)
    win.set_title("SYSTEM MONITOR")

    
    
    f = Figure(figsize=(5,4), dpi=80)
    a = f.add_subplot(111)
    a.grid(True)
    a.set_xlabel('Time')
    a.set_ylabel('Usage in %')
    a.set_ylim(0,100)
    a.set_xlim(0,50)
	    
    canvas = FigureCanvas(f)
    win.add(canvas) 
    win.show_all()        
	
    gobject.idle_add(graph(a,f))
    gtk.main()
    
     
def graph(a,f):
    line_cpu=[]
    c=[]
    m=[]
    d=[]
    while True:
        c.append(data.cpu())
	m.append(data.mem())
	d.append(data.dsk())
	
	if len(c)>50:
	    del c[0]
	    del m[0]
	    del d[0]
	if len(line_cpu)!=0:
	    l = line_cpu.pop(0)
	    l.remove()
	    l = line_mem.pop(0)
	    l.remove()
	    l = line_dsk.pop(0)
	    l.remove()
	    
	line_cpu=a.plot(c,'b')
	line_mem=a.plot(m,'r')
	line_dsk=a.plot(d,'g')
	cc='CPU  : '+c[-1]+'%'
	mm='RAM  : '+m[-1]+'%'
	dd='DISK : '+d[-1]+'%'
	
	f.legend( (line_cpu, line_mem, line_dsk), (cc, mm, dd))
	
	f.canvas.draw()
	
main()