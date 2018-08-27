//dynamic programming으로 풀면된다
//현재 최솟값은 전에 것의 최솟값이라고 생각하면됨

#include <stdio.h>
#include <algorithm>

using namespace std;

int h[1001][3];
int dp[1001][3];

int n;
int r,g,b;
int ans;

int main(int argc, char* argv[]){
	scanf("%d",&n);

	for(int i = 1; i <=n; i++){
		scanf("%d %d %d", &r, &g, &b);
		h[i][0] = r;
		h[i][1] = g;
		h[i][2] = b;
	}
	for(int i = 1; i <=n; i++){
		for(int j = 0; j <=n; j++){
			switch(j){
				case 0:
					dp[i][j] = min(dp[i-1][1],dp[i-1][2]) + h[i][j];
					break;
				case 1:
					dp[i][j] = min(dp[i-1][0],dp[i-1][2]) + h[i][j];
					break;
				case 2:
					dp[i][j] = min(dp[i-1][0],dp[i-1][1]) + h[i][j];
					break;
			}
		}
	}
	ans = min(dp[n][0],min(dp[n][1],dp[n][2]));
	//printf("%d %d %d\n", dp[n][0],dp[n][1],dp[n][2]);
	printf("%d\n", ans);


	return 0;
}