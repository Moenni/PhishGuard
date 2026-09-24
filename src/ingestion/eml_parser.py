from email.parser import BytesParser
from email import policy
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from analysis.url_extractor import extraer_urls
from detection.scoring_engine import (
    calcular_score,
    clasificar
)


def cargar_eml(ruta_archivo):
    with open(ruta_archivo, "rb") as archivo:
        mensaje = BytesParser(
            policy=policy.default
        ).parse(archivo)

    return {
        "subject": mensaje["subject"],
        "sender": mensaje["from"],
        "body": mensaje.get_body(
            preferencelist=("plain")
        ).get_content()
    }


if __name__ == "__main__":

    correo = cargar_eml("datasets/test.eml")

    print("Asunto:", correo["subject"])
    print("Remitente:", correo["sender"])
    print("Cuerpo:", correo["body"])

    urls = extraer_urls(correo["body"])

    score, hallazgos = calcular_score(urls)

    clasificacion = clasificar(score)

    print("\nURLs encontradas:")
    print(urls)

    print("\nScore:")
    print(score)

    print("\nClasificación:")
    print(clasificacion)

    print("\nHallazgos:")

    for hallazgo in hallazgos:
        print("-", hallazgo)