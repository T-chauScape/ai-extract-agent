import os

configModel = {
    "model_name": "gemini-2.5-flash-lite",
    "temperature": 0,
    "max_output_tokens": 2048,
    "api_key": os.getenv("GEMINI_API_KEY"),
    "top_p": 0.1,  # deixa mais determinístico
    "top_k": 1     # reduz variação
}
