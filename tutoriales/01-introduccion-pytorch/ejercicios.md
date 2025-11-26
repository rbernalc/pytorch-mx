# Ejercicios - Introducción a PyTorch

## 🎯 Objetivo

Estos ejercicios te ayudarán a practicar y reforzar los conceptos aprendidos sobre tensores en PyTorch.

---

## Ejercicio 1: Creación de Tensores (Básico)

Crea los siguientes tensores:

a) Un tensor 1D con los números del 0 al 9
b) Un tensor 2D de forma (3, 4) lleno de ceros
c) Un tensor 2D de forma (2, 3) lleno de unos
d) Un tensor aleatorio de forma (4, 4) con valores entre 0 y 1
e) Un tensor identidad de tamaño 5x5

**Pista**: Usa `torch.arange()`, `torch.zeros()`, `torch.ones()`, `torch.rand()`, `torch.eye()`

---

## Ejercicio 2: Operaciones Básicas (Básico)

Dado dos tensores:
```python
a = torch.tensor([1, 2, 3, 4, 5])
b = torch.tensor([2, 3, 4, 5, 6])
```

Calcula:
- a + b
- a * b
- a / b
- a ** 2 (a al cuadrado)
- La suma de todos los elementos de a

---

## Ejercicio 3: Indexing y Slicing (Intermedio)

Dado el tensor:
```python
x = torch.arange(24).reshape(4, 6)
```

Obtén:
a) La primera fila
b) La última columna
c) El elemento en la posición [2, 3]
d) Las dos primeras filas y las tres primeras columnas
e) Todos los elementos pares (usando indexing avanzado)

---

## Ejercicio 4: Reshape y View (Intermedio)

a) Crea un tensor de forma (2, 3, 4) con números del 0 al 23

b) Cambia su forma a (4, 6) usando `.reshape()`

c) Cambia su forma a (8, 3) usando `.view()`

d) Aplana el tensor a una dimensión usando `.flatten()`

---

## Ejercicio 5: Broadcasting (Avanzado)

a) Crea un tensor `a` de forma (3, 1) con valores [1, 2, 3]

b) Crea un tensor `b` de forma (1, 4) con valores [10, 20, 30, 40]

c) Suma `a + b` y explica la forma del resultado

d) Multiplica `a * b` y explica qué sucede

---

## Ejercicio 6: GPU (Si está disponible)

a) Verifica si tienes GPU disponible

b) Si está disponible, crea un tensor en GPU

c) Crea otro tensor en CPU y súmalos (¿qué necesitas hacer?)

d) Mide el tiempo de una operación en CPU vs GPU con tensores grandes

---

## Ejercicio 7: Proyecto Mini (Avanzado)

Implementa una función que:

1. Tome una imagen RGB como tensor de forma (3, H, W)
2. Convierta la imagen a escala de grises usando la fórmula:
   ```
   gray = 0.299 * R + 0.587 * G + 0.114 * B
   ```
3. Normalice los valores al rango [0, 1]
4. Retorne el tensor de escala de grises

Prueba tu función con un tensor aleatorio de forma (3, 224, 224).

---

## 🎓 Desafío Extra

Investiga e implementa:

1. **Gradient Computation**: Crea un tensor con `requires_grad=True` y calcula gradientes
2. **Concatenación**: Une múltiples tensores usando `torch.cat()` y `torch.stack()`
3. **Operaciones Estadísticas**: Calcula media, mediana, desviación estándar de un tensor

---

## 📝 Notas

- Intenta resolver los ejercicios sin mirar las soluciones primero
- Experimenta con diferentes valores y formas
- Usa `print()` para visualizar los resultados
- Consulta la documentación si te atascas

---

## ✅ Soluciones

Las soluciones están disponibles en el archivo `soluciones.py`. Intenta resolver los ejercicios por ti mismo antes de consultarlas.

**¡Buena suerte!** 🚀
