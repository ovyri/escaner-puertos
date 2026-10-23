import socket
import sys
from datetime import datetime

# Diccionario con puertos comunes para dar un diagnóstico más claro
PUERTOS_CONOCIDOS = {
    21: "FTP (Transferencia de archivos)",
    22: "SSH (Acceso remoto seguro)",
    23: "Telnet (Acceso remoto no seguro)",
    25: "SMTP (Correo electrónico)",
    53: "DNS (Resolución de nombres)",
    80: "HTTP (Navegación Web)",
    110: "POP3 (Correo electrónico)",
    143: "IMAP (Correo electrónico)",
    443: "HTTPS (Navegación Web segura)",
    3306: "MySQL (Base de datos)",
    8080: "HTTP-Alt (Servidor web alternativo)"
}

def escanear_puerto(host_ip, puerto):
    """
    Intenta conectarse a un puerto específico en la IP dada.
    Retorna True si el puerto está abierto, False si está cerrado o no responde.
    """
    try:
        # AF_INET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Tiempo de espera máximo de 0.5s por puerto
        
        # connect_ex devuelve 0 si la conexión fue exitosa
        resultado = s.connect_ex((host_ip, puerto))
        s.close()
        
        return resultado == 0
    except socket.error:
        return False

def iniciar_escaneo():
    print("=" * 55)
    print("   🔍 Escáner de Puertos TCP - Herramienta de Auditoría")
    print("=" * 55)
    
    objetivo = input("Ingresa la IP o dominio a escanear (ej: scanme.nmap.org): ").strip()
    
    if not objetivo:
        print("❌ Error: Debes ingresar un objetivo válido.")
        return

    # Traducir nombre de dominio a dirección IP
    try:
        ip_objetivo = socket.gethostbyname(objetivo)
    except socket.gaierror:
        print(f"❌ Error: No se pudo resolver el dominio '{objetivo}'.")
        return

    print("\n" + "-" * 55)
    print(f"Escaneando objetivo : {objetivo} ({ip_objetivo})")
    print(f"Inicio del escaneo : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 55 + "\n")

    # Lista de puertos a evaluar (puedes ajustar el rango)
    puertos_a_escanear = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]
    puertos_abiertos = 0

    for puerto in puertos_a_escanear:
        if escanear_puerto(ip_objetivo, puerto):
            servicio = PUERTOS_CONOCIDOS.get(puerto, "Servicio desconocido")
            print(f"  [+] Puerto {puerto:<5} [ABIERTO]  -> Servicio: {servicio}")
            puertos_abiertos += 1

    print("\n" + "=" * 55)
    print(f"Resumen: Escaneo finalizado. Se encontraron {puertos_abiertos} puerto(s) abierto(s).")
    print("=" * 55)

if __name__ == "__main__":
    iniciar_escaneo()