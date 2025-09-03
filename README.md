📸 Melhorar Fotos
<p align="center"> <img src="https://img.shields.io/badge/python-3.11-blue?logo=python" alt="Python"> <img src="https://img.shields.io/badge/OpenCV-Enabled-green?logo=opencv" alt="OpenCV"> <img src="https://img.shields.io/badge/Pillow-Enhanced-orange?logo=pillow" alt="Pillow"> </p> <p align="center"> ✨ Projeto em Python para <b>melhorar automaticamente fotos</b> de família, comida e retratos. Ajustes de cor, brilho, contraste e nitidez com processamento em lote. </p>

# Melhorar Fotos de Família 📸

Este projeto aplica **ajustes fotográficos automáticos** em fotos de família, deixando-as mais vivas e profissionais, usando **Python**, **OpenCV** e **Pillow**.  
O objetivo é deixar as imagens mais vivas e naturais, com ajustes de cor, brilho, contraste e nitidez.


---

## 🚀 Funcionalidades
- Ajuste de brilho, contraste e nitidez
- Correção de cores
- Três níveis de intensidade: leve, médio, forte
- Processamento em lote (todas as fotos da pasta `fotos/`)
- Salva os resultados em `fotos_melhoradas/`

---

## 🛠️ Requisitos

- [Python 3.11+](https://www.python.org/downloads/release/python-3110/)  
- [Git](https://git-scm.com/downloads)  
- [VS Code](https://code.visualstudio.com/)  

---

## 📂 Estrutura do projeto
melhorar-fotos
│── fotos/                # Copie todas as fotos originais neste local
│── fotos_melhoradas/     # será criada automaticamente
│── melhorar_fotos.py     # o script Python
│── README.md             # explicação do projeto
│── requirements.txt      # dependências
│── .gitignore


---

## ⚙️ Instalação e uso

### 1. Clonar o repositório

git clone https://github.com/fjavier777/melhorar-fotos.git

cd melhorar-fotos

## Como usar
1. Crie a pasta `fotos` e adicione suas imagens (`.jpg`, `.jpeg`, `.png`).

2. No terminal, rode um dos comandos:

python melhorar_foto.py leve
python melhorar_foto.py medio
python melhorar_foto.py forte

As fotos melhoradas serão salvas na pasta fotos_melhoradas.

Requisitos
pip install -r requirements.txt

Tecnologias

Python

OpenCV

Pillow


📌 Notas

As pastas imagens/ e resultados/ estão no .gitignore para não sobrecarregar o repositório.

Ajustes de intensidade (mais ou menos brilho/contraste) podem ser configurados no código (main.py).

👨‍💻 Autor

Projeto desenvolvido por Fernando Javier Aracena Bello
