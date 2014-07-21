# coding=utf-8
#
# Pablo T. Carreira



from PySide.QtCore import *
from PySide.QtGui import *

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
        self._bbox()

    def _bbox(self):
        print self.start_coord
        print self.end_coord
        # imagem = self.pixmap().toImage().constBits()

    def _converte_coordenadas(self, mouse_event):
        widget_size = self.size().toTuple()
        pixmap_size = self.pixmap().size().toTuple()
        widget_coord = mouse_event.pos().toTuple()
        x = widget_coord[0] * pixmap_size[0] / widget_size[0]
        y = widget_coord[1] * pixmap_size[1] / widget_size[1]
        return x, y





