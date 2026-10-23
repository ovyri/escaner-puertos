import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

PUERTOS_CONOCIDOS = {
    21: "FTP (Transferencia de archivos)",
    22: "SSH (Acceso remoto seguro)",
    25: "SMTP (Correo electrónico)",
    53: "DNS (Resolución de nombres)",
    80: "HTTP (Servidor web abierto)",
    110: "POP3 (Correo electrónico)",
    135: "RPC (Microsoft RPC)",
    143: "IMAP (Correo electrónico)",
    443: "HTTPS (Sitio web seguro)",
    445: "SMB (Compartir archivos en Windows)",
    3306: "MySQL (Base de datos)",
    8080: "HTTP-Alt (Servidor web alternativo)"
}

def escaner_puerto(ip, puerto):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            resultado = s.connect_ex((ip, puerto))
            if resultado == 0:
                return puerto, True
    except socket.error:
        pass
    return puerto, False

def escaner_principal(ip, puertos_a_escanear):
    inicio = datetime.now()
    encabezado = f"-" * 50 + f"\nEscaneando objetivo: {ip}\nHora de inicio: {inicio}\n" + "-" * 50
    print(encabezado)
    
    puertos_abiertos = []
    lineas_resultado = [encabezado]

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(escaner_puerto, ip, puerto): puerto for puerto in puertos_a_escanear}
        
        for future in futures:
            puerto, abierto = future.result()
            if abierto:
                servicio = PUERTOS_CONOCIDOS.get(puerto, "Servicio desconocido")
                linea = f"[+] Puerto {puerto} abierto - {servicio}"
                print(linea)
                lineas_resultado.append(linea)
                puertos_abiertos.append(puerto)

    resumen = "-" * 50 + f"\nEscaneo finalizado. Puertos abiertos encontrados: {len(puertos_abiertos)}\n" + "-" * 50
    print(resumen)
    lineas_resultado.append(resumen)

    # Guardar reporte en archivo .txt
    nombre_archivo = f"reporte_{ip.replace('.', '_')}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas_resultado))
    
    print(f"\n[i] Reporte guardado exitosamente en: {nombre_archivo}")

if __name__ == "__main__":
    ip_objetivo = input("Ingresá la IP o dominio a escanear (presioná Enter para 127.0.0.1): ").strip()
    if not ip_objetivo:
        ip_objetivo = "127.0.0.1"
    
    puertos = range(1, 1025)
    escaner_principal(ip_objetivo, puertos)