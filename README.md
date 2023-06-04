# api-diabetes-tc2

Api criada utilizando Python e FastAPI para desenvolvimento e validação do TCII

## Executando o Projeto

- Crie o ambiente virtual, ative e instale as bibliotecas listadas no requirements.txt
- Execute ```uvicorn app.main:app --reload``` para executar o projeto
- Acesse ```http://127.0.0.1:8000/docs``` para visualizar a documentação e mais informações sobre os endpoints

### As seguintes variáveis devem ser configuradas

```secret
DATABASE_URL="postgresql://user:password@url:port/database"
SECRET_KEY="another-secret-key"
FIRST_SUPERUSER="first-email@email.com"
FIRST_SUPERUSER_PASSWORD="first-pass"
```

### Se desejar subir uma base postgresql com o docker

```shell
docker run -d \
 --name postgresql \
 -e POSTGRES_PASSWORD=admin \
 -e POSTGRES_USER=admin \
 -e POSTGRES_DB=application \
 -e PGDATA=/var/lib/postgresql/data/pgdata \
 -v /custom/mount:/var/lib/postgresql/data \
 postgres
```
