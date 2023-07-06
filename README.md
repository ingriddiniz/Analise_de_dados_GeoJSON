# Analise de Dados do Metro do Porto (GeoJSON)
Este é um projeto da cadeira de Programação 2 proposto pela Faculdade de Ciências da Universidade do Porto, cujo objetivo é a análise de dados do metro do porto e criar um ficheiro no formato GeoJSON.

Para este projeto, foi considerado um dataset com informação sobre a rede de Metro do Porto, disponibilizada abertamente [neste link](https://opendata.porto.digital/ne/dataset/horarios-paragens-e-rotas-em-formato-gtfs), e com uma cópia dos ficheiros mais relevantes na pasta [metro](metro).

## Objetivo

A tarefa proposta consiste em gerar um arquivo GeoJSON que represente geograficamente as linhas e estações do Metro do Porto, facilitando a visualização dos dados. O  [GeoJSON](https://geojson.org/) é um formato válido de JSON que segue uma estrutura específica para representar marcadores geográficos e seus metadados associados. Um exemplo básico de um ponto em GeoJSON é:
```python
{
    "type": "FeatureCollection", 
    "features": [
        {
            "geometry": {
                "type": "Point", 
                "coordinates": [
                    float com valor de longitude, 
                    float com valor de latitude
                ]
            }, 
            "type": "Feature", 
            "properties": um dicionário com a meta-informação associada ao ponto geográfico
            }
        }]
}
```
  
## Passos do Projeto
  
1. Ler cada arquivo do conjunto de dados para um DataFrame separado e combinar os dados em um único DataFrame.
2. Representar cada estação como um ponto no mapa, com propriedades adicionais, como o nome da estação.
3. Representar cada linha de metrô como um conjunto de segmentos de reta no mapa, considerando que o caminho entre duas estações é uma reta. A cor do segmento foi ajustada para ser consistente com a cor do nome da linha de metrô correspondente.
4. Após a representação das estações e linhas, os dados foram convertidos em formato GeoJSON e um arquivo chamado metro.geojson foi gerado. Esse arquivo contém todas as informações necessárias para visualizar o Metro do Porto em um mapa interativo.
  
## Utilização e Visualização
  
O arquivo metro.geojson pode ser facilmente visualizado em plataformas de visualização de mapas, como o <https://geojson.io/>. Basta importar o arquivo para a plataforma e explorar as estações e linhas do Metro do Porto de forma interativa.
