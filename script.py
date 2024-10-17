# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import openai
import random

app = Flask(__name__)
CORS(app)  # Autoriser CORS pour toutes les routes

# Remplacez par votre clé d'API OpenAI
openai.api_key = " "

# Fonction pour générer une question
def generate_question(topic):
    system_message = {
        "role": "system", 
        "content": (
            "Tu es une IA qui doit créer des questions sur le thème de la sécurité sur les réseaux sociaux. "
            "Tu dois par exemple demander la définition d'un mot ou mettre l'utilisateur dans une situation où il devra choisir la bonne réponse. "
            "Tu dois écrire un code JSON contenant une question (question), une bonne réponse (right_answer) et deux mauvaises réponses (wrong_answer1 et wrong_answer2). Rien d'autre ne doit figurer."
        )
    }
    user_message = {"role": "user", "content": f"Crée une question sur le thème de {topic}."}
    
    # Appel à l'API OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Assurez-vous d'utiliser le bon modèle
        messages=[system_message, user_message]
    )
    
    # Extraire le contenu JSON de la réponse
    question_data = response['choices'][0]['message']['content']
    return question_data

# Route pour obtenir une question
@app.route('/api/question', methods=['GET'])
def get_question():
    topics = ["Phishing", "Harcèlement", "Ransomware", "Mots de passe"]
    topic = random.choice(topics)  # Choisir un sujet aléatoire
    question_data = generate_question(topic)
    return question_data

if __name__ == '__main__':
    app.run(debug=True)