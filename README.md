# Prueba de Reconocimiento de Entidades con FastAPI y Flask
## Descripción del Problema
En el marco de la prueba técnica para evaluar las habilidades en el desarrollo de APIs para el reconocimiento de entidades nombradas, se presentan dos soluciones independientes implementadas en dos frameworks distintos de Python: FastAPI y Flask.


# Instrucciones para Ejecutar la Solución Flask:

## Requisitos Previos:

 * Asegúrate de tener Python 3.8 o superior instalado en tu sistema.

## Configuración del Entorno Virtual:

* Abre una terminal y navega hasta el directorio de la solución Flask.
* Crea un nuevo entorno virtual (recomendado):

```sh
python3.8 -m venv myenv
source myenv/bin/activate  # Para Linux/Mac
myenv\Scripts\activate    # Para Windows
```

* Instala las dependencias necesarias:


```sh
pip install -r requirements.txt
```

## Ejecución del Servidor:

* Una vez configurado el entorno, ejecuta el servidor Flask con el siguiente comando:

```sh
python app.py
```

* El servidor FastAPI estará disponible en http://127.0.0.1:5000

## Probando la API

* Utiliza una herramienta como Insomnia o Postman para enviar solicitudes POST a http://127.0.0.1:5000/ner/ con un cuerpo JSON que contenga el campo "oraciones" y una lista de oraciones a procesar.

```sh
 {
 "oraciones": [
 
 ]
}
```
<image src="https://i.ibb.co/888B7bp/Captura-de-Pantalla-2023-10-11-a-la-s-10-32-25.png">
<image src="https://i.ibb.co/4FSMKzv/Captura-de-Pantalla-2023-10-11-a-la-s-10-32-33.png">
<image src="https://i.ibb.co/tYP09WR/Captura-de-Pantalla-2023-10-11-a-la-s-10-32-41.png">

## [Resultado Flask]: https://github.com/PerlaTovarGarcia/prueba/blob/main/JSON/Resultado_Flask.json

# Instrucciones para Ejecutar la Solución FastAPI:

## Requisitos Previos:

 * Asegúrate de tener Python 3.8 o superior instalado en tu sistema.

## Configuración del Entorno Virtual:

* Abre una terminal y navega hasta el directorio de la solución FastAPI.
* Crea un nuevo entorno virtual (recomendado):

```sh
python3.8 -m venv myenv
source myenv/bin/activate  # Para Linux/Mac
myenv\Scripts\activate    # Para Windows
```

* Instala las dependencias necesarias:


```sh
pip install -r requirements.txt
```

## Ejecución del Servidor:

* Una vez configurado el entorno, ejecuta el servidor FastAPI con el siguiente comando:

```sh
uvicorn main:app --reload
```

* El servidor FastAPI estará disponible en http://127.0.0.1:8000

## Probando la API

* Entras a http://127.0.0.1:8000/docs/ y en Request body aparece una ventana asi para poner las oraciones

```sh
 {
 "oraciones": [
 
 ]
}
```
<image src="https://i.ibb.co/rd08n9T/Captura-de-Pantalla-2023-10-11-a-la-s-10-34-05.png">
<image src="https://i.ibb.co/37LcS9K/Captura-de-Pantalla-2023-10-11-a-la-s-10-34-15.png">

## [Resultado Fast API]: https://github.com/PerlaTovarGarcia/prueba/blob/main/JSON/Resultado_fastAPI.json

# [Los resultados estan en la carpeta de JSON]: https://github.com/PerlaTovarGarcia/prueba/tree/main/JSON

