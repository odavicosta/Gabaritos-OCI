import ctypes
from ctypes import c_int, c_char_p, c_char, POINTER, Structure
import os
from django.conf import settings

# Caminho absoluto para a pasta libs dentro do gabarito_oci
#LIB_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'libs'))



LIB_DIR = os.path.join(settings.BASE_DIR, 'libs')


# Primeiro carrega a dependência
raylib_path = os.path.join(LIB_DIR, 'libraylib.so.550')
ctypes.CDLL(raylib_path)

# Depois carrega sua lib principal
lib_path = os.path.join(LIB_DIR, 'libleitor.so')
lib = ctypes.CDLL(lib_path)



# Define a struct Reading como no header C
class Reading(Structure):
    _fields_ = [
        ("erro", c_int),
        ("id_prova", c_int),
        ("id_participante", c_int),
        ("leitura", c_char_p)
    ]

# Configurar o retorno e os tipos de argumentos das funções
lib.read_image_path.argtypes = [c_char_p]
lib.read_image_path.restype = Reading

lib.read_image_data.argtypes = [c_char_p, POINTER(c_char), c_int]
lib.read_image_data.restype = Reading


def ler_prova_por_dados(tipo_arquivo, dados_bytes):
    tipo_bytes = tipo_arquivo.encode('utf-8')
    dados = (c_char * len(dados_bytes))(*dados_bytes)
    resultado = lib.read_image_data(tipo_bytes, dados, len(dados_bytes))
    return {
        "erro": resultado.erro,
        "id_prova": resultado.id_prova,
        "id_participante": resultado.id_participante,
        "leitura": resultado.leitura.decode('utf-8') if resultado.leitura else None
    }
