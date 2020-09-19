#include <stdio.h>

int min(int arreglo[], int len, int inicio){
	int minimo = arreglo[inicio];
	int indice = inicio;
	for (int i = inicio + 1; i < len; ++i){
		if (arreglo[i] < minimo){
			minimo = arreglo[i];
			indice = i;
		}
	}
	return indice;
}

void imprimir_arreglo(int arreglo[], int len){
	for (int i = 0; i < len; ++i){
		printf("%d ", arreglo[i]);
	}
	printf("\n");
}

void swap(int numeros[],int pos1,int pos2){
	int aux = numeros[pos1];
	numeros[pos1] = numeros[pos2];
	numeros[pos2] = aux;

}

void seleccion(int numeros[], int len){
	int pos_minimo;
	for (int i = 0; i < len; ++i){
		pos_minimo = min(numeros, len, i);
		swap(numeros, i, pos_minimo);
	}
}

int main(){
	int arreglo[5] = {-2,-40,70,4,-3};
	imprimir_arreglo(arreglo, sizeof(arreglo)/sizeof(int));
	seleccion(arreglo, sizeof(arreglo)/sizeof(int));
	imprimir_arreglo(arreglo, sizeof(arreglo)/sizeof(int));
	return 0;
}