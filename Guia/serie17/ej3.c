#include <stdio.h>
#define TAM 4

float promedio(int lista[], int len){
	int suma;
	for (int i = 0; i < len ; ++i){
		suma = suma + lista[i];
	}
	return (float)suma/ len;
}

int main(void){
	float prom;
	int arreglo[TAM] = {1, 2, 1, 1};
	prom = promedio(arreglo, TAM);
	printf("%f\n", prom);
	return 0;
}