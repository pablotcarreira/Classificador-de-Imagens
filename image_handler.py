# coding=utf-8
#
# Pablo T. Carreira - 2014
import cv2
import exifread
import numpy as np


class ImageHandler(object):
    def __init__(self, image_path):
        """Handles a single image providing methods for it's manipulation.

        :param image_path: Full path to the image file.
        """
        self.image_path = image_path
        self.exif = self.read_exif()
        self.cv_image = cv2.imread(image_path)
        self.color_format = 'BGR'

        # Parametros da camera, podem pertencer a classe camera ou a classe foto.
        self.camera_altura = 2000  # Milimetros
        self.camera_f = 7.6  # Distância focal.
        self.camera_dim_sensor = 35  # Tamanho do sensor (tamanho do filme).

    def _calcula_tamanho_uma_dimensao(self, dimensao_camera):
        """Calcula uma dimensão real representada pela foto, em mm.

        :param dimensao_camera:
        :return:
        """
        cos_alpha = (dimensao_camera / 2.0) / self.camera_f
        dimensao_imagem = self.camera_altura * cos_alpha * 2
        return dimensao_imagem

    def calcular_tamanho_pixel(self, image_shape, real_shape):
        """Calcula as dimensẽs no mundo real que são representadas por um pixel da imagem.

        :param image_shape: Image shape (cols, rows) in pixels.
        :param real_shape: Real world shape represented by the image (width, height) in mm.
        """
        x_size = real_shape[0] / image_shape[0]
        y_size = real_shape[1] / image_shape[1]
        return x_size, y_size

    def read_exif(self):
        """Read exif data from image.

        :return dict: Dictionary of exif tags/values.
        """
        with open(self.image_path, 'rb') as arquivo:
            tags = exifread.process_file(arquivo)
        # for k, v in tags.iteritems():
        #     print k, v
        return tags


    def classificar_imagem(self, cor=None):
        """Separa os pixels que estão próximos a esta determinada cor. Retorna uma matriz bool
          com True para as posições atendidas e False para as que estão fora do intervalo.

          Utiliza o thresholdind para realizar esta função:
          http://docs.opencv.org/trunk/doc/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding
          http://docs.opencv.org/trunk/modules/imgproc/doc/miscellaneous_transformations.html#adaptivethreshold

          Ou simplesmente verifica valores de verde acima de um determinado nível.

        :param cor:
        """
        # resultado = cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst])

        # Ou
        # Usar o HSV pois permite definir intervalos.
        hsv_image = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2HSV)

        lower_green = np.array([30,30,40])
        upper_green = np.array([150,200,120])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv_image, lower_green, upper_green)
        mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
        return mask_color

