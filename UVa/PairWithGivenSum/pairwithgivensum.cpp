#include<bits/stdc++.h>
using namespace std;

pair<int,int> pair_with_given_sum(vector<int> &array,int X)
{
	sort(array.begin(),array.end());//O(nlogn)
	auto n = array.size();
	if( array[0] + array[1] > X || array[n-2] + array[n-1] < X )
		return make_pair(-1,-1);
	auto iter = array.begin()+2;
	for(int i=0;i<(int)array.size() -1;++i)//O(n)
	{
		iter = lower_bound(iter-1,array.end(),X-array[i]);//O(logn)
		if(*iter + array[i] == X)
			return make_pair(*iter,array[i]);
		else if(iter == array.end())
			return make_pair(-1,-1);
	}
	//overall O(nlogn)
	return make_pair(-1,-1);
}

pair<int,int> pair_with_given_sum1(vector<int> &array,int X)
{
	auto q1 = array;
	make_heap(q1.begin(),q1.end());
	//make_heap(qmax.begin(),qmax.end(),greater<int>());
	auto q2 = q1;

	while(!q1.empty() && !q2.empty())
	{
		auto elem = q1.front();
		pop_heap(q1.begin(),q1.end());
		while( X > (elem + q2.front())  && !q2.empty() )
		{
			pop_heap(q2.begin(),q2.end());
		}
		if( X == elem + q2.front() )
			return make_pair(elem,q2.front());
	}
	return make_pair(-1,-1);
}

int main()
{
	int n,X;
	scanf("%d",&n);
	vector<int> array(n);
	for(int i=0;i<n;++i)
		scanf("%d",&array[i]);
	scanf("%d",&X);
	printf("input finished");
	auto p = pair_with_given_sum1(array,X);
	printf("%d %d",p.first,p.second);
	return 0;
}
