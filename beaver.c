#include <stdio.h>
#include <string.h> 
#include <windows.h>

char* getModuleFileDir () {
	char* buffer = (char*) malloc (1025);
	GetModuleFileName (NULL, buffer, 1025);
	int idx = strlen (buffer)-1;
	while (idx && buffer[idx] != '\\') buffer[idx] = '\0', --idx;
	return buffer;
}

int __strlensum__ (int n, char* argv[]) {
	int i,sum = 0;
	for (i=0;i<n;++i) {
		sum += strlen (argv[i]) + 3; // space, and 2 quote
	}
	return sum;
}

int main(int argc, char *argv[] ) {
	const char* module = getModuleFileDir();
	const char* exec = "python ";
	const char* script = "beaver.py";
	int len = __strlensum__(argc, argv), i;
	char* str = (char*) malloc (strlen (module) + strlen (exec) + strlen (script) + len + 1);
	memset (str, 0, sizeof (str));
	
	strcat (str, exec);
	strcat (str, module);
	strcat (str, script);
	for (i=1; i<argc; ++i) {
		strcat (str, " \"");
		strcat (str, argv[i]);
		strcat (str, "\"");
	}
//	printf ("%s ", str)	;
	system (str);		
	return 0;
}

