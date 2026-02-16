import time

from app.models.extractor_model import extractorModel
from app.models.chunck.chunk_method import chuck_string

def extract_transactions(texto_completo):
    chunks = chuck_string(texto_completo=texto_completo,regex_pattern=r'(?=.*\d{2} (?:JAN|FEV|MAR|ABR|MAI|JUN|JUL|AGO|SET|OUT|NOV|DEZ) \d{4})' )
    print(f"Total chunks created: {len(chunks)}")
    transactions = []

    PACE_SECONDS = 0.4 

    for i, chunk in enumerate(chunks, start=1):
        print(f"\nProcessing chunk {i}/{len(chunks)}...")
        llm = extractorModel()
        result = llm.extract(chunk_atual=chunk,chunk_indice=i)
        transactions.append(result["transactions"])
        time.sleep(PACE_SECONDS)
    return transactions
