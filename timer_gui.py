from tkinter import *
from tkinter import ttk
from datetime import *

timer_end = datetime.now()

def start():
    timer_length = timedelta(minutes = int(mins.get()), seconds = int(secs.get()) + 1)
    global timer_end; timer_end = datetime.now() + timer_length
    global interrupt; interrupt = False
    root.after(1, update)
    
def stop():
    global interrupt; interrupt = True
    
def update():
    if interrupt:
        return
    time_left = timer_end - datetime.now()
    if datetime.now() < timer_end:
        minsValue = time_left // timedelta(minutes = 1)
        secsValue = int(time_left.total_seconds() % 60)
        mins.set('0' + str(minsValue) if minsValue < 10 else minsValue)
        secs.set('0' + str(secsValue) if secsValue < 10 else secsValue)
        root.after(100, update)
    else:
        mins.set('00')
        secs.set('00')

def capMins(val):
    if val >= 60:
        return 0
    if val < 0:
        return 60
    return val

def capSecs(val):
    if val >= 59:
        return 0
    if val < 0:
        return 59
    return val

def incrementMins(*args):
    val = capMins(int(mins.get()) + 1)
    mins.set('0' + str(val) if val < 10 else val)

def decrementMins(*args):
    val = capMins(int(mins.get()) - 1)
    mins.set('0' + str(val) if val < 10 else val)

def incrementSecs(*args):
    val = capSecs(int(secs.get()) + 1)
    secs.set('0' + str(val) if val < 10 else val)

def decrementSecs(*args):
    val = capSecs(int(secs.get()) - 1)
    secs.set('0' + str(val) if val < 10 else val)
    
root = Tk()
root.title("Timer")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mins = StringVar()
mins.set('00')
mins_label = ttk.Label(mainframe, textvariable=mins)
mins_label.grid(column = 0, row = 1, sticky = E)

ttk.Button(mainframe, command = incrementMins, text = '+', width = 2).grid(column = 0, row = 0, sticky = E)
ttk.Button(mainframe, command = decrementMins, text = '-', width = 2).grid(column = 0, row = 2, sticky = E)

ttk.Label(mainframe, text = ':').grid(column = 1, row = 1, sticky = (W, E))

secs = StringVar()
secs.set('00')
secs_label = ttk.Label(mainframe, textvariable=secs)
secs_label.grid(column = 2, row = 1, sticky = W)

ttk.Button(mainframe, command = incrementSecs, text = '+', width = 2).grid(column = 2, row = 0, sticky = W)
ttk.Button(mainframe, command = decrementSecs, text = '-', width = 2).grid(column = 2, row = 2, sticky = W)

ttk.Button(mainframe, text = 'Start', command = start).grid(column = 0, row = 3, sticky = (W, E))
ttk.Button(mainframe, text = 'Stop', command = stop).grid(column = 2, row = 3, sticky = (W, E))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
    
root.mainloop()
