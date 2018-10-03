#include <stdio.h>

int n;
int Ni[9];
int m[9];
int cnt, t ,f;




int main(int argc, char* argv[]){

	scanf("%d", &n);
	for (int i = 1; i <= n; i++){
		scanf("%d", &Ni[i]);
	}
	for (int i = 1; i <= n; i++){
		scanf("%d", &m[i]);
		if(m[i] > Ni[i]){
			printf("-1\n");
			return 0;
		}
	}
	scanf("%d",&cnt);
	for (int i = n; i > 0; i--){
		f = 0;
		if(cnt == 0) break;
		t = cnt % (Ni[i] + 1);
		m[i] += t;
		if(m[i] > Ni[i]){
			f = 1;
			m[i]-= (Ni[i] + 1);
		}
		cnt /= (Ni[i] + 1);
		if (f == 1){
			cnt++;
		}
	}

	for(int i = 1; i <= n; i++){
		printf("%d", m[i]);
	}
	printf("\n");

	return 0;
}