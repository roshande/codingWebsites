#include<bits/stdc++.h>
using namespace std;

int main()
{
	int N;
	scanf("%d",&N);
	vector<int> array(N);
	for(int i=0;i<N;++i)
	{
		scanf("%d",&array[i]);
	}
	long int totalsum = accumulate(array.begin(),array.end(),0.0);
	int i=0;
	for(;i<N;++i)
	{
		int result = accumulate(array.begin(),array.begin()+i,0.0);
		if(totalsum == (2*result + array[i] ))
		{
			printf("YES\n");
			break;
		}
	}
	if(i==N)
		printf("NO\n");
	return 0;
}
