# PROCESORY SYGNAŁOWE - PROJEKT
# ETAP 4 - ODDANIE PROJEKTU
# KACPER POŁATAJKO 241603

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import scipy.io.wavfile
import sys

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
      # print("Błąd wczytywania pliku wave: " + filename)
      return None
#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
# Funkcja dla przycisku "Wyjdź" - wyjście z programu
#===================================================
def exit_prog():
    sys.exit(0)
#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
# Klasa opisująca wszytskie potrzebne elementy GUI oraz
# inicjalizująca wszystkie potrzebne do działania funkcje.
#=========================================================
class Ui_MainWindow(object):
    # Inicjalizacja wszystkich elementów GUI (tak jak zostały zaprojektowane w QtDesignerze)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Procesor dźwięku")
        MainWindow.resize(341, 747)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 90, 321, 461))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")

        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_9.setGeometry(QtCore.QRect(0, 110, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")

        self.button_reverse = QtWidgets.QRadioButton(self.groupBox_9)
        self.button_reverse.setGeometry(QtCore.QRect(10, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_reverse.setFont(font)
        self.button_reverse.setObjectName("button_reverse")

        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 30, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")

        self.button_paulstretch = QtWidgets.QRadioButton(self.groupBox_7)
        self.button_paulstretch.setGeometry(QtCore.QRect(10, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_paulstretch.setFont(font)
        self.button_paulstretch.setObjectName("button_paulstretch")

        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(230, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")

        self.spinbox_paulstretch_wsp = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        self.spinbox_paulstretch_wsp.setGeometry(QtCore.QRect(140, 50, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinbox_paulstretch_wsp.setFont(font)
        self.spinbox_paulstretch_wsp.setDecimals(3)
        self.spinbox_paulstretch_wsp.setSingleStep(0.5)
        self.spinbox_paulstretch_wsp.setObjectName("spinbox_paulstretch_wsp")

        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setGeometry(QtCore.QRect(130, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")

        self.spinbox_paulstretch_roz = QtWidgets.QDoubleSpinBox(self.groupBox_7)
        self.spinbox_paulstretch_roz.setGeometry(QtCore.QRect(240, 50, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinbox_paulstretch_roz.setFont(font)
        self.spinbox_paulstretch_roz.setDecimals(3)
        self.spinbox_paulstretch_roz.setSingleStep(0.05)
        self.spinbox_paulstretch_roz.setObjectName("spinbox_paulstretch_roz")

        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_10.setGeometry(QtCore.QRect(0, 270, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setObjectName("groupBox_10")

        self.spinbox_amplify_wzm = QtWidgets.QDoubleSpinBox(self.groupBox_10)
        self.spinbox_amplify_wzm.setGeometry(QtCore.QRect(230, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinbox_amplify_wzm.setFont(font)
        self.spinbox_amplify_wzm.setDecimals(3)
        self.spinbox_amplify_wzm.setMinimum(-50.0)
        self.spinbox_amplify_wzm.setMaximum(50.0)
        self.spinbox_amplify_wzm.setSingleStep(0.5)
        self.spinbox_amplify_wzm.setObjectName("spinbox_amplify_wzm")
        self.button_amplify = QtWidgets.QRadioButton(self.groupBox_10)
        self.button_amplify.setGeometry(QtCore.QRect(10, 40, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_amplify.setFont(font)
        self.button_amplify.setObjectName("button_amplify")

        self.label_8 = QtWidgets.QLabel(self.groupBox_10)
        self.label_8.setGeometry(QtCore.QRect(200, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")

        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_8.setGeometry(QtCore.QRect(0, 180, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")

        self.spinbox_speed_mnoz = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.spinbox_speed_mnoz.setGeometry(QtCore.QRect(230, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinbox_speed_mnoz.setFont(font)
        self.spinbox_speed_mnoz.setDecimals(3)
        self.spinbox_speed_mnoz.setMinimum(0.0)
        self.spinbox_speed_mnoz.setMaximum(5.0)
        self.spinbox_speed_mnoz.setSingleStep(0.5)
        self.spinbox_speed_mnoz.setObjectName("spinbox_speed_mnoz")

        self.button_speed = QtWidgets.QRadioButton(self.groupBox_8)
        self.button_speed.setGeometry(QtCore.QRect(10, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_speed.setFont(font)
        self.button_speed.setObjectName("button_speed")

        self.label_7 = QtWidgets.QLabel(self.groupBox_8)
        self.label_7.setGeometry(QtCore.QRect(230, 10, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")

        self.checkBox_speed_1 = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_speed_1.setGeometry(QtCore.QRect(10, 30, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_speed_1.setFont(font)
        self.checkBox_speed_1.setObjectName("checkBox_speed_1")

        self.checkBox_speed_2 = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_speed_2.setGeometry(QtCore.QRect(100, 30, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_speed_2.setFont(font)
        self.checkBox_speed_2.setObjectName("checkBox_speed_2")

        self.groupBox_11 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_11.setGeometry(QtCore.QRect(0, 350, 321, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")

        self.label = QtWidgets.QLabel(self.groupBox_11)
        self.label.setGeometry(QtCore.QRect(90, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.groupBox_11)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.spinbox_repeat_start = QtWidgets.QDoubleSpinBox(self.groupBox_11)
        self.spinbox_repeat_start.setGeometry(QtCore.QRect(90, 40, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinbox_repeat_start.setFont(font)
        self.spinbox_repeat_start.setDecimals(3)
        self.spinbox_repeat_start.setMaximum(99999.99)
        self.spinbox_repeat_start.setSingleStep(0.1)
        self.spinbox_repeat_start.setObjectName("spinbox_repeat_start")

        self.spinbox_repeat_stop = QtWidgets.QDoubleSpinBox(self.groupBox_11)
        self.spinbox_repeat_stop.setGeometry(QtCore.QRect(170, 40, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinbox_repeat_stop.setFont(font)
        self.spinbox_repeat_stop.setDecimals(3)
        self.spinbox_repeat_stop.setMinimum(0.0)
        self.spinbox_repeat_stop.setMaximum(99999.99)
        self.spinbox_repeat_stop.setSingleStep(0.1)
        self.spinbox_repeat_stop.setObjectName("spinbox_repeat_stop")

        self.spinboxone_repeat_powt = QtWidgets.QSpinBox(self.groupBox_11)
        self.spinboxone_repeat_powt.setGeometry(QtCore.QRect(260, 70, 41, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinboxone_repeat_powt.setFont(font)
        self.spinboxone_repeat_powt.setObjectName("spinboxone_repeat_powt")

        self.label_3 = QtWidgets.QLabel(self.groupBox_11)
        self.label_3.setGeometry(QtCore.QRect(250, 30, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAcceptDrops(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.button_repeat = QtWidgets.QRadioButton(self.groupBox_11)
        self.button_repeat.setGeometry(QtCore.QRect(10, 70, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_repeat.setFont(font)
        self.button_repeat.setObjectName("button_repeat")

        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 0, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")

        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(60, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.filename_to_edit = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.filename_to_edit.setGeometry(QtCore.QRect(60, 40, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.filename_to_edit.setFont(font)
        self.filename_to_edit.setObjectName("filename_to_edit")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 560, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.button_save_many = QtWidgets.QRadioButton(self.groupBox)
        self.button_save_many.setGeometry(QtCore.QRect(10, 60, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_save_many.setFont(font)
        self.button_save_many.setObjectName("button_save_many")
        # self.button_save_many.toggled.connect(self.btnstate)

        self.button_save_one = QtWidgets.QRadioButton(self.groupBox)
        self.button_save_one.setGeometry(QtCore.QRect(10, 30, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_save_one.setFont(font)
        self.button_save_one.setObjectName("button_save_one")
        # self.button_save_one.toggled.connect(self.btnstate)

        self.button_apply = QtWidgets.QPushButton(self.centralwidget)
        self.button_apply.setGeometry(QtCore.QRect(10, 670, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_apply.setFont(font)
        self.button_apply.setObjectName("button_apply")
        self.button_apply.clicked.connect(self.exec_prog)

        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(220, 670, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_exit.setFont(font)
        self.button_exit.setDefault(False)
        self.button_exit.setObjectName("button_exit")
        self.button_exit.clicked.connect(lambda: exit_prog())

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 710, 321, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Funkcja wyświetlająca okno powiadomienia o poprawnym wykonaniu edycji dźwięku
    def show_popup_ok(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Gotowe!")
        msg.setInformativeText("Przetwarzanie dźwięku zakończone sukcesem.")
        msg.setWindowTitle("Procesor dźwięku - info")
        msg.exec_()

    # Funkcja wyświetlająca okno błędnego wyboru sposobu zapisu plików.
    def show_popup_error_save(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Błąd wyboru zapisu plików!")
        msg.setInformativeText("Nie wybrano opcji zapisu dźwięku.\nSpróbuj ponownie.")
        msg.setWindowTitle("Procesor dźwięku - błąd")
        msg.exec_()

    # Funkcja wyświetlająca okno błędnego wyboru pliku dźwiękowego wave.
    def show_popup_error_file(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Błąd wyboru pliku dźwiękowego wave!")
        msg.setInformativeText("Wybrany plik nie istnieje lub wpisano błędną nazwę.\nSpróbuj ponownie.")
        msg.setWindowTitle("Procesor dźwięku - błąd")
        msg.exec_()

    # Funkcja wyświetlająca okno błędnego wyboru efektu dźwiękowego.
    def show_popup_error_effects(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Błąd wyboru efektów dźwiękowych!")
        msg.setInformativeText("Nie wybrano żadnego efektu dźwiękowego.\nSpróbuj ponownie.")
        msg.setWindowTitle("Procesor dźwięku - błąd")
        msg.exec_()

    # Funkcja inicjalizująca zapewnienie całej funkcjonalności programu przy pomocy GUI
    def exec_prog(self):
        effect_param = [0, 0, 0, 0, 0]

        # Wybór opcji zapisu
        if self.button_save_one.isChecked():
            save_param = 1
        elif self.button_save_many.isChecked():
            save_param = 2
        else:
            self.show_popup_error_save()
            return

        # Wybór efektów
        if self.button_paulstretch.isChecked():
            effect_param[0] = 1
            window_size = self.spinbox_paulstretch_roz.value()
            stretch = self.spinbox_paulstretch_wsp.value()
        if self.button_reverse.isChecked():
            effect_param[1] = 1
        if self.button_speed.isChecked():
            effect_param[2] = 1
            multiplier = self.spinbox_speed_mnoz.value()
            chsp_choice_1 = self.checkBox_speed_1.isChecked()
            chsp_choice_2 = self.checkBox_speed_2.isChecked()
        if self.button_amplify.isChecked():
            effect_param[3] = 1
            dB = self.spinbox_amplify_wzm.value()
        if self.button_repeat.isChecked():
            effect_param[4] = 1
            start_time = self.spinbox_repeat_start.value()
            stop_time = self.spinbox_repeat_stop.value()
            amount = self.spinboxone_repeat_powt.value()
        elif (self.button_paulstretch.isChecked() or self.button_reverse.isChecked() or self.button_speed.isChecked()
              or self.button_amplify.isChecked() or self.button_repeat.isChecked()) == False:
            self.show_popup_error_effects()
            return

        # Wybór pliku do edycji
        name_wav = self.filename_to_edit.toPlainText()
        if load_wav_file(name_wav) == None:
            self.show_popup_error_file()
            return

        if effect_param[0] == 1:
            (samplerate, samples) = load_wav_file(name_wav)
            if save_param == 1:
               new_name_wav = name_wav
            elif save_param == 2:
               new_name_wav = 'Paulstretch_' + name_wav
            paulstretch(samplerate, samples, stretch, window_size, new_name_wav)

        if effect_param[1] == 1:
            (samplerate, samples) = load_wav_file(name_wav)
            if save_param == 1:
               new_name_wav = name_wav
            elif save_param == 2:
               new_name_wav = 'Reverse_' + name_wav
            reverse(samplerate, samples, new_name_wav)

        if effect_param[2] == 1:
            (samplerate, samples) = load_wav_file(name_wav)
            if save_param == 1:
               new_name_wav_1 = name_wav
               new_name_wav_2 = name_wav
            elif save_param == 2:
               new_name_wav_1 = 'ChangeSpeed1_' + name_wav
               new_name_wav_2 = 'ChangeSpeed2_' + name_wav
            if chsp_choice_1 == True:
               change_speed_1(samplerate, samples, multiplier, new_name_wav_1)
            if chsp_choice_2 == True:
               change_speed_2(samplerate, samples, multiplier, new_name_wav_2)

        if effect_param[3] == 1:
            (samplerate, samples) = load_wav_file(name_wav)
            if save_param == 1:
               new_name_wav = name_wav
            elif save_param == 2:
               new_name_wav = 'Amplify_' + name_wav
            amplify(samplerate, samples, dB, new_name_wav)

        if effect_param[4] == 1:
            (samplerate, samples) = load_wav_file(name_wav)
            if save_param == 1:
               new_name_wav = name_wav
            elif save_param == 2:
               new_name_wav = 'Repeat_' + name_wav
            repeat_sample(samplerate, samples, start_time, stop_time, amount, new_name_wav)
        self.show_popup_ok()

    # Funkcja nadająca każdemu elementowi GUI nazwę w oknie
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Procesor dźwięku"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Efekty"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Reverse"))
        self.button_reverse.setText(_translate("MainWindow", "Odwrócenie w czasie"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Paulstretch"))
        self.button_paulstretch.setText(_translate("MainWindow", "Efekt Paustretch"))
        self.label_5.setText(_translate("MainWindow", "Rozdzielczość czasu"))
        self.label_6.setText(_translate("MainWindow", "Współczynnik rozciągania"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Amplify"))
        self.button_amplify.setText(_translate("MainWindow", "Wzmocnienie dźwięku"))
        self.label_8.setText(_translate("MainWindow", "Wartość wzmocnienia w dB"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Change Speed"))
        self.button_speed.setText(_translate("MainWindow", "Zmiana prędkości odtwarzania"))
        self.label_7.setText(_translate("MainWindow", "Mnożnik prędkości"))
        self.checkBox_speed_1.setText(_translate("MainWindow", "Metoda I"))
        self.checkBox_speed_2.setText(_translate("MainWindow", "Metoda II"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Repeat"))
        self.label.setText(_translate("MainWindow", "START"))
        self.label_2.setText(_translate("MainWindow", "STOP"))
        self.label_3.setText(_translate("MainWindow", "Ilość powtórzeń"))
        self.button_repeat.setText(_translate("MainWindow", "Powtórz zaznaczony fragment"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Plik"))
        self.label_4.setText(_translate("MainWindow", "Podaj nazwę pliku do edycji"))
        self.groupBox.setTitle(_translate("MainWindow", "Zapis"))
        self.button_save_many.setText(_translate("MainWindow", "Każdy efekt w osobnym pliku"))
        self.button_save_one.setText(_translate("MainWindow", "Nadpisanie pliku wejściowego"))
        self.button_apply.setText(_translate("MainWindow", "Zastosuj"))
        self.button_exit.setText(_translate("MainWindow", "Wyjdź"))
        self.label_9.setText(_translate("MainWindow", "Wykonał: Kacper Połatajko 241603"))
#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
# Funkcja main programu.
# Inicjalizuje wszystkie zmienne potrzebne do uruchomienia programu z GUI.
#=========================================================================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
#--------------------------------------------------------------------------------------------------