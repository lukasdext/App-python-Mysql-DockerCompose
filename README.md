# App-python-Mysql-DockerCompose

Criar um ambiente local com Docker Compose que roda uma aplicação Python que se conecta a um banco de dados de sua escolha, colea a strin que informação e a retorna via request HTTP. Todos os elementos devem ser deployados em containeres.

Requisitos:

Todos os recursos devem ser geridos no próprio código
É esperado que a imagem do container aplicação Python seja construída por você ao invés de utilizar imagens prontas (como do Docker Hub). Entretando, a imagem do container que você irá construir, poderá utilizar imagens pré-existentes como base sem problemas (FROM no Dockerfile) 
Para os demais pontos da infraestrutura (DB, Proxy), você pode usar imagens prontas
A solução deve ser simples. Aplique boas práticas onde achar cabível!
