#
#
#
# Vitor Fernando da Silva - Grupo Z

from pathlib import Path
from urllib.request import urlopen
from PIL import Image

RES = Path("./res")


def criarImagemRGB():
    img = Image.new( "RGB", (512,256))
    raster = img.load()
        
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            raster[i,j] = (220,219,97,255)
            
    # obtendo o pixel 0,0
    (r, g, b) = img.getpixel((0, 0))
    print("Pixel (0,0) com getpixel:", r, g, b)
    
    # outra forma
    print("Pixel (0,0): com raster", raster[0, 0])
    
    return img

def criarImagemCinza():
    img = Image.new( "L", (256,256))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            raster[i,j] = i
    y = img.getpixel((5, 5))
    print(y)
    return img

def criarImagemBinaria():
    # checkerboard pattern.
    img = Image.new("1", (500,500))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if ((int(i/50)+int(j/50)) % 2 == 0):
                raster[i,j] = 0
            else:
                raster[i,j] = 1
    y = img.getpixel((0, 0))
    print(y)
    return img


def resize(image: Image.Image, new_width: int, new_height: int):
    new_image: Image.Image = Image.new("RGB", (new_width, new_height))
    src = image.load()
    dest = new_image.load()

    x_ratio = image.width / new_width
    y_ratio = image.height / new_height

    for i in range(new_width):
        for j in range(new_height):
            x = int(i * x_ratio)
            y = int(j * y_ratio)
            dest[i, j] = src[x, y]

    return new_image


def convert_to_gray(image: Image.Image):
    width, height = image.size
    gray: Image.Image = Image.new("L", (width, height))
    src = image.load()
    dest = gray.load()
    for x in range(width):
        for y in range(height):
            r, g, b = src[x, y]
            dest[x, y] = int(0.299 * r + 0.587 * g + 0.114 * b)
    return gray


def convert_to_binary(image: Image.Image):
    img_gray: Image.Image = convert_to_gray(image)
    width, height = img_gray.size
    new_image = Image.new('1', (width, height))
    gray = img_gray.load()
    binary = new_image.load()
    for i in range(width):
        for j in range(height):
            binary[i, j] = 1 if gray[i, j] > 127 else 0
    return new_image


def reduce_to_3_bits(image: Image.Image):
    width, height = image.size
    new_image = Image.new('RGB', (width, height))
    src = image.load()
    dest = new_image.load()
    for x in range(width):
        for y in range(height):
            r, g, b = src[x, y]
            nr = r & 0xE0
            ng = g & 0xE0
            nb = b & 0xE0
            dest[x, y] = (nr, ng, nb)
    return new_image


def split_channels(image: Image.Image):
    width, height = image.size

    src = image.load()
    
    dest_r = Image.new('RGB', (width, height))
    dest_g = Image.new('RGB', (width, height))
    dest_b = Image.new('RGB', (width, height))
    r_raster = dest_r.load()
    g_raster = dest_g.load()
    b_raster = dest_b.load()

    for x in range(width):
        for y in range(height):
            r, g, b = src[x, y]
            r_raster[x, y] = (r, 0, 0)
            g_raster[x, y] = (0, g, 0)
            b_raster[x, y] = (0, 0, b)

    return dest_r, dest_g, dest_b

def main() -> None:
    RES.mkdir(exist_ok=True)
    url = 'https://www.inf.ufsc.br/~roberto.willrich/INE5431/RGB.png'
    img: Image.Image = Image.open(urlopen(url)).convert('RGB')
    print('Imagem carregada: {} x {}'.format(img.width, img.height))
    img.save(RES / "0_default.png")

    # criarImagemRGB().show()
    # criarImagemCinza().show()
    # criarImagemBinaria().show()

    # 1
    output = resize(img, img.width // 2, img.height // 2)
    output.save(RES / '1_resize.png')

    # 2
    output = convert_to_gray(img)
    output.save(RES / '2_gray.png')

    # 3
    output = convert_to_binary(img)
    output.save(RES / '3_binary.png')

    # 4
    output = reduce_to_3_bits(img)
    output.save(RES / '4_3bits.png')

    # 5
    r_img, g_img, b_img = split_channels(img)
    r_img.save(RES / '5_1_r.png')
    g_img.save(RES / '5_2_g.png')
    b_img.save(RES / '5_3_b.png')

    print(f"Imagens geradas na pasta: {RES.absolute()}")
    for i, file in enumerate(RES.iterdir()):
        print(f"[{i}] -> {file.absolute()}")

    r = input("Show images [y/N]: ").strip().lower()
    if r == 'y':
        for file in RES.iterdir():
            Image.open(file).show()


if __name__ == '__main__':
    main()