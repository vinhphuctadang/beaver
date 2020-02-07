#include <stdio.h>
#include <string.h> 
int __strlensum__ (int n, char* argv[]) {
	int i,sum = 0;
	for (i=0;i<n;++i) {
		sum += strlen (argv[i]) + 3; // space, and 2 quote
	}
	return sum;
}

int main(int argc, char *argv[] ) {
	const char* exec = "python beaver.py";
	int len = __strlensum__(argc, argv), i;
	char* str = (char*) malloc (strlen (exec) + len + 1);
	memset (str, 0, sizeof (str));
	
	strcat (str, exec);
	for (i=1; i<argc; ++i) {
		strcat (str, " \"");
		strcat (str, argv[i]);
		strcat (str, "\"");
	}
//	printf ("%s ", str)	;
	system (str);		
	return 0;
}

