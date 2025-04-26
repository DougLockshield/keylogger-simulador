
# 🖥️ Keylogger Simulador - Projeto Educacional

Este projeto demonstra, de forma **educativa e controlada**, como um programa aparentemente inofensivo — como um **joguinho falso** — pode capturar tudo que um usuário digita e enviar essas informações para um **servidor remoto**.

⚠️ **Atenção:**  
Este conteúdo é exclusivamente para **fins de aprendizado** e **demonstrações laboratoriais**.  
**Não utilize este projeto fora de ambientes de testes controlados.**

---

## 🚀 Como Funciona

- **Servidor Flask:** Roda em um Kali Linux (ou outra máquina) e fica esperando receber os dados capturados.
- **Jogo Falso:** Um pequeno programa que abre uma interface de "jogo", enquanto secretamente captura todas as teclas digitadas e as envia para o servidor.

O objetivo é **educar** sobre os riscos de executar arquivos desconhecidos ou de fontes não confiáveis.

---

## 🛠️ Requisitos

### Para o servidor (Kali Linux ou qualquer Linux/Windows):
- Python 3 instalado
- Flask
  ```bash
  pip install flask
  ```

### Para o cliente (vítima/jogador - Windows ou Linux):
- Python 3 instalado
- Bibliotecas:
  ```bash
  pip install pynput requests
  ```

---

## 📄 Instruções de Uso

1. **Configurar e Rodar o Servidor**
   - Edite o arquivo `servidor_flask.py` se necessário (o IP padrão `0.0.0.0` já aceita conexões de toda a rede).
   - Execute o servidor no Kali ou na máquina escolhida:
     ```bash
     sudo python3 servidor_flask.py
     ```
   - O servidor começará a escutar na porta 80.

2. **Configurar e Rodar o Jogo Falso**
   - No `jogo_falso.py`, altere a variável `SERVIDOR` para o IP do seu servidor:
     ```python
     SERVIDOR = "http://IP_DO_SERVIDOR/log.php"
     ```
   - Execute o jogo falso:
     ```bash
     python jogo_falso.py
     ```
   - A janela do "Super Jogo" será aberta. Tudo o que for digitado será capturado e enviado automaticamente.

3. **Visualizar os Dados Capturados**
   - No servidor, as informações digitadas serão armazenadas no arquivo `log.txt`.

---

## 📂 Estrutura dos Arquivos

| Arquivo | Descrição |
|:--------|:----------|
| `jogo_falso.py` | Código do "jogo" que captura e envia as teclas |
| `servidor_flask.py` | Código do servidor Flask que recebe e salva as teclas |

---

## 📢 Importante
Este projeto é uma simulação educativa para demonstrar como programas maliciosos podem agir disfarçados.  
Utilizar estes conceitos sem autorização pode ser considerado **crime**, sujeito às penalidades previstas em lei.

---

## 👨‍💻 Autor
Douglas Lockshield  
[🔗 YouTube: Lockshield Security](https://youtu.be/v6ANdcbrVIs)  

---

# 🛡️ **Seja sempre ético. Conhecimento é proteção.**
