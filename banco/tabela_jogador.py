from flask import flash
from sqlalchemy import select
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
    jogadores_sql = select(Jogador)

    jogadores = db_session.execute(jogadores_sql).scalars().all()
    return jogadores

