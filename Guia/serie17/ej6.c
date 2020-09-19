#include <stdio.h>

void invertir(char *s, unsigned int len){
	for (int i = 0; i < len/2; i++){
		char aux = s[i];
		s[i] = s[len - 1 - i];
		s[len - 1 - i] = aux;
	}
}

unsigned int len(const char *s){
	unsigned int i;
	for (i = 0; s[i] != '\0'; ++i){ }
	return i;
}

int main(void){
	char s[] = "Hola Mundo!";
	printf("%s\n", s);
	unsigned int largo = len(s);
	printf("%d\n", largo);
	invertir(s, largo);
	printf("%s\n", s);

	return 0;
}