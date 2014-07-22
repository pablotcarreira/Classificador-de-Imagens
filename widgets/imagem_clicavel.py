# coding=utf-8
#
# Pablo T. Carreira



from PySide.QtCore import *
from PySide.QtGui import *
import numpy as np

class ImagemClicavel(QLabel):

    def mousePressEvent(self, event):
        # Retangulo.
        self.rubberBand = None
        self.origin = event.pos()
        if not self.rubberBand:
            self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.rubberBand.setGeometry(QRect(self.origin, QSize()))
        self.rubberBand.show()

        print "oi"
        self.start_coord = self._converte_coordenadas(event)

    def mouseMoveEvent(self, event):
        self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, mouse_event):
        self.rubberBand.hide()
        self.end_coord = self._converte_coordenadas(mouse_event)
        self.calcular_statisticas()

    def calcular_statisticas(self):
        #FIXME: Funciona apenas selecionando da esqueda para a direita e de cima para baixo.
        print self.start_coord
        print self.end_coord
        print self.cv_image.shape
        row_min = self.start_coord[1]
        row_max = self.end_coord[1]
        col_min = self.start_coord[0]
        col_max = self.end_coord[0]

        # Lembrando que array e "row major".
        slice = self.cv_image[row_min:row_max, col_min:col_max]
        print slice.shape
        bandas = dict(
            hue=slice[:,:,0],
            saturation=slice[:,:,1],
            value=slice[:,:,2], )

        # Gera as estatisticas:
        for chave, valores in bandas.iteritems():
            print ">>>" + chave
            print "Média: {}".format(valores.mean())
            print "Maximo: {}".format(valores.max())
            print "Minimo: {}".format(valores.min())
            print "Q1: {}".format(np.percentile(valores, 25))
            print "Q3: {}".format(np.percentile(valores, 75))



    def _converte_coordenadas(self, mouse_event):
        widget_size = self.size().toTuple()
        pixmap_size = self.pixmap().size().toTuple()
        widget_coord = mouse_event.pos().toTuple()
        x = widget_coord[0] * pixmap_size[0] / widget_size[0]
        y = widget_coord[1] * pixmap_size[1] / widget_size[1]
        return x, y





