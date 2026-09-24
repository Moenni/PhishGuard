from bs4 import BeautifulSoup
import re


def extraer_urls(contenido):

    urls = []

    soup = BeautifulSoup(contenido, "html.parser")

    for enlace in soup.find_all("a"):
        href = enlace.get("href")

        if href:
            urls.append(href)

    if not urls:
        patron = r'https?://[^\s"<>\']+'
        urls = re.findall(patron, contenido)

    return urls
# Ejemplo de uso
html = """
<a href="https://fake-login-security.com">
Verificar cuenta
</a>
"""

print(extraer_urls(html))