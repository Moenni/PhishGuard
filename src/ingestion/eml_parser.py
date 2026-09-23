from email import policy
from email.parser import BytesParser


def cargar_eml(ruta_archivo):
    with open(ruta_archivo, "rb") as archivo:
        mensaje = BytesParser(policy=policy.default).parse(archivo)

    return {
        "subject": mensaje["subject"],
        "sender": mensaje["from"],
        "body": mensaje.get_body(preferencelist=("plain")).get_content()
    }


if __name__ == "__main__":
    correo = cargar_eml("datasets/test.eml")

    print("Asunto:", correo["subject"])
    print("Remitente:", correo["sender"])
    print("Cuerpo:", correo["body"])