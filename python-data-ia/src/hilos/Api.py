import requests

import urllib


api_URL = "https://www.mapquestapi.com/directions/v2/route?"
api_KEY = "zhMfhlEN9LthjkniYUAaWaQLiN261cO7"

while True:
    origen = input("Dame Origen: ")
    if origen=="out":
        break
    destino = input("Dame Destino: ")
    if destino =="out":
        break



    url = api_URL + urllib.parse.urlencode({"key":api_KEY,"from":origen,"to":destino})

    json_dta = requests.get(url).json()

    estado_peticion = json_dta["info"]["statuscode"]
    if estado_peticion == 0:
        print(f"Ruta Localizada{origen}-{destino}")
        duracion = json_dta["route"]["formattedTime"]
        print(f"Duracion del viaje: {duracion}")
        distancia = json_dta["route"]["distance"]
        print(f"Distancia del viaje:{distancia}")

        distancia = distancia * 1.61

        print(f"Distancia del viaje en km: " + str("{:.2f}".format(distancia)))

        for each in json_dta["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"])
    else:
        print("Ruta Errónea")


