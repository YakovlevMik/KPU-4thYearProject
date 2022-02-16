import pyvisa
import time
#import statistics
import numpy as np
#import random

rm=pyvisa.ResourceManager() # creates resource manager require for communication with function generator
#func_gen=rm.open_resource('USB0::0x1AB1::0x0642::DG1ZA201701936::INSTR')
#osc=rm.open_resource('USB0::0x0699::0x0368::C026273::INSTR')

size=2
V_max=0.1
V_delta=0.1
t_delta=0.1

i=V_max*-1
v_set=1
while i!=999:
    i=i+V_delta
    if i==V_max or i>V_max:
        i=999
    else:
        v_set=v_set+1

data_func=[0]*v_set
data_osc=[0]*v_set
data_avg=[0]*v_set
data_stdev=[0]*v_set





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_1.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_1.txt", "wt")
n = text_file.write(string)
text_file.close()





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_2.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_2.txt", "wt")
n = text_file.write(string)
text_file.close()





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_3.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_3.txt", "wt")
n = text_file.write(string)
text_file.close()





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_4.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_4.txt", "wt")
n = text_file.write(string)
text_file.close()





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_5.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_5.txt", "wt")
n = text_file.write(string)
text_file.close()





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_6.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_6.txt", "wt")
n = text_file.write(string)
text_file.close()





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_7.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_7.txt", "wt")
n = text_file.write(string)
text_file.close()





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_8.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_8.txt", "wt")
n = text_file.write(string)
text_file.close()


string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_9.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_9.txt", "wt")
n = text_file.write(string)
text_file.close()





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_10.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_10.txt", "wt")
n = text_file.write(string)
text_file.close()





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_11.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_11.txt", "wt")
n = text_file.write(string)
text_file.close()





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_12.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_12.txt", "wt")
n = text_file.write(string)
text_file.close()





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_13.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_13.txt", "wt")
n = text_file.write(string)
text_file.close()





string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max*-1+i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("forward_14.txt", "wt")
n = text_file.write(string)
text_file.close()

string="Voltage DC (V),Mean Frequency (Hz), STDEV Frequency (Hz)\n"
i=0
while i <len(data_osc):
    data_osc[i]=[0]*size
    data_func[i]=V_max-i*V_delta
    #func_command=func_gen.write(":SOUR1:APPL:NOIS 0.002,"+str(data_func[i]))
    j=0
    while j<size:
        #data_osc[i][j]=float(osc.query("TRIGger:MAIn:FREQuency?"))
        time.sleep(t_delta)
        j=j+1
    data_avg[i]=np.mean(data_osc[i])
    data_stdev[i]=np.std(data_osc[i])
    string=string+str(data_func[i])+","+str(data_avg[i])+","+str(data_stdev[i])+"\n"
    i=i+1
text_file = open("backward_14.txt", "wt")
n = text_file.write(string)
text_file.close()