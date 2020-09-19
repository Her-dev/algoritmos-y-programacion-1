#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM_ENTRADA 200

int main() {
	char entrada[TAM_ENTRADA];
	printf("ingrese una cadena\n");
	fgets(entrada, TAM_ENTRADA, stdin);

	int tam = strlen(entrada);

	if (entrada[tam -1] == '\n'){
		entrada[tam -1] = '\0';
	}

	for (int i = 0; i < tam + 3; i++){
		printf("*");
	}
	printf("\n");

	printf("* ");
	for (int i = 0; i < tam; ++i){
		printf("%c",entrada[i]);
	}
	printf(" *\n");
	
	for (int i = 0; i < tam + 3; i++){
		printf("*");
	}
	printf("\n");

	return 0;	

}