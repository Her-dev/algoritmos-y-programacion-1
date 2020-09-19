#include <stdio.h>

int factorial(int n){
	int fact = 1;
		for (int i = 1; i < n + 1; ++i){
			fact = fact * i;
		}
		return fact;
}

int factorial_recursivo(int n){
	int fact;
	if(n == 1){
		return 1;
	}
	else{
		fact = n * factorial_recursivo(n - 1);
	}
	return fact;
}

int main(void){
	int fact = factorial(10);
	int facto = factorial_recursivo(5);
	printf("%d\n", fact);
	printf("%d\n", facto);

	return 0;
}
