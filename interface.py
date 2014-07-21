# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pablo/PythonProjects/Classificador/interface.ui'
#
# Created: Mon Jul 21 11:38:38 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from widgets.imagem_clicavel import ImagemClicavel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1405, 806)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagem_original = ImagemClicavel(self.centralwidget)
        self.imagem_original.setGeometry(QtCore.QRect(10, 10, 681, 491))
        self.imagem_original.setMouseTracking(False)
        self.imagem_original.setFrameShape(QtGui.QFrame.Box)
        self.imagem_original.setScaledContents(True)
        self.imagem_original.setObjectName("imagem_original")
        self.imagem_classificada = QtGui.QLabel(self.centralwidget)
        self.imagem_classificada.setGeometry(QtCore.QRect(720, 10, 671, 491))
        self.imagem_classificada.setFrameShape(QtGui.QFrame.Box)
        self.imagem_classificada.setScaledContents(True)
        self.imagem_classificada.setObjectName("imagem_classificada")
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(820, 710, 62, 27))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(770, 720, 66, 17))
        self.label.setObjectName("label")
        self.files_list = QtGui.QListWidget(self.centralwidget)
        self.files_list.setGeometry(QtCore.QRect(10, 530, 241, 211))
        self.files_list.setObjectName("files_list")
        self.imagem_exif_list = QtGui.QListView(self.centralwidget)
        self.imagem_exif_list.setGeometry(QtCore.QRect(1140, 550, 256, 192))
        self.imagem_exif_list.setObjectName("imagem_exif_list")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 540, 66, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1150, 510, 66, 17))
        self.label_4.setObjectName("label_4")
        self.caminho_pasta_imagens = QtGui.QLineEdit(self.centralwidget)
        self.caminho_pasta_imagens.setGeometry(QtCore.QRect(260, 720, 161, 27))
        self.caminho_pasta_imagens.setObjectName("caminho_pasta_imagens")
        self.botao_pasta_imagens = QtGui.QPushButton(self.centralwidget)
        self.botao_pasta_imagens.setGeometry(QtCore.QRect(427, 720, 61, 27))
        self.botao_pasta_imagens.setObjectName("botao_pasta_imagens")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(430, 540, 341, 111))
        self.groupBox.setObjectName("groupBox")
        self.hsv_h = QtGui.QDoubleSpinBox(self.groupBox)
        self.hsv_h.setGeometry(QtCore.QRect(20, 30, 62, 27))
        self.hsv_h.setMaximum(1000.0)
        self.hsv_h.setObjectName("hsv_h")
        self.hsv_s = QtGui.QDoubleSpinBox(self.groupBox)
        self.hsv_s.setGeometry(QtCore.QRect(90, 30, 62, 27))
        self.hsv_s.setMaximum(1000.0)
        self.hsv_s.setObjectName("hsv_s")
        self.hsv_v = QtGui.QDoubleSpinBox(self.groupBox)
        self.hsv_v.setGeometry(QtCore.QRect(160, 30, 62, 27))
        self.hsv_v.setMaximum(1000.0)
        self.hsv_v.setObjectName("hsv_v")
        self.hsv_h_2 = QtGui.QDoubleSpinBox(self.groupBox)
        self.hsv_h_2.setGeometry(QtCore.QRect(20, 70, 62, 27))
        self.hsv_h_2.setMaximum(1000.0)
        self.hsv_h_2.setObjectName("hsv_h_2")
        self.hsv_v_2 = QtGui.QDoubleSpinBox(self.groupBox)
        self.hsv_v_2.setGeometry(QtCore.QRect(160, 70, 62, 27))
        self.hsv_v_2.setMaximum(1000.0)
        self.hsv_v_2.setObjectName("hsv_v_2")
        self.hsv_s_2 = QtGui.QDoubleSpinBox(self.groupBox)
        self.hsv_s_2.setGeometry(QtCore.QRect(90, 70, 62, 27))
        self.hsv_s_2.setMaximum(1000.0)
        self.hsv_s_2.setObjectName("hsv_s_2")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(240, 70, 67, 17))
        self.label_5.setObjectName("label_5")
        self.recalcular = QtGui.QPushButton(self.centralwidget)
        self.recalcular.setGeometry(QtCore.QRect(560, 710, 99, 27))
        self.recalcular.setObjectName("recalcular")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(750, 540, 341, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.hsv_h_3 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.hsv_h_3.setGeometry(QtCore.QRect(20, 30, 62, 27))
        self.hsv_h_3.setMaximum(1000.0)
        self.hsv_h_3.setObjectName("hsv_h_3")
        self.hsv_s_3 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.hsv_s_3.setGeometry(QtCore.QRect(90, 30, 62, 27))
        self.hsv_s_3.setMaximum(1000.0)
        self.hsv_s_3.setObjectName("hsv_s_3")
        self.hsv_v_3 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.hsv_v_3.setGeometry(QtCore.QRect(160, 30, 62, 27))
        self.hsv_v_3.setMaximum(1000.0)
        self.hsv_v_3.setObjectName("hsv_v_3")
        self.hsv_h_4 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.hsv_h_4.setGeometry(QtCore.QRect(20, 70, 62, 27))
        self.hsv_h_4.setMaximum(1000.0)
        self.hsv_h_4.setObjectName("hsv_h_4")
        self.hsv_v_4 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.hsv_v_4.setGeometry(QtCore.QRect(160, 70, 62, 27))
        self.hsv_v_4.setMaximum(1000.0)
        self.hsv_v_4.setObjectName("hsv_v_4")
        self.hsv_s_4 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.hsv_s_4.setGeometry(QtCore.QRect(90, 70, 62, 27))
        self.hsv_s_4.setMaximum(1000.0)
        self.hsv_s_4.setObjectName("hsv_s_4")
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(240, 30, 67, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(240, 70, 67, 17))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1405, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.botao_pasta_imagens, QtCore.SIGNAL("clicked()"), MainWindow.selecionar_pasta)
        QtCore.QObject.connect(self.files_list, QtCore.SIGNAL("itemSelectionChanged()"), MainWindow.selecionar_imagem)
        QtCore.QObject.connect(self.recalcular, QtCore.SIGNAL("clicked()"), MainWindow.alterar_parametro)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.imagem_original.setText(QtGui.QApplication.translate("MainWindow", "Original", None, QtGui.QApplication.UnicodeUTF8))
        self.imagem_classificada.setText(QtGui.QApplication.translate("MainWindow", "Classificada", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Altura", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Imagens", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.botao_pasta_imagens.setText(QtGui.QApplication.translate("MainWindow", "Dir", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "HSV - Verde", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Upper", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Lower", None, QtGui.QApplication.UnicodeUTF8))
        self.recalcular.setText(QtGui.QApplication.translate("MainWindow", "Recalcular", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "HSV - Solo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Upper", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Lower", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

