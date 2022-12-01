from numpy import *
import wave

#--------------------------------------------------------------------------------------------------
# Funkcja powtarzająca wybrany fragment dźwięku (w sek.) o wybraną ilosć razy.
#=============================================================================
def repeat_sample(samplerate, samples, start_time, stop_time, amount,  outfilename):
   nchannels = samples.shape[0]
   outfile = wave.open(outfilename, 'wb')
   outfile.setsampwidth(2)
   outfile.setframerate(samplerate)
   outfile.setnchannels(nchannels)
   
   # print("Długość: ", samples.shape[1] / samplerate)

   newL = samples[0]
   newR = samples[1]

   start_id = int(start_time * samplerate)
   stop_id = int(stop_time * samplerate)

   # print(start_id)
   # print(stop_id)

   sample_pieces = arange(start_id, stop_id + 1, 1)
   # print(sample_pieces)

   newL_piece = newL[sample_pieces]
   newR_piece = newR[sample_pieces]

   for i in range(amount):
      newL = insert(newL, start_id, newL_piece)
      newR = insert(newR, start_id, newR_piece)

   new = vstack((newL, newR))

   outfile.writeframes(int16(new.reshape(-1, order='F') * 32767.0).tobytes())
   outfile.close()
   print('Repeat - Gotowe!')
# --------------------------------------------------------------------------------------------------