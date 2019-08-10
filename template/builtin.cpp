#include<stdio.h>
#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n=5328;//00000000000000000001010011010000
	printf("Number: %x\n",n);//19
	printf("1+positionOfleastSignificantSetBit: %x\n",__builtin_ffs(n));//5
	printf("Number of Ones: %d\n",__builtin_popcount(n));//19
	printf("Terminating Zeros: %d\n",__builtin_ctz(n));//4
	printf("Leading Zeros: %d\n",__builtin_clz(n));//5
	printf("Parity: %d\n",__builtin_parity(n));//1
	printf("gcd(24,32):%d",__gcd(24,32));
	return 0;
}
