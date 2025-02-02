import argparse
import os
from http.server import HTTPServer, CGIHTTPRequestHandler, SimpleHTTPRequestHandler

def start_server(port, directory, bind, cgi):
    """
    Inicia el servidor HTTP con los parámetros proporcionados.
    """
    try:
        # Cambia al directorio especificado
        os.chdir(directory)

        # Define el manejador de solicitudes (handler)
        if cgi:
            handler = CGIHTTPRequestHandler
        else:
            handler = SimpleHTTPRequestHandler

        # Crea una instancia del servidor HTTP
        server = HTTPServer((bind, port), handler)

        # Mensaje personalizado
        print("==============================================")
        print("NeoHTTPServer - Creado por josevdr95")
        print("v1.0 2025")
        print("==============================================")
        print(f"Iniciando servidor HTTP en http://{bind}:{port}")
        print(f"Sirviendo archivos desde: {directory}")
        if cgi:
            print("CGI habilitado.")
        print("Presiona Ctrl + C para detener el servidor.")
        print("==============================================")

        # Inicia el servidor
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido. ¡Hasta luego!")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """
    Función principal que maneja los argumentos de la línea de comandos.
    """
    # Configura el parser de argumentos
    parser = argparse.ArgumentParser(description="NeoHTTPServer - Servidor HTTP simple usando 'http.server'.")
    parser.add_argument("--port", type=int, default=8000, help="Puerto en el que se ejecutará el servidor (por defecto: 8000).")
    parser.add_argument("--directory", type=str, default=os.getcwd(), help="Directorio desde el cual se servirán los archivos (por defecto: directorio actual).")
    parser.add_argument("--bind", type=str, default="localhost", help="Dirección IP en la que se ejecutará el servidor (por defecto: localhost).")
    parser.add_argument("--cgi", action="store_true", help="Habilita el soporte para CGI (Common Gateway Interface).")
    
    # Parsea los argumentos
    args = parser.parse_args()
    
    # Inicia el servidor con los parámetros proporcionados
    start_server(args.port, args.directory, args.bind, args.cgi)

if __name__ == "__main__":
    main()