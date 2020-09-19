#include <stdio.h>
#include <stdlib.h>

#define BUFFER_TAM 11

int pedir_numero(){
	char buffer[BUFFER_TAM];
	fgets(buffer, BUFFER_TAM, stdin);
	return atoi(buffer);
}

int pregunta_numero(int minimo, int maximo){
	printf("ingrese un número entre %d y %d \n ", minimo, maximo);
	for ( ; ; ){
		int x = pedir_numero();
		if (x > minimo && x < maximo){
			printf("el número ingresado fue %d\n", x);
			return 0;
		}
		printf("Recuerde! el numero a ingresar debe estar entre %d y %d \n ", minimo, maximo);
	}
}

int main(){
	pregunta_numero(9, 16);
	return 0;
}