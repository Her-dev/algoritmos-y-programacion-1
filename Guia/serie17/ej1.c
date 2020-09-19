#include <stdio.h>

float area(float a, float b){
	float area = a * b;
	return area;

}

int main(void){
	float ar;
	ar = area(2.5, 5);
	printf("el área del cuadrado es %f \n", ar);
	return 0;
}