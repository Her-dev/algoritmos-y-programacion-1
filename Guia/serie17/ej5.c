#include <stdio.h>

int stringlen(char cadena[]){
	int i = 0;
	for (i ; cadena[i] != '\0'; ++i){}
	return i;
}

int stringlen_rec1(char cadena[], int i){
	if (cadena[i] == '\0'){
		return i;
	}
	i = i + 1;
	return stringlen_rec1(cadena, i);
	
}

int stringlen_rec(char cadena[]){
	int j;
	j = stringlen_rec1(cadena, 0);
	return j;
}


int main(void){
	char x[9] = "hola gato";
	printf("%d\n", stringlen(x));
	printf("%d\n", stringlen_rec(x));
	return 0;
}