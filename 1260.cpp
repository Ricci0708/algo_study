#include <stdio.h>
#include <stack>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> graph[1001];
int t;
int n,m,s;
int e0,e1;
int visited[1001];

void initialize_visit(){
	for(int i = 1; i <= n; i++){
		visited[i] = 0;
	}
}
void dfs(vector<int> graph[], int start){
	initialize_visit();

	stack<int> s;
	s.push(start);

	while(!s.empty()){
		t = s.top();
		// printf("stack: %d\n", t);
		s.pop();
		if(!visited[t]){
			printf("%d ", t);
			visited[t] = 1;			
		}
		

		for(int i = graph[t].size() - 1; i >= 0; i--){
			if(visited[graph[t][i]]) continue;
			else s.push(graph[t][i]);
		}
	}
	printf("\n");
};

void bfs(vector<int> graph[], int start){
	initialize_visit();
	queue<int> q;
	q.push(start);
	visited[start] = 1;
	while(!q.empty()){
		t = q.front();
		q.pop();
		printf("%d ", t);
		for(int i = 0; i < graph[t].size(); i++){
			// printf("a: %d ", graph[t][i]);
			if(visited[graph[t][i]]) continue;
			else {
				q.push(graph[t][i]);
				visited[graph[t][i]] = 1;
			}
		}
	}
	printf("\n");
}
int main(){
	scanf("%d %d %d",&n,&m,&s);
	for(int i = 0; i < m; i++){
		scanf("%d %d", &e0, &e1);
		if(find(graph[e0].begin(),graph[e0].end(),e1) == graph[e0].end()){
			graph[e0].push_back(e1);
			graph[e1].push_back(e0);
		}
	}

	for(int i= 1; i <= n; i++){
		sort(graph[i].begin(), graph[i].end());

	}

	dfs(graph, s);
	bfs(graph, s);
	return 0;
}