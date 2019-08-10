using vector<int> vi;
inline int leastSignificantOne(unsigned long long int n)   { return n&-n;            }
class FenwickTree{//BinaryIndexedTree

	private:
		vi ft;

	public:
		FenwickTree(int n){ ft.assign(n+1,0); }//init n+1 zeros

		int rsq(int b){//returns rsq(1,b)
			int sum=0;
			for(;b;b-=leastSignificantOne(b))
				sum += ft[b];
			return sum;
		}
		int rsq(int a,int b){
			return rsq(b) - (a==1?0:rsq(a-1));}

		//adjusts value of kth element by v
		void adjust(int k,int v){
			for(;k <static_cast<int>(ft.size());k+=leastSignificantOne(k))
				ft[k]+=v;
		}
};
