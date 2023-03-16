
# Dada una URL con parámetros, crea una función que obtenga sus valores.
# No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.

# Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
# los parámetros serían ["2023", "0"]
 

def get_params(url):
    url_params = url[url.index("?")+1::]
    url_params = url_params.split("&")
    url_params = [param.split("=") for param in url_params]
    return [param[1] for param in url_params]


url = "https://www.mercadolibre.com.co/ventas/omni/listado?startPeriod=WITH_DATE_CLOSED_6M_OLD&sort=DATE_CLOSED_DESC#menu-user"
print(get_params(url))
