//Implementar una función que me copie un arreglo en otra direccion
#include <stdio.h>

void strcopy(const char *origen, char *destino){
	int i;
	for (i = 0; origen[i] != '\0'; i++) {
		destino[i] = origen[i];
	}
}

unsigned int len(const char *s){
	unsigned int i;
	for (i = 0; s[i] != '\0'; ++i){ }
	return i;
}

int main() {
	char origen[] = "Hola mundo!";
	unsigned int tam = len(origen);
	char destino[tam + 1];
	printf("%s\n", origen);
	strcopy(origen, destino);
	printf("%s\n", destino);
	return 0;
}