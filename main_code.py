### Library imports
import numpy as np
import tkinter as tk
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import threading
import time
import random
import pyvisa


### Threading variables used to run data gathering and graphing
global endThread
endThread=threading.Event() # event to stop data gather
global EventDATA
EventDATA=threading.Event() # event to perform graphing
global LockThread
LockThread=threading.Lock() # lock that allows access to variables between threads

### Variables that will be shared by multiple functions
global run_start
run_start=""
global big_s
big_s=""
global topa
global bota
global span
global funcgen_fcent
topa=5.0
bota=5.0
span=30
global data_time
global data_time_
global data_freq

###ADJUST TIME DELAY TO YOUR NEEDS#####
global time_delay
time_delay=0.5


### placeholder that will be used to contorl instruments
global rm 
rm=pyvisa.ResourceManager() # creates resource manager require for communication with function generator
global func_gen
func_gen=0
global osc
osc=0

### Font stylization for UI
font_A='Helvetica 12 bold'
font_B='Helvetica 12'

root = tk.Tk() # frame of the UI
control_frame= tk.Frame(root) #sub-frame for all interactables
control_frame.pack(side=tk.LEFT)
root.wm_title("QTF Sensor - Frequency Acquisition Software")
    
#def save_data():
#    global run_start
#    global big_s
#    dt_string = run_start
#    title="DATA"+str(dt_string)+".csv" 
#    text_file = open(title, "wt")
#    n = text_file.write(big_s)
#    text_file.close()

### Function that cheecks and adjusts graphing parameters
def adjust_graph():
    global topa
    global bota
    global span
    t=float(topf_var.get()) #obtain the value in corresponding textbox
    b=float(botf_var.get()) #" "
    s=int(timespan_var.get()) #" "
    if topa!=t: #if obtained value differs from the currently set, the set is made to be equalt to the textbox value
        topa=t
    if bota!=b: #" "
        bota=b
    if span!=s: #" "
        span=s
    
def graphing():
    global topa
    global bota
    global span
    global funcgen_fcent
    global root
    global canvas
    global fig
    global graph
    global data_freq
    global run_start
    global data_time_
    while (1==1):
        if endThread.is_set():
            break
        LockThread.acquire()
        if (EventDATA.is_set() and len(data_time_)==len(data_freq)):            
            if len(data_time_)<=span:
                jj=data_time_[0]-0.5
            else:
                jj=data_time_[len(data_time_)-span]-0.5
            jjj=data_time_[len(data_time_)-1]+2
            topa_=funcgen_fcent+topa
##            print(str(data_time_[len(data_time_)-1])+"   "+str(topa)+"   "+str(topa_)+"\n")
            bota_=funcgen_fcent-bota
            title_="Run:     "+str(run_start)
            graph.clear()
            graph.plot(data_time_,data_freq,color="red")
            graph.set_title(title_,fontsize=15,fontweight='bold')
            graph.axis([jj,jjj,bota_,topa_])
            graph.set_xlabel("\nTime, t (s)", fontsize=11,fontweight='bold')
            graph.set_ylabel("Frequency, f (Hz)\n", fontsize=11,fontweight='bold')
            graph.grid()
            canvas.draw_idle()
            EventDATA.clear()
        LockThread.release()
        time.sleep(0.05)

def osc_signal_processor(data,scale,fcent):
    quant=10.0*scale/256.0;
    volts=[0]*(len(data)-7)
    i=0
    while i<len(volts):
        volts[i]=(float(data[i+6])-127.0)*quant;
        i=i+1
    value_volt=np.mean(volts)
    
    #####FIX THIS NUMERIC VALUE; IT COMES FROM THE CALIBRATION CURVE SLOPE AS    Hz/V ####
    output=value_volt*(0.4545/5)+fcent
    
    
    return output

##    return value_volt   
 
def freq_meassure():
    adjust_graph()
    global funcgen_fcent
    global rm
    global func_gen
    global osc
##    func_gen=rm.open_resource('USB0::0x1AB1::0x0642::DG1ZA201701936::INSTR')
    osc=rm.open_resource('USB0::0x0699::0x0368::C026273::INSTR')
    global data_time
    global data_time_
    global data_freq
    global run_start
    global big_s
    run_start=datetime.now().strftime("%Y.%m.%d-%H,,%M,,%S")
    title=str(run_start)+"__FreqData.csv"
    big_s="[Date] (Time),Time Stamp,Frequency f (Hz)\n"
    text_file = open(title, "wt")
    text_content = text_file.write(big_s)
    text_file.close()
    Fcentering=float(Fcenter_var.get())
##    func_gen.write(":SOUR1:APPL:SIN "+str(Fcentering)+",1.250,0,0")
##    funcgen_fcent=float(func_gen.query(':SOUR1:FREQ?'))
    funcgen_fcent=Fcentering
    data_time=[0]*1
    data_time_=[0]*1
    data_freq=[0]*1
    i=0
    while (1==1):
        if endThread.is_set():
            func_gen.close()
            osc.close()
            return
        else:
            LockThread.acquire()
            if (data_time[0]==0):
                
                data_time[0]=datetime.now()
##                data_freq[0]=funcgen_fcent+random.random()*1-0.5
                osc_curve=osc.query_binary_values('CURVE?', datatype='b', is_big_endian=True)
                osc_scale=float(osc.query('CH1:SCALe?'))
                data_freq[0]=osc_signal_processor(osc_curve,osc_scale,funcgen_fcent)
                data_time_[0]=data_time[0].timestamp()
            else:
                
                data_time.append(datetime.now())
##                data_freq.append(funcgen_fcent+random.random()*1-0.5)
                osc_curve=osc.query_binary_values('CURVE?', datatype='b', is_big_endian=True)
                osc_scale=float(osc.query('CH1:SCALe?'))
                data_freq.append(osc_signal_processor(osc_curve,osc_scale,funcgen_fcent))
                data_time_.append(data_time[i].timestamp())
            EventDATA.set()
            LockThread.release()
            print(str(data_time_[i])+"   "+str(data_freq[i])+"\n")
            big_s=data_time[i].strftime("%Y-%m-%d %H:%M:%S.%f")+","+str(data_time_[i])+","+str(data_freq[i])+"\n"
            text_file = open(title, 'a')
            text_content = text_file.write(big_s)
            text_file.close()
            i=i+1
            time.sleep(time_delay)
    endThread.set()

def data_thread_start():
    start["state"] = "disabled" #prevents the ability to press START until released
    endThread.clear()
    EventDATA.clear()
    thread_1=threading.Thread(target=graphing)
    thread_1.start()
    thread_2=threading.Thread(target=freq_meassure)
    thread_2.start()

def data_thread_stop():
    endThread.set()
    start["state"] = "normal" #pressing STOP releases START


fig= Figure(figsize=(8,6),dpi=123)
graph = fig.add_subplot()
canvas = FigureCanvasTkAgg(fig,master=root)
canvas.get_tk_widget().pack(side=tk.RIGHT)




timespan_label = tk.Label(control_frame,font=font_A,text="Graphing Window")
timespan_label_ = tk.Label(control_frame,text="latest points",font=font_B)
timespan_var = tk.StringVar(value="30")
timespan_entry = tk.Entry(control_frame,bg="#ffffff",textvariable=timespan_var,font=font_B)

Fcenter_label = tk.Label(control_frame,font=font_A,text="Center Frequency")
Fcenter_label_ = tk.Label(control_frame,text="Hz",font=font_B)
Fcenter_var = tk.StringVar(value="32745")
Fcenter_entry = tk.Entry(control_frame,bg="#ffffff",textvariable=Fcenter_var,font=font_B)

#Fspan_label = tk.Label(control_frame,font=font_A,text="Frequency Modulation Deviation")
#Fspan_label_ = tk.Label(control_frame,text="Hz",font=font_B)
#Fspan_var = tk.StringVar(value="2.5")
#Fspan_entry = tk.Entry(control_frame,bg="#ffffff",textvariable=Fspan_var,font=font_B)

topf_label = tk.Label(control_frame,font=font_A,text="Top Frequncy Limit Around Center")
topf_label_ = tk.Label(control_frame,text="Hz",font=font_B)
topf_var = tk.StringVar(value="5")
topf_entry = tk.Entry(control_frame,bg="#ffffff",textvariable=topf_var,font=font_B)

botf_label = tk.Label(control_frame,font=font_A,text="Bottom Frequncy Limit Around Center")
botf_label_ = tk.Label(control_frame,text="Hz",font=font_B)
botf_var = tk.StringVar(value="5")
botf_entry = tk.Entry(control_frame,bg="#ffffff",textvariable=botf_var,font=font_B)


Fcenter_label.grid(row=0,column=0,sticky="ews",padx=(25,10),pady=(50,5))
Fcenter_entry.grid(row=0,column=1,sticky="ews",padx=(10,10),pady=(50,5))
Fcenter_label_.grid(row=0, column=2,sticky="ews",padx=(10,25),pady=(50,5))

#Fspan_label.grid(row=1,column=0,sticky="ews",padx=(25,10),pady=(5,20))
#Fspan_entry.grid(row=1,column=1,sticky="ews",padx=(10,10),pady=(5,20))
#Fspan_label_.grid(row=1, column=2,sticky="ews",padx=(10,25),pady=(5,20))

topf_label.grid(row=5,column=0,sticky="ews",padx=(25,10),pady=(20,5))
topf_entry.grid(row=5,column=1,sticky="ews",padx=(10,10),pady=(20,5))
topf_label_.grid(row=5, column=2,sticky="ews",padx=(10,25),pady=(20,5))

botf_label.grid(row=6,column=0,sticky="ews",padx=(25,10),pady=(5,5))
botf_entry.grid(row=6,column=1,sticky="ews",padx=(10,10),pady=(5,5))
botf_label_.grid(row=6, column=2,sticky="ews",padx=(10,25),pady=(5,5))

timespan_label.grid(row=7,column=0,sticky="ews",padx=(25,10),pady=(5,75))
timespan_entry.grid(row=7,column=1,sticky="ews",padx=(10,10),pady=(5,75))
timespan_label_.grid(row=7, column=2,sticky="ews",padx=(10,25),pady=(5,75))


start=tk.Button(control_frame,text="START",font=font_A,bg="#7b7b7b",fg="#00DEDE",command=data_thread_start)
start.grid(row=10,column=0,columnspan=3,sticky="ews",padx=(25,25),pady=(2,2))
stop=tk.Button(control_frame,text="STOP",font=font_A,bg="#7b7b7b",fg="#DE0000",command=data_thread_stop)
stop.grid(row=11,column=0,columnspan=3,sticky="ews",padx=(25,25),pady=(2,2))
adjust=tk.Button(control_frame,text="ADJUST GRAPHING",font=font_A,bg="#00007B",fg="#ffffff",command=adjust_graph)
adjust.grid(row=12,column=0,columnspan=3,sticky="ews",padx=(25,25),pady=(35,2))
#save=tk.Button(control_frame,text="SAVE",font=font_A,bg="#7b7b7b",fg="#ffffff",command=save_data)
#save.grid(row=12,column=0,columnspan=3,sticky="ews",padx=(25,25),pady=(2,2))
Quit_button=tk.Button(control_frame,text="QUIT",font=font_A,bg="#6f0000",fg="#ffffff",command=quit)
Quit_button.grid(row=99,column=0,columnspan=3,sticky="ews",padx=(25,25),pady=(35,25))

tk.mainloop()
