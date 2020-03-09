# Teste Técnico DataSprints - NYC Taxi Trips

## Pré-requisitos do ambiente
- [Python 3](https://www.python.org/downloads/)
- [Jupyter](https://jupyter.org/install)
- [MariaDB 10.4](https://mariadb.org/download/) (ou [MySQL 5.7](https://dev.mysql.com/downloads/mysql/5.7.html))

O ambiente usado foi o WSL/Ubuntu. O script deve ser compatível com qualquer distro de Linux, mas possivelmente não com Windows.

É necessário instalar as dependências usando:
```
pip3 install -r requirements.txt
```

## Carregando os dados
O código está divido em duas partes, um script e um notebook Jupyter. Primeiramente deve ser executado o script `src/load_data.py`, que fará o tratamento necessário e carregará os dados no banco. Aqui assumi que o banco está no localhost, e s usuário root e sem senha.

```
python3 src/load_data.py
```

## Analisando os dados
As análises por sua vez estão em um notebook Jupyter. 

```
jupyter notebook analises
```
Após abrir a página do Jupyter deve-se abrir o notebook nyctaxi_analise.

O código necessário para gerar os resultados está no próprio notebook, e pode ser executado célula a célula com <kbd>Shift</kbd>+<kbd>Enter</kbd>, ou todo de uma vez pelo menu Cell -> Run All.

## Exportando o resultado
O notebook com os resultados pode ser exportado para HTML:
```
jupyter nbconvert analises/nyctaxi_analise.ipynb --to html --output Análise.html
```