import os

BEAVER_DIR = os.path.dirname (os.path.realpath (__file__))
BEAVER_TEMPLATE_FOLDER = BEAVER_DIR + '/template/'

# TODO: Cache init
def init ():
	if not os.path.isdir (BEAVER_TEMPLATE_FOLDER):
		os.mkdir (BEAVER_TEMPLATE_FOLDER)
	pass

def printList ():
	root, dirs, files = next (os.walk (BEAVER_TEMPLATE_FOLDER))
	for file in files:
		print (file)
	print ('[SUCCESS] Total {} template(s) found'.format (len (files)))
def this (src, dest = ''):
	if dest == '':
		dest = os.path.basename (src)
	dest = os.path.basename (dest)

	try:
		f = open (src, 'r', encoding='utf8')
	except Exception as e:
		print ('[ERROR]', e)
		return
	
	ABS_DEST_PATH = BEAVER_TEMPLATE_FOLDER + dest;
	info = f.read ()
	f.close ()

	if os.path.isfile (ABS_DEST_PATH):
		confirm = input ('There is a template "{}" existed, override [y/n]?'.format (dest))
		if confirm.lower () != 'y':
			print ('[ERROR] No template saved')
			return
	try:
		g = open (ABS_DEST_PATH, 'w')
		g.write (str (info))
		g.close ()	
	except Exception as e: 
		print ('[ERROR]', e)
		return 
	
	print ('[SUCCESS] Made template name "{}"'.format (dest))
	pass

def make (src, dest=''):

	src = os.path.basename (src)
	if dest == '':
		dest = src
	src = BEAVER_TEMPLATE_FOLDER + src
	
	ABS_DEST_PATH = dest

	try:
		f = open (src, 'r', encoding='utf8')		
	except Exception as e:
		print ('[ERROR]', e)
		return
	
	info = f.read ()
	f.close ()
	try:
		g = open (ABS_DEST_PATH, 'a+')
		if (g.tell () > 0):
			g.write ("\n")
		g.write (str (info))
		g.close ()
	except Exception as e:
		print ('[ERROR]', e)
		return
	print ('[SUCCESS] File append to "{}"'.format(ABS_DEST_PATH))

def interface ():
	import argparse
	import sys
	parser = argparse.ArgumentParser()
	parser.add_argument("task", type=str, help="choose task to perform, either 'save', 'make', or 'list'")
	parser.add_argument('source', nargs='?', default='template', type=str, help='specific the source of either "save" or "make" task');
	parser.add_argument("--to", type=str, help='name of "save" or "make" destination file, should be abbreviation or something recalled', default='')
	args = parser.parse_args(sys.argv[1:])
	
	tsk = args.task
	src  = args.source
	dst  = args.to

	if (tsk.lower () == 'save'):
		this (src, dst)
	elif (tsk.lower () == 'make'):
		make (src, dst)
	elif (tsk.lower () == 'list'):
		printList ();
	else:
		print ('[ERROR] Unsupported task "{}"'.format (tsk.lower ()))

def main ():
	interface ()	
	pass

if __name__ == "__main__":
	init ()
	main ()
	pass