from flask import Flask

app = Flask(__name__)


@app.route("/")
def curriculo():
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - Otávio</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        h2 { color: #3498db; margin-top: 20px; }
        .info-contato { background-color: #f4f4f4; padding: 10px; border-radius: 5px; }
        .experiencia, .educacao, .cursos { margin-bottom: 15px; }
        .empresa, .escola { font-weight: bold; }
        .data { font-style: italic; color: #7f8c8d; }
    </style>
</head>
<body>

    <header>
        <h1>Otávio Cesar</h1>
        <div class="info-contato">
            <p>Telefone: (11) 99999-9999</p>
            <p>E-mail: otaviocesarnudo@gmail.com</p>
        </div>
    </header>

    <section>
        <h2>Experiência de Trabalho</h2>
        <div class="experiencia">
            <p class="empresa">Empresa XYZ - Analista de Sistemas</p>
            <p class="data">Jan 2020 - Atual</p>
            <ul>
                <li>Desenvolvimento de aplicações web com Flask.</li>
                <li>Otimização de bancos de dados SQL.</li>
            </ul>
        </div>
        <div class="experiencia">
            <p class="empresa">Empresa ABC - Estagiário de TI</p>
            <p class="data">Jan 2018 - Dez 2019</p>
            <ul>
                <li>Suporte técnico e manutenção de computadores.</li>
            </ul>
        </div>
    </section>

    <section>
        <h2>Educação</h2>
        <div class="educacao">
            <p class="escola">Universidade Exemplo - Bacharelado em Ciência da Computação</p>
            <p class="data">2016 - 2020</p>
        </div>
        <div class="educacao">
            <p class="escola">Escola Técnica Estadual - Ensino Médio Técnico</p>
            <p class="data">2013 - 2015</p>
        </div>
    </section>

    <section>
        <h2>Cursos e Certificações</h2>
        <div class="cursos">
            <ul>
                <li>Curso Avançado de Python - Udemy</li>
                <li>Flask Web Development - Coursera</li>
            </ul>
        </div>
    </section>

    <section>
        <h2>Idiomas</h2>
        <ul>
            <li><strong>Inglês:</strong> Avançado</li>
            <li><strong>Espanhol:</strong> Intermediário</li>
        </ul>
    </section>

</body>
</html>"""


if __name__ == "__main__":
    app.run(debug=True)
