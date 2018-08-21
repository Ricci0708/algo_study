#include <stdio.h>

#define MAX_V 101
#define MAX_E 100001
#define INF 987654321


int arr[MAX_V][MAX_V];


int main(int argc, char* argv[]){
	int n,m;
	scanf("%d", &n);
	scanf("%d", &m);

	for(int i = 1; i <= n; i++){
		for (int j = 1; j <= n; j++){
			arr[i][j] = INF;
		}
		arr [i][i] = 0;
	}

	int from, to, val;
	for(int i = 0; i < m; i++){
		scanf("%d %d %d", &from, &to, &val);
		if(arr[from][to] > val){
			arr[from][to] = val;
		}
	}


	for(int k = 1; k <= n; k++){
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <=n; j++){
				if(arr[i][j] > arr[i][k] + arr[k][j]){
					if(arr[i][k] != INF && arr[k][j] != INF){	
						arr[i][j] = arr[i][k] + arr[k][j];
					}
				}
			}
		}

	}	
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= n; j++){
			if(arr[i][j] == INF){
				printf("0 ");
			}
			else printf("%d ", arr[i][j]);
		}
		printf("\n");
	}

	return 0;
}