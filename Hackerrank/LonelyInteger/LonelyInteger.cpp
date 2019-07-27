#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

int lonelyinteger(vector < int > a) {
	set<int> _my_set;
	set<int>::iterator itr;
	for(auto i:a)
	{
		itr=find(_my_set.begin(),_my_set.end(),i);
		if(itr != _my_set.end())
			_my_set.insert(i);
		else _my_set.erase(i);
	}
	return itr;

}
int main() {
	int res;

	int _a_size;
	cin >> _a_size;
	cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n'); 
	vector<int> _a;
	int _a_item;
	for(int _a_i=0; _a_i<_a_size; _a_i++) {
		cin >> _a_item;
		_a.push_back(_a_item);
	}

	res = lonelyinteger(_a);
	cout << res;

	return 0;
}

