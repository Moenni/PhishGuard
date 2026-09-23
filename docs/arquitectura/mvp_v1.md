# MVP 1.0 - PhishGuard
 
## Objetivo
 
Construir una primera versión funcional capaz de analizar correos electrónicos y detectar indicadores básicos de phishing.
 
---
 
## Alcance
 
La versión MVP será capaz de:
 
- Leer archivos .eml
- Extraer URLs
- Analizar dominios
- Aplicar reglas heurísticas
- Calcular un score de riesgo
- Clasificar el correo
- Generar un reporte JSON
 
---
 
## Flujo
 
Correo .eml
│
▼
Parser
│
▼
Extracción de URLs
│
▼
Análisis de Dominio
│
▼
Sistema de Reglas
│
▼
Scoring Engine
│
▼
Clasificación
│
▼
Reporte JSON
 
---
 
## Salida Esperada
 
{
"score": 75,
"classification": "Probable Phishing",
"findings": [
"Dominio sospechoso",
"SSL inválido",
"Palabra clave detectada"
]
}
`
MVP 1.0 - PhishGuard
Objetivo
Construir una primera versión funcional capaz de analizar correos electrónicos y detectar indicadores básicos de phishing.

Alcance
La versión MVP será capaz de:

Leer archivos .eml
Extraer URLs
Analizar dominios
Aplicar reglas heurísticas
Calcular un score de riesgo
Clasificar el correo
Generar un reporte JSON
Flujo
Correo .eml │ ▼ Parser │ ▼ Extracción de URLs │ ▼ Análisis de Dominio │ ▼ Sistema de Reglas │ ▼ Scoring Engine │ ▼ Clasificación │ ▼ Reporte JSON

Salida Esperada
{ "score": 75, "classification": "Probable Phishing", "findings": [ "Dominio sospechoso", "SSL inválido", "Palabra clave detectada" ] } `