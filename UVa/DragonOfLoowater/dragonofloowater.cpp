#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n,m;
	scanf("%d %d",&n,&m);
	if(n>m)
	{
		printf("-1");
		return -1;
	}
	vector<int> dragonheads(n);
	vector<int> knightheight(m);
	for(int i=0;i<n;++i)
		cin>>dragonheads[i];
	for(int i=0;i<m;++i)
		cin>>knightheight[i];

	int gold=0;
	make_heap(dragonheads.begin(),dragonheads.end());//O(2n)
	make_heap(knightheight.begin(),knightheight.end());//O(2m)
	int diameter;
	auto iter = knightheight.begin();
	while(!dragonheads.empty() && !knightheight.empty())//O(n)
	{
		diameter = dragonheads.front();
		pop_heap(dragonheads.begin(),dragonheads.end());//O(logn)
		while(!knightheight.empty())//O(m)
		{
			int height = knightheight.front();
			pop_heap(knightheight.begin(),knightheight.end());//O(logm)
			if(diameter <= height)
			{
				gold+=height;
				break;
			}
		}
	}
	//overall O(nlogn + mlogm)
	if(iter == knightheight.end())
		printf("-1");
	else printf("%d",gold);
	return 0;
}
