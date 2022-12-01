# PROCESORY SYGNAŁOWE - PROJEKT
# ETAP 4 - ODDANIE PROJEKTU
# KACPER POŁATAJKO 241603

# Importowanie wszystkich potrzebnych bibliotek
import scipy.io.wavfile
# from numpy import *

from Paulstretch import *
from Reverse import *
from Change_speed import *
from Repeat import *
from Amplify import *

#--------------------------------------------------------------------------------------------------
# Funkcja wczytująca plik wave i pobierająca z niego dane (częstotliwość próbkowania i próbki).
#==============================================================================================
def load_wav_file(filename):
   try:
      wavedata = scipy.io.wavfile.read(filename)
      samplerate = int(wavedata[0])
      samples = wavedata[1] * (1.0 / 32768.0) # 1/(2^15)
      samples = samples.transpose()
      if len(samples.shape) == 1:  # jeśli plik mono to przekonwertuj do stereo
         samples = tile(samples, (2, 1))
      return (samplerate, samples)
   except:
      print("Błąd wczytywania pliku wave: " + filename)
      return None
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
# Funkcja wyświetlająca menu główne.
#===================================
def print_menu_1():
   print('\n_______________| MENU |_______________')
   print('[1] - Podaj nazwę pliku wave do edycji')
   print('[2] - Wyjdź')
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
# Funkcja wyświetlająca menu efektów (po dodaniu pliku wave do edycji).
#======================================================================
def print_menu_2():
   print('\n__________| EFEKTY |__________')
   print('[1] - Paulstretch')
   print('[2] - Reverse')
   print('[3] - Change Speed')
   print('[4] - Amplify')
   print('[5] - Repeat')
   print('[6] - Cofnij')
#--------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------
# Główna pętla programu.
#=======================
while True:
   print_menu_1()
   choice_1 = input('Wybierz: ')
   choice_1 = int(choice_1)

   if choice_1 == 1:
      print('\nWprowadź nazwę pliku wave')
      name_wav = input('Podaj nazwę: ')

      if load_wav_file(name_wav) == None:
         # print('Nie udało się wczytać pliku wave')
         choice_2 = False
      else:
         print('Wczytano plik: '+ name_wav)
         choice_2 = True

      print('\nWybierz sposób zapisu pliku:')
      print('[1] - Nadpisywanie pliku wejściowego')
      print('[2] - Nowy plik na każdy wybrany efekt')
      saving_choice = input('Wybierz: ')
      saving_choice = int(saving_choice)

      # Pętla efektów
      while choice_2:
         print_menu_2()
         choice_3 = input('Wybierz: ')
         choice_3 = int(choice_3)

         if choice_3 == 1:
            print('\nWybrano efekt: Paulstretch')
            (samplerate, samples) = load_wav_file(name_wav)

            if saving_choice == 1:
               new_name_wav = name_wav
            else:
               new_name_wav = 'Paulstretch_' + name_wav

            stretch, window_size = input('Wprowadź współczynnik rozciągania i '
                                         'rozdzielczość czasu (sekundy): ').split(',')
            print('\nWspółczynnik rozciągania: ', stretch)
            print('Rozdzielczość czasu: ' + window_size + '\n' )
            stretch = float(stretch)
            window_size = float(window_size)

            paulstretch(samplerate, samples, stretch, window_size, new_name_wav)

         elif choice_3 == 2:
            print('\nWybrano efekt: Reverse')
            (samplerate, samples) = load_wav_file(name_wav)

            if saving_choice == 1:
               new_name_wav = name_wav
            else:
               new_name_wav = 'Reverse_' + name_wav

            reverse(samplerate, samples, new_name_wav)

         elif choice_3 == 3:
            print('\nWybrano efekt: Change Speed')
            (samplerate, samples) = load_wav_file(name_wav)

            if saving_choice == 1:
               new_name_wav_1 = name_wav
               new_name_wav_2 = name_wav
            else:
               new_name_wav_1 = 'ChangeSpeed1_' + name_wav
               new_name_wav_2 = 'ChangeSpeed2_' + name_wav

            multiplier = input('Wprowadź wartość mnożnika prędkości: ')
            multiplier = float(multiplier)

            print('\nKtóry parametr uchronić przed edycją?')
            print('[1] - Częstotliwość próbkowania')
            print('[2] - Ilość próbek')
            chsp_choice = input('Wybierz: ')
            chsp_choice = int(chsp_choice)

            if chsp_choice == 1:
               change_speed_1(samplerate, samples, multiplier, new_name_wav_1)
            elif chsp_choice == 2:
               change_speed_2(samplerate, samples, multiplier, new_name_wav_2)
            else:
               print('Podano zły numer. Spróbuj jeszcze raz.')

         elif choice_3 == 4:
            print('\nWybrano efekt: Amplify')
            (samplerate, samples) = load_wav_file(name_wav)

            if saving_choice == 1:
               new_name_wav = name_wav
            else:
               new_name_wav = 'Amplify_' + name_wav

            dB = input('Wprowadź wartość wzmocnienia (dB): ')
            dB = float(dB)

            amplify(samplerate, samples, dB, new_name_wav)

         elif choice_3 == 5:
            print('\nWybrano efekt: Repeat')
            (samplerate, samples) = load_wav_file(name_wav)

            if saving_choice == 1:
               new_name_wav = name_wav
            else:
               new_name_wav = 'Repeat_' + name_wav

            start_time, stop_time = input('Podaj czas początku i końca fragmentu do powtórzenia (sekundy): ').split(',')
            start_time = float(start_time)
            stop_time = float(stop_time)

            amount = input('Ile razy powtórzyć wybrany fragment?: ')
            amount = int(amount)

            repeat_sample(samplerate, samples, start_time, stop_time, amount, new_name_wav)

         elif choice_3 == 6:
            print('\nWybrano Cofnij...')
            choice_2 = False

   elif choice_1 == 2:
      print('\nZamykanie...')
      break

   else:
      print('Podano zły numer. Spróbuj jeszcze raz.\n')
# --------------------------------------------------------------------------------------------------