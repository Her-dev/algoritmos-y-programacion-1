#include <stdio.h>

void imprime_size(void){
	
	int b = sizeof(_Bool);
	int c = sizeof(char); 
	int s = sizeof(short); 
	int i = sizeof(int); 
	int l = sizeof(long); 
	int f = sizeof(float);
	int d = sizeof(double);
	int bp = sizeof(_Bool*);
	int cp = sizeof(char*); 
	int sp = sizeof(short*);
	int ip = sizeof(int*);
	int lp = sizeof(long*);

	printf("bool:%d\n char:%d\n short:%d\n int:%d\n long:%d\n float:%d\n double:%d\n puntero bool:%d\n puntero char:%d\n puntero short:%d\n puntero int:%d\n puntero long:%d\n ", b,c,s,i,l,f,d,bp,cp,sp,ip,lp);

}

int main(void){
	imprime_size();
	return 0;
}