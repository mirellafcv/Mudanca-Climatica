from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '' # Necessário para usar a session


@app.route('/')
def index():
    return render_template('cadastrologin.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Captura os dados do formulário
        usuario = request.form.get('usuario')
        email = request.form.get('email')

        nome_final = usuario if usuario else (
            email.split('@')[0] if email else 'green_runner'
        )
        if not nome_final.startswith('@'):
            nome_final = '@' + nome_final

        # Salva o usuário e inicializa a pontuação na sessão
        session['usuario'] = nome_final
        if 'pontos' not in session:
            session['pontos'] = 450

        # Redireciona para a rota do menu
        return redirect(url_for('menu'))

    return render_template('cadastrologin.html')


@app.route('/menu')
def menu():
    username = session.get('usuario', '@membro')
    pontos = session.get('pontos', 450)
    return render_template('menu.html', username=username, pontos=pontos)


@app.route('/ranking')
def ranking():
    username = session.get('usuario', '@membro')
    pontos = session.get('pontos', 450)
    return render_template('ranking.html', username=username, pontos=pontos)


@app.route('/desafio', methods=['GET', 'POST'])
def desafio_semanal():
    if 'pontos' not in session:
        session['pontos'] = 450

    if request.method == 'POST':
        # Pega a pontuação conquistada no formulário do quiz
        pontos_ganhos = int(request.form.get('pontos_ganhos', 0))

        # Soma à pontuação acumulada do usuário na sessão
        session['pontos'] += pontos_ganhos

        # Redireciona para o ranking com a pontuação atualizada
        return redirect(url_for('ranking'))

    return render_template('desafiosemanal.html')


if __name__ == '__main__':
    app.run(debug=True)
