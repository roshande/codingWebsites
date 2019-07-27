#include<bits/stdc++.h>
using namespace std;

int main()
{
	int testcases;
	cin>>testcases;
	double N,C;
	for(int i=0;i<testcases;++i)
	{
		cin>>N>>C;
		double sum_candies =0;
		for(int ii=0;ii<N;++ii)
		{
			double candies;
			cin>>candies;
			sum_candies+=candies;
		}
		if(sum_candies <= C)
		{
			printf("YES\n");
		}
		else{
			printf("NO\n");
		}
	}
}
