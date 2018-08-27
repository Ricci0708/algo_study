// 풀어야함
#include <stdio.h>

int map[102][102];
int n, m;
int t;
int chcnt; //number of cheese
int times;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};
//각각 좌 하 우 상



int main(int argc, char* argv[]){
	scanf("%d %d",&n,&m);
	for(int i = 1; i <= m; i++){
		for(int j = 1; j<= n; j++){
			scanf("%d",&t);
			map[i][j] = t;
			if(t) chcnt++;
		}
	}




	return 0;
}