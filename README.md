# Seminario TREE-MANADINE - Curso 2026/2027
Este repositorio contiene el material utilizado en el seminario impartido por Treelogic en el Máster Universitario en Análisis de Datos para la Inteligencia de Negocios de la Universidad de Oviedo durante el curso académico 2026/2027.

En este seminario construiremos un detector de **noticias falsas en español**. Primero entrenaremos un modelo clásico de NLP (TF-IDF + regresión logística) y después aplicaremos **transfer learning** con modelos preentrenados: extracción de *embeddings* con sentence-transformers y ajuste fino (*fine-tuning*) de BETO, un BERT entrenado en español. Por último, comprobaremos qué modelo generaliza mejor a noticias publicadas años después y sobre temas que nunca ha visto, como la COVID-19.

## Contenido

| Notebook | Contenido | Abrir |
|---|---|---|
| `01-introduccion_python.ipynb` | Variables, cadenas de texto, listas, diccionarios, funciones y primeros pasos con pandas | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Vins16/seminario-manadine-transfer-learning/blob/main/01-introduccion_python.ipynb) |
| `02-inspeccion_limpieza.ipynb` | Carga, inspección y limpieza del corpus; fuga de información y armonización de dos épocas distintas | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Vins16/seminario-manadine-transfer-learning/blob/main/02-inspeccion_limpieza.ipynb) |
| `03-visualizacion_baseline.ipynb` | Visualización, preprocesamiento, TF-IDF y modelo base; evaluación sobre noticias nuevas | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Vins16/seminario-manadine-transfer-learning/blob/main/03-visualizacion_baseline.ipynb) |
| `04-transfer_learning.ipynb` | *Embeddings* con sentence-transformers, *fine-tuning* de BETO y comparación de los tres modelos | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Vins16/seminario-manadine-transfer-learning/blob/main/04-transfer_learning.ipynb) |

Los notebooks contienen huecos marcados con `???` que se completan durante el seminario. La carpeta `soluciones` contiene los notebooks resueltos.

## Cómo ejecutarlo

**Google Colab (recomendado):** pulsa en cualquiera de los botones *Open in Colab*. La primera celda de cada notebook descarga el repositorio y las librerías necesarias. Para el notebook 4, activa la GPU en *Entorno de ejecución*, después *Cambiar tipo de entorno de ejecución* y elige *GPU T4*.

**En local:**

```bash
git clone https://github.com/Vins16/seminario-manadine-transfer-learning.git
cd seminario-manadine-transfer-learning
pip install -r requirements.txt
jupyter notebook
```

Sin GPU, el notebook 4 entrena BETO automáticamente con una muestra reducida para que no tarde demasiado.

## Estructura

- `01-introduccion_python.ipynb` a `04-transfer_learning.ipynb`: notebooks del seminario.
- `utils.py`: funciones de preprocesamiento reutilizadas en el notebook 4.
- `requirements.txt`: librerías necesarias.
- `data/raw/`: corpus original (`train.xlsx`, `development.xlsx` y `test.xlsx`).
- `data/*.csv`: conjuntos limpios generados por los notebooks 2 y 3.
- `models/`: modelos generados durante el seminario.
- `soluciones/`: notebooks resueltos.

## Datos

Se utiliza el **Spanish Fake News Corpus** ([jpposadas/FakeNewsCorpusSpanish](https://github.com/jpposadas/FakeNewsCorpusSpanish)), distribuido bajo licencia [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Las noticias de 2018 (`train.xlsx` y `development.xlsx`) se usan para entrenar y validar; las de 2020-2021 (`test.xlsx`) se reservan como "noticias nuevas".

- Posadas-Durán, J. P., Gómez-Adorno, H., Sidorov, G., & Escobar, J. J. M. (2019). Detection of fake news in a new corpus for the Spanish language. *Journal of Intelligent & Fuzzy Systems*, 36(5), 4869-4876.
- Gómez-Adorno, H., Posadas-Durán, J. P., Bel Enguix, G., & Porto Capetillo, C. (2021). Overview of FakeDeS at IberLEF 2021: Fake News Detection in Spanish Shared Task. *Procesamiento del Lenguaje Natural*, 67, 223-231.

## Modelos preentrenados

- [`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)
- [`dccuchile/bert-base-spanish-wwm-cased`](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) (BETO)
