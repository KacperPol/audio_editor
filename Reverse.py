from numpy import *
import wave

#--------------------------------------------------------------------------------------------------
# Funkcja odwracająca utwór w czasie.
#====================================
def reverse(samplerate, samples, outfilename):
   nchannels = samples.shape[0]
   outfile = wave.open(outfilename, 'wb')
   outfile.setsampwidth(2)
   outfile.setframerate(samplerate)
   outfile.setnchannels(nchannels)

   newL = samples[0][::-1]
   newR = samples[1][::-1]
   new = vstack((newL, newR))

   # new = new.transpose()
   # scipy.io.wavfile.write('odwr.wav', samplerate, new)

   outfile.writeframes(int16(new.reshape(-1, order='F') * 32767.0).tobytes())
   outfile.close()
   print('Reverse - Gotowe!')
#--------------------------------------------------------------------------------------------------
