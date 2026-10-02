from flask import flash
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from database import db_session, Partida

def salvar():

        try:
            partida_nova = Partida(time_casa_id=time_casa_id ,time_visitante_id=time_visitante_id ,gols_casa=gols_casa,gols_visitante=gols_visitante ,data_partida=data_partida)
            db_session.add(partida_nova)
            db_session.commit()
            flash('partida cadastrada com sucesso', 'success')


        except SQLAlchemyError as e:
            db_session.rollback()
            flash('ocorreu um erro,tente novamente', 'error')
            print(f"Erro: {e}")
        except Exception as e:
            db_session.rollback()
            flash('ocorreu um erro,tente novamente', 'error')
            print(f"Erro: {e}")
def select_todas_partidas():
    partidas_sql = select(Partida)

    partidas = db_session.execute(partidas_sql).scalars().all()