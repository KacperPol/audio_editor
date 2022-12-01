from numpy import *
import wave

#--------------------------------------------------------------------------------------------------
# Funkcja wzmacniająca cały utwór o wybraną wartość wzmocnienia (w dB.).
#=======================================================================
def amplify(samplerate, samples, dB, outfilename):
   nchannels = samples.shape[0]
   outfile = wave.open(outfilename, 'wb')
   outfile.setsampwidth(2)
   outfile.setframerate(samplerate)
   outfile.setnchannels(nchannels)

   newL = samples[0]
   newR = samples[1]

   amp = pow(10, dB / 20)

   newL = newL * amp
   newR = newR * amp

   newL[newL > 1.0] = 1.0
   newL[newL < -1.0] = -1.0
   newR[newR > 1.0] = 1.0
   newR[newR < -1.0] = -1.0

   # print(max(newL))
   # print(max(newR))
   # print(min(newL))
   # print(min(newR))
   new = vstack((newL, newR))

   outfile.writeframes(int16(new.reshape(-1, order='F') * 32767.0).tobytes())
   outfile.close()
   print('Amplify - Gotowe!')
#--------------------------------------------------------------------------------------------------