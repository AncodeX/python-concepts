"""
Lea la API de gatos y cats_api = ' https://api.thecatapi.com/v1/breeds ' y busque:
    - el mínimo, máximo, media, mediana, desviación estándar del peso de los gatos en unidades métricas.
    - el mínimo, máximo, media, mediana, desviación estándar de la vida útil de los gatos en años.
"""
import requests, statistics


def weight_lifespan():
    api_response = requests.api.get("https://api.thecatapi.com/v1/breeds")
    content_api = api_response.json()
    weight = []
    life_span = []

    for i in content_api:
        weight_range = i["weight"]["metric"].replace("-", "").split()
        lifespan_range = i["life_span"].replace("-", "").split()

        weight_int = list(map(lambda x: int(x), weight_range))
        lifespan_int = list(map(lambda x: int(x), lifespan_range))

        weight_data = sum(weight_int)/2
        weight.append(weight_data)

        lifespan_data = sum(lifespan_int)/2
        life_span.append(lifespan_data)
    
    # min del peso de los gatos
    min_weight = min(weight)
    # max del peso de los gatos
    max_weight = max(weight)
    # media del peso de los gatos
    mean_weight = statistics.mean(weight)
    # mediana del peso de los gatos
    median_weight = statistics.median(weight)
    # desviacion estandar del peso de los gatos
    stdev_weight = statistics.stdev(weight)

    # min de la vida util de los gatos
    min_life_span = min(life_span)
    # max de la vida util de los gatos
    max_life_span = max(life_span)
    # media de la vida util de los gatos
    mean_life_span = statistics.mean(life_span)
    # mediana de la vida util de los gatos
    median_life_span = statistics.median(life_span)
    # desviacion estandar de la vida util de los gatos
    stdev_life_span = statistics.stdev(life_span)

    lsp = [min_life_span, max_life_span, mean_life_span, median_life_span, stdev_life_span]
    w = [min_weight, max_weight, mean_weight, median_weight, stdev_weight]

    return lsp, w

if __name__ == "__main__":
    life_span, weight = weight_lifespan()
    print(f"Vida util de los gatos\n- min: {life_span[0]}\n- max: {life_span[1]}\n- media: {life_span[2]}\n- mediana: {life_span[3]}\n- desviacion estandar: {life_span[4]}")

    print(f"Peso de los gatos\n- min: {weight[0]}\n- max: {weight[1]}\n- media: {weight[2]}\n- mediana: {weight[3]}\n- desviacion estandar: {weight[4]}")