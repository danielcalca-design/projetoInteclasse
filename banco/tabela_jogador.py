import time

from flask import flash
from sqlalchemy import select, func, join
from sqlalchemy.exc import SQLAlchemyError

from database import Jogador, db_session, Time, Partida


def salvar(nome, numero_camisa,time_id,posicao):


    try:
        jogador_novo = Jogador(nome=nome, numero_camisa=numero_camisa, time_id=time_id, posicao=posicao)
        db_session.add(jogador_novo)
        db_session.commit()
        flash('jogador cadastrado com sucesso', 'success')


    except SQLAlchemyError as e:
        db_session.rollback()
        flash('ocorreu um erro,tente novamente', 'error')
        print(f"Erro: {e}")
    except Exception as e:
        db_session.rollback()
        flash('ocorreu um erro,tente novamente', 'error')
        print(f"Erro: {e}")

def select_todos_jogador():
    # 1 - montar o select
    # join(tabela que euqiero juntar,contição = chave estrangeira igual chave primaria)
    jogadores_sql = select(Jogador,Time).join(Time,Jogador.time_id == Time.id)
    # 2 - executar select
    # usar scalars quando tiver somente uma tabela
    jogadores = db_session.execute(jogadores_sql).all()
    return jogadores

def select_quantidade_total():
    jogadores_sql = select(func.count(Jogador.id))
    qtd_total = db_session.execute(jogadores_sql).scalar()
    return qtd_total
print(select_quantidade_total())

def select_um(id_jogador):
    jogador_sql = (select(Jogador).where(Jogador.id == id_jogador))
    jogador = db_session.execute(jogador_sql).scalar_one_or_none()
    return jogador
print(select_um(1))
# trazer jogadore de um time
def select_por_time(time_id):
    jogador_sql = (select(Jogador).where(time_id == Jogador.time_id))
    jogador = db_session.execute(jogador_sql).scalars().all()
    return jogador
print(select_por_time(1))




