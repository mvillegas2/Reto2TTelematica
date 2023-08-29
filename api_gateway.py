import grpc
import archivo_pb2
import archivo_pb2_grpc
from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

MSERV1_URL = os.getenv("URL_MS1")
MSERV2_URL = os.getenv("URL_MS2")


# MSERV1_URL = "localhost:5001"
# MSERV2_URL = "localhost:5002"

class ApiGateway:
    def __init__(self):
        self.channel_mserv1 = grpc.insecure_channel(MSERV1_URL)
        self.stub_mserv1 = archivo_pb2_grpc.ArchivoStub(self.channel_mserv1)
        
        self.channel_mserv2 = grpc.insecure_channel(MSERV2_URL)
        self.stub_mserv2 = archivo_pb2_grpc.ArchivoStub(self.channel_mserv2)
    
    def listar_archivos(self):
        response = self.stub_mserv1.ListarArchivos(archivo_pb2.ArchivoVacio())
        return response.archivos
    
    def buscar_archivos(self, archivo_buscado):
        request = archivo_pb2.ArchivoRequest(archivo_buscado=archivo_buscado)
        response = self.stub_mserv2.BuscarArchivos(request)
        return response.archivos

app = Flask(__name__)
api_gateway = ApiGateway()

@app.route('/listar_archivos', methods=['GET'])
def listar_archivos_endpoint():
    archivos = api_gateway.listar_archivos()
    archivos_serializable = list(archivos)
    return jsonify(archivos_serializable), 200

@app.route('/buscar_archivos/<nombre_archivo>', methods=['GET'])
def buscar_archivos_endpoint(nombre_archivo):
    archivos = api_gateway.buscar_archivos(nombre_archivo)
    archivos_serializable = list(archivos)
    return jsonify(archivos_serializable), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
