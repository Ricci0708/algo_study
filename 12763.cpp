#include <stdio.h>
#include <queue>
#include <vector>

using namespace std;

#define max_size 101
#define INF 987654321
class route{
public:
	int _to;
	int _time;
	int _budget;
	route(int _to, int _time, int _budget);
};

route::route(int _to, int _time, int _budget){
	this->_to = _to;
	this->_time = _time;
	this->_budget = _budget;
}


vector<route> route_arr[max_size];
priority_queue<route> pq;


int n;
int time_limit, budget_limit;
int r;
int from, to, hour, budget;
int t[max_size];
int b[max_size];

//문제 자체는 dijkstra algorithm으로 해결가능할것으로 보임
int main(int argc, char* argv[]){
	scanf("%d",&n);
	scanf("%d %d",&time_limit,&budget_limit);
	scanf("%d",&r);
	for(int i = 0; i < n; i++){
		scanf("%d %d %d %d", &from, &to, &hour, &budget);
		route_arr[from].push_back(route (to, hour, budget) );
	}

	for(int i = 2; i <= n; i ++){
		t[i] = INF;
		b[i] = INF;
	}
	t[1] = 0;
	b[1] = 0;


	return 0;
}