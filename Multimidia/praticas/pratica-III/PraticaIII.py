from PIL import Image
from Cuif import Cuif
import math


def MSE(ori: Image.Image, dec: Image.Image) -> float:
    n = ori.width * ori.height * 3
    count = 0
    
    for i in range(ori.width):
        for j in range(ori.height):
            ori_r, ori_g, ori_b = ori.getpixel((i, j))
            dec_r, dec_g, dec_b = dec.getpixel((i, j))            
            count += (ori_r - dec_r) ** 2
            count += (ori_g - dec_g) ** 2
            count += (ori_b - dec_b) ** 2
            
    return count / n


def PSNR(original: Image.Image, decodificada: Image.Image, b: int) -> float | str:
    try:
        mse = MSE(original, decodificada)
        if mse == 0:
            return "Infinity"
            
        max_pixel_value = (2 ** b) - 1
        psnr = 10 * math.log10((max_pixel_value ** 2) / mse)
        return psnr
    except ValueError as e:
        return str(e)


if __name__ == "__main__":
    filepath = 'lena.bmp'
    img = Image.open(filepath)
    matriculas = [20201566]
    
    # instancia objeto Cuif, convertendo imagem em CUIF.1
    cuif = Cuif(img, 2, matriculas)
    
    # imprime cabeçalho Cuif
    cuif.printHeader()
    
    #gera o arquivo Cuif.1
    cuif.save('lena2.cuif')
    
    #Abre um arquivo Cuif e gera o objeto Cuif
    cuif1 = Cuif.openCUIF('lena2.cuif')
    
    # Converte arquivo Cuif em BMP e mostra
    cuif1.saveBMP("lena2.bmp")
    cuif1.show()
    img1 = Image.open("lena2.bmp")

    # Cálculo do PSNR
    psnr = PSNR(img, img1, 8)
    print(f'Cálculo do PSNR: {psnr}')

  

