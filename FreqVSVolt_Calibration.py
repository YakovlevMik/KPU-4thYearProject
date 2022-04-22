#Library imports
import pyvisa
import time
import statistics
import numpy as np
import random

#PARAMETERS FOR CALLIBRATION RUN

FG_name='USB0::0x1AB1::0x0642::DG1ZA201701936::INSTR'
OSC_name='USB0::0x0699::0x0368::C026273::INSTR'
size=600 # number of oscilloscope frequency measurements per voltage point
V_max=6.5 # absolute maximum voltage to be checked in sweep (Volt)
V_delta=0.1 # spacing of voltage points (Volt)
t_delta=0.1 # rate of oscilloscope frequency capture (seconds)
fwd_bwd_cycles=20 # Number of forward-backward sweeps




#Setting up connection with function generator & oscilloscope
rm=pyvisa.ResourceManager()
func_gen=rm.open_resource(FG_name) #function generator
osc=rm.open_resource(OSC_name) #oscilloscope



# Loop for figuring out the number of voltage points for dta-storing arrays
i=V_max*-1
v_set=1
while i!=999:
    i=i+V_delta
    if i>V_max:
        i=999
    else:
        v_set=v_set+1

#array creation
data_func=[0]*v_set
data_osc=[0]*v_set
data_avg=[0]*v_set
data_stdev=[0]*v_set

# measurement/saving cycle
cycle=0
while (cycle<fwd_bwd_cycles):
    string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n" #headers for the data storing
    i=0
    while i <len(data_osc):
        data_osc[i]=[0]*size
        data_func[i]=V_max*-1+i*V_delta
        func_command=func_gen.write(":SOUR1:APPL:DC 1,1,2"+str(data_func[i])) #set new voltage on function generator
        j=0
        while j<size:
            data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?")) #obtaining frequency reading from oscilloscope
            time.sleep(t_delta) #time delay between frequency captures
            j=j+1
        data_avg[i]=np.mean(data_osc[i]) # obtaining average frequency for the specific voltage point
        data_stdev[i]=np.std(data_osc[i]) # obtaining standard deviation in frequency for the specific voltage point
        string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n" # adding average and stdev values to total string that will be later saved
        i=i+1
    name="FG___Freq_vs_Volt_Calibration___forward_"+str(cycle+1)+".txt" #automated naming of data files
    text_file = open(name, "wt") #data file creation
    n = text_file.write(string) #saving the string into the data file
    text_file.close() #data file closure
    
    string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
    i=0
    while i <len(data_osc):
        data_osc[i]=[0]*size
        data_func[i]=V_max-i*V_delta
        func_command=func_gen.write(":SOUR1:APPL:DC 1,1,2"+str(data_func[i]))
        j=0
        while j<size:
            data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
            time.sleep(t_delta)
            j=j+1
        data_avg[i]=np.mean(data_osc[i])
        data_stdev[i]=np.std(data_osc[i])
        string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
        i=i+1
    name="FG___Freq_vs_Volt_Calibration___backward_"+str(cycle+1)+".txt"
    text_file = open(name, "wt")
    n = text_file.write(string)
    text_file.close()
    cycle=cycle+1
