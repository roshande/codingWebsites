#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;


int LCS(stack<int> *st,vector<int>::reverse_iterator start1,vector<int>::reverse_iterator end1,vector<int>::reverse_iterator start2,vector<int>::reverse_iterator end2)
    {
    if(start1==end1 || start2==end2)
        return 0;
    else if(*start1 == *start2)
        {
        st->push(*start1);
        return 1+LCS(st,start1+1,end1,start2+1,end2);
    }
    else {
        stack<int> st1;
        int max1=LCS(&st1,start1+1,end1,start2,end2);
        
        stack<int> st2;
        int max2=LCS(&st2,start1,end1,start2+1,end2);
        if(max1>max2)
            {
            while(!st1.empty())
                {
                st->push(st1.top());
                st1.pop();
            }
            return max1;
        }
        else {
            while(!st2.empty())
                {
                st->push(st2.top());
                st2.pop();
            }
            return max2;
        }
    }
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int len1,len2;
    vector<int> array1(len1),array2(len2);
    for(int i=0;i<len1;++i)
        cin>>array1[i];
    for(int i=0;i<len2;++i)
        cin>>array2[i];
    stack<int> st;
    LCS(&st,array1.rbegin(),array1.rend(),array2.rbegin(),array2.rend());
    while(!st.empty())
        {
        cout<<st.top()<<" ";
        st.pop();
    }
    return 0;
}

