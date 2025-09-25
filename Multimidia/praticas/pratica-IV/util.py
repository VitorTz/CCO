from PIL import Image
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
