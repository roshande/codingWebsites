#include <iostream>
using namespace std;
class Node{

	private :int value;
	Node *left;
	Node *right;

	public:
	Node(int val):value(val){}
};

class Tree{
	private :Node root;

	public :Tree(){}

			Tree(int level)
			{
				
			}
	int createnew()
	{

	}
};
int main()
{
    int nolevel,noquery;
    cin>>nolevel;
    cin>>noquery;
    int num1;
    int num2;
    Tree tree(nolevel);
    for(register unsigned int i=0;i<noquery;++i)
    {
    	cin>>num1;
    	cin>>num2;
    	cout<<compute(num1,num2);
    }
    //cout << "Hello World!" << endl;
    return 0;
}

