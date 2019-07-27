#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

pair<int ,int> mindays(vector<int> array,int profit,int end,int start=0)
{
	if( end == start+1 )
	{
		if(profit == array.at(end) -array.at(start))
			return make_pair(start,end);
		return make_pair(0,array.size());//end-start);
	}
	else 
	{
		int mid = end - (end-start)/2;
		pair<int ,int> result1 = mindays(array,profit,mid,start);
		pair<int ,int> result2 = mindays(array,profit,end,mid+1);
		int diff1 = result1.second - result1.first;
		int diff2 = result2.second - result2.first;
		if(diff1 == 1)
			return result1;
		else if(diff2 == 1)
			return result2;
		if(diff1 < diff2 || diff2 == mid)
		{
			result2 = mindays(array,profit,mid+diff1/2,mid-diff1/2);
			diff2 = result2.second - result2.first;
		}
		else if(diff1 > diff2 || diff1 == mid){
			result1 = mindays(array,profit,mid+diff2/2,mid-diff2/2);
			diff1 = result1.second - result1.first;
		}
		if(diff1<diff2)
			return result1;
		return result2;
	}
}
/*int find_min(vector<int> array,int start,int profit)
  {
  int min=array.size();
  for(int i=start;i<int(array.size());++i)
  {
  if(profit == array.at(i))
  {
  if(min>i-start)
  min=i-start;
  }
  }
  return min;
  }
  */

int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */   
	int nodays,query;
	cin>>nodays;
	cin>>query;
	vector<int>shares(nodays);
	for(int i=0;i<nodays;++i)
	{
		cin>>shares.at(i);
	}
	for(int i=0;i<query;++i)
	{
		int profit;
		cin>>profit;
		pair<int ,int> result = mindays(shares,profit,nodays-1);
		if(result.first == -1)
			cout<< -1;
		else 
		{
			cout<<result.first+1<<"  "<<result.second+1<<endl;
		}
	}
	return 0;
}
