#include <stdio.h>
#include <algorithm>
#include <vector>

#define mxn 1000001

using namespace std;

int arr[mxn];
int dp[mxn];
int p[mxn];
vector<int> v;

int ans, idx;
int n;



int main(int argc, char* argv[]) {
	scanf("%d", &n);
	
	int t;
	for (int i = 1; i <= n; i++) {
		scanf("%d", arr + i);
	}
	dp[0] = 0;

	for (int i = 1; i <= n; i++) {
		int i_max = 0;
		for (int j = 1; j < i; j++) {
			if (arr[j] < arr[i]) {
				if (i_max < dp[j]) {
					i_max = dp[j];
					p[i] = j;
				}
			}
		}
		dp[i] = i_max + 1;
		if (dp[i] > ans) {
			ans = dp[i];
			idx = i;
		}
	}
	/*
	for (int i = 1; i <= n; i++) {
		printf("%d ", dp[i]);
	}
	printf("\n");
	for (int i = 1; i <= n; i++) {
		printf("%d ", p[i]);
	}
	printf("\n");
	*/
	printf("%d\n", ans);
	while (idx != 0) {
		v.push_back(arr[idx]);
		idx = p[idx];
	}
	for (int i = v.size() - 1; i >= 0; i--) {
		printf("%d ", v[i]);
	}
	printf("\n");
	return 0;
}