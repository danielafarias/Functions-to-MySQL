from main import create_table, delete_value, insert_value, select_value, update_value, foreing_key

########################################################+++++##########################################################

''' 
                         !!! Comandos utilizando as funções para o exercício passado !!!
'''

# ################################# >>>>>> CRIANDO AS TABELAS POR DICT <<<<<< ########################################
# 1. Criar uma função para criar uma tabela país
# 2. Criar uma função para criar uma tabela estado
# 3. Criar uma função para criar uma tabela cidade
# 4. Criar uma função para criar uma tabela Usuário
# 5. Criar uma função para criar uma tabela Produto
# 6. Criar uma função para criar uma tabela Categoria de Produto
# 7. Criar uma função para criar uma tabela Venda
# 8. Criar uma função para criar uma tabela VendaProduto (liga a venda com o produto)
# 9. Criar uma função para criar uma tabela Estoque

tabelas = {"paises": "sigla char(3), nome varchar(255)",
           "estados": "sigla char(3), nome varchar(255), id_pais INT NULL",
           "cidades": "nome varchar(255), id_estado INT NULL",
           "usuários": "nome varchar(255), senha varchar(255), email varchar(255), endereco varchar(255), id_cidade INT NULL",
           "produtos": "nome varchar(255), preco DECIMAL(7,2) NOT NULL, id_categoria INT NULL",
           "categorias_produtos": "nome varchar(255), id_categoria_geral INT NULL",
           "vendas": "data_venda DATE, id_usuario INT NULL",
           "vendas_produtos": "quantidade INT, id_produto INT NULL, id_venda INT NULL",
           "estoques": "id_produto INT NULL, id_venda INT NULL, quantidade INT"
           }
for tabela, colunas in tabelas.items():
    create_table(tabela, colunas)

# ###################### >>>>>>> OU <<<<<< ####################################
create_table('pais', 'sigla char(3), nome varchar(255)')


# ################################# >>>>>> FUNÇÃO PARA CHAVE ESTRANGEIRA <<<<<< ##################################
foreing_key("vendas_produtos", "fk_vendas_produtos_produtos", "id_produto", "produtos", "id")
foreing_key("vendas_produtos", "fk_vendas_produtos_vendas", "id_venda", "vendas", "id")

# >>>>>> LIGA A TABELA VENDAS_PRODUTOS COM PRODUTOS E COM VENDAS DIRETO <<<<<<
def foreing_key(execute):
    execute("""ALTER TABLE vendas_produtos
    ADD CONSTRAINT fk_vendas_produtos_produtos FOREIGN KEY id_produto REFERENCES produtos(id)""")

def foreing_key(execute):
    execute("""ALTER TABLE vendas_produtos
    ADD CONSTRAINT fk_vendas_produtos_vendas FOREIGN KEY id_venda REFERENCES vendas(id)""")


# ###################### >>>>>> APAGA UM VALOR DENTRO DE UMA COLUNA EM UMA TABELA <<<<<< ############################
# 10. Criar uma função para Apagar um País
# 11. Criar uma função para Apagar um Estado
# 12. Criar uma função para Apagar uma Cidade
# 13. Criar uma função para Apagar um Usuário
# 14. Criar uma função para Apagar um Produto
# 15. Criar uma função para Apagar uma Categoria de Produto
# 16. Criar uma função para Apagar uma Venda
# 17. Criar uma função para Apagar um VendaProduto
# 18. Criar uma função para Apagar um Produto no Estoque

delete_value("paises", "id", "1")
delete_value("estados", "id", "1")
delete_value("cidades", "id", "1")
delete_value("usuarios", "id", "1")
delete_value("produtos", "id", "1")
delete_value("categorias_produtos", "id", "1")
delete_value("vendas", "id", "1")
delete_value("vendas_produtos", "id", "1")
delete_value("estoques", "id", "1")



# #################### >>>>>> INSERE UM VALOR DENTRO DE UMA OU MAIS COLUNAS EM UMA TABELA <<<<<< ####################
# 19. Criar uma função para Inserir um País
# 20. Criar uma função para Inserir um Estado
# 21. Criar uma função para Inserir uma Cidade
# 22. Criar uma função para Inserir um Usuário
# 23. Criar uma função para Inserir um Produto
# 24. Criar uma função para Inserir uma Categoria de Produto
# 25. Criar uma função para Inserir uma Venda
# 26. Criar uma função para Inserir um VendaProduto
# 27. Criar uma função para Inserir um Produto no Estoque

insert_value("paises", "nome", "'Danilandia'")
insert_value("estados", "nome", "'Inad'")
insert_value("cidades", "nome", "'Santa Dani'")
insert_value("usuarios", "nome", "'Daniela'")
insert_value("produtos", "nome", "'Bolo'")
insert_value("categorias_produtos", "nome", "'Doces'")
insert_value("vendas", "data_venda", "'2021-04-02'")
insert_value("vendas_produtos", "quantidade", "100")
insert_value("estoques", "id", "1")




# #################### >>>>>> BUSCA UM VALOR DENTRO DE UMA COLUNA EM UMA TABELA <<<<<< #############################
# 28. Criar uma função para Buscar um País
# 29. Criar uma função para Buscar um Estado
# 30. Criar uma função para Buscar uma Cidade
# 31. Criar uma função para Buscar um Usuário
# 32. Criar uma função para Buscar um Produto
# 33. Criar uma função para Buscar uma Categoria de Produto
# 34. Criar uma função para Buscar uma Venda
# 35. Criar uma função para Buscar um VendaProduto
# 36. Criar uma função para Buscar um Produto no Estoque

select_value("nome", "paises", "id", "2")
select_value("id", "estados", "id", "2")
select_value("id", "cidades", "id", "2")
select_value("id", "usuarios", "id", "2")
select_value("id", "produtos", "id", "2")
select_value("id", "categorias_produtos", "id", "2")
select_value("id", "vendas", "id", "2")
select_value("id", "vendas_produtos", "id", "2")
select_value("id", "estoques", "id", "2")



# #################### >>>>>> ALTERA UM VALOR DENTRO DE UMA COLUNA EM UMA TABELA <<<<<< ############################
# 37. Criar uma função para Alterar um Estado
# 38. Criar uma função para Alterar uma Cidade
# 39. Criar uma função para Alterar um Usuário
# 40. Criar uma função para Alterar um Produto
# 41. Criar uma função para Alterar uma Categoria de Produto
# 42. Criar uma função para Alterar uma Venda
# 43. Criar uma função para Alterar um VendaProduto
# 44. Criar uma função para Alterar um Produto no Estoque

update_value("paises", "nome", "'Caos'", "nome", "'BRA'")
update_value("estados", "nome", "'Santa Paula'", "nome", "'SP'")
update_value("cidades", "nome", "'Terra dos maconheiros'", "nome", "São Tomé das Letras")
update_value("usuarios", "senha", "123456", "id", "2")
update_value("produtos", "id", "90", "id", "1")
update_value("categorias_produtos", "id", "55", "id", "1")
update_value("vendas", "id", "55", "id", "1")
update_value("vendas_produtos", "id", "55", "id", "1")
update_value("estoques", "id", "55", "id", "1")