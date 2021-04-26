from mysql.connector import connect

#show_schemas = "SHOW SCHEMAS"
#params = None


# >>>>>> FUNÇÃO DE EXECUÇÃO
def execute(sql, params=None):
    # Executa um comando no mysql e salva os valores. Serve para:
    # insert, update, delete, create, alter, drop
    with connect(host="localhost", user="root", password="root", database="bluecommerce") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            conn.commit()



# >>>>>> FUNÇÃO DE 'BUSCA'
def query(sql, params=None):
    # Executa um comando no mysql e retorna o resultado
    # Serve para: Select, SHOW
    with connect(host="localhost", user="root", password="root", database="bluecommerce") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()



# >>>>>> FUNÇÃO PARA CRIAR TABELAS
def create_table(nome_tabela, colunas):
            execute(f"""CREATE TABLE {nome_tabela}
            (id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT, {colunas})""")

# create_table('pais', 'sigla char(3), nome varchar(255)')


# >>>>>> CRIANDO TABELAS POR DICT
# >>>> PAISES, ESTADOS, CIDADES, USUARIOS, PRODUTOS
# >>>> CATEGORIAS, VENDAS, VENDAS_PRODUTOS, ESTOQUES
# tabelas = {"paises": "sigla char(3), nome varchar(255)",
#            "estados": "sigla char(3), nome varchar(255), id_pais INT NULL",
#            "cidades": "nome varchar(255), id_estado INT NULL",
#            "usuários": "nome varchar(255), senha varchar(255), email varchar(255), endereco varchar(255), id_cidade INT NULL",
#            "produtos": "nome varchar(255), preco DECIMAL(7,2) NOT NULL, id_categoria INT NULL",
#            "categorias_produtos": "nome varchar(255), id_categoria_geral INT NULL",
#            "vendas": "data_venda DATE, id_usuario INT NULL",
#            "vendas_produtos": "quantidade INT, id_produto INT NULL, id_venda INT NULL",
#            "estoques": "id_produto INT NULL, id_venda INT NULL, quantidade INT"
#            }
# for tabela, colunas in tabelas.items():
#     create_table(tabela, colunas)



# # >>>>>> FUNÇÃO PARA CHAVE ESTRANGEIRA
# # >>>>>> LIGA A TABELA VENDAS_PRODUTOS COM PRODUTOS E COM VENDAS
# def foreing_key(execute):
#     execute("""ALTER TABLE vendas_produtos
#     ADD CONSTRAINT fk_vendas_produtos_produtos FOREIGN KEY id_produto REFERENCES produtos(id)""")
#
# def foreing_key(execute):
#     execute("""ALTER TABLE vendas_produtos
#     ADD CONSTRAINT fk_vendas_produtos_vendas FOREIGN KEY id_venda REFERENCES vendas(id)""")




# # >>>>>> FUNÇÃO PARA APAGAR UM VALOR
# def delete_value(nome_tabela, coluna, id):
#     execute(f"DELETE FROM {nome_tabela} WHERE {coluna} = {id}")
#
# # >>>>>> APAGA UM VALOR DENTRO DE UMA COLUNA EM UMA TABELA
# delete_value("paises", "id", "1")
# delete_value("estados", "id", "1")
# delete_value("cidades", "id", "1")
# delete_value("usuarios", "id", "1")
# delete_value("produtos", "id", "1")
# delete_value("categorias_produtos", "id", "1")
# delete_value("vendas", "id", "1")
# delete_value("vendas_produtos", "id", "1")
# delete_value("estoques", "id", "1")
#
#
# # >>>>>> FUNÇÃO PARA INSERIR UM VALOR IGNORANDO REPETIDOS
# def insert_value(nome_tabela, colunas, inserir_valor):
#     execute(f"INSERT IGNORE INTO {nome_tabela}({colunas}) VALUES ({inserir_valor})")
#
# # >>>>>> INSERE UM VALOR DENTRO DE UMA OU MAIS COLUNAS EM UMA TABELA
# insert_value("paises", "nome", "'Danilandia'")
# insert_value("estados", "nome", "'Inad'")
# insert_value("cidades", "nome", "'Santa Dani'")
# insert_value("usuarios", "nome", "'Daniela'")
# insert_value("produtos", "nome", "'Bolo'")
# insert_value("categorias_produtos", "nome", "'Doces'")
# insert_value("vendas", "data_venda", "'2021-04-02'")
# insert_value("vendas_produtos", "quantidade", "100")
# insert_value("estoques", "id", "1")
#
#
# # >>>>>> FUNÇÃO PARA BUSCAR UM VALOR
# def select_value(coluna, tabela, condicao, valor):
#     print(query(f"""SELECT {coluna} FROM {tabela} WHERE {condicao} = {valor}"""))
#
# # >>>>>> BUSCA UM VALOR DENTRO DE UMA COLUNA EM UMA TABELA
# select_value("nome", "paises", "id", "2")
# select_value("id", "estados", "id", "2")
# select_value("id", "cidades", "id", "2")
# select_value("id", "usuarios", "id", "2")
# select_value("id", "produtos", "id", "2")
# select_value("id", "categorias_produtos", "id", "2")
# select_value("id", "vendas", "id", "2")
# select_value("id", "vendas_produtos", "id", "2")
# select_value("id", "estoques", "id", "2")
#
#
# # >>>>>> FUNÇÃO PARA ALTERAR UM VALOR
# def update_value(tabela, coluna, valor_alterar, condicao, valor_condicao):
#     execute(f"""UPDATE {tabela} SET {coluna} = {valor_alterar} WHERE {condicao} = {valor_condicao}""")
#
# # >>>>>> ALTERA UM VALOR DENTRO DE UMA COLUNA EM UMA TABELA
# update_value("paises", "nome", "'Caos'" "nome", "'BRA'")
# update_value("estados", "nome", "'Santa Paula'", "nome", "'SP'")
# update_value("cidades", "nome", "'Terra dos maconheiros'", "nome", "São Tomé das Letras")
# update_value("usuarios", "senha", "123456", "id", "2")
# update_value("produtos", "id", "90", "id", "1")
# update_value("categorias_produtos", "id", "55", "id", "1")
# update_value("vendas", "id", "55", "id", "1")
# update_value("vendas_produtos", "id", "55", "id", "1")
# update_value("estoques", "id", "55", "id", "1")



##################################################################################################





