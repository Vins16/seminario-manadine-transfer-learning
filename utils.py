"""Funciones auxiliares del seminario (las mismas que se construyen en los notebooks 1 y 3)."""
import re
import unicodedata

from stop_words import get_stop_words


def quitar_tildes(texto):
    """Elimina tildes y diéresis: 'canción' se convierte en 'cancion'."""
    texto = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in texto if not unicodedata.combining(c))


STOPWORDS_ES = {quitar_tildes(p) for p in get_stop_words("spanish")}


def preprocesar(texto):
    """Normalización para modelos clásicos (TF-IDF): minúsculas, sin tildes,
    solo letras y sin palabras vacías ni palabras muy cortas."""
    texto = quitar_tildes(texto.lower())
    texto = re.sub(r"[^a-z\s]", " ", texto)
    tokens = [t for t in texto.split() if t not in STOPWORDS_ES and len(t) > 2]
    return " ".join(tokens)


def proporcion_mayusculas(texto):
    """Devuelve la proporción de letras en mayúscula de un texto (entre 0 y 1)."""
    letras = [c for c in texto if c.isalpha()]
    if len(letras) == 0:
        return 0
    return sum(c.isupper() for c in letras) / len(letras)
