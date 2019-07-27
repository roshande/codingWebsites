#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n;
	scanf("%d",&n);
	vector<vector<int> > mat(n,vector<int>(n));

	for(int i=0;i<n;++i)
	{
		for(int j=0;j<n;++j)
		{
			scanf("%d",&mat[i][j]);
			if(i>0)mat[i][j]+=mat[i-1][j];
			if(j>0)mat[i][j]+=mat[i][j-1];
			if(i>0 && j>0 )mat[i][j]-=mat[i-1][j-1];
		}
	}

	int maxsubrect=-(1<<31);
	for(int i=0;i<n;++i)
	{
		for(int j=0;j<n;++j)
		{
			for(int k=i;k<n;++k)
			{
				for(int l=j;l<n;++l)
				{
					int sum=mat[k][l];
					if(k>0)sum-=mat[k-1][l];
					if(l>0)sum-=mat[k][l-1];
					if(k>0 && l>0)sum+=mat[k-1][l-1];
					maxsubrect=max(maxsubrect,sum);
				}
			}
		}
	}

	printf("%d",maxsubrect);
	return 0;
}
