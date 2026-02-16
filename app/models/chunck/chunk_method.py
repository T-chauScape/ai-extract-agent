import re
## Simplificado para usar regex diretamente, sem necessidade de definir chunk_size e overlap, já que o padrão de divisão é baseado em datas explícitas.
def chuck_string(regex_pattern, texto_completo):
    pattern = regex_pattern

    return re.split(pattern, texto_completo)
