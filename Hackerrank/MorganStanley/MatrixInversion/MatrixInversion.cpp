#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int matrix[1000][1000];

int inversion_array(int lastend,int end,int start=0)
{

}
int inversion_matrix(int end,int start=0)
{
	if(end == start+1)
	{
		if(matrix[start][start] > matrix[end][end])
			return 1;
		return 0;
	}
	else 
	{
		int mid=(end+start)/2;
		//		pair<int ,int> mid = make_pair((end.first+start.first)/2,(end.second+start.second)/2);
		int count1 = inversion_array(mid,start);
		int count2 = inversion_array(end,mid+1);
		int count3 = inversion_matrix(end,start+1);
		return count1+count2+count3;
	}
}

int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */   
	int size;
	cin>>size;
	//	int **matrix = new int*[size];
	//    vector<vector<int> >matrix(size);
	for(int i=0;i<size;++i)
	{
		//		matrix[i]=new int[size];
		for(int j=0;j<size;++j)
		{
			cin>>matrix[i][j];
		}
	}

	/*	int count=0;
		for(int i=0;i<size;++i)
		{
		for(int j=0;j<size;++j)
		{
		for(int k=i;k<size;++k)//k>i
		{
		for(int l=j;l<size;++l)//l<i
		{
		if(matrix[i][j] > matrix[k][l])
		++count;
		}
		}
		}
		}
		for(int i=0;i<size;++i)
		delete[] matrix[i];
		delete[] matrix;
		cout<<count;
		*/
	cout<<inversion_matrix(size-1);
	return 0;
}

