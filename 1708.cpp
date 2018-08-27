#include <stdio.h>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

 //algorithm적으로 문제가 없었으나 ccw와 distance 함수내부에서 int끼리의 계산에서 overflow가 발생해서 계속 오류가 났었음
// 그래서 명시적으로 모든 계산의 값을 long type으로 type casting 함으로써 해결.
typedef pair<int, int> point;
point p0;

long ccw(int ax, int ay, int bx, int by, int cx, int cy) {
	long ret = ((long)ax*by + (long)bx*cy + (long)cx*ay) - ((long)ay*bx +(long) by*cx + (long)cy*ax);
	return ret;
}

bool point_sort(point a, point b) {
	if (a.second < b.second) return true;
	else if (b.second == a.second) {
		return (a.first < b.first);
	}
	else {
		return false;
	}
}

long dist(point a, point b) {
	long ret = (long)(a.first - b.first) * (long)(a.first - b.first) + (long)(a.second - b.second) *(long)(a.second - b.second);
	return ret;
}

bool angle_sort(point a, point b) {
	if (ccw(p0.first, p0.second, a.first, a.second, b.first, b.second) > 0) return true;
	else if (ccw(p0.first, p0.second, a.first, a.second, b.first, b.second) == 0) 
		return dist(p0,a) < dist(p0,b);
	else return false;
}


vector<point> v;
stack<point> s;

int n;
int x, y;
int main(int argc, char* argv[]) {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &x, &y);
		v.push_back(make_pair(x, y));
	}
	sort(v.begin(), v.end(), point_sort);

	p0 = v[0];
	
	sort(v.begin() + 1, v.end(), angle_sort);

	
	s.push(v[0]);
	s.push(v[1]);

	for (int i = 1; i < n; i++) {
		while (s.size() > 1) {
			point L = s.top();
			s.pop();
			point L1 = s.top();
			s.pop();
			if (ccw(L1.first, L1.second, L.first, L.second, v[i].first, v[i].second) <= 0) {
				s.push(L1);
			}
			else {
				s.push(L1);
				s.push(L);
				break;
			}
		}
		s.push(v[i]);
	}

	printf("%d\n", s.size());

	return 0;
}
