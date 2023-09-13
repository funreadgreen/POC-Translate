from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from googletrans import Translator
from django.http import JsonResponse
import os
from gtts import gTTS
import pygame

# Traductor
@api_view(['GET'])
def google_translate(request):
    text_to_translate = request.GET.get(
        'text', 'Para habilitar la traducción de voz en una aplicación Django, necesitarás incorporar tecnologías de reconocimiento de voz y síntesis de voz además de la traducción de texto. A continuación, te proporciono un enfoque general sobre cómo puedes lograr esto, pero ten en cuenta que es un proceso más complejo que la traducción de texto escrito y requerirá la integración de múltiples servicios y bibliotecas.')
    target_language = request.GET.get('target_language', 'en')
    
    # Traducir el texto
    translator = Translator()
    translation = translator.translate(text_to_translate, dest=target_language)
    translated_text = translation.text
    
    return JsonResponse({'translated_text': translated_text})

#Leer texto
@api_view(['GET'])
def text_to_speech(request):
    text_to_speak = request.GET.get(
        'text', 'Para habilitar la traducción de voz en una aplicación Django, necesitarás incorporar tecnologías de reconocimiento de voz y síntesis de voz además de la traducción de texto. A continuación, te proporciono un enfoque general sobre cómo puedes lograr esto, pero ten en cuenta que es un proceso más complejo que la traducción de texto escrito y requerirá la integración de múltiples servicios y bibliotecas.')
    target_language = request.GET.get('target_language', 'es')
    
    # Generar voz a partir del texto original
    tts = gTTS(text_to_speak, lang=target_language)
    
    # Crear una carpeta para almacenar archivos de audio si no existe
    audio_folder = 'audio_folder'  # Nombre de la carpeta donde se guardarán los archivos de audio
    if not os.path.exists(audio_folder):
        os.mkdir(audio_folder)
    
    # Guardar el audio en un archivo en la carpeta
    audio_file = os.path.join(audio_folder, 'text_to_speech_audio.mp3')
    tts.save(audio_file)
    
    # Reproducir el audio usando pygame (opcional)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    
    return JsonResponse({'text_to_speech_audio_url': audio_file})