
import time
import random

from langchain_google_genai import ChatGoogleGenerativeAI
from google.genai.errors import ClientError

from app.views.schema.schema import OutputSchema
from app.views.prompt.context import PROMPT_EXTRACAO
from app.config.configModel import configModel


class extractorModel:
    
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=configModel["model_name"],
            temperature=configModel["temperature"],
            max_output_tokens=configModel["max_output_tokens"],
            google_api_key=configModel["api_key"],
            top_p=configModel["top_p"],
            top_k=configModel["top_k"],
        ).with_structured_output(OutputSchema)
        self.prompt = PROMPT_EXTRACAO
        self.chain = self.prompt | self.llm

    
    def extract(self, chunk_atual,chunk_indice) -> OutputSchema:
        MAX_RETRIES = 5
        
        last_err = None
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                extracted = self.chain.invoke({"texto_extraido": chunk_atual})
                print(f"Extracted: {extracted}")
                
                return extracted

            except ClientError as e:
                last_err = e
                status = getattr(e, "status_code", None)

                if status == 429 and attempt < configModel["max_retries"]:
                    base = 1.0
                    sleep = min(30.0, base * (2 ** (attempt - 1)))
                    sleep *= (0.5 + random.random())  # jitter
                    print(f"429 RESOURCE_EXHAUSTED. Retry {attempt}/{configModel['max_retries']} in {sleep:.2f}s")
                    time.sleep(sleep)
                    continue

                raise

            except Exception as e:
                raise
        else:
            # se saiu do for sem break (não deve acontecer com o fluxo acima, mas fica seguro)
            raise RuntimeError(f"Falhou no chunk {chunk_indice}. Último erro: {last_err}")
