#!/usr/bin/python
# coding=utf-8
#
# Pablo T. Carreira
import json
import cv2
import os
import sys
from PySide.QtGui import *
from PySide.QtCore import QSettings
from image_handler import ImageHandler
from interface import Ui_MainWindow


# Start Qt Application.
app = QApplication(sys.argv)


class ImagemSettings(object):
    def __init__(self, arquivo_imagem, pasta_settings):
        """Classe que representa os parametros de configuração de uma imagem.
        """
        self.pasta_settings = pasta_settings
        self.arquivo_imagem_settings = os.path.join(pasta_settings, arquivo_imagem + '_settings')
        try:
            self.param = self.ler()
        except IOError:
            self.param = None

    def salvar(self):
        """Salva as configurações de classificação da imagem.
        Cria a pasta image_settings dentro da pasta onde estão as imagens.
        """
        try:
            os.makedirs(self.pasta_settings)
        except OSError:
            pass
        with open(self.arquivo_imagem_settings, 'w') as arquivo_settings:
            json.dump(self.param, arquivo_settings)

    def ler(self):
        """Lê as configurações."""
        with open(self.arquivo_imagem_settings, 'r') as arquivo_settings:
            imagem_settings = json.load(arquivo_settings)
        return imagem_settings


class ControlMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QSettings('Classificador', 'Independente')
        self._prepare_settings()
        self._abrir_pasta(self.settings.value('pasta_imagens'))
        # Caminho da pasta com as configurações de parâmetro.
        self.pasta_settings = os.path.join(self.settings.value('pasta_imagens'), 'images_settings')

    def _prepare_settings(self):
        # Verifica se tem o dir de imagens
        if not self.settings.contains('pasta_imagens'):
            self.settings.setValue('pasta_imagens', '.')

    def _inicio_selecao(self):
        print ("oi")


    def show_image(self, cv_image, destination='imagem_original'):
        """Show image on the interface.

        :param np.ndarray cv_image: OpenCV image (numpy array).
        :param destination: Name of QLabel to display the image.
        """
        # Muda a ordem das cores
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

        # Alpha ou não.
        alpha = False
        formato = QImage.Format_ARGB32 if alpha else QImage.Format_RGB888

        # Caso  para mostrar a cv_image lida do disco, strides é necessaorio ou fica distorcida.
        # Strides é mais ou menos os espaços na memória entres as bandas.
        qimage = QImage(cv_image, cv_image.shape[1], cv_image.shape[0], cv_image.strides[0], formato)
        qpixmap = QPixmap.fromImage(qimage)
        imagem_widget = self.ui.centralwidget.findChild(QLabel, destination)
        imagem_widget.setPixmap(qpixmap)

    def _abrir_pasta(self, pasta):
        self.ui.caminho_pasta_imagens.setText(pasta)
        self.pasta = pasta
        #Lista os arquivos jpg.
        arquivos = os.listdir(pasta)
        arquivos_imagens = []
        for arquivo in arquivos:
            print os.path.splitext(arquivo)[1]
            if os.path.splitext(arquivo)[1] in ('.jpg', '.JPG', '.png', '.PNG'):
                arquivos_imagens.append(arquivo)
        self.ui.files_list.clear()
        self.ui.files_list.insertItems(0, arquivos_imagens)

    def selecionar_pasta(self):
        pasta = QFileDialog.getExistingDirectory(self, caption="Selecione uma pasta.")
        self.settings.setValue('pasta_imagens', pasta)
        # Caminho da pasta com as configurações de parâmetro.
        self.pasta_settings = os.path.join(self.settings.value('pasta_imagens'), 'images_settings')
        self._abrir_pasta(pasta)

    def selecionar_imagem(self):
        item = self.ui.files_list.currentItem()
        arquivo_imagem = os.path.join(self.pasta, item.text())
        imagem_settings = ImagemSettings(item.text(), self.pasta_settings)

        self.image_handler = ImageHandler(arquivo_imagem, imagem_settings)

        # Disponibiliza a imagem HSV no widget
        self.ui.imagem_original.cv_image = self.image_handler.hsv_image
        self.alterar_interface()


        self.show_image(self.image_handler.cv_image)
        self.show_image(self.image_handler.classificar_imagem(), destination='imagem_classificada')

    def alterar_interface(self):
        parametro = 'verde_upper'
        self.ui.hsv_h.setValue(self.image_handler.imagem_settings.param[parametro][0])
        self.ui.hsv_s.setValue(self.image_handler.imagem_settings.param[parametro][1])
        self.ui.hsv_v.setValue(self.image_handler.imagem_settings.param[parametro][2])
        parametro = 'verde_lower'
        self.ui.hsv_h_2.setValue(self.image_handler.imagem_settings.param[parametro][0])
        self.ui.hsv_s_2.setValue(self.image_handler.imagem_settings.param[parametro][1])
        self.ui.hsv_v_2.setValue(self.image_handler.imagem_settings.param[parametro][2])
        parametro = 'palha_upper'
        self.ui.hsv_h_3.setValue(self.image_handler.imagem_settings.param[parametro][0])
        self.ui.hsv_s_3.setValue(self.image_handler.imagem_settings.param[parametro][1])
        self.ui.hsv_v_3.setValue(self.image_handler.imagem_settings.param[parametro][2])
        parametro = 'palha_lower'
        self.ui.hsv_h_4.setValue(self.image_handler.imagem_settings.param[parametro][0])
        self.ui.hsv_s_4.setValue(self.image_handler.imagem_settings.param[parametro][1])
        self.ui.hsv_v_4.setValue(self.image_handler.imagem_settings.param[parametro][2])

    def alterar_parametro(self):
        # Pega os parametros.
        # Verde.
        parametro = 'verde_upper'
        h, s, v = self.ui.hsv_h.value(), self.ui.hsv_s.value(), self.ui.hsv_v.value()
        self.image_handler.imagem_settings.param[parametro] = [h, s, v]
        parametro = 'verde_lower'
        h, s, v = self.ui.hsv_h_2.value(), self.ui.hsv_s_2.value(), self.ui.hsv_v_2.value()
        self.image_handler.imagem_settings.param[parametro] = [h, s, v]
        self.image_handler.imagem_settings.salvar()

        # Palha.
        parametro = 'palha_upper'
        h, s, v = self.ui.hsv_h_3.value(), self.ui.hsv_s_3.value(), self.ui.hsv_v_3.value()
        self.image_handler.imagem_settings.param[parametro] = [h, s, v]
        parametro = 'palha_lower'
        h, s, v = self.ui.hsv_h_4.value(), self.ui.hsv_s_4.value(), self.ui.hsv_v_4.value()
        self.image_handler.imagem_settings.param[parametro] = [h, s, v]

        #Salva.
        self.image_handler.imagem_settings.salvar()

        #Recalcula.
        self.show_image(self.image_handler.classificar_imagem(), destination='imagem_classificada')





if __name__ == "__main__":
    # QT stuff
    my_window = ControlMainWindow()
    my_window.show()


    sys.exit(app.exec_())