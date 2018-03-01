from visualization.models import Linha
from table import Table
from table.columns import Column, LinkColumn, Link

from table.utils import A


class Linha(Table):
    codigo_atual = Column(field='codigo_atual', header="Código Atual")
    nome_atual = Column(field='nome_atual', header="Nome Atual")
    novo_nome = Column(field='novo_nome', header="Novo Nome")
    proposta = Column(field='proposta', header="Proposta")


    class Meta:
        model = Linha
        search_placeholder = "Procure por sua linha"
