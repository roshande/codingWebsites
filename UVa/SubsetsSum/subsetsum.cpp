/*
 * Given a list l containing 1<=n<=20 integers, is there a subset of list l that
 * sums to another given integer X?
 */
#include<bits/stdc++.h>

using namespace std;

void print_set(vector<int> v,int bitmask)
{
	for(int i=0;i<(int)v.size();++i)
		if(bitmask & (1<<i))
			printf("%d ",v[i]);
}
int main()
{
	int n=0;
	scanf("%d",&n);
	vector<int> set(n);
	for(int i=0;i<n;++i)
		cin>>set[i];
	int X;
	scanf("%d",&X);
	if(n>30)
	{
		bitset<1000> bitmask;
	}
	for(int bitmask=0;bitmask<(1<<n);++bitmask)//O(2^n)
	{
		int sum=0;
		for(int j=0;j<n;++j)//O(n)
		{
			if(bitmask & (1<<j))
				sum+=set[j];
		}
		if(sum == X)
			print_set(set,bitmask);
	}
	//overall O(n*2^n)
	return 0;
}
