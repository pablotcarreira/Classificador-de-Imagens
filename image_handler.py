# coding=utf-8
#
# Pablo T. Carreira - 2014
import cv2
import exifread
import numpy as np
import math

DEFAULT_PARAMS = dict(
    palha_upper=[150, 200, 120],
    palha_lower=[30, 30, 40],
    verde_upper=[150, 200, 120],
    verde_lower=[30, 30, 40],
)


class ImageHandler(object):
    def __init__(self, image_path, imagem_settings):
        """Handles a single image providing methods for it's manipulation.

        :param image_path: Full path to the image file.
        """
        if not imagem_settings.param:
            imagem_settings.param = DEFAULT_PARAMS
            imagem_settings.salvar()

        self.imagem_settings = imagem_settings



        self.image_path = image_path
        self.exif = self.read_exif()
        self.cv_image = cv2.imread(image_path)
        self.color_format = 'BGR'

        # Parametros da camera, podem pertencer a classe camera ou a classe foto.
        self.camera_altura = 3000  # Milimetros
        self.camera_f = 18  # Distância focal.
        self.camera_dim_sensor = 35  # Tamanho do sensor (tamanho do filme).
        self.camera_angulo = 80

    def _calcula_tamanho_uma_dimensao(self, dimensao_camera=None, angulo=None):
        """Calcula uma dimensão real representada pela foto, em mm.

        :param dimensao_camera:
        :return:
        """
        if dimensao_camera:
            cos_alpha = (dimensao_camera / 2.0) / self.camera_f
        if angulo:
            cos_alpha = math.cos(angulo / 2)
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
        param = self.imagem_settings.param

        lower = np.array(param['verde_lower'])
        upper = np.array(param['verde_upper'])
        mask1 = cv2.inRange(hsv_image, lower, upper)

        # lower = np.array(param['palha_lower'])
        # upper = np.array(param['palha_upper'])
        #DEV
        lower = np.array([20, 30, 80])
        upper = np.array([35, 40, 90])


        mask2 = cv2.inRange(hsv_image, lower, upper)

        #muda a cor (BGR):
        # preto, verde, marrom, ciano
        cores = [(0, 0, 0), (34, 255, 0), (27, 119, 247), (244, 247, 27)]
        cores = np.array(cores)

        indice_verde = np.where(mask1==255, 1, 0)
        indice_palha = np.where(mask2==255, 2, 0)
        indice_sobreposicao = np.where((mask1==255)*(mask2==255), 3, 0)

        indice_composto = np.where(indice_sobreposicao==0, indice_verde, indice_sobreposicao)
        indice_composto = np.where(indice_composto==0, indice_palha, indice_composto)
        indices = indice_composto

        indices = indices.reshape((indices.shape[0], indices.shape[1], 1))
        saida = np.asarray(np.choose(indices, cores), dtype=np.uint8)
        return saida

