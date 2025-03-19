import json
import requests
import os
from dotenv import load_dotenv

# Carregando as variáveis de ambiente
load_dotenv()

def fazer_requisicao_api(url, param)