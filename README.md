# Trabalho Mineração de Séries Temporais

## Classificação de séries temporais univariadas a partir de formas manuscritas

### Dado o contorno de uma forma desenhada a mão (foto), será convertido o contorno em uma série temporal univariada (distância de cada ponto do contorno ao centroide da forma, percorrida ao longo do perímetro) e classificar a forma (>=3 classes) a partir dessa série.

### **OBS:** Estrutura de pastas (necessário criá-las dessa forma):
```
.
├─ data/
      train/
        circulo/   img1.jpg  img2.jpg  ...
        quadrado/  img1.jpg  ...
        triangulo/ img1.jpg  ...
        estrela/   img1.jpg  ...
├─ test/
        circulo/   ...
        quadrado/  ...
        triangulo/ ...
        estrela/   ...
```

### Cada imagem deve conter uma forma desenhada com traço sólido e escuro sobre um fundo claro/uniforme (ex: caneta preta em folha branca), fotografada de cima, evitando sombras fortes sobre o traço.


## Dependências
 - opencv-python-headless, numpy, scipy, scikit-learn, matplotlib


## Uso de IA

Conforme a **Resolução CONSUN PUCPR 274/2024**: quando ferramentas de IA forem usadas no preparo da entrega, o uso é **declarado** no relatório final (modelo institucional). A IA **não** é listada como autora. A responsabilidade pelo conteúdo é dos integrantes do grupo.
