#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n;
	scanf("%d",&n);
	vector<int> array(n);
	for(int i=0;i<n;++i)
		scanf("%d",&array[i]);

	int sum=0,ans=0;
	for(int i=0;i<n;++i)
	{
		sum+=array[i];
		ans = max(ans,sum);
		if( sum <0 )sum=0;
	}

	printf("%d",ans);
	return 0;
}
