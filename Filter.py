import soundfile as sf
import numpy as np
hold =0.03560  #560
y,sr =sf.read("junshi.wav") # The path of reading file
y_new=y.copy()
flags =[]
final =[]
#print(y,sr,np.shape(y))
print("Begin Filter")
length =len(y_new)
step =int((0.001*length)/2) #0.02
index =int(0.04*length)  #0.3
for i in range(length):
  if (-hold<y_new[i]<hold) and (y_new[i]!=0):
    y_new[i]=0  #clear the noise
print("Building")
for i in range(length):
  flag=0
  if y_new[i]!=0:
    flag=i
    flags.append(flag)
#print(flags[0],flags[-1])
sig_add=[]
fir_flag =flags[0]
final_flag =flags[-1]
sig_add.append(fir_flag)
while(fir_flag<=final_flag):
  fir_flag+=step
  sig_add.append(fir_flag)
#print("flags are in flags list",flags,flags[0],flags[-1])
#print("recover signal is :",sig_add,np.shape(sig_add))
for i in sig_add:
  left =i-step
  right =i+step
  if right>length:
    right =length
  for j in range(left,right):
    if y_new[j]==0:
      y_new[j]=y[j] # recover the speech

sf.write("junshiFilter.wav",y_new,sr) #The path of saving file
print("Over Filter")