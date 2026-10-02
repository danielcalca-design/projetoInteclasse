from time import time

from flask import flash
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database import Time, db_session, Jogador, Partida
from sqlalchemy import select
def select_todos_times():

    # Buscar todos os times no banco
    # 1- Montar o select
    times_sql = select(Time)

    # 2- Executar o select
    times = db_session.execute(times_sql).scalars().all()

    return times
def salvar(nome, turma, responsavel):
    try:
        novo_time = time(nome=nome,turma=turma,responsavel=responsavel)
        db_session.add(novo_time)
        db_session.commit()
        flash('time cadastrado com sucesso', 'success')
    except SQLAlchemyError as e:
        db_session.rollback()
        flash('ocorreu um erro,tente novamente', 'error')
        print(f"Erro: {e}")
    except Exception as e:
        db_session.rollback()
        flash('ocorreu um erro,tente novamente', 'error')
        print(f"Erro: {e}")


