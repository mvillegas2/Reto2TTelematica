import grpc
from concurrent import futures
import archivo_pb2
import archivo_pb2_grpc
import os
from dotenv import load_dotenv

load_dotenv()

MSERV2_URL = os.getenv("PUERTO_MS2")

class ArchivoServicer(archivo_pb2_grpc.ArchivoServicer):
    def BuscarArchivos(self, request, context):
        archivo_buscado = request.archivo_buscado
        archivos_encontrados = os.path.join("./files", archivo_buscado)

        if os.path.exists(archivos_encontrados):
            return archivo_pb2.ArchivoLista(archivos=[archivos_encontrados])
        else:
            return archivo_pb2.ArchivoLista(archivos=[])

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    archivo_pb2_grpc.add_ArchivoServicer_to_server(ArchivoServicer(), server)
    server.add_insecure_port(f'[::]:{MSERV2_URL}')
    server.start()
    print(f"Microservicio mserv2 escuchando en el puerto {MSERV2_URL} ...")
    server.wait_for_termination()

if __name__ == '__main__':
    main()
