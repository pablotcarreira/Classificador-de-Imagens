#!/usr/bin/python
# coding=utf-8
#
# Pablo T. Carreira
import os
import sys
from PySide.QtGui import *
from PySide.QtCore import QSettings
from image_handler import ImageHandler
from interface import Ui_MainWindow


# Start Qt Application.
app = QApplication(sys.argv)


class ControlMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = QSettings('Classificador', 'Independente')
        self._prepare_settings()
        self._abrir_pasta(self.settings.value('pasta_imagens'))

    def _prepare_settings(self):
        # Verifica se tem o dir de imagens
        if not self.settings.contains('pasta_imagens'):
            self.settings.setValue('pasta_imagens', '.')

    def show_image(self, cv_image, destination='imagem_original'):
        """Show image on the interface.

        :param np.ndarray cv_image: OpenCV image (numpy array).
        :param destination: Name of QLabel to display the image.
        """
        # Muda a ordem das cores
        # cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

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
        self._abrir_pasta(pasta)

    def selecionar_imagem(self):
        item = self.ui.files_list.currentItem()
        arquivo_imagem = os.path.join(self.pasta, item.text())
        image_handler = ImageHandler(arquivo_imagem)
        image_handler.read_exif()
        self.show_image(image_handler.cv_image)
        self.show_image(image_handler.classificar_imagem(), destination='imagem_classificada')

if __name__ == "__main__":
    # QT stuff
    my_window = ControlMainWindow()
    my_window.show()


    sys.exit(app.exec_())