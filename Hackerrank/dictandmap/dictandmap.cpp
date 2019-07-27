#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;


int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */   
	int cases;
	unordered_map<string,long int> dict;
	string name;
	long int number;
	cin>>cases;
	for(int i=0;i<cases;++i)
	{
		cin>>name>>number;
		dict[name]=number;
	}
	getline(cin,name);
	while(!name.empty())
	{
		if(dict.find(name) == dict.end())
			cout<<"Not found"<<endl;
		else
			cout<<name<<"="<<dict[name]<<endl;
		getline(cin,name);
	}
	return 0;
}

