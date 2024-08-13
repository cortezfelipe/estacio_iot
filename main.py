from flask import Flask, jsonify, request
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

app = Flask(__name__)

# Rota para obter os resultados do banco de dados
@app.route('/<tabela>', methods=['GET'])
def obter_dados(tabela):
    try:
        # Conecta ao banco de dados PostgreSQL
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )

        # Abre um cursor para executar as consultas SQL
        cur = conn.cursor()

        # Executa a consulta SQL
        cur.execute(f'SELECT * FROM {tabela}')

        # Obtém os resultados da consulta
        results = cur.fetchall()

        # Fecha o cursor e a conexão com o banco de dados
        cur.close()
        conn.close()

        # Converte os resultados em um formato JSON e retorna
        return jsonify(results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()