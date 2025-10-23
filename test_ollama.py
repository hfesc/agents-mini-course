import os
import urllib.error
import urllib.request
import json

# https://ollama.com/library
DEFAULT_MODEL = "gemma2:2b"
DEFAULT_OLLAMA_URL = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
OUTPUT_DIR = "out"


def check_ollama_available(url: str = DEFAULT_OLLAMA_URL) -> bool:
    """Check if Ollama is available at the specified URL."""
    try:
        with urllib.request.urlopen(f"{url}/api/tags", timeout=2) as response:
            return response.status == 200
    except (urllib.error.URLError, TimeoutError):
        return False


def model_exists(model: str) -> bool:
    """Verifica se o modelo já foi baixado."""
    try:
        with urllib.request.urlopen(f"{DEFAULT_OLLAMA_URL}/api/tags") as response:
            tags = json.loads(response.read().decode("utf-8"))
            return any(m["name"] == model for m in tags.get("models", []))
    except Exception:
        return False


def pull_model(model: str):
    """Baixa o modelo usando a API do Ollama."""
    print(f"⬇️ Baixando modelo '{model}' (isso pode levar alguns minutos)...")
    data = json.dumps({"name": model}).encode("utf-8")
    req = urllib.request.Request(
        f"{DEFAULT_OLLAMA_URL}/api/pull",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as response:
        for line in response:
            info = json.loads(line.decode("utf-8"))
            status = info.get("status") or info.get("error")
            if status:
                print("   ", status)
    print("✅ Download concluído!")


def run_ollama_test(model: str = DEFAULT_MODEL):
    """Envia uma requisição de teste ao modelo Ollama."""
    data = json.dumps({"model": model, "prompt": "Diga 'Olá Mundo'"}).encode("utf-8")
    req = urllib.request.Request(
        f"{DEFAULT_OLLAMA_URL}/api/generate",
        data=data,
        headers={"Content-Type": "application/json"},
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            for line in response:
                decoded = json.loads(line.decode("utf-8"))
                if "response" in decoded:
                    print("🧠 Resposta do modelo:", decoded["response"].strip())
                    break
    except Exception as e:
        print(f"❌ Erro ao executar requisição: {e}")


def main():

    print(f"🔍 Verificando Ollama em: {DEFAULT_OLLAMA_URL}")
    if not check_ollama_available(DEFAULT_OLLAMA_URL):
        print("❌ Ollama não está disponível no URL especificado.")
        return
    print("✅ Ollama está disponível!")

    if not model_exists(DEFAULT_MODEL):
        pull_model(DEFAULT_MODEL)
        print(f"✅ Modelo '{DEFAULT_MODEL}' baixado com sucesso!")
    else:
        print(f"✅ Modelo '{DEFAULT_MODEL}' já disponível localmente!")

    print(f"\n🚀 Testando modelo: {DEFAULT_MODEL}")
    run_ollama_test(DEFAULT_MODEL)


if __name__ == "__main__":
    main()
