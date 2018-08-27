#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;


vector<int> g[501];
queue<int> q;

long build_time[501];
long total_time[501];
int indegree[501];
long max_[501];

int n;
int t;

int main(int argc, char*argv[]){
	scanf("%d",&n);

	for(int i = 1; i <= n; i++){
		scanf("%d",&t);
		build_time[i] = t;

		while(true){
			scanf("%d", &t);
			if(t == -1) break;
			else{
				g[t].push_back(i);
				indegree[i]++;
			}
		}
	}
	for(int i = 1; i <=n; i++){
		if(indegree[i] == 0){
			q.push(i);
			indegree[i] = -1;
			total_time[i] = build_time[i];
		}
	}

	while(!q.empty()){
		int c = q.front();
		q.pop();
		while(!g[c].empty()){
			int d = g[c].back();
			g[c].pop_back();
			indegree[d]--;
			max_[d] = max(max_[d], total_time[c]);
		}
		for(int i = 1; i <=n; i++){
			if(indegree[i] == 0){
				q.push(i);
				indegree[i] = -1;
				total_time[i] = max_[i] + build_time[i];
			}
		}
	}

	for(int i = 1; i <= n; i++){
		printf("%ld\n", total_time[i]);
	}



	return 0;
}