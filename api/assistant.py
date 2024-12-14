import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


openai.api_key = openai_api_key
def interactuar_con_tutor_ingles():
    print("Bienvenido al asistente de inglés. Escribe 'salir' para terminar.")
    
    # Configuración del mensaje de inicio con un contexto
    messages = [{"role": "system", "content": "Eres un tutor de inglés. Ayudas a los estudiantes a mejorar su gramática, vocabulario y comprensión. Explicas errores y das ejemplos prácticos."}]
    
    while True:
        # Solicitar la entrada del usuario
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("¡Adiós!")
            break
        
        # Añadir la entrada del usuario a la conversación
        messages.append({"role": "user", "content": user_input})
        
        # Obtener la respuesta del modelo
        response = openai.beta.assistants.create(
            model="gpt-4",  # O usa "gpt-3.5-turbo"
            messages=messages,
            max_tokens=200,
            temperature=0.7  # Nivel de creatividad de la respuesta
        )
        
        # Obtener y mostrar la respuesta generada
        reply = response['choices'][0]['message']['content']
        print(f"Tu tutor de inglés: {reply}")
        
        # Añadir la respuesta del asistente al historial para contexto continuo
        messages.append({"role": "assistant", "content": reply})

# Llamar a la función para interactuar con el tutor
interactuar_con_tutor_ingles()