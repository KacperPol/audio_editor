from numpy import *
import wave
import random

#--------------------------------------------------------------------------------------------------
# Funkcja zmieniająca prędkość utworu.
# W zależności od zmiany prędkości usuwamy losowo lub dodajemy zdublowane losowo próbki.
#=======================================================================================
def change_speed_1(samplerate, samples, multiplier, outfilename):
   nchannels = samples.shape[0]
   outfile = wave.open(outfilename, 'wb')
   outfile.setsampwidth(2)
   outfile.setframerate(samplerate)
   outfile.setnchannels(nchannels)
   
   newL = samples[0]
   newR = samples[1]
   # print('Max value: ', max(newL))
   # print('Min value: ', min(newR))

   # procent = multiplier * 100.00 - 100.00

   to_del = int(newL.size * (multiplier - 1.00))
   # new_smp = newL.size - to_del

   # Jeśli multiplier > 1.00 to zmniejsz liczbę próbek
   # Próbki losowane są z tablicy próbek i usuwane
   if multiplier > 1.00:
      randomList = random.sample(range(0, newL.size), to_del)
      newL = delete(newL, randomList)
      newR = delete(newR, randomList)
   # Jeśli multiplier < 1.00 to zwiększ liczbę próbek
   # Próbki losowane są z tablicy próbek i dublowane
   elif multiplier < 1.00:
      randomList = random.sample(range(0, newL.size), -to_del)
      itemListL = newL[randomList]
      itemListR = newR[randomList]
      newL = insert(newL, randomList, itemListL)
      newR = insert(newR, randomList, itemListR)
       
   new = vstack((newL, newR))

   outfile.writeframes(int16(new.reshape(-1, order='F') * 32767.0).tobytes())
   outfile.close()
   print('Change speed (metoda I) - Gotowe!')
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
# Funkcja zmieniająca prędkość utworu.
# Jedyny parametr, który zmieniamy to częstotliwość próbkowania.
#===============================================================
def change_speed_2(samplerate, samples, multiplier, outfilename):
   nchannels = samples.shape[0]
   outfile = wave.open(outfilename, 'wb')
   outfile.setsampwidth(2)
   outfile.setframerate(samplerate * multiplier)
   outfile.setnchannels(nchannels)
   
   newL = samples[0]
   newR = samples[1]
   new = vstack((newL, newR))

   outfile.writeframes(int16(new.reshape(-1, order='F') * 32767.0).tobytes())
   outfile.close()
   print('Change speed (metoda II) - Gotowe!')
#--------------------------------------------------------------------------------------------------