# Questão 1. 

Abra o arquivo lena.bmp no editor hexadecimal em https://hexed.it/ e, analisando o formato do cabeçalho BMP apresentado na Seção 2, indique no relatório: qual é o valor dos campos offset e tamanho do arquivo? Quais são os valores dos componentes de cor R, G e B do primeiro pixel armazenado no arquivo

# R: 

- 36 (hexadecimal) ou 54 (decimal) bytes de offset
- C0036 (hexadecimal) ou 786.486 (decimal) bytes de tamanho de arquivo.
- B (39 hex), G (16 hex) e R (52 hex) | R (82 decimal), G (22 decimal) e B (57 decimal)

# Questão 2

Qual é o tamanho do cabeçalho do arquivo lena1.cuif para seu grupo

# R:
- 18 bytes

# Questão 4

Indique o PSNR comparando a imagem original mandril.bmp (original) com a imagem obtida a
partir do arquivo CUIF.1 (lena1.bmp). Explique porque do resultado do PSNR para o caso do CUIF.1.

# R: 
Não foram aplicadas nenhum tipo de compressão no arquivo CUIF.1. O que mudou foi apenas ordem em que os valores R, G e B foram armazenados. 

O formato CUIF armazena todos os valores de R, seguido de todos os valores de G e todos 
os valores de B, ou seja, RRR,GGG,BBB...

Já o formato BMP armazena os valores de rgb juntos em ordem inversa, ou seja, BGR, BGR, BGR

# Questão 5

Compacte as imagens lena.bmp e lena1.cuif com zip. Qual a taxa de compressão obtida para os dois arquivos? Qual arquivo compactou mais? Explique porque deste resultado, ou seja, indique a vantagem de organizar os pixels nesta sequência definida pelo CUIF.1 (primeiro os valores de R, depois de G e finalmente de B) para a compressão baseada em RLE ou DPCM? Dica: relembre os princípios da compressão RLE e DPCM e compare a parte de dados de imagem do arquivo lena.bmp e lena1.cuif no editor hexadecimal.

# R:

- lena.bmp: 715.608 bytes

- lena1.cuif: 607.692 bytes

- taxa de compressão: 607.692 / 715.608 = 0.85 (aproximadamente)

As imagens foram comprimidas usando .zip, nesta tática de compressão, quanto mais redundância de dados, melhor a compressão.

As imagens no formato bmp armazenam os valores dos pixels no formato BGR, BGR, BGR...
Tendo em vista que a simularidade entre os bytes B, G e R de um pixel é, em sua maioria, baixa, e eles estão armazenados em sequência, podemos concluir que o formato BMP tem menos bytes parecidos ou similares entre si perto um do outro. Desta forma, o formato de compressão .zip não é tão eficiênte para imagens BMP.

Já as imagens no formato cuif armazenam todos os valores R seguido de todos os valores G e todos os valores B (RRRGGGBBB). Valores do mesmo canal de pixels vizinhos tendem a ser mais parecidos, então armazenar os dados das cores separados por canais tende a aumentar a similaridades entre bytes perto um do outro, fazendo com que a compressão no formato .zip seja maior para imagens cuif.


# Questão 6

Agora altere o código em PraticaIII.py para que seja gerado o arquivo lena2.cuif, que utiliza a versão CUIF.2 (usar 2 em vez de 1 para indicação da versão) e lena2.bmp. Visualiza as imagens lena1.bmp e lena2.bmp para ver se existem diferenças visíveis. Analise o código que gera o arquivo CUIF.2 (em Cuif.py) e explique o princípio da compressão adotada no CUIF.2


A compressão adotada em CUIF.2 diminui o tamanho necessário para armazenar a cor de um pixel. Antes eram necessários 8 bits para cada canal (r, g e b) e agora são necessários apenas 8 bits para todos os 3 canais. A compressão pega apenas os 3 bits mais significativos do canal r, os 3 bits mais significativos do canal g e os 2 bits mais significativos do canal b, diminuindo o tamanho de um pixel de 24 bits para 8 bits.

# Questão 7

Indique as taxas de compressão obtidas pelos CUIF.1 e CUIF.2 para a imagem lena.bmp? Para este cálculo determine a razão entre um arquivo cuif e a imagem lena.bmp. Qual versão do CUIF compactou mais

# R:
- lena.bmp: 786.486 bytes
- lena1.cuif: 607.692 bytes | 0.85 de taxa de compressão
- lena2.cuif: 65.643 bytes | 0.083 de taxa de compressão (compactou mais)

# Questão 8

Indique o PSNR comparando a imagem original lena.bmp (original) com a imagem obtida a partir do arquivo CUIF.2 (lena2.bmp). Justifique a resposta do PSNR indicando a fonte do ruído

# R:

PSNR (lena.bmp -> lena2.cuif): 19.780741729886877

Foram descartados 5 bits do canal R, 5 bits do canal G e 6 bits do canal B de cada pixel da imagem lena.bmp. Estes bits descartados formaram um ruido que foi mensurado pelo calculo do PSNR.