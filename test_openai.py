from dotenv import load_dotenv
import os
from openai import OpenAI

# Carrega as variáveis do .env
load_dotenv()

# Lê as credenciais
api_key = os.getenv("OPENAI_API_KEY")
org_id = os.getenv("OPENAI_ORG_ID")
project_id = os.getenv("OPENAI_PROJECT_ID")

print("✅ Testando variáveis de ambiente...")
print(f"API Key encontrada: {'OK' if api_key else 'FALHOU'}")
print(f"Organization ID: {'OK' if org_id else 'FALHOU'}")
print(f"Project ID: {'OK' if project_id else 'FALHOU'}")

# Testa uma chamada simples à API
if api_key:
    client = OpenAI(api_key=api_key, organization=org_id, project=project_id)
    print("\n🚀 Enviando requisição de teste...")
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Diga 'Olá Mundo'"}],
    )
    print("Resposta da API:", completion.choices[0].message.content)
else:
    print("\n❌ Falha: variável OPENAI_API_KEY não encontrada no .env")
