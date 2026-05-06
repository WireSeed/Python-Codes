from urllib.parse import quote

texto = " Texto a convertir a URL "
url_segura = quote(texto)

print(url_segura)
