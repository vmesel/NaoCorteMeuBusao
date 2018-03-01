import os
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from visualization.models import Linha
import pandas as pd
from tqdm import tqdm


class Command(BaseCommand):
    @staticmethod
    def _get_linhas():
        base = os.path.dirname(os.path.abspath('__file__'))
        full_path = "{}/static/busos_cortados.csv".format(base)
        linhas = []
        df = pd.read_csv(full_path)
        print("Pré-processamento dos dados")
        for df_i in tqdm(df.to_dict('records')):
            linhas.append({
                "codigo_atual": df_i["CÓDIGO ATUAL"],
                "nome_atual": df_i["NOME ATUAL"],
                "novo_nome": df_i["NOME NOVO"],
                "proposta": df_i["PROPOSTA DO DÓRIA"]
            })
        return linhas


    def handle(self, *args, **options):
        gen_locs = self._get_linhas()
        print("Inserção no banco")
        for linha in tqdm(gen_locs):
            try:
                linha_obj = Linha.objects.create(**linha)
            except IntegrityError as e:
                pass
