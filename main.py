# Importando las clases necesarias de FastAPI
from fastapi import FastAPI, HTTPException, Body 
# Importando la biblioteca spaCy 
import spacy  

app = FastAPI()  # Creando una instancia de FastAPI

# Cargando el modelo de lenguaje de spaCy
nlp = spacy.load("es_core_news_sm")  


# El decorador `@app.post` especifica que esta función maneja solicitudes POST a la ruta /ner/
@app.post("/ner/")  # Definiendo una ruta de la API como POST /ner/

# `data` es un diccionario que se espera como cuerpo de la solicitud JSON
async def recognize_entities(data: dict = Body(...)):
    

    
    # Obteniendo la lista de oraciones del diccionario `data`
    oraciones = data.get("oraciones", [])  

    if not oraciones:
        # Si la lista de oraciones está vacía, se levanta una excepción HTTP con un mensaje de error
        raise HTTPException(status_code=400, detail="No se proporcionaron oraciones")
        
    # Inicializando una lista vacía para almacenar los resultados
    resultados = []

    # Iterando sobre las oraciones
    for oracion in oraciones: 
        # Procesando la oración con spaCy
        doc = nlp(oracion)  
        # Extrayendo las entidades nombradas y sus etiquetas
        entidades = {ent.text: ent.label_ for ent in doc.ents}  
        # Agregando un diccionario con la oración y las entidades a la lista de resultados
        resultados.append({"oración": oracion, "entidades": entidades})
        
    # Devolviendo el resultado como un diccionario JSON
    return {"resultado": resultados}  