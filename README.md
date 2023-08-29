# info de la materia: ST0263
#
# Estudiante(s): Martin Villegas Aristizabal, mvillegas2@eafit.edu.co
#
# Profesor: Edwin Montoya Munera, emontoya@eafit.brightspace.com
#
# Reto 2
#
# 1. En este proyecto como idea principal se tiene una aplicacion para la comunicacion entre dos microservicios y un apigateway por medio de grpc, con el objetivo de buscar y listar archivos, con la ayuda de rabbitmq.
#
<texto descriptivo>
## 1.1. Se logró la implementacion de los dos microservicios para listar y buscar archivos y la comunicacion con el api gateway funcionando ambos en la maquina virtual de aws

## 1.2. La implementación de RabbitMQ en el proyecto no se pudo completar

# 2. Se utilizó una arquitectura basada en microservicios, donde cada microservicio se encuentra en un archivo separado. Se implementó un API Gateway para gestionar las solicitudes y redirigirlas a los microservicios adecuados.

# 3. Para este proyecto se utilizo python, flask, grpc, protobuf, entre otras. (para mas info visitar requirements.txt)

## Se deben crear 3 instancias desde las cuales se deben correr los 3 servicios: api_gateway.py, mserv1.py, mserv2.py.
## Para acceder a los archivos se encuentran en la carpera /Reto2/Reto2TTelematica
## detalles del desarrollo.
## - Cada microservicio tiene su propia lógica para listar y buscar archivos en un directorio.
## - El API Gateway redirige las solicitudes a los microservicios utilizando peticiones HTTP.

## pantallazos 
## Api corriendo
![Screen Shot 2023-08-28 at 10 31 04 PM](https://github.com/mvillegas2/Reto2TTelematica/assets/60147106/9f52718f-9ab4-40db-b5b0-12fd2d35770e)
## Respuesta microservicio 1
![Screen Shot 2023-08-28 at 10 33 08 PM](https://github.com/mvillegas2/Reto2TTelematica/assets/60147106/f45c8075-7c6e-47d1-932e-b4466d5ef462)

## Respuesta microservicio 2
![Screen Shot 2023-08-28 at 10 32 46 PM](https://github.com/mvillegas2/Reto2TTelematica/assets/60147106/ed5c3dca-d08e-4a35-a27d-26662b3ca02c)


# 4. Para este proyecto se utilizo python, flask, grpc, protobuf, entre otras. (para mas info visitar requirements.txt)

# IP o nombres de dominio en nube o en la máquina servidor:
## 54.242.202.49/5000
## 54.242.202.49/5000/listar_archivos
## 54.242.202.49/5000/{nombreArchivo}

# 5. Bastante complejo el proyecto

# referencias:
## https://flask.palletsprojects.com/
## https://grpc.io/
## https://docs.aws.amazon.com/es_es/transfer/latest/userguide/transfer-file.html
## https://www.freecodecamp.org/espanol/news/administrar-multiples-versiones-de-python-y-entornos-virtuales/
## https://github.com/protocolbuffers/protobuf/releases
## https://github.com/rabbitmq/rabbitmq-server/releases?page=11
## https://www.youtube.com/watch?v=iQ4kENLfaNI&list=PLalrWAGybpB-UHbRDhFsBgXJM1g6T4IvO
