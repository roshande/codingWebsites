#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */   
	int len1,len2,len3;
	cin>>len1>>len2>>len3;
	vector<int> vec1(len1);
	vector<int> vec2(len2);
	vector<int> vec3(len3);
	int sum[3]={0,0,0};
	for(int i=0;i<len1;++i)
	{
		cin>>vec1[len1-1-i];
		sum[0]+=vec1[len1-1-i];
	}        
	for(int i=0;i<len2;++i)
	{
		cin>>vec2[len2-1-i];
		sum[1]+=vec2[len2-1-i];
	}

	for(int i=0;i<len3;++i)
	{
		cin>>vec3[len3-1-i];
		sum[2]+=vec3[len3-1-i];
	}
	while(sum[0]!=sum[1] && sum[1]!=sum[2])
	{
		if(sum[0]>sum[1])
		{
			if(sum[0]>sum[2])
			{
				sum[0]-=vec1.back();
				vec1.pop_back();
			}
			else if(sum[2] > sum[0])
			{
				sum[2]-=vec3.back();
				vec3.pop_back();
			}
			else if(vec1.back() > vec3.back())
			{
				sum[0]-=vec1.back();
				vec1.pop_back();
			}
			else //if(vec1.back() < vec3.back())
			{
				sum[2]-=vec3.back();
				vec3.pop_back();
			}
			/*else{
			  sum[1]-=vec2.back();
			  vec2.pop_back();
			  }*/
		}
		else if(sum[1]>sum[0]){
			if(sum[1]>sum[2])
			{
				sum[1]-=vec2.back();
				vec2.pop_back();
			}
			else if(sum[2] > sum[1])
			{
				sum[2]-=vec3.back();
				vec3.pop_back();
			}
			else if(vec2.back() > vec3.back())
			{
				sum[1]-=vec2.back();
				vec2.pop_back();
			}
			else {
				sum[2]-=vec3.back();
				vec3.pop_back();
			}
			/*else {
			  sum[0]-=vec1.back();
			  vec1.pop_back();
			  }*/
		}
		else if (sum[0] < sum[2]){
			sum[2]-=vec3.back();
			vec3.pop_back();
		}
		else {
			if(vec1.back() > vec2.back())
			{
				sum[0]-=vec1.back();
				vec1.pop_back();
			}
			else {
				sum[1]-=vec2.back();
				vec2.pop_back();
			}
		}
	}
	cout<<sum[0];
	return 0;
}

