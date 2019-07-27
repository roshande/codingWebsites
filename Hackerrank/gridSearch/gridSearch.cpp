#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool gridSearch(vector<string> grid, vector<string> pattern)
{
	if(pattern.size() > grid.size() || pattern.front().size() > grid.front().size())
		return false;
	for(int i=0;i<grid.size()-pattern.size();++i)
	{
		size_t prev_pos=grid[i].find(pattern.front());
		//cout<<"i"<<i<<endl;
		while(prev_pos != string::npos)
		{
			//cout<<"	prev_pos"<<prev_pos<<endl;
			int j=0;
			int temp_i=i;
			while(j<pattern.size())
			{
				//cout<<"			temp_i"<<temp_i<<endl;
				size_t new_pos = grid[++temp_i].find(pattern[++j],prev_pos);
				//cout<<"		new_pos"<<new_pos<<endl;
				if(new_pos != prev_pos)
					break;
			}
			if(j==pattern.size())
				return true;
			prev_pos=grid[i].find(pattern.front(),prev_pos+1);
		}
	}
	return false;
}

//recursive Search
/*bool gridSearch(vector<string> grid, vector<string> pattern,int g_r=0,int g_c=0)
  {
  if(g_r+pattern.size()> grid.size() || g_c + pattern.front().size() > grid.front().size())
  return false;
  int i=0;
  for(;i<pattern.size();++i)
  {
  size_t pos=grid[g_r+i].find(pattern[i],g_c);
  if(pos != g_c)
  {
  return (gridSearch(grid,pattern,g_r+1,g_c) || gridSearch(grid,pattern,g_r,g_c+1));
  }
  }
  return true;
  }
  */
int main(){
	int t;
	cin >> t;
	for(int a0 = 0; a0 < t; a0++){
		int R;
		int C;
		cin >> R >> C;
		vector<string> G(R);
		for(int G_i = 0;G_i < R;G_i++){
			cin >> G[G_i];
		}
		int r;
		int c;
		cin >> r >> c;
		vector<string> P(r);
		for(int P_i = 0;P_i < r;P_i++){
			cin >> P[P_i];
		}
		if(gridSearch(G,P))
			cout<<"YES"<<endl;
		else 
			cout<<"NO"<<endl;
	}
	return 0;
}

