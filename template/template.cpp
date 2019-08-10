#pragma warning(disable:4996)
#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize ("Ofast")
#pragma GCC target ("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize ("-ffloat-store")

#include <bits/stdc++.h>
using namespace std; 

#ifndef ONLINE_JUDGE
bool debug=false;
#else
bool debug=true;
#endif

/*
 * ans = a ? b: c;		//to simply if(a) ans = b; else ans =c;
 * ans += val;			//ans = ans +val;
 * index = (index+1)%n;	//index++; if(index>=n) index=0;
 * index = (index+n-1)%n	//index--;if(index<0) index = n-1;
 * ans = (int)((double)d + 0.5);	//for rounding to nearest integer
 * ans = min(ans,new_computation);	//min/max;
 * 
 * ans = min({a,b,c,d})		//ans = min(min(min(a,b),c),d)
 * //interval checking
 * if(unsigned(i-min_i) <= unsigned(max_i - min_i))		//min_i <= i && i <= max_i
 *
 * if(*(int*)&f & 0x7FFFFFF ) *(int*)&f += n<<23; //f*=pow(2,n)
 *
 * //binarylookuptable
 * static const type lookup_table[] = {c,b};
 * ans = lookup_table[a]			//ans = a ? b : c;
 *
 * static const type lookup_table[] = {d,c3,c2,c2,c1,c1,c1,c1}		//a = b1 ?c1 :b2 ?c2 :b3 ?c3 :d;
 * a = lookup_table[(b1<<2) + (b2<<1) + b3];
 */
#define deb(x) cerr << #x << " = " << x << endl;
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define MEM(x,val) memset((x),(val),sizeof(x));
#define RITE(x) freopen((x,"w",stdout);
#define READ(x) freopen(x,"r",stdin);
#define ALL(x) x.begin(),x.end()
#define TR(c,i) for(auto i = (c).begin(); i != (c).end(); ++i)
#define PRESENT(c,x) ((c).find(x) != (c).end())
#define CPRESENT(c,x) (find(ALL(c),x) != (c).end())
#define SZ(x) ((int)x.size())
#define SQR(x) ((x)*(x))
#define CLR clear()
#define MID(s,e) (s+(e-s)/2.0)
#define RSORT(a) greater<a>
#define GC getchar_unlocked
#define PC putchar_unlocked
#define IFC(i)                (flag[i>>6]&(1<<((i>>1)&31)))
#define ISC(i)                (flag[i>>6]|=(1<<((i>>1)&31)))
#define CHK(n)                (n==2||(n>2&&(n&1)&&!IFC(n)))
/*#define sv(t)                  int t; scanf("%d",&t); while(t--)*/
const int INF = 1<<30;
const int MOD = 1E9 + 7;
const double EPS = 1E-9 ;
const int MX=10010896;
const int lmt=3164;

using ll=long long;
using lli = long long int;
using ull =unsigned long long;
using st=string;
using vi=vector<int>;
using vs=vector<st>;
using vll=vector<ll>;
using mii=map<int,int>;
using mci=map<char,int>;
using msi=map<st,int>;
using si=set<int>;
using ss=set<st>;
using pii=pair<int,int>;
using psi=pair<st,int>;
using pss=pair<st,st>;
using pll=pair<ll,ll>;
using vpii=vector<pii>;
using mseti=multiset<int>;
//using edgelist = vector<pair<int, pair<int, int> > > ;
using edgelist = priority_queue<pair<int, pair<int, int> > >;
//using edgelist = priority_queue<tuple<int,int,int> >;
//get<0>(tp)
//tie
using adjlist = vector<vector<pair<int, int> > >;
using adjmat = vector<vector<int> >;

/*typedef string st;
  typedef vector<int> vi;
  typedef vector<st> vs;
  typedef vector<ll> vll;
  typedef map<int,int> mii;
  typedef map<char,int> mci;
  typedef map<st,int> msi;
  typedef set<int> si;
  typedef set<st> ss;
  typedef pair<int,int> pii;
  typedef pair<st,int> psi;
  typedef pair<st,st> pss;
  typedef pair<ll,ll> pll;
  typedef vector<pii> vpii;
  typedef multiset<int> mseti;
  */
int flag[MX>>6];
ll extGCD(ll a,ll b,ll& x,ll& y){if(b==0){x=1;y=0;return a;}else{int g=extGCD(b,a%b,y,x);y-=a/b*x;return g;}}
ll modpow(ll a,ll b) {ll res=1;a%=MOD;for(;b;b>>=1){if(b&1)res=res*a%MOD;a=a*a%MOD;}return res;}
void sieve(){ int i,j,k; for(i=3;i<lmt;i+=2) if(!IFC(i)) for(j=i*i,k=i<<1;j<MX;j+=k) ISC(j);}

/* Fast Input-Output */
inline void rdi(int &n) { n=0; char c=GC(); while(c<'0' or c>'9') c=GC(); while(c>='0' and c<='9') { n=(n<<3)+(n<<1)+c-'0'; c=GC(); }}
inline void rdl(ll &n) { n=0; char c=GC(); while(c<'0' or c>'9') c=GC(); while(c>='0' and c<='9') { n=(n<<3)+(n<<1)+c-'0'; c=GC(); }}
inline void print(int a) { char s[20]; int i=0; do { s[i++]=a%10+'0'; a/=10; } while(a); i--; while(i>=0) PC(s[i--]); PC('\n'); }
inline void prlong(ll a) { char s[20]; int i=0; do { s[i++]=a%10+'0'; a/=10; } while(a); i--; while(i>=0) PC(s[i--]); PC('\n'); }
void fastscan(int &x)
{
	bool neg=false;
	x =0;
	int c=getchar();
	if(c=='-')
	{
		neg = true;
		c=getchar();
	}
	for(;(c>47 && c<58);c=getchar())
		x = (x<<1) + (x<<3) +c -48;
	if(neg)
		x *=-1;
}

inline int two(int n)                                      { return 1 << n;          }
inline bool isPowerOfTwo(unsigned long long int n)         { return !(n&(n-1));      }
inline bool isSetBit(unsigned long long int n, int b)      { return (n>>b)&1;        }
inline void setBit(unsigned long long int & n, int b)      { n |=  two(b);           }
inline void clearBit(unsigned long long int & n, int b)    { n &= ~two(b);           }
inline void toggleBit(unsigned long long int &n, int b)    { n ^=  two(b);           }
inline void turnOffLastOne (unsigned long long int &n)     { n &= (n-1);             }
inline void turnOnLastZero(unsigned long long int &n)      { n |= (n+1);             }

inline void turnOffTrailingOnes(unsigned long long int &n) { n &= (n+1);             }
inline void turnOnTrailingZeros(unsigned long long int &n) { n |= (n-1);             }

inline int leastSignificantOne(unsigned long long int n)   { return n&-n;            }
inline void turnOffLastContiguousOnes(unsigned long long int n){ n &= ((n|(n-1))+1); }
inline bool is2jminus2k(unsigned long long int n)          { return !(((n|(n-1))+1)&n); }

inline int pop(unsigned long long int n) { short res = 0; while(n && ++res) n-=leastSignificantOne(n); return res; }

inline unsigned snoob(unsigned n)
{
	if(n==0) return 0;
	unsigned smallest,ripple,ones;	//n = xxx0 1111 0000

	smallest = n & -n;				//    0000 0001 0000
	ripple = n + smallest;			//    xxx1 0000 0000
	ones = n ^ ripple;				//    0001 1111 0000
	ones = (ones >> 2)/(smallest);	//    0000 0000 0111
	return ripple | ones;			//    xxx1 0000 0111
}

inline bool EQ(double a, double b) { return fabs(a-b) < EPS; }

class FenwickTree{//BinaryIndexedTree
	private:
		vector<int> ft;

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
		void adjust(int k, int v){
			for(;k <static_cast<int>(ft.size());k+=leastSignificantOne(k))
				ft[k]+=v;
		}
};

class UnionFindDisjointSet{
	private:
		struct node{
			long long int pset,rank;
		}node;
		vector<struct node> p;
		int _findSet(long int i) { return (p[i].pset==i) ? i :(p[i].pset = _findSet(p[i].pset)); }

	public:
		UnionFindDisjointSet(){}
		inline UnionFindDisjointSet(long long int _size){
			p.resize(_size);

			for(int i=0;i<_size;++i)
			{
				p[i].pset=i;
				p[i].rank=0;
			}
		}

		int findSet(int i){ return p[i].pset; }
		void unionSet(long long int i,long long int j){
			i=_findSet(i);
			j=_findSet(j);
			if( p[j].rank < p[i].rank )
				p[j].pset=i;
			else
				p[i].pset=j;
			if( p[i].rank == p[j].rank )
				p[j].rank=p[j].rank+1;
		}
		bool isSameSet(long long int i,long long int j) { return _findSet(i) == _findSet(j); }
		int sizeOfSet(long long int i){
			i=_findSet(i);
			int size=0;
			int n=p.size();
			for(int j=0;j<n;++j)
				if(_findSet(j)==i)
					++size;
			return size;
		}
		int numberOfSets()const{
			int num_sets=0;
			int n = p.size();
			for(int i=0;i<n;++i)
			{
				if(p[i].pset == i)
					++num_sets;
			}
			return num_sets;
		}
};

inline void make_set(vi& st){FOR(i,0,SZ(st))st[i]=i;}
inline int find_set(vi& st,int x){int y=x,z;while(y!=st[y])y=st[y];while(x!=st[x])z=st[x],st[x]=y,x=z;return y;}
inline bool union_set(vi& st,int a,int b){a=find_set(st,a),b=find_set(st,b);return a!=b?st[a]=b,true:false;}

inline void make_set(vpii& st){FOR(i,0,SZ(st))st[i]=make_pair(i,1);}
inline int find_set(vpii& st,int x){int y=x,z;while(y!=st[y].first)y=st[y].first;while(x!=st[x].first)z=st[x].first,st[x].first=y,x=z;return y;}
inline bool union_set(vpii& st,int a,int b){a=find_set(st,a),b=find_set(st,b);return a!=b?(st[a].second>st[b].second?st[a].first=b,st[a].second+=st[b].second:st[b].first=a,st[b].second+=st[a].second),true:false;}

struct Initializer{
#ifndef DEBUG
	Initializer(){ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);}
#else
	~Initializer(){/*runtime();*/}
#endif
}initializer;
/////////////////////////////////////////////////////////////////////

//convert string to int,double,float
template< typename T>
T strToNum(const st& str)
{
	stringstream ss(str);
	T tmp;
	ss >> tmp;

	if(ss.fail()){
		st s = "Unable to format";
		s += str;
		s += " as number";
		throw(s);
	}
	return tmp;
}//double d = strToNum<double>("7.0");

//Convert int to string
template < typename T >
st to_str(T str)
{
	stringstream stream;
	stream << str;
	return stream.str();
}//string str = to_str<int>(2.3);

lli seed;
mt19937 rng(seed=chrono::steady_clock::now().time_since_epoch().count());
inline lli rnd(lli l=0,lli r=INF)
{return uniform_int_distribution<lli>(l,r)(rng);}

//print pair surrounded by ()
template < typename F, typename S >
ostream& operator << ( ostream& os, const pair< F, S > & p ) {
	return os << "(" << p.first << ", " << p.second << ")"<<endl;
}

//print vector surrounded by {} and separated by ,
template < typename T >
ostream &operator << ( ostream & os, const vector< T > &v ) {
	os << "\n[";
	//typename vector< T > :: const_iterator it=v.begin();
	//if( !v.empty() )
	//	os<<*(v.begin());

	copy(v.begin(),v.end(),ostream_iterator<T>(os,", "));
	/*auto it = v.begin();
	for( ++it ; it != v.end(); ++it ) {
		os << ", "<<*it;
	}*/
	return os << "]"<<endl;
}

//print set surrounded by [] and separated by ,
template < typename T >
ostream &operator << ( ostream & os, const set< T > &v ) {
	os <<"\nSet[";
	copy(v.begin(),v.end(),ostream_iterator<T>(os,", "));
	//typename set< T > :: const_iterator it = v.begin();
	/*if( !v.empty() )
		os<<*(v.begin());
	auto it = v.begin();
	for ( ++it ; it != v.end(); ++it ) {
		os << ", "<<*it;
	}*/
	return os << "]"<<endl;
}

//print map surrounded by [] and separated by ,
template < typename F, typename S >
ostream &operator << ( ostream & os, const map< F, S > &v ) {
	os <<"\n{";
	//typename map< F , S >::const_iterator it=v.begin();
	if( !v.empty() )
		os<<v.begin()->first<<" = "<<v.begin()->second;
	//for_each(v.cbegin()+1,v.cend(),[](decltype(v[0]) it,ostream& os){ os<<", "<<it->first<<" = "<<it->second; });
	auto it=v.begin();
	for( ++it; it != v.end(); ++it ) {
		os <<", "<< it -> first << " : " << it -> second ;
	}
	return os << "}"<<endl;
}

ostream& operator << (ostream &os, const adjmat &mat)
{
	int n = mat.size();
	for(int i=0;i<n;++i)
	{
		os<<"\n";
		for(int j=0;j<n;++j)
			os<<mat[i][j]<<"  ";
	}
	return os<<endl;
}

ostream& operator<<(ostream& os,const adjlist &list )
{
	int n = list.size();
	for(int i=0;i<n;++i)
	{
		os<<"\n"<<i;
		for(auto elem=list[i].begin();elem!=list[i].end();++elem)
			os<<"->("<<elem->first<<","<<elem->second<<")";
	}
	return os<<endl;
}

//pass by value so that it can be emptied for display
ostream& operator<<(ostream& os,edgelist elist)
{
	while(!elist.empty())
	{
		auto elem = elist.top();
		elist.pop();
		os<<"\n["<<elem.first<<","<<elem.second.first<<"-"<<elem.second.second<<"]";
	}
	return os<<endl;
}

//Split String by Single Character Delimiter
vs split(const st& s, char delim=' ')
{
	vs elems;
	stringstream ss(s);
	st item;
	while (getline(ss, item, delim))
		elems.push_back(item);
	return elems;
}

//split string using more than one delims
vs split(const st str1,const st str2=" ")
{
	vs elems;
	auto itr = str1.begin();
	while(itr != str1.end())
	{
		auto itr2 = find_first_of(itr,str1.end(),str2.begin(),str2.end());
		if(itr2 != itr)
			elems.emplace_back(itr,itr2);
		itr = itr2+1;
	}
	return elems;
}

void toadjlist(adjlist &list,const adjmat &mat)
{
	int n = mat.size();
	list.resize(n);

	for(int i=0;i<n;++i)
	{
		for(int j=0;j<n;++j)
		{
			if(mat[i][j]!=0){
				list[i].emplace_back(j,mat[i][j]);
				list[i].push_back(make_pair(j,mat[i][j]));
			}
		}
	}
}

void toadjmat(adjmat &mat,const adjlist &list)
{
	int n = list.size();
	mat.resize(n);
	//adjmat mat(n,vector<int>(n,0));

	for(int i=0;i<n;++i)
	{
		for(auto elem = list[i].begin();elem != list[i].end();++elem)
		{
			mat[i][elem->first]=elem->second;
		}
	}
}

void toedgelist(edgelist &elist,const adjlist &list)
{
	int n = list.size();
	for(int i=0;i<n;++i)
	{
		for(auto elem=list[i].begin();elem!=list[i].end();++elem)
			elist.push(make_pair(elem->second,make_pair(i,elem->first)));
	}
}

void toedgelist(edgelist &elist,const adjmat &mat)
{
	int n = mat.size();
	for(int i=0;i<n;++i)
	{
		for(int j=0;j<n;++j)
		{
			if(mat[i][j]!=0)
				elist.push(make_pair(mat[i][j],make_pair(i,j)));
		}
	}
}

/*Below conversion cannot be exhaustively implemented as few data is
 * implicitly lost
 * 	# of vertices
 * 	isolated vertex
 */
void toadjlist(adjlist& list,const edgelist &elist)
{

}

void toadjmat(adjmat& mat,const edgelist &elist)
{

}

struct DeleteObject{
template<typename T>
		void operator()(const T* ptr)const{ delete ptr; }
};//for_each(container.begin(),container.end(),DeleteObject()) 
//used when container is of pointers which needs to be deleted explicitly

int main()
{
	time_t start = clock();
	//read("in.txt");
	//rite("out.txt");
	int test,kas=0;
	//cin>>test;
	map<int,int> mp;
	mp.insert(make_pair<int,int>(2,3));
	mp.insert(make_pair<int,int>(3,4));
	mp.insert(make_pair<int,int>(6,5));

	cout<<mp;
	test=0x7FFFFFFF;
	while(test--)
	{
		//start code here
		//snoob(0xF0);
		//cout<<"Case #"<<++kas<<":";
	}
	cerr<<"Program has run"<<(clock()-start)/*CLOCKS_PER_SEC*/<<" s"<<endl;
	cout<<min({1,2,3,4});
	return 0;
}
