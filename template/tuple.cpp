#include<bits/stdc++.h>
#include <tuple>
using namespace std;

int main()
{
	tuple<int,int,int> t1 = make_tuple(1,2,3);
	tuple<char,int,double,int,long long int >t2;
	t2=make_tuple( 'a' , 2 , 2.3 , 1 , 10000 );
	cout<<get<2>t1<< " "<< get<0>t2;// will print 3 and 'a'

	// Usage of tie
	int a;
	int b;
	char c;
	tie ( a, b , c ) = make_tuple(4,1,'a'); // this is equilvalent to a=4; b=1 ; c='a'
	tie ( a , b ) = make_tuple(b,a); // swapping b and a
	int c1=10;
	int d=5;
	int e=15;
	tie(c1,d,e) = make_tuple( c1+d+e, c1+2*d , 10*c1 ); // Now c will be equal to 30, //d will be equal to 20 and e will be equal to 100.
	return 0;
} 
