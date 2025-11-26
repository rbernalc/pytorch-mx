# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a **pytorch-mx**! Este proyecto crece gracias a personas como tú que dedican su tiempo y conocimiento para ayudar a la comunidad.

## 🌟 Formas de Contribuir

Hay muchas maneras de contribuir, y todas son valiosas:

### 📝 Contenido
- Crear nuevos tutoriales
- Escribir nuevos cursos o módulos
- Desarrollar laboratorios prácticos
- Traducir contenido existente
- Mejorar la documentación

### 🐛 Mantenimiento
- Reportar errores o bugs
- Corregir errores en el código
- Actualizar dependencias
- Mejorar la organización del repositorio

### 💡 Ideas y Sugerencias
- Proponer nuevos temas
- Sugerir mejoras
- Compartir recursos útiles
- Dar feedback sobre el contenido existente

### 👥 Comunidad
- Responder preguntas en Discussions
- Ayudar a otros usuarios
- Compartir tus proyectos
- Promover el repositorio

## 🚀 Proceso de Contribución

### 1. Antes de Comenzar

1. **Busca issues existentes**: Revisa si alguien ya está trabajando en algo similar
2. **Crea un issue**: Si es algo nuevo, abre un issue para discutir tu idea
3. **Espera feedback**: Dale tiempo a la comunidad para comentar

### 2. Preparar tu Entorno

```bash
# Fork el repositorio en GitHub

# Clona tu fork
git clone https://github.com/TU-USUARIO/pytorch-mx.git
cd pytorch-mx

# Agrega el repositorio original como upstream
git remote add upstream https://github.com/rbernalc/pytorch-mx.git

# Crea una rama para tu contribución
git checkout -b nombre-de-tu-rama
```

### 3. Hacer Cambios

1. **Sigue las convenciones**: Respeta el estilo y estructura existente
2. **Código limpio**: Asegúrate de que el código sea legible y esté bien comentado
3. **Prueba tu código**: Verifica que todo funcione correctamente
4. **Documenta**: Incluye README y explicaciones claras

### 4. Commit y Push

```bash
# Agrega tus cambios
git add .

# Commit con un mensaje descriptivo
git commit -m "Descripción clara de los cambios"

# Push a tu fork
git push origin nombre-de-tu-rama
```

### 5. Crear Pull Request

1. Ve a GitHub y crea un Pull Request desde tu rama
2. Describe claramente los cambios realizados
3. Referencia el issue relacionado (si existe)
4. Espera la revisión

## 📋 Estándares y Convenciones

### Estructura de Archivos

#### Para Tutoriales:
```
tutoriales/
└── XX-nombre-tutorial/
    ├── README.md           # Descripción y objetivos
    ├── notebook.ipynb      # Código y explicaciones
    ├── ejercicios.md       # Ejercicios prácticos
    └── recursos.md         # Enlaces adicionales
```

#### Para Cursos:
```
cursos/
└── nombre-curso/
    ├── README.md           # Syllabus completo
    ├── modulo-01/
    │   ├── leccion-01/
    │   │   ├── teoria.md
    │   │   ├── notebook.ipynb
    │   │   └── ejercicios.md
    └── proyecto-final/
```

#### Para Laboratorios:
```
laboratorios/
└── nombre-laboratorio/
    ├── README.md
    ├── requirements.txt
    ├── notebooks/
    ├── src/
    └── data/
```

### Estilo de Código

- **Python**: Sigue PEP 8
- **Comentarios**: En español, claros y concisos
- **Nombres de variables**: Descriptivos y en español cuando sea apropiado
- **Notebooks**: Incluye celdas markdown explicativas entre código

### Estilo de Documentación

- **Lenguaje**: Español neutro, evita regionalismos cuando sea posible
- **Tono**: Amigable, educativo y profesional
- **Formato**: Usa Markdown correctamente
- **Emojis**: Úsalos con moderación para mejorar la legibilidad

### Mensajes de Commit

Usa mensajes claros y descriptivos:

```
✅ Bueno:
- "Agrega tutorial sobre redes convolucionales"
- "Corrige error en el laboratorio de GANs"
- "Actualiza README con nuevos recursos"

❌ Malo:
- "Update"
- "Fix"
- "Cambios varios"
```

## 🎯 Guías Específicas

### Creando Tutoriales

1. **Identifica un tema**: Que sea relevante y útil
2. **Define objetivos**: Qué aprenderá el usuario
3. **Estructura progresiva**: De lo simple a lo complejo
4. **Incluye ejemplos**: Código ejecutable y explicado
5. **Agrega ejercicios**: Para reforzar el aprendizaje
6. **Prueba todo**: Ejecuta el código completo antes de enviar

### Creando Cursos

1. **Planifica el syllabus**: Define módulos y lecciones
2. **Establece requisitos**: Conocimientos previos necesarios
3. **Crea contenido progresivo**: Cada lección construye sobre la anterior
4. **Incluye proyecto final**: Que integre todo lo aprendido
5. **Proporciona recursos**: Bibliografia y materiales adicionales

### Creando Laboratorios

1. **Define el problema**: Claro y concreto
2. **Especifica requisitos**: Hardware, software, datos
3. **Proporciona datos**: O instrucciones para obtenerlos
4. **Documenta resultados**: Métricas, visualizaciones
5. **Código reproducible**: Que otros puedan ejecutar
6. **Incluye referencias**: Papers, artículos relevantes

## ✅ Checklist antes de Enviar

Antes de crear tu Pull Request, verifica:

- [ ] El código funciona correctamente
- [ ] Todos los notebooks se ejecutan sin errores
- [ ] La documentación está completa y clara
- [ ] Los archivos siguen la estructura establecida
- [ ] Los mensajes de commit son descriptivos
- [ ] No hay archivos innecesarios (caché, checkpoints grandes, etc.)
- [ ] Has probado en un ambiente limpio (si es posible)

## ❓ ¿Necesitas Ayuda?

- **Preguntas generales**: Usa [GitHub Discussions](../../discussions)
- **Issues técnicos**: Abre un [issue](../../issues)
- **Contacto directo**: Comenta en un issue o PR existente

## 🙏 Reconocimiento

Todos los contribuidores serán reconocidos en el proyecto. Tu nombre aparecerá automáticamente en la lista de contributors de GitHub.

## 📜 Código de Conducta

Al contribuir, aceptas seguir nuestro [Código de Conducta](CODE_OF_CONDUCT.md). Mantenemos un ambiente respetuoso e inclusivo para todos.

---

**¡Gracias por ayudarnos a construir la mejor comunidad de PyTorch en Latinoamérica!** 🚀🇲🇽
