# Import Libraries
import matplotlib.pyplot as plt
from scipy.io import wavfile
from pylab import *

#Read Audio File
samplingFrequency, sound=wavfile.read('440_sine.wav')
numberOfSamples=sound.shape[0]

#Single Channel
sound1=sound[:,0]

# Show Length
print("Length of Audio file:", (numberOfSamples/samplingFrequency)*1000, " ms")

#Plotting Amplitude over time
timeArray=arange(0, numberOfSamples, 1)
timeArray=timeArray/samplingFrequency
timeArray=timeArray*1000
print('Plotting Amplitude Vs Time....')
plt.plot(timeArray,sound1, color='k')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.show()


n=len(sound1)
p=fft(sound1)
uniqueFreqs=int(ceil((n+1)/2.0))
p=p[0:uniqueFreqs]
p=abs(p)

p=p/float(n)
p=p**2

if n%2>0:
    p[1:len(p)]=p[1:len(p)]*2
else:
    p[1:len(p)-1]=p[1:len(p)-1]*2
freqArray=arange(0, uniqueFreqs, 1.0)*(samplingFrequency/n)
print('Plotting Frequency Content.....')
plt.plot(freqArray/1000, 10*log10(p), color='k')
plt.xlabel('Frequency (KHz)')
plt.ylabel('Power (dB)')
plt.show()
    