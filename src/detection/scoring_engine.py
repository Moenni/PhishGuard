def calcular_score(urls):

    score = 0

    palabras_sospechosas = [
        "login",
        "verify",
        "security",
        "account",
        "update",
        "password"
    ]

    hallazgos = []

    for url in urls:

        for palabra in palabras_sospechosas:

            if palabra in url.lower():

                score += 10

                hallazgos.append(
                    f"Palabra sospechosa detectada: {palabra}"
                )

    return score, hallazgos

def clasificar(score):

    if score < 30:
        return "Seguro"

    elif score < 60:
        return "Sospechoso"

    return "Probable Phishing"

if __name__ == "__main__":

    urls = [
        "https://fake-login-security.com"
    ]

    score, hallazgos = calcular_score(urls)

    clasificacion = clasificar(score)

    print("Score:", score)
    print("Clasificación:", clasificacion)

    print("\nHallazgos:")

    for hallazgo in hallazgos:
        print("-", hallazgo)