from flask import Flask, render_template, request, redirect, url_for, flash, g
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from banco import tabela_time, tabela_partida, tabela_jogador
from database import *

app = Flask(__name__)
app.secret_key = "chave-secreta-interclasse-2026"


@app.route("/")
def dashboard():
    times = tabela_time.select_todos()
    jogador = tabela_jogador.select_todos_jogador()
    partida = tabela_partida.select_todas_partidas()

    return render_template(
        "dashboard.html",
        total_jogadores=len(jogador),
        total_times=len(times),
        total_partidas=len(partida),

    )


@app.route("/jogadores")
def listar_jogadores():
    jogadores = tabela_jogador.select_todos_jogador()

    return render_template("jogadores.html", jogadores=jogadores)


@app.route("/jogadores/novo", methods=["GET", "POST"])
def novo_jogador():
    if request.method == "POST":
        # 1 - Pegar os valores digitados no form
        nome = request.form.get("nome", "").strip()
        numero_camisa = request.form.get("numero_camisa", "").strip()
        time_id = request.form.get("time_id", "").strip()
        posicao = request.form.get("posicao", "").strip()

        # 2 - Verificar se foi digitado
        if not nome:
            flash('preencha o nome', 'error')
            return redirect(url_for(novo_jogador))
        if not numero_camisa:
            flash('preencha o numero_camisa', 'error')
            return redirect(url_for(novo_jogador))
        if not time_id:
            flash('preencha o time_id', 'error')
            return redirect(url_for(novo_jogador))
        if not posicao:
            flash('preencha a posicao', 'error')
            return redirect(url_for(novo_jogador))
        tabela_jogador.salvar(nome=nome, numero_camisa=numero_camisa, time_id=time_id,posicao=posicao)
        jogadores = tabela_jogador.select_todos_jogador()
        tabela_time.salvar(nome=nome,turma=turma,responsavel=responsavel)
        times = tabela_time.select_todos_times()


    return render_template("jogadores.html", times=times, jogadores=jogadores)


@app.route("/times")
def listar_times():
    times = tabela_time.select_todos_times()
    return render_template("times.html", times=times)

@app.route("/times/novo", methods=["GET", "POST"])
def novo_time():

    if request.method == "POST":
        #1 - Pegar os valores digitados no form
        nome = request.form.get("nome", "").strip()
        turma = request.form.get("turma", "").strip()
        responsavel = request.form.get("responsavel", "").strip()

        #2 - Verificar se foi digitado
        if not nome:
            flash('preencha o nome', 'error')
            return redirect(url_for(novo_time))
        if not turma:
                flash('preencha a turma', 'error')
                return redirect(url_for(novo_time))
        if not responsavel:
                flash('preencha o responsavel', 'error')
                return redirect(url_for(novo_time))
        tabela_time.salvar(nome=nome, turma=turma, responsavel=responsavel)
        times = tabela_jogador.select_todos_times()

    return render_template("times.html", times=times)





@app.route("/partidas")
def listar_partidas():
    partidas_sql = select(Partida)

    # 2- Executar o select
    partidas = db_session.execute(partidas_sql).scalars().all()
    print(partidas)

    return render_template("partidas.html", partidas=partidas)


@app.route("/partidas/nova", methods=["GET", "POST"])
def nova_partida():

    if request.method == "POST":
        time_casa_id = request.form.get("time_casa_id")
        time_visitante_id = request.form.get("time_visitante_id")
        gols_casa = request.form.get("gols_casa") or 0
        gols_visitante = request.form.get("gols_visitante") or 0
        data_partida = request.form.get("data_partida", "").strip()

        if not time_casa_id:
            flash('preencha o time da casa', 'error')
            return redirect(url_for(nova_partida))
        if not time_visitante_id:
            flash('preencha o time visitante', 'error')
            return redirect(url_for(nova_partida))
        if not gols_casa:
            flash('preencha o total de gols do time da casa', 'error')
            return redirect(url_for(nova_partida))
        if not gols_visitante:
            flash('preencha o total de gols do time do visitante', 'error')
            return redirect(url_for(nova_partida))
        if not data_partida:
            flash('preencha a data da partida', 'error')
            return redirect(url_for(nova_partida))

            # 3 - salvar no banco
        tabela_partida.salvar()

    partidas = tabela_partida.select_todas_partidas()




            # Buscar todos os times no banco
            # 1- Montar o select
    times_sql = select(Time)

        # 2- Executar o select
    times = db_session.execute(times_sql).scalars().all()
    print(times)

    partidas_sql = select(Partida)

        # 2- Executar o select
    partidas = db_session.execute(partidas_sql).scalars().all()
    print(partidas)

    return render_template("partidas.html", partidas=partidas, times=times)


if __name__ == "__main__":
    app.run(debug=True)
