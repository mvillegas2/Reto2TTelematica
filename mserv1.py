import grpc
from concurrent import futures
import os
import archivo_pb2
import archivo_pb2_grpc
from dotenv import load_dotenv

load_dotenv()

MSERV1_URL = os.getenv("PUERTO_MS1")

class ArchivoServicer(archivo_pb2_grpc.ArchivoServicer):
    def ListarArchivos(self, request, context):
        # Directorio que quieres listar
        directorio = "./files"
        
        try:
            archivos = os.listdir(directorio)
        except Exception as e:
            # Manejar errores en caso de que el directorio no se pueda acceder, etc.
            return archivo_pb2.ArchivoLista(archivos=[])

        return archivo_pb2.ArchivoLista(archivos=archivos)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    archivo_pb2_grpc.add_ArchivoServicer_to_server(ArchivoServicer(), server)
    server.add_insecure_port(f'[::]:5001{MSERV1_URL}')
    server.start()
    print(f"Microservicio mserv1 escuchando en el puerto {MSERV1_URL}...")
    server.wait_for_termination()

if __name__ == '__main__':
    main()
