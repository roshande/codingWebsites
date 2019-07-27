#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n,m;
	map<int,int> mp;
	mp[5] = 5;
	mp[3] = 3;
	mp[1] = 5;
	mp[6] = 4;
	mp[2] = 5;
	/*mp.insert(make_pair(4,2));
	mp.insert(make_pair(3,5));
	mp.insert(make_pair(6,5));
	mp.insert(make_pair(1,5));*/
	for(pair<int,int> e:mp)
	{
		cout<<e.first<<e.second<<endl;
	}
	return 0;
}
