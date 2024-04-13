## RESTful API Python(FastAPI) e MySQL
Meu primeiro projeto basico em Python, usando FastAPI e conexao com banco de dados MySQL (Workbench).

No momento estou seguindo o padrão de arquitetura que usava nos meus projetos Java, tentando aplicar conceitos de POO (Programação Orientada a Objetos) e Arquitetura Limpa.

Este repositório esta organizado em:

- `Repository`: Métodos responsáveis por interagir diretamente com o sistema de armazenamento de dados, como bancos de dados ou sistemas de arquivos.
- `Service`: O pacote Service contém a lógica de negócios principal da aplicação. Aqui estão definidos os serviços e operações que manipulam os dados e implementam a lógica de negócio da aplicação.
   - **UserService**: Assinaturas (contratos) das funções
   - **UserServiceImpl**: A regra de negócio, implementação da lógica de negócio.
- `Controller`: Este pacote contém os controladores ou "handlers" responsáveis por receber as requisições do usuário e direcioná-las para os serviços apropriados. É aqui que ocorre a interação entre a interface do usuário e a lógica de negócios.
- `ConfigDatabase`: Pacote responsável por configurar e inicializar a conexão com o banco de dados.
- `main.py`: O arquivo principal do projeto, que inicia a aplicação e coordena a inicialização de outros componentes necessários.

A estrutura do projeto foi organizada dessa forma para promover a separação de preocupações e a manutenção do código de forma mais organizada e escalável.

Por enquanto tenho a entidade **User** e o método - `@post (create_user)`.
</br>
</br>
Em breve novas atualizações! :)

``` mermaid

classDiagram
    class User {
        -username: String
        -email: String
        -first_name: String
        -last_name: String
        -password: String
        -identity_user: String
    }

```

Dependencies (libs) used:
- pip install fastapi
- pip install "uvicorn[standard]"
- pip install mysql-connector-python
- pip install python-multipart

  **Run the server with:** uvicorn main:app --reload
</br>
</br>
Para facilitar a execução do servidor, pode alterar o arquivo principal:

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
