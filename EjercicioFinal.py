import openai

openai.api_key = ""
system_rol = """Has de cuenta que eres un analizador de sentimientos.
                Yo te paso sentimientos y tu analizas los sentimientos de los mensajes
                y me das una respuesta con al menos 1 caractery como maximo 4 caracteres
                SOLO RESPUESTAS NUMERICAS, donde -1 es negatividad maxima, 0 es neutral y 1 es positividad maxima.
                (Puedes responder solo con ints o floats)"""

mensajes = [{'role': 'system', 'content': system_rol}]

#terminar script












































# from textblob import TextBlob

# class AnalizadorDeSentimientos:
#     def analizar_sentimiento(self, texto):
#         analisis = TextBlob(texto)
#         if analisis.sentiment.polarity > 0:
#             return 'Positivo'
#         elif analisis.sentiment.polarity == 0:
#             return 'Neutral'
#         else:
#             return 'Negativo'
        
        
# analizador = AnalizadorDeSentimientos()
# resultado = analizador.analizar_sentimiento('this is funny ')  # solo funciona en ingles 
# print(resultado)