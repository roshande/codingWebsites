/* 
 * https://www.topcoder.com/community/competitive-programming/tutorials/range-minimum-query-and-lowest-common-ancestor/
 *
 * The notation for overall complexity of algorithm having preprocessing time 
 * f(n) and query time g(n) is <f(n),g(n)>
 */
#include<iostream>
#include<algorithm>
using namespace std;

#include<string.h>
#include<math.h>

#define MAX (1+(1<<6))
#define inf 0x7fffffff

class RMQ{
    
    private:
        vector<int> tree, array;

    public:
        RMQ(){ }
};

void process1(int M[MAXN][MAXN], int A[MAXN], int N)
{
    int i,j;
    for(int i =0;i<N;++i)
    { M[i][i] = 1; }
    for(int i = 0;i<N;++i) {
        for(int j = i+1; j<N;++j) {
            if(A[M[i][j-1]] < A[j])
                M[i][j] = M[i][j-1];
            else
                M[i][j] = j;
        }
    }
}

void process2(int )
