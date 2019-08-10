#include<vector>
#include<iostream>
using namespace std;

class UnionFindDisjointSet{
	private:
		struct node{
			long long int pset,rank;
		} node;
		vector<struct node> p;
		int _findSet(long int i) { return (p[i].pset==i) ? i :(p[i].pset = _findSet(p[i].pset)); }

	public:
		UnionFindDisjointSet(){}

		inline UnionFindDisjointSet(long long int _size){
			this->p.resize(_size);
			for(int i=0;i<_size;++i){
				this->p[i].pset=i;
				this->p[i].rank=0;
			}
		}

		int findSet(int i){ return this->p[i].pset; }

		void unionSet(long long int i,long long int j){
			i=this->_findSet(i);
			j=this->_findSet(j);
			if( this->p[j].rank < this->p[i].rank )
				this->p[j].pset=i;
			else
				this->p[i].pset=j;
			if( this->p[i].rank == this->p[j].rank )
				this->p[j].rank = this->p[j].rank+1;
		}
		bool isSameSet(long long int i,long long int j) { return this->_findSet(i) == this->_findSet(j); }

		int sizeOfSet(long long int i) {
			i=this->_findSet(i);
			int n=this->p.size();
			int size=0;
			for(int j=0;j<n;++j)
				if(this->_findSet(j)==i)
					++size;
			return size;
		}

		int numberOfSets(){
			int num_sets=0;
			int n = this->p.size();
			for(int i=0;i<n;++i)
			{
				if(this->p[i].pset == i)
					++num_sets;
			}
			return num_sets;
		}
};


int main(){return 0;}
