import os
import google.genai as genai

# Eu não preciso definir a variavel de ambiente GEMINI_API_KEY, pois o genai já a utiliza automaticamente. 
# Basta garantir que a variável de ambiente esteja definida corretamente no sistema operacional.
# agent = genai.Agent(api_key=api_key)

Client = genai.Client()
response = Client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Make a joke about programming.",
    # input=[
    #     {
    #         "role": "user",
    #         "content": [
    #             {"type": "input_text", "text": "Encontre o crachá de acesso do escritório."}
    #         ],
    #     }
    # ],
)
print(response.text)