#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

inline long int sum(int *array,int end)
{
	long int result=0;
	for(int i=0;i<end;++i)
	{
		result+=array[i];
	}
	return result;
}

int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */   
	short T;
	cin>>T;
	int *array = new int[100000];
	for(int j=0;j<T;++j)
	{
		int N;
		//cin>>N;
		scanf("%d",&N);
		//int *array = new int[N];
		long int totalsum=0;
		for(int i=0;i<N;++i)
		{
			//cin>>array[i];
			scanf("%d",array+i);
			totalsum += array[i];
		}
		int i=0;
		for(;i<N;++i)
		{
			long int result=0;
			for(int j=0;j<i;++j)
			{
				result+=array[j];
			}
			if(totalsum == (2*result + array[i]))
			{
				//cout<<"YES"<<endl;
				printf("YES\n");
				break;
			}
		}
		if(i==N)
			printf("NO\n");
		//cout<<"NO"<<endl;
		//delete[] array;
	}
	delete[] array;
	return 0;
}

