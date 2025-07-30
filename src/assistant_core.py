import os
from dotenv import load_dotenv
import google.generativeai as genai
from config import GOOGLE_API_KEY

load_dotenv()

genai.configure(api_key=GOOGLE_API_KEY)
model_gemini = genai.GenerativeModel('gemini-2.0-flash')

def get_gemini_response(messages):
    try:
        response = model_gemini.generate_content(messages, request_options={'timeout': 120})
        if response and response.text:
            return response.text
        else:
            return "Não consegui gerar uma resposta para sua pergunta no momento. Tente reformular, por favor."
    except Exception as e:
        return f"Desculpe, houve um erro ao processar sua solicitação com Gemini: {e}"

def responder_pergunta_loja(pergunta_usuario, chat_history):
    system_prompt = """
    Você é a assistente virtual da **TrueTec**, uma empresa de tecnologia em Teresina, PI.
    Seu principal objetivo é auxiliar clientes na **abertura de chamados técnicos**, coletando todas as informações necessárias de forma conversacional, assim como um formulário.

    **Seu processo de coleta de informações para abertura de chamado deve seguir a seguinte ordem:**
    1.  **Nome da Empresa Solicitante**
    2.  **Tipo de Serviço/Produto TrueTec** que o cliente utiliza para o problema (Ex: Roteador TrueTec modelo X, Switch TrueTec modelo Y, Contrato de suporte técnico, etc.).
    3.  **Detalhes do Problema/Solicitação:** Peça uma descrição completa, incluindo o ponto de falha (Ex: internet não funciona, equipamento específico com defeito, etc.), mensagens de erro, e se já tentaram reiniciar equipamentos.
    4.  **Nome Completo do Solicitante**
    5.  **Telefone de Contato (com DDD e se tem WhatsApp)**
    6.  **E-mail de Contato**
    7.  **Detalhes Adicionais/Especificação do Problema:** Pergunte se há algo mais a acrescentar, como eventos recentes (ex: queda de energia) ou observações.

    **Regras Importantes:**
    * Seja sempre educado, prestativo e profissional.
    * **Faça UMA pergunta por vez** para coletar as informações, a menos que o usuário já forneça múltiplas informações de uma vez.
    * **Confirme as informações** que o usuário já forneceu antes de pedir a próxima.
    * Se o usuário desviar do assunto ou perguntar algo fora do escopo de abertura de chamados, redirecione-o gentilmente para o processo de coleta de informações ou diga que você pode ajudar com outros assuntos da TrueTec.
    * Ao final da coleta de todas as informações, **resuma os dados coletados** e **confirme que o chamado foi encaminhado**, informando que a equipe TrueTec entrará em contato.
    * Se o usuário perguntar sobre "imagens" ou "anexos", explique que no chat não é possível, mas que a equipe técnica poderá solicitá-las.

    **Informações da TrueTec (para contexto, não para ser dito diretamente a menos que perguntado):**
    - Localização: Teresina, PI
    - Serviços: Suporte técnico, soluções de rede, etc.
    - Contato: (86) 800-800-3200 (Ramal: 449)

    **Contexto da Conversa Atual:**
    """

    full_messages = [
        {"role": "user", "parts": [{"text": system_prompt}]}
    ]
    full_messages.extend(chat_history)
    full_messages.append({"role": "user", "parts": [{"text": pergunta_usuario}]})

    resposta_ia = get_gemini_response(full_messages)
    return resposta_ia

def iniciar_assistente():
    print("---")
    print("Olá! Bem-vindo(a) à TrueTec, sua assistente virtual aqui em Teresina.")
    print("Estou aqui para ajudar com suas dúvidas e na abertura de chamados técnicos.")
    print("Como posso ajudar hoje? (Digite 'sair' para encerrar a conversa)")
    print("---")

    conversation_history = []

    while True:
        pergunta = input("\nVocê: ")
        if pergunta.lower() == 'sair':
            print("---")
            print("Obrigado por entrar em contato com a TrueTec. Esperamos vê-lo(a) novamente!")
            print("---")
            break
        else:
            print("TrueTec Assistente (digitando...)", end='\r')
            resposta = responder_pergunta_loja(pergunta, conversation_history)
            print(f"TrueTec Assistente: {resposta}")

            conversation_history.append({"role": "user", "parts": [{"text": pergunta}]})
            conversation_history.append({"role": "model", "parts": [{"text": resposta}]})

if __name__ == "__main__":
    iniciar_assistente()