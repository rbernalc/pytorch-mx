# 🔬 Laboratorio: Clasificación de Imágenes con MNIST

## 📋 Descripción

Este laboratorio te guía en la construcción de un clasificador de dígitos escritos a mano usando el famoso dataset MNIST y una red neuronal convolucional (CNN) en PyTorch.

**Nivel**: 🟢 Básico

## 🎯 Objetivos

- Cargar y explorar el dataset MNIST
- Implementar una CNN desde cero en PyTorch
- Entrenar el modelo con técnicas de optimización
- Evaluar el rendimiento del modelo
- Visualizar predicciones y errores
- Guardar y cargar modelos entrenados

## 🔧 Requisitos

### Software
- Python 3.8+
- PyTorch 2.0+
- torchvision
- matplotlib
- numpy
- tqdm

### Hardware
- CPU: Suficiente para este proyecto (entrenamiento ~5-10 min)
- GPU (opcional): Acelera el entrenamiento (~1-2 min)

### Conocimientos Previos
- Conceptos básicos de PyTorch
- Redes neuronales básicas
- Python y programación orientada a objetos

## 📊 Dataset

**MNIST** (Modified National Institute of Standards and Technology)
- 60,000 imágenes de entrenamiento
- 10,000 imágenes de prueba
- Imágenes en escala de grises 28x28 píxeles
- 10 clases (dígitos 0-9)

El dataset se descargará automáticamente la primera vez que ejecutes el código.

## 📁 Estructura del Proyecto

```
clasificacion-imagenes-mnist/
├── README.md                    # Este archivo
├── requirements.txt             # Dependencias específicas
├── notebooks/
│   ├── 01-exploracion.ipynb    # Exploración del dataset
│   ├── 02-modelo.ipynb         # Construcción y entrenamiento
│   └── 03-evaluacion.ipynb     # Evaluación y visualización
├── src/
│   ├── model.py                # Definición del modelo CNN
│   ├── train.py                # Script de entrenamiento
│   ├── evaluate.py             # Script de evaluación
│   └── utils.py                # Funciones auxiliares
├── configs/
│   └── config.yaml             # Configuración de hiperparámetros
└── data/                       # Dataset (se descarga automáticamente)
```

## 🚀 Guía de Uso

### 1. Instalación

```bash
cd laboratorios/clasificacion-imagenes-mnist
pip install -r requirements.txt
```

### 2. Exploración (Notebook 1)

Abre y ejecuta `notebooks/01-exploracion.ipynb`:
- Visualiza imágenes del dataset
- Analiza la distribución de clases
- Comprende el formato de los datos

### 3. Entrenamiento (Notebook 2)

Abre y ejecuta `notebooks/02-modelo.ipynb`:
- Define la arquitectura CNN
- Configura el optimizador y función de pérdida
- Entrena el modelo
- Visualiza el progreso del entrenamiento

O usa el script de línea de comandos:
```bash
python src/train.py --epochs 10 --batch-size 64 --lr 0.001
```

### 4. Evaluación (Notebook 3)

Abre y ejecuta `notebooks/03-evaluacion.ipynb`:
- Evalúa el modelo en el conjunto de prueba
- Genera matriz de confusión
- Analiza errores comunes
- Visualiza predicciones

O usa el script:
```bash
python src/evaluate.py --model-path checkpoints/best_model.pth
```

## 🏗️ Arquitectura del Modelo

Red Neuronal Convolucional (CNN) básica:

```
Input (1x28x28)
    ↓
Conv2d (32 filtros, kernel 3x3)
    ↓
ReLU
    ↓
MaxPool2d (2x2)
    ↓
Conv2d (64 filtros, kernel 3x3)
    ↓
ReLU
    ↓
MaxPool2d (2x2)
    ↓
Flatten
    ↓
Linear (128 unidades)
    ↓
ReLU
    ↓
Dropout (0.5)
    ↓
Linear (10 unidades - salida)
```

## 📈 Resultados Esperados

Con la configuración por defecto, deberías obtener:
- **Accuracy en entrenamiento**: ~99%
- **Accuracy en prueba**: ~98-99%
- **Tiempo de entrenamiento**: 5-10 minutos (CPU), 1-2 minutos (GPU)

## 🔬 Experimentos Sugeridos

1. **Arquitectura**:
   - Agrega más capas convolucionales
   - Prueba diferentes tamaños de kernel
   - Experimenta con diferentes activaciones

2. **Hiperparámetros**:
   - Cambia el learning rate
   - Ajusta el batch size
   - Prueba diferentes optimizadores (SGD, RMSprop)

3. **Regularización**:
   - Ajusta el dropout
   - Implementa L2 regularization
   - Prueba data augmentation

4. **Técnicas Avanzadas**:
   - Implementa learning rate scheduling
   - Usa batch normalization
   - Prueba early stopping

## 📊 Visualizaciones

El laboratorio incluye:
- Curvas de entrenamiento (loss y accuracy)
- Matriz de confusión
- Ejemplos de predicciones correctas e incorrectas
- Visualización de filtros convolucionales

## 💾 Modelos Guardados

Los modelos entrenados se guardan en `checkpoints/`:
- `best_model.pth`: Mejor modelo según validación
- `last_model.pth`: Último checkpoint
- `model_epoch_X.pth`: Checkpoints por época

## 🐛 Troubleshooting

**Problema**: Out of memory
- **Solución**: Reduce el batch size

**Problema**: Entrenamiento muy lento
- **Solución**: Verifica que estés usando GPU si está disponible

**Problema**: Overfitting
- **Solución**: Aumenta dropout o reduce la complejidad del modelo

## 📚 Referencias

- [PyTorch MNIST Tutorial](https://pytorch.org/tutorials/beginner/basics/intro.html)
- [LeCun et al. - MNIST Database](http://yann.lecun.com/exdb/mnist/)
- [CS231n - Convolutional Networks](http://cs231n.github.io/convolutional-networks/)

## 🎓 Siguientes Pasos

Después de completar este laboratorio:
1. Intenta con datasets más complejos (CIFAR-10, Fashion-MNIST)
2. Implementa transfer learning con modelos pre-entrenados
3. Despliega tu modelo como una API REST

## 🤝 Contribuir

¿Mejoras o extensiones? ¡Pull requests bienvenidos!

---

**¡Feliz experimentación!** 🚀
