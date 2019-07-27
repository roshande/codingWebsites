#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n=8;
	int A[8] = {0,1,2,3,4,5,6,7};
	vector<int> p(A,A+n);
	do{
		for_each(p.begin(),p.end(),[](int num){printf("%d",num);});
		printf("\n");
	}while(next_permutation(p.begin(),p.end()));
	return 0;
}
