from django.shortcuts import render

# core/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests # Importamos a biblioteca para fazer chamadas HTTP

class CurrencyConverterView(APIView):
    """
    Uma View de API para converter moedas.
    Espera parâmetros na URL: ?de=USD&para=BRL&valor=10
    """

    def get(self, request):
        # 1. Pegar os dados que o usuário enviou na URL
        # request.query_params é um dicionário com os parâmetros da URL
        try:
            de_moeda = request.query_params.get('de').upper()
            para_moeda = request.query_params.get('para').upper()
            valor = float(request.query_params.get('valor'))
        except Exception as e:
            # Se faltar algum parâmetro ou o valor não for um número, retorna um erro
            return Response(
                {"erro": "Parâmetros inválidos. Use ?de=MOEDA&para=MOEDA&valor=NUMERO"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 2. Chamar a API externa (nossa fonte da verdade)
        # Usamos a API gratuita "open.er-api.com"
        # Pedimos a ela todas as taxas baseadas na moeda 'de_moeda' (ex: USD)
        try:
            url_api_externa = f"https://open.er-api.com/v6/latest/{de_moeda}"
            resposta_api = requests.get(url_api_externa)
            
            # Se a API externa falhar (ex: moeda "DE" não existe), repassamos o erro
            if resposta_api.status_code != 200:
                return Response(
                    {"erro": "Não foi possível obter as taxas de câmbio para a moeda base."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            dados = resposta_api.json() # Convertemos a resposta para JSON (um dicionário Python)
            taxas = dados.get('rates')

            # 3. Encontrar a taxa específica e calcular
            taxa_conversao = taxas.get(para_moeda)

            if taxa_conversao is None:
                # Se a moeda "PARA" (ex: "XYZ") não existir nas taxas retornadas
                return Response(
                    {"erro": f"A moeda de destino '{para_moeda}' não foi encontrada."},
                    status=status.HTTP_404_NOT_FOUND
                )

            resultado = valor * taxa_conversao

            # 4. Devolver a resposta final (sucesso!)
            dados_resposta = {
                'valor_original': valor,
                'moeda_origem': de_moeda,
                'moeda_destino': para_moeda,
                'taxa_utilizada': taxa_conversao,
                'resultado_conversao': round(resultado, 2) # Arredondamos para 2 casas decimais
            }
            
            # O DRF (Response) transforma nosso dicionário Python em JSON automaticamente.
            return Response(dados_resposta, status=status.HTTP_200_OK)

        except Exception as e:
            # Uma captura geral para qualquer outro erro inesperado (ex: sem internet)
            return Response(
                {"erro_geral": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )