## **Table of Contents**
- [E6 - Komercio Local](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_02_komercio-local.html&ref=master#mcetoc_1esj4slvm0) 
  - [Objetivo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_02_komercio-local.html&ref=master#mcetoc_1f362b6b10)
  - [Preparativos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_02_komercio-local.html&ref=master#mcetoc_1f362b6b11)
  - [Sistema de Komercio Local](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_02_komercio-local.html&ref=master#mcetoc_1eg6l938o6l)
- [Entregáveis](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_02_komercio-local.html&ref=master#mcetoc_1f362b6b12) 
  - [Repositório](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_02_komercio-local.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2a_e_02_komercio-local.html&ref=master#mcetoc_1eh146n6m3)
# **E6 - Komercio Local**
Para essa entrega você criará um sistema para uma loja de produtos diversos que irá listar produtos com paginação e retornar um produto específico.
## **Objetivo**
Essa atividade foi elaborada para trabalhar seus conhecimentos de montagem de requisição e obtenção de dados da requisição na rota.
## **Preparativos**
Você deve criar um arquivo chamado komercio.py, onde utilizará [este snippet](https://gitlab.com/-/snippets/2118021) para transferir os produtos em uma lista nesse arquivo denominada lista\_de\_produtos.

Além disso, crie também o arquivo app.py, onde será feita a aplicação back-end.
## **Sistema de Komercio Local**
Defina as seguintes Rotas na sua aplicação

- **Listagem de produtos** 
  - **Caminho da Rota:** /products
  - **Query Param:** page=<numero da página>&per\_page=<quantidade de produtos por página>
  - **Assinatura da função:** list\_products()
  - **Procedimento:** Listar todos os produtos da lista lista\_de\_produtos com paginação de acordo com os parâmetros em formato **query params** recebidos
- **Obtenção de produto** 
  - **Caminho da Rota:** /products/<product\_id>
  - **Assinatura da função:** get\_product()
  - **Procedimento:** Retornar o produto com **id idêntico** a string param product\_id
-----
# **Entregáveis**
## **Repositório**
- Link do **repositório** do **GitLab**
- **Código fonte:** 
  - arquivo **komercio.py**.
  - arquivo **app.py** com os endpoints
- **Privacidade** 
  - Incluir **ka-br-out-2020-correcoes** como reporter.
-----
# **Critérios de aceitação**

|**pts**|**Dado**|**Quando**|**É esperado**|
| :-: | :-: | :-: | :-: |
|5|rota **/products**|enviado requisição|Resposta contendo os produtos em formato lista de objetos JSON de acordo com a paginação solicitada|
|5|rota **/products/<product\_id>**|Executada a função|Resposta contendo o produto em formato de objeto JSON de acordo com a string param da requisição|
**Boa diversão, devs!** 👾


