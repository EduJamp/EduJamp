import datetime

# Leer los chistes
try:
    with open("jokes.txt", "r", encoding="utf-8") as f:
        jokes = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    jokes = ["¡Programando con energía!"]

# Leer las frases motivadoras
try:
    with open("quotes.txt", "r", encoding="utf-8") as f:
        quotes = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    quotes = ["El código limpio es arte en movimiento."]

# Usar el día del año para rotar de forma ordenada sin repetir
day_of_year = datetime.datetime.now().timetuple().tm_yday

selected_joke = jokes[day_of_year % len(jokes)] if jokes else "¡Día de código!"
selected_quote = quotes[day_of_year % len(quotes)] if quotes else "Sigue construyendo el futuro."

# Leer el README actual
with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()

# 1. Actualizar sección del chiste
start_joke = "<!--START_SECTION:joke-->"
end_joke = "<!--END_SECTION:joke-->"
joke_section = f"{start_joke}\n💡 **Chiste del día:** *{selected_joke}*\n{end_joke}"

if start_joke in readme_content and end_joke in readme_content:
    s_idx = readme_content.find(start_joke)
    e_idx = readme_content.find(end_joke) + len(end_joke)
    readme_content = readme_content[:s_idx] + joke_section + readme_content[e_idx:]
else:
    readme_content += "\n\n" + joke_section

# 2. Actualizar sección de la frase motivadora
start_quote = "<!--START_SECTION:quote-->"
end_quote = "<!--END_SECTION:quote-->"
quote_section = f"{start_quote}\n🚀 **Frase motivadora:** *{selected_quote}*\n{end_quote}"

if start_quote in readme_content and end_quote in readme_content:
    s_idx = readme_content.find(start_quote)
    e_idx = readme_content.find(end_quote) + len(end_quote)
    readme_content = readme_content[:s_idx] + quote_section + readme_content[e_idx:]
else:
    readme_content += "\n\n" + quote_section

# Guardar los cambios en el README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
