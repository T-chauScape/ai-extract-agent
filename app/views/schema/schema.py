from pydantic import BaseModel, Field
from typing import List, Optional, Literal



class Investment(BaseModel):
    product: Optional[Literal["RDB", "CDB", "OUTRO"]] = Field(
        None,
        description="Produto (ex: RDB, CDB, OUTRO)."
    )
    operation: Optional[Literal["APLICACAO", "RESGATE"]] = Field(
        None,
        description="Operação: APLICACAO ou RESGATE."
    )


class Transaction(BaseModel):
    date: str = Field(
        ...,
        description="Data da transação no formato YYYY-MM-DD.",
        pattern=r"^\d{4}-\d{2}-\d{2}$"
    )

    category: Optional[str] = Field(
        None,
        description="Categoria (ex: SALARIO, ALIMENTACAO, CARTAO, TARIFA...)."
    )

    type: Literal["CREDITO", "DEBITO"] = Field(
        ...,
        description="Tipo: CREDITO (entrada) ou DEBITO (saída)."
    )

    amount: str = Field(
        ...,
        description="Valor absoluto da transação (sem sinal)."
    )

    currency: Literal["BRL"] = Field(
        ...,
        description="Moeda da transação (normalmente BRL)."
    )

    description: str = Field(
        ...,
        description="Descrição conforme aparece no extrato."
    )

    card_type: Optional[Literal["DEBITO", "CREDITO"]] = Field(
        None,
        description="Tipo do cartão, se aplicável."
    )

    counterparty_name: Optional[str] = Field(
        None,
        description="Nome da contraparte, se disponível."
    )

    investment: Optional[Investment] = Field(
        None,
        description="Informações de investimento relacionadas, se aplicável."
    )

    evidence: str = Field(
        ...,
        description="Linha/trecho exato do extrato usado para extrair a transação."
    )


class OutputSchema(BaseModel):
    transactions: List[Transaction] = Field(
        ...,
        description="Lista de transações no extrato."
    )
