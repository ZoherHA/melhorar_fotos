import cv2
import numpy as np
from PIL import Image, ImageEnhance
import os
import sys

def melhorar_foto_familia(caminho_imagem, salvar_como, intensidade="medio"):
    ajustes = {
        "leve":  {"cor": 1.05, "contraste": 1.05, "brilho": 1.02, "nitidez": 1.05},
        "medio": {"cor": 1.15, "contraste": 1.1,  "brilho": 1.05, "nitidez": 1.1},
        "forte": {"cor": 1.25, "contraste": 1.2,  "brilho": 1.1,  "nitidez": 1.2},
    }

    if intensidade not in ajustes:
        raise ValueError("Escolha a intensidade entre: leve, medio ou forte")

    config = ajustes[intensidade]

    img = cv2.imread(caminho_imagem)
    if img is None:
        print(f"⚠️ Não consegui abrir {caminho_imagem}")
        return

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)

    # Melhorias fotográficas
    pil_img = ImageEnhance.Color(pil_img).enhance(config["cor"])
    pil_img = ImageEnhance.Contrast(pil_img).enhance(config["contraste"])
    pil_img = ImageEnhance.Brightness(pil_img).enhance(config["brilho"])
    pil_img = ImageEnhance.Sharpness(pil_img).enhance(config["nitidez"])

    # Converter de volta para OpenCV
    img_final = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    cv2.imwrite(salvar_como, img_final)
    print(f"✅ {salvar_como} salvo com sucesso ({intensidade})")


def processar_pasta(pasta_entrada="fotos", pasta_saida="fotos_melhoradas", intensidade="medio"):
    os.makedirs(pasta_saida, exist_ok=True)
    extensoes = [".jpg", ".jpeg", ".png"]

    for arquivo in os.listdir(pasta_entrada):
        if any(arquivo.lower().endswith(ext) for ext in extensoes):
            entrada = os.path.join(pasta_entrada, arquivo)
            saida = os.path.join(pasta_saida, arquivo)
            melhorar_foto_familia(entrada, saida, intensidade)

    print(f"\n🎉 Todas as fotos foram processadas e salvas em '{pasta_saida}'")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        intensidade = sys.argv[1].lower()
    else:
        intensidade = "medio"  # padrão

    processar_pasta("fotos", "fotos_melhoradas", intensidade)
