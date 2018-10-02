#include <stdio.h>

int f_l[] = {1,3,6,10,15,21};
int f_m[] = {500,300,200,50,30,10};
int s_l[] = {1,3,7,15,31};
int s_m[] = {512,256,128,64,32};

int n;
int f,s;
int main(int argc, char* argv[]){
	scanf("%d", &n);
	
	for(int i = 0; i < n; i++){
		int result = 0;
		scanf("%d %d",&f,&s);
		if(f != 0) {
			for(int j = 0; j < 6; j++){
				if(f <= f_l[j]){
					result += f_m[j];
					break;
				}
			}
		}
		if(s != 0){
			for(int j = 0; j < 5; j++){
				if(s <= s_l[j]){
					result += s_m[j];
					break;
				}
			}
		}
		printf("%d\n",result * 10000);
	}
	return 0;
}

