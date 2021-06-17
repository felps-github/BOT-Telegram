from PIL import Image
import pytesseract

def mostraTexto():
    try:
        print("\n---- Este é um programa para ler uma imagem ----")
        url_img = input("Digite o nome da imagem (com a extensão): ")
        type_img = input("(T) - Caracteres do tipo texto\n(N) - Caracteres do tipo número\nResposta: ").upper()
        
        if type_img == 'T':
            print(pytesseract.image_to_string(Image.open(url_img)))
        elif type_img == 'N':
            print(pytesseract.image_to_string(Image.open(url_img), config='--psm 6'))
        else:
            print("Erro, encerrando o programa...")

    except Exception as error:
        print(error)

mostraTexto()
