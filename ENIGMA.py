import telebot

CHAVE_API = "my token"

bot = telebot.TeleBot(CHAVE_API)

    ##Opção 1.1

@bot.message_handler(commands=["Enigma_free"])
def Enigma_free(mensagem):
    bot.send_message(mensagem.chat.id, "https://play.google.com/store/apps/details?id=br.com.well.enigma")

@bot.message_handler(commands=["Enigma_Pro"])
def Enigma_Pro(mensagem):
    bot.send_message(mensagem.chat.id, "https://play.google.com/store/apps/details?id=br.com.well.enigmapro")

@bot.message_handler(commands=["Soteador"])
def Soteador(mensagem):
    bot.send_message(mensagem.chat.id, "https://play.google.com/store/apps/details?id=br.com.well.sortear")
    
@bot.message_handler(commands=["Testa_porta"])
def Testa_porta(mensagem):
    bot.send_message(mensagem.chat.id, "https://play.google.com/store/apps/details?id=br.com.well.testaporta")
    
@bot.message_handler(commands=["Teste_SMTP"])
def Teste_SMTP(mensagem):
    bot.send_message(mensagem.chat.id, "https://play.google.com/store/apps/details?id=br.com.well.testesmtp")
    
@bot.message_handler(commands=["Soteador_Pro"])
def Soteador_Pro(mensagem):
    bot.send_message(mensagem.chat.id, "https://play.google.com/store/apps/details?id=br.com.well.sortearpro")
    
@bot.message_handler(commands=["Tia_Francy_Kids"])
def Tia_Francy_Kids(mensagem):
    bot.send_message(mensagem.chat.id, "https://play.google.com/store/apps/details?id=kids.francy.tia.com.br.tiafrancykids")

@bot.message_handler(commands=["IMC_Peso_Ideal"])
def IMC_Peso_Ideal(mensagem):
    bot.send_message(mensagem.chat.id, "https://play.google.com/store/apps/details?id=imc.maxwellfreire.aplicativo.br.imc")

@bot.message_handler(commands=["MaxPlay"])
def MaxPlay(mensagem):
    bot.send_message(mensagem.chat.id, "https://play.google.com/store/apps/details?id=br.com.well.musicas")

@bot.message_handler(commands=["TimeFly"])
def TimeFly(mensagem):
    bot.send_message(mensagem.chat.id, "https://play.google.com/store/apps/details?id=br.com.well.timefly")       

    ## Opcção 1.0
    
@bot.message_handler(commands=["op1"])
def op1(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
    /Enigma_free
    /Enigma_Pro
    /MaxPlay
    /TimeFly
    /Soteador
    /Testa_porta
    /Teste_SMTP
    /Soteador_Pro
    /Tia_Francy_Kids
    /IMC_Peso_Ideal
    """
    bot.send_message(mensagem.chat.id, texto)

    ## Opcção 2.0

@bot.message_handler(commands=["op2"])
def op2(mensagem):
    bot.send_message(mensagem.chat.id, "Nunca foi tão fácil de enviar uma reclamação, mande um e-mail para maxwellplayaplicativos@gmail.com")


@bot.message_handler(commands=["op3"])
def op5(mensagem):
    bot.send_message(mensagem.chat.id, "https://www.mediafire.com/file/ontevckvnth2qkc/Pack_papeis_de_parede%2528Enigma%25F0%259F%25A7%2599%25F0%259F%258F%25BC%25E2%2580%258D%25E2%2599%2582%25EF%25B8%258F%2529.rar/file")

@bot.message_handler(commands=["rsocial"])
def rsocial(mensagem):
    bot.send_message(mensagem.chat.id,"https://bit.ly/MaxwellPlay")
    
@bot.message_handler(commands=["Consulta"])
def Consulta(mensagem):
    bot.send_message(mensagem.chat.id, "Lista de bot para #consulta de dados: @buscacpfbot @MkBuscaBot @LoPeliosso_bot @ConsultasPlusBot @ArcadianRobot @Skynet02Robot Consulta via Web: https://www.techbusca.org/ Busca por nome de usuário: @maigret_osint_bot Atualizado: 06/10/2022 Canal Telegram: https://t.me/+eQ2Kz6LP_tc1NGYx")

    ## Configuração inicial

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
   Saiba mais sobre o bot: https://Jetronix.tk/bot 🤖
    Escolha uma opção para continuar (Clique no item):
     /op1 Apps do Max
     /Consulta
     /op2 Reclamar de um app
     /op3 Baixar papeis de parede Enigma
     /rsocial Redes sociais do Max
     """
    bot.reply_to(mensagem, texto)

bot.polling()
