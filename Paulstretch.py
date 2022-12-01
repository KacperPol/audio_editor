from numpy import *
import wave

# --------------------------------------------------------------------------------------------------
# Funkcja implementująca efekt dźwiękowy paulstretch.
# ===================================================
def paulstretch(samplerate, samples, stretch, window_size_seconds, outfilename):
    # Przygotowanie dźwięku (próbek) do edycji
    # ========================================
    nchannels = samples.shape[0]
    outfile = wave.open(outfilename, 'wb')
    outfile.setsampwidth(2)
    outfile.setframerate(samplerate)
    outfile.setnchannels(nchannels)

    # Sprawdzenie czy rozmiar okna (ilość próbek) jest parzysty i większy od 16
    window_size = int(window_size_seconds * samplerate)
    if window_size < 16:
        window_size = 16
    window_size = opt_window_size(window_size)
    window_size = int(window_size / 2) * 2
    half_window_size = int(window_size / 2)

    # Poprawienie końca zbioru próbek
    nsamples = samples.shape[1]
    end_size = int(samplerate * 0.05)
    if end_size < 16:
        end_size = 16
    samples[:, nsamples - end_size:nsamples] *= linspace(1, 0, end_size)

    # Obliczenie przesunięcia wewnątrz pliku wejściowego
    start_pos = 0.0
    displace_pos = (window_size * 0.5) / stretch

    # Stworzenie okna okna czasu
    window = pow(1.0 - pow(linspace(-1.0, 1.0, window_size), 2.0), 1.25)
    old_windowed_buffer = zeros((2, window_size))

    # Właściwe zastosowanie efektu
    # ============================
    while True:
        # Znalezienie bufora okna
        istart_pos = int(floor(start_pos))
        buffer = samples[:, istart_pos:istart_pos + window_size]
        if buffer.shape[1] < window_size:
            buffer = append(buffer, zeros((2, window_size - buffer.shape[1])), 1)
        buffer = buffer * window

        # Uzyskanie amplitudy składowych częstotliwości i pominięcie fazy
        frequencies = abs(fft.rfft(buffer))

        # Dobranie losowo faz poprzez pomnożenie przez losową liczbę zespoloną o module = 1
        phase = random.uniform(0, 2 * pi, (nchannels, frequencies.shape[1])) * 1j
        frequencies = frequencies * exp(phase)

        # Odwrotna szybka transformata Fouriera
        buffer = fft.irfft(frequencies)

        # Dodanie do okna wyjściowego bufferora
        buffer *= window

        # Nałożenie wyjścia
        output = buffer[:, 0:half_window_size] + old_windowed_buffer[:, half_window_size:window_size]
        old_windowed_buffer = buffer

        # Ograniczenie wartości w przedziale <-1.0, 1.0>
        output[output > 1.0] = 1.0
        output[output < -1.0] = -1.0

        # Zapisz wyjście do pliku wave (.wav)
        outfile.writeframes(int16(output.reshape(-1, order='F') * 32767.0).tobytes())

        # Sprawdzenie czy wszystkie próbki zostały przetworzone (jeśli tak - wyświetl "Gotowe!")
        start_pos += displace_pos
        if start_pos >= nsamples:
            print('Paulstretch - Gotowe!')
            break

    outfile.close()  # zamknięcie edycji pliku
# --------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------
# Funkcja optymalizująca rozdzielczość okna czasu.
# (a dokładniej liczbę próbek mieszczących się w danym oknie) efektu paulstretch.
# ===============================================================================
def opt_window_size(n):
    temp_n = n
    while True:
        n = temp_n
        while (n % 2) == 0:
            n /= 2
        while (n % 3) == 0:
            n /= 3
        while (n % 5) == 0:
            n /= 5
        if n < 2:
            break
        temp_n += 1
    return temp_n
# --------------------------------------------------------------------------------------------------
