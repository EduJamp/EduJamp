import datetime

# Leer la lista de chistes
with open("jokes.txt", "r", encoding="utf-8") as f:
    jokes = [line.strip() for line in f if line.strip()]

if jokes:
    # Selecciona un chiste secuencial basado en el día actual del año (1 al 365)
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    index = day_of_year % len(jokes)
    selected_joke = jokes[index]
else:
    selected_joke = "¡Programando código limpio hoy!"

# Leer el README actual
with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()

# Marcadores de la sección del chiste
start_marker = "<!--START_SECTION:joke-->"
end_marker = "<!--END_SECTION:joke-->"

new_joke_section = f"{start_marker}\n💡 **Chiste del día:** *{selected_joke}*\n{end_marker}"

# Reemplazar la sección en el README
if start_marker in readme_content and end_marker in readme_content:
    start_idx = readme_content.find(start_marker)
    end_idx = readme_content.find(end_marker) + len(end_marker)
    updated_readme = readme_content[:start_idx] + new_joke_section + readme_content[end_idx:]
else:
    updated_readme = readme_content + "\n\n" + new_joke_section

# Guardar los cambios
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_readme)
