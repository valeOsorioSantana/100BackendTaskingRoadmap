import os
import re
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()
client.api_key = openai_api_key

respuesta = client.beta.assistants.create(
    name="Desarrollador de software",
    instructions="Eres un desarrollador experto en backend con conocimientos profesionales en obsidian y markdown de la empresa Aquicreamos",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4o-mini",
)


def convertir_a_nombre_archivo(titulo):
    nombre_archivo = titulo.lower()
    nombre_archivo = nombre_archivo.replace(" ", "_")
    nombre_archivo = re.sub(r'[^a-z0-9_\-.]', '', nombre_archivo)

    return nombre_archivo


info = [
    {
        "info": "Dame las instrucciones necesarias para Configurar un servidor local con docker desde Python con Fastapi",
        "route": "../Python/Fastapi/install.md",
        "tema": "Python con Fastapi Config Install"
    },
    {
        "info": "Dame las instrucciones necesarias para Configurar un servidor local con docker desde Python con Flask",
        "route": "../Python/Flask/install.md",
        "tema": "Python con Flask Config Install"
    },
    {
        "info": "Dame las instrucciones necesarias para Configurar un servidor local con docker desde Python con Django",
        "route": "../Python/Django/install.md",
        "tema": "Python con Django Config Install"
    },
    {
        "info": "Dame las instrucciones necesarias para Configurar un servidor local con docker desde Golang con Gin",
        "route": "../Go/Gin/install.md",
        "tema": "Golang con Gin Config Install"
    },
    {
        "info": "Dame las instrucciones necesarias para Configurar un servidor local con docker desde Node js con Nestjs",
        "route": "../Nodejs/Nest/install.md",
        "tema": "Node con Nest js Config Install"
    },
    {
        "info": "Dame las instrucciones necesarias para Configurar un servidor local con docker desde Java con Spring Boot",
        "route": "../Java/Spring/install.md",
        "tema": "Java con Spring Config Install"
    },
    {
        "info": "Dame las instrucciones necesarias para Configurar un servidor local con docker desde Kotlin con Spring Boot",
        "route": "../Kotlin/Spring/install.md",
        "tema": "Kotlin con Spring Config Install"
    },
    {
        "info": "Dame las instrucciones necesarias para Configurar un servidor local con docker desde Nodejs con Express",
        "route": "../Nodejs/Express/install.md",
        "tema": "Nodejs con Express Config Install"
    },
    {
        "info": "Dame las instrucciones necesarias para Configurar un servidor local con docker desde PHP con Laravel",
        "route": "../PHP/Laravel/install.md",
        "tema": "PHP con Laravel Config Install"
    }
]


def generarRespuestas(promt, route, titulo):
    thread = client.beta.threads.create()

    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=promt,
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=respuesta.id,
        instructions=f"Da la bienvenida al user pues somos Aquicreamos genera la consulta el tema es {titulo}",
    )

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    final = vars(vars(vars(vars(messages)['data'][0])['content'][0])['text'])

    if run.status == "completed":
        file_path = os.path.dirname(os.path.abspath(route))
        os.makedirs(file_path, exist_ok=True)

        if os.path.exists(file_path):

            archivo_path = os.path.join(
                file_path, convertir_a_nombre_archivo(titulo) + ".md")
            # Guardar el contenido en el archivo
            with open(archivo_path, "w", encoding='utf-8') as file:
                file.write(final['value'])

            print("Content written to " + file_path)
        else:
            print('No existe', file_path)


for x in info:
    generarRespuestas(x['info'], x['route'], x['tema'])
    print(x)
