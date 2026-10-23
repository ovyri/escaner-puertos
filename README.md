# Escáner de Puertos TCP (Port Scanner) 🔍

Herramienta de auditoría de red desarrollada en **Python** diseñada para escanear puertos TCP abiertos en hosts remotos o locales, mapeando los servicios activos asociados.

---

## 🚀 Características Principales
* **Resolución de Objetivos:** Capacidad de traducir nombres de dominio (ej. `scanme.nmap.org`) a direcciones IP reales de forma automática.
* **Control de Tiempo (Timeout):** Implementación de límites de tiempo de espera (`settimeout`) para evitar bloqueos del programa ante respuestas lentas.
* **Mapeo de Servicios:** Identificación de servicios comunes asociados a puertos clave (SSH, HTTP, DNS, FTP, etc.).
* **Manejo de Excepciones:** Uso seguro de sockets y control de errores de red sin interrupciones críticas.

---

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python 3** (Lenguaje principal)
* **Módulo `socket`** (Gestión de conexiones TCP/IP a nivel de sistema operativo)
* **Módulo `datetime`** (Registro de marcas temporales de ejecución)
* **Git / GitHub** (Control de versiones)

---

## ⚙️ Instrucciones de Uso

1. Clona este repositorio o descarga el script `port_scanner.py`:
   ```bash
   git clone [https://github.com/ovyri/escaner-puertos.git](https://github.com/ovyri/escaner-puertos.git)