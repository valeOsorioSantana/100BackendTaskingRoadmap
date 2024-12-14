import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def obtener_respuesta(mensaje):
    openai.api_key = openai_api_key
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un asistente útil."},
                {"role": "user", "content": mensaje}
            ],
            temperature=0.7
        )
        return respuesta['choices'][0]['message']['content']
    except Exception as e:
        return f"Error al obtener respuesta: {str(e)}"

contexto = """
La guerra Israel-Gaza, también llamada guerra de Gaza, o guerra Israel-Hamás, es un conflicto armado en curso que comenzó el 7 de octubre de 2023, mientras los israelíes festejaban la fiesta de Simjat Torá y los judíos que viven en el extranjero celebraban el último día de la fiesta de Sucot. Ese día, grupos armados de militantes palestinos, principalmente de Hamás y de la Yihad Islámica Palestina, lanzaron un ataque contra Israel desde la Franja de Gaza con una andanada de cohetes y un ataque de comandos en camiones, motocicletas y parapentes motorizados.19​ El ataque, denominado «Operación Inundación de Al-Aqsa», tomó a Israel por sorpresa pese a ocurrir al día siguiente al 50.º aniversario de la guerra de Yom Kipur.20​ Israel respondió poco después con una represalia denominada «Operación Espadas de Hierro», con bombardeos y una posterior invasión de la Franja de Gaza.21​

Los militantes armados de Hamás capturaron rehenes tras sucesivas razias en el sur de Israel,22​ lo que llevó al Gobierno de Israel a declarar el estado de guerra por primera vez desde 1973.23​ Los ataques con cohetes fueron acompañados de infiltraciones de militantes en varios de los kibutz que rodean Gaza y en la ciudad israelí de Sederot.20​ Como resultado del ataque de Hamás en comunidades cercanas a la Franja de Gaza y en las bases del ejército israelí murieron 695 civiles israelíes (incluidos 36 menores de edad), 71 civiles extranjeros y 373 soldados y policías.24​ Cerca del kibutz Reim, unos cincuenta milicianos mataron a 364 personas en el festival de música Supernova.24​ Human Rights Watch ha denunciado que el ataque deliberado contra civiles, los ataques indiscriminados y la toma de civiles como rehenes constituyen crímenes de guerra según el derecho internacional humanitario.25​
"""

# Prueba con un mensaje
fin = obtener_respuesta(f"""
analiza el texto y define si la respuesta respuesta del usuario es congruente
 o parecido al contenido {contexto},
Usuario: guerra entre israel y palestina.
solo responde json asi:
- respuesta (SI o NO)
""")
print(fin)