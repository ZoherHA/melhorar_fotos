import cv2
from PIL import Image, ImageEnhance
import os

# Caminhos das pastas
entrada = "imagens"
saida = "resultados"

os.makedirs(saida, exist_ok=True)

def melhorar_foto(img_path, output_path):
    # Abrir imagem com OpenCV
    img = cv2.imread(img_path)

    # Correção de cor (BGR → RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Converter para PIL
    pil_img = Image.fromarray(img)

    # Melhorar brilho
    enhancer = ImageEnhance.Brightness(pil_img)
    pil_img = enhancer.enhance(1.2)

    # Melhorar contraste
    enhancer = ImageEnhance.Contrast(pil_img)
    pil_img = enhancer.enhance(1.3)

    # Melhorar nitidez
    enhancer = ImageEnhance.Sharpness(pil_img)
    pil_img = enhancer.enhance(1.4)

    # Salvar imagem processada
    pil_img.save(output_path)
    print(f"✅ Foto salva em: {output_path}")

# Processar todas as imagens da pasta
for arquivo in os.listdir(entrada):
    if arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(entrada, arquivo)
        output_path = os.path.join(saida, f"melhorada_{arquivo}")
        melhorar_foto(input_path, output_path)
