# Vacinação Rotas


||
|---|---|
| Utiliza **SQLAlchemy**, **Dataclass**, **Blueprint**, **Migrations** e **Padrão Flask Factory** corretamente. ||
| [POST] **/vaccinations**. Ao fazer requisição nessa rota passando os dados corretos retorna o status code **201** (**CREATED**) e faz a inserção dos dados normalizados no banco de dados. | 1 |
| [POST] **/vaccination**. Ao fazer requisição nessa rota passando uma **string** com mais de 11 characters para a chave 'cpf', retorna o status code **400** (**BAD REQUEST**) com uma mensagem de erro | |
| [POST] **/vaccination**. Ao fazer a requisição nessa rota com o valor de qualquer uma das chaves sendo diferente de **string**, retorna o status code **400** (**BAD REQUEST**)) com uma mensagem de erro  | |
| [POST] **/vaccination**. Ao fazer a requisição nessa rota faltando qualquer uma das chaves (**cpf**, **name**, **health_unit_name** e **vaccine_name**), retorna o status code **400** (**BAD REQUEST**) com uma mensagem de erro | |
| [POST] **/vaccination**. Ao fazer a requisição nessa rota passando um **CPF** que já exista no banco de dados,retorna o status code **409** (**CONFLICT**) com uma mensagem de erro| |
| [POST] **/vaccinations**. Ao fazer requisição nessa rota passando uma chave a mais, retorna o status code **201** (**CREATED**) e faz a criação corretamente ignorando a chave passada. | |
| [GET] **/vaccinations**. retorna todas as vacinas registradas no banco de dados, status code **200** (**OK**) | |
