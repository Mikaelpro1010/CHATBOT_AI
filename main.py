import google.generativeai as genai

# Configurando a chave de API
genai.configure(api_key="AIzaSyArPQMjVASSz6kCTJYJ3HN807Kt3vhdrm8")

# Configurando as opções de geração
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

# Configurando as configurações de segurança
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

# Inicializando o modelo
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Iniciando a conversa
convo = model.start_chat(history=[])

# Função para iniciar o chat
def start_chat():
    while True:
        # Obtendo a entrada do usuário
        user_input = input("Você: ")

        # Verificando se o usuário deseja sair
        if user_input.lower() == "exit":
            print("Chat finalizado.")
            break

        # Enviando a entrada do usuário para o chatbot
        convo.send_message(user_input)

        # Obtendo e exibindo a resposta do chatbot
        print("Chatbot:", convo.last.text)

# Iniciando o chat
start_chat()