# 🚀 Inicio Rápido

¡Bienvenido a **pytorch-mx**! Esta guía te ayudará a comenzar rápidamente con los recursos del repositorio.

## ⚡ En 5 Minutos

### 1. Clona el Repositorio
```bash
git clone https://github.com/rbernalc/pytorch-mx.git
cd pytorch-mx
```

### 2. Instala PyTorch

**Opción A - CPU (Más simple)**
```bash
pip install torch torchvision torchaudio
```

**Opción B - GPU con CUDA (Más rápido)**

Visita [pytorch.org/get-started](https://pytorch.org/get-started/locally/) y selecciona tu configuración específica.

Ejemplo para CUDA 11.8:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 3. Instala Dependencias Adicionales
```bash
pip install -r requirements.txt
```

### 4. Verifica la Instalación
```bash
python -c "import torch; print(f'PyTorch versión: {torch.__version__}'); print(f'CUDA disponible: {torch.cuda.is_available()}')"
```

## 🎯 ¿Por Dónde Empezar?

### Si eres nuevo en PyTorch:
1. Empieza con [Tutoriales Básicos](./tutoriales/README.md)
2. Comienza con: [01-introduccion-pytorch](./tutoriales/01-introduccion-pytorch/README.md)
3. Practica con los ejercicios incluidos

### Si ya conoces PyTorch:
1. Explora los [Cursos Avanzados](./cursos/README.md)
2. Prueba los [Laboratorios Prácticos](./laboratorios/README.md)
3. Comienza con: [Clasificación de Imágenes MNIST](./laboratorios/clasificacion-imagenes-mnist/README.md)

### Si quieres contribuir:
1. Lee la [Guía de Contribución](./CONTRIBUTING.md)
2. Revisa el [Código de Conducta](./CODE_OF_CONDUCT.md)
3. Busca issues etiquetados como "good first issue"

## 📚 Estructura del Repositorio

```
pytorch-mx/
├── tutoriales/          # Tutoriales paso a paso
├── cursos/              # Cursos completos estructurados
├── laboratorios/        # Proyectos prácticos hands-on
├── CONTRIBUTING.md      # Guía para contribuir
├── CODE_OF_CONDUCT.md   # Código de conducta
└── requirements.txt     # Dependencias del proyecto
```

## 🔧 Configuración de Entorno de Desarrollo

### Usando venv (Recomendado)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Linux/Mac)
source venv/bin/activate

# Activar entorno (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Usando conda
```bash
# Crear entorno
conda create -n pytorch-mx python=3.10

# Activar entorno
conda activate pytorch-mx

# Instalar PyTorch
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# Instalar otras dependencias
pip install -r requirements.txt
```

## 📓 Ejecutando Notebooks

### Jupyter Notebook
```bash
jupyter notebook
```
Luego navega a los archivos `.ipynb` en las carpetas de tutoriales o laboratorios.

### JupyterLab (Interfaz moderna)
```bash
pip install jupyterlab
jupyter lab
```

### VS Code (Si lo prefieres)
1. Instala la extensión "Jupyter" en VS Code
2. Abre cualquier archivo `.ipynb`
3. Selecciona el kernel de Python correcto

## 💡 Primeros Pasos Recomendados

1. **Día 1**: Lee el README principal y explora la estructura
2. **Día 2-3**: Completa el tutorial de introducción a PyTorch
3. **Semana 1**: Termina los tutoriales básicos
4. **Semana 2**: Comienza un curso o laboratorio de tu interés
5. **Semana 3+**: Contribuye con tu propio contenido o ayuda a otros

## 🆘 Necesitas Ayuda?

- **Preguntas generales**: [GitHub Discussions](../../discussions)
- **Reportar problemas**: [GitHub Issues](../../issues)
- **Documentación PyTorch**: [pytorch.org/docs](https://pytorch.org/docs/)
- **Foro PyTorch**: [discuss.pytorch.org](https://discuss.pytorch.org/)

## 🌟 Mantente Actualizado

- ⭐ Da una estrella al repositorio
- 👁️ Activa las notificaciones ("Watch")
- 🍴 Haz un fork para tus propios experimentos
- 📢 Comparte con tu comunidad usando #PyTorchMX

## 🎓 Recursos Externos Útiles

### Documentación Oficial
- [PyTorch Docs](https://pytorch.org/docs/) - Documentación oficial
- [PyTorch Tutorials](https://pytorch.org/tutorials/) - Tutoriales oficiales (inglés)

### Cursos Online Gratuitos
- [Deep Learning Specialization](https://www.deeplearning.ai/) - Andrew Ng (inglés)
- [Fast.ai](https://www.fast.ai/) - Curso práctico de deep learning (inglés)

### Comunidades
- [PyTorch Forums](https://discuss.pytorch.org/) - Foro oficial
- [Reddit r/pytorch](https://reddit.com/r/pytorch) - Comunidad en Reddit
- [Discord PyTorch](https://discord.gg/pytorch) - Chat en vivo

### Papers y Artículos
- [Papers with Code](https://paperswithcode.com/) - Papers con implementaciones
- [Arxiv Sanity](http://www.arxiv-sanity.com/) - Explorador de papers

## 🔄 Actualizaciones

Para obtener las últimas actualizaciones del repositorio:

```bash
git pull origin main
```

Si hiciste cambios locales:
```bash
git stash                  # Guarda cambios temporalmente
git pull origin main       # Actualiza
git stash pop             # Recupera tus cambios
```

---

## ✅ Checklist de Inicio

- [ ] Repositorio clonado
- [ ] PyTorch instalado
- [ ] Dependencias instaladas
- [ ] Instalación verificada
- [ ] Primer tutorial completado
- [ ] Jupyter funcionando
- [ ] Perfil configurado en GitHub
- [ ] Repositorio marcado con ⭐

---

**¡Listo para comenzar tu viaje con PyTorch!** 🎉

Si tienes preguntas, no dudes en abrir un issue o iniciar una discusión. La comunidad está aquí para ayudarte.

**¡Nos vemos en el código!** 👨‍💻👩‍💻
