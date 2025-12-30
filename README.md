# 📚 Projeto de Modelagem de Dados – Livraria Páginas & Letras

## 🧩 Contexto do Projeto

A livraria **Páginas & Letras** enfrentava dificuldades no controle e na organização de suas informações, como cadastro de livros, autores, clientes e vendas. A ausência de uma estrutura de dados bem definida dificultava o acesso às informações, a manutenção do sistema e a possibilidade de crescimento do negócio.

Diante desse cenário, tornou-se necessária a criação de um **banco de dados relacional**, capaz de representar de forma fiel as regras e os processos do negócio.

---

## 🎯 Objetivo

Desenvolver um **Modelo Entidade-Relacionamento (MER)** que sirva como base para a implementação de um banco de dados relacional, garantindo:

- Organização e padronização dos dados
- Integridade e consistência das informações
- Facilidade de manutenção e evolução do sistema
- Suporte ao crescimento da livraria

---

## 📐 Desenvolvimento do MER

Após uma análise detalhada das necessidades da livraria, foi elaborado um **Modelo Entidade-Relacionamento** com o objetivo de estruturar todas as informações essenciais do negócio.

A modelagem de dados permite que a livraria implemente um banco de dados eficiente, seguro e escalável, facilitando o acesso às informações e reduzindo inconsistências.

O MER desenvolvido oferece uma **base sólida**, permitindo futuras adaptações conforme novas demandas da empresa.

---

## 🧱 Entidades Identificadas

As principais entidades identificadas no modelo foram:

- **Livro**
- **Autor**
- **Editora**
- **Categoria**
- **Cliente**
- **Funcionário**
- **Venda**
- **Item_Venda**

Essas entidades representam os elementos centrais do funcionamento da livraria e possibilitam o registro completo das operações do negócio.

---

## 🔗 Relacionamentos

O modelo contempla os seguintes relacionamentos principais:

- Um **Autor** pode escrever um ou vários **Livros**, e um **Livro** pode ter um ou vários **Autores** (N:N)
- Uma **Editora** publica vários **Livros**, e cada **Livro** pertence a uma única **Editora** (1:N)
- Um **Livro** pertence a uma **Categoria** (1:N)
- Um **Funcionário** registra várias **Vendas** (1:N)
- Cada **Venda** possui um ou mais **Itens de Venda**, que detalham os livros comercializados

O relacionamento entre **Venda** e **Livro** é resolvido pela entidade associativa **Item_Venda**, permitindo o controle de quantidade e preço no momento da venda.

---

## 🧠 Paradigmas:

🧠 **Por que NÃO ligar Cliente ↔ Funcionário?**
❌ O relacionamento ficaria ambíguo:

Qual funcionário? 
Em qual venda?
Em que data?
Comprou o quê?

✔️ **A entidade Venda resolve tudo isso:**

O cliente se relaciona diretamente com a entidade **sale**, pois é ele quem realiza a compra. O funcionário também se relaciona com **sale**, pois é quem registra a venda. Não há relacionamento direto entre cliente e funcionário, já que a venda é a entidade que contextualiza essa interação.

🧠 **Por que NÃO ligar as entidade LIVRO ↔ AUTOR?**

O relacionamento entre **Livro** e **Autor** é do tipo **muitos-para-muitos (N:N)**, pois um autor pode escrever vários livros e um livro pode ser escrito por vários autores. Como bancos de dados relacionais não suportam relacionamentos **N:N** diretamente, foi criada a entidade associativa **Livro_Autor** para resolver essa cardinalidade, garantindo a integridade e a normalização dos dados.

🧠 **Por que NÃO ligar as entidade VENDAS ↔ LIVROS?**

O relacionamento entre **Sale** e **Book** é do tipo **muitos-para-muitos (N:N)**, pois uma venda pode conter vários livros e um mesmo livro pode participar de várias vendas. Como relacionamentos N:N não podem ser representados diretamente em bancos de dados relacionais, foi criada a entidade associativa **Item_Sale**, responsável por vincular cada livro a uma venda específica e armazenar informações próprias dessa relação, como quantidade vendida e preço unitário no momento da venda, garantindo integridade e normalização dos dados.



🔗 Relacionamentos e Cardinalidades 

book ↔ author → N:N **(via book_author entidade associativa)**

publisher ↔ book → 1:N

category ↔ book → 1:N

employee ↔ sale → 1:N

sale ↔ book → N:N **(via item_sale entidade associativa)**

client ↔ venda → 1:N


## 🖼️ Diagrama MER

O diagrama MER representa graficamente as entidades, seus atributos e relacionamentos, facilitando a compreensão da estrutura do banco de dados e servindo como referência para a implementação do modelo lógico e físico.

https://dbdesigner.page.link/Y3G7G9Myu3yjas3q7
---

## 🚀 Considerações Finais

Este projeto demonstra a aplicação prática dos conceitos de **modelagem de dados**, **normalização** e **bancos de dados relacionais**, utilizando boas práticas amplamente adotadas no mercado.

O MER desenvolvido fornece uma base consistente para a implementação futura do banco de dados da livraria **Páginas & Letras**, possibilitando evolução, manutenção e escalabilidade do sistema.

---

## 🛠️ Ambiente Virtual e Instalação de Dependências

Para garantir isolamento das dependências e evitar conflitos de versões, este projeto utiliza um **ambiente virtual Python (`venv`)**.

### 📌 Pré-requisitos:

- Python 3.10 ou superior
- Git
- VS Code (recomendado)

---

### 🧪 Criação do ambiente virtual

No diretório raiz do projeto, execute:

```bash
python -m venv amb_virt_bookstore
```
### Estrutura do projeto:
```
project_livraria/
│
├── amb_virt_bookstore/
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── models.py
│── MER/
|   |── model_data_james_martin.png
|   |── model_data_peter_chen.png
|   |── models_data.dbml
├── requirements.txt
├── README.md
└── main.py
└──.gitignore
```

## 🛢️ Implementação do Banco de Dados com SQLAlchemy

A implementação do banco de dados foi realizada utilizando o **SQLAlchemy**, uma biblioteca ORM (Object-Relational Mapping) que permite mapear entidades do modelo relacional para classes Python, facilitando a manipulação dos dados e a manutenção do sistema.

Essa abordagem garante maior abstração, organização do código e aderência às boas práticas de desenvolvimento.

---

## 🔌 Configuração da Conexão

Foi utilizada a base de dados **SQLite**, adequada para fins acadêmicos e prototipação. A conexão é centralizada no módulo `connection.py`, onde são definidos:

- Engine de conexão com o banco
- Sessão de comunicação (`SessionLocal`)
- Classe base (`Base`) para os modelos ORM

---

## 📚 Mapeamento das Entidades (ORM)

Cada entidade do **Modelo Entidade-Relacionamento (MER)** foi implementada como uma classe Python, respeitando:

- Chaves primárias
- Chaves estrangeiras
- Relacionamentos 1:N e N:N
- Entidades associativas

As principais entidades implementadas foram:

- `Book`
- `Author`
- `Publisher`
- `Category`
- `Client`
- `Employee`
- `Sale`
- `ItemSale`   (entidade associativa)
- `BookAuthor` (entidade associativa)

---

## 🔗 Relacionamentos Implementados

- **Book ↔ Author**: relacionamento N:N, resolvido pela entidade associativa `BookAuthor`
- **Sale ↔ Book**: relacionamento N:N, resolvido pela entidade associativa `ItemSale`
- **Publisher ↔ Book**: relacionamento 1:N
- **Category ↔ Book**: relacionamento 1:N
- **Client ↔ Sale**: relacionamento 1:N
- **Employee ↔ Sale**: relacionamento 1:N

Os relacionamentos foram implementados utilizando `ForeignKey` e `relationship`, garantindo integridade referencial e navegação entre as entidades.

---

## 📦 Entidades Associativas

As entidades associativas desempenham papel fundamental no modelo:

- **BookAuthor**: representa a associação entre livros e autores
- **ItemSale**: representa os livros que compõem cada venda, armazenando atributos próprios da relação, como quantidade e preço unitário no momento da venda

Essa abordagem permite a correta representação de relacionamentos muitos-para-muitos e mantém o modelo normalizado.

---

## ⚙️ Criação das Tabelas

A criação física das tabelas é realizada por meio do método:

```python
Base.metadata.create_all(bind=engine)
```

## 👤 Autor

**Daniel Martins França**

Projeto desenvolvido com foco em **modelagem de dados**, **bancos de dados relacionais** e **boas práticas de implementação utilizando ORM**, aplicando conceitos acadêmicos e profissionais.

---

## 🛠️ Ferramentas e Tecnologias Utilizadas

- **Python 3.11**
- **SQLAlchemy** (ORM)
- **SQLite** (Banco de dados relacional)
- **VS Code** (Ambiente de desenvolvimento)
- **Git & GitHub** (Versionamento de código)
- **DB Designer** (Modelagem do MER)
- **Jupyter Notebook** (Análises e testes, quando aplicável)
- **PowerShell** (Execução dos comandos no Windows)

---

## 📬 Contato

- 📧 **E-mail:** f.daniel.m@gmail.com  
- 💼 **LinkedIn:** www.linkedin.com  

---

## 📌 Observação

Este projeto faz parte do portfólio acadêmico desenvolvido para aplicar conceitos de Modelagem de Dados e Banco de Dados Relacional, utilizando SQLAlchemy ORM, com foco em boas práticas e estrutura profissional. e tem como objetivo demonstrar a aplicação prática de conceitos de **Modelagem de Dados**, **Normalização**, **Banco de Dados Relacional** e **SQLAlchemy ORM**.
