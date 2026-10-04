from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('cadastrologin.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Captura os dados do formulário
        usuario = request.form.get('usuario')
        email = request.form.get('email')

        nome_final = usuario if usuario else (email.split('@')[0] if email
                                              else 'green_runner')
        if not nome_final.startswith('@'):
            nome_final = '@' + nome_final

        # Renderiza diretamente a página do menu
        return render_template('menu.html', username=nome_final)

    return render_template('cadastrologin.html')


if __name__ == '__main__':
    app.run(debug=True)
