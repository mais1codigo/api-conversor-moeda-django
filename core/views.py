from django.shortcuts import render

# core/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests 
class CurrencyConverterView(APIView):
    """
    Uma View de API para converter moedas.
    Espera parâmetros na URL: ?de=USD&para=BRL&valor=10
    """

    def get(self, request):
        try:
            de_moeda = request.query_params.get('de').upper()
            para_moeda = request.query_params.get('para').upper()
            valor = float(request.query_params.get('valor'))
        except Exception as e:
        
            return Response(
                {"erro": "Parâmetros inválidos. Use ?de=MOEDA&para=MOEDA&valor=NUMERO"},
                status=status.HTTP_400_BAD_REQUEST
            )


        try:
            url_api_externa = f"https://open.er-api.com/v6/latest/{de_moeda}"
            resposta_api = requests.get(url_api_externa)
            
            
            if resposta_api.status_code != 200:
                return Response(
                    {"erro": "Não foi possível obter as taxas de câmbio para a moeda base."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            dados = resposta_api.json()
            taxas = dados.get('rates')

           
            taxa_conversao = taxas.get(para_moeda)

            if taxa_conversao is None:
                
                return Response(
                    {"erro": f"A moeda de destino '{para_moeda}' não foi encontrada."},
                    status=status.HTTP_404_NOT_FOUND
                )

            resultado = valor * taxa_conversao

           
            dados_resposta = {
                'valor_original': valor,
                'moeda_origem': de_moeda,
                'moeda_destino': para_moeda,
                'taxa_utilizada': taxa_conversao,
                'resultado_conversao': round(resultado, 2) 
            }
            
           
            return Response(dados_resposta, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"erro_geral": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )