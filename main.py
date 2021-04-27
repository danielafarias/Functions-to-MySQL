from mysql.connector import connect

#show_schemas = "SHOW SCHEMAS"
#params = None


# ################################## >>>>>> FUNÇÃO DE EXECUÇÃO <<<<<< #########################################
def execute(sql, params=None):
    # Executa um comando no mysql e salva os valores. Serve para:
    # insert, update, delete, create, alter, drop
    with connect(host="localhost", user="root", password="root", database="bluecommerce") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            conn.commit()



# ################################## >>>>>> FUNÇÃO DE 'BUSCA' <<<<<< ##########################################
    # Executa um comando no mysql e retorna o resultado
    # Serve para: Select, SHOW
def query(sql, params=None):
    with connect(host="localhost", user="root", password="root", database="bluecommerce") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()



# ################################## >>>>>> FUNÇÃO PARA CRIAR TABELAS <<<<<< ###################################
def create_table(nome_tabela, colunas):
            execute(f"""CREATE TABLE {nome_tabela}
            (id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT, {colunas})""")



# ################################# >>>>>> FUNÇÃO PARA CHAVE ESTRANGEIRA <<<<<< ##################################
def foreing_key(tabela, fk, coluna, tabela_referencia, coluna_referencia):
    execute(f"""ALTER TABLE {tabela}
    ADD CONSTRAINT {fk} FOREIGN KEY {coluna} REFERENCES {tabela_referencia}({coluna_referencia})""")



# ################################# >>>>>> FUNÇÃO PARA APAGAR UM VALOR <<<<<< ######################################
def delete_value(nome_tabela, coluna, id):
    execute(f"DELETE FROM {nome_tabela} WHERE {coluna} = {id}")



# ########################## >>>>>> FUNÇÃO PARA INSERIR UM VALOR IGNORANDO REPETIDOS <<<<<< #########################
def insert_value(nome_tabela, colunas, inserir_valor):
    execute(f"INSERT IGNORE INTO {nome_tabela}({colunas}) VALUES ({inserir_valor})")



# ################################# >>>>>> FUNÇÃO PARA BUSCAR UM VALOR <<<<<< ######################################
def select_value(coluna, tabela, condicao, valor):
    print(query(f"""SELECT {coluna} FROM {tabela} WHERE {condicao} = {valor}"""))



# ################################# >>>>>> FUNÇÃO PARA ALTERAR UM VALOR <<<<<< ######################################
def update_value(tabela, coluna, valor_alterar, condicao, valor_condicao):
    execute(f"""UPDATE {tabela} SET {coluna} = {valor_alterar} WHERE {condicao} = {valor_condicao}""")





