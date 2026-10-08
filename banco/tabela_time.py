from time import time
from tokenize import group

from flask import flash
from sqlalchemy import select, func
from sqlalchemy.exc import SQLAlchemyError

from database import Time, db_session, Jogador, Partida
from sqlalchemy import select
def select_todos_times():

    # Buscar todos os times no banco
    # 1- Montar o select
    times_sql = (select(Time,func.count(Time.id).label("jogadores"))
                 .outerjoin(Jogador,Jogador.time_id == Time.id)
                 .group_by(Time.id))
    # 2- Executar o select
    times = db_session.execute(times_sql).all()

    return times
def select_quantidade_total():
    times_sql = select(func.count(Time.id))
    qtd_total = db_session.execute(times_sql).scalar()
    return qtd_total
print(select_quantidade_total())

def salvar(nome, turma, responsavel):
    try:
        novo_time = Time(nome=nome,turma=turma,responsavel=responsavel)
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


