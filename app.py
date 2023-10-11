# Importando clases necesarias de Flask
from flask import Flask, request, jsonify  

# Creando una instancia de la aplicación Flask
app = Flask(__name__)  

#importando la libreria de spacy
import spacy

# Cargando el modelo de lenguaje de spaCy
nlp = spacy.load("es_core_news_sm")  


# Definiendo una ruta de la API como POST /ner/
@app.route('/ner/', methods=['POST'])  
def recognize_entities():
    # Esta función maneja solicitudes POST a la ruta /ner/


    # Obteniendo los datos de la solicitud en formato JSON
    data = request.json  

    # Obteniendo la lista de oraciones del diccionario `data`
    oraciones = data.get("oraciones", [])  

    if not oraciones:
        # Si la lista de oraciones está vacía, se retorna un mensaje de error JSON y un código de estado 400
        return jsonify({"error": "No se proporcionaron oraciones"}), 400
    

    # Inicializando una lista vacía para almacenar los resultados
    resultados = []  
    # Iterando sobre las oraciones
    for oracion in oraciones: 
        # Procesando la oración con spaCy 
        doc = nlp(oracion)  
         # Extrayendo las entidades nombradas y sus etiquetas
        entidades = {ent.text: ent.label_ for ent in doc.ents} 
        resultados.append({"oración": oracion, "entidades": entidades})
        
    # Devolviendo el resultado como una respuesta JSON
    return jsonify({"resultado": resultados})  


# Iniciando la aplicación Flask en modo de depuración si se ejecuta como script principal
if __name__ == '__main__':
    app.run(debug=True)  