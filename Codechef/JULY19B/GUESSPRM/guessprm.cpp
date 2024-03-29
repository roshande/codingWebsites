/*
  Warn - Don't change next line else you will get WA verdict. Online Judge is configured to give WA if next line is not present.
  "An ideal problem has no test data."
  Author - Aryan Choudhary (@aryanc403)
*/

#pragma warning(disable:4996)
#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize ("Ofast")
#pragma GCC target ("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize ("-ffloat-store")

#include<iostream>
#include<bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define fo(i,n)   for(i=0;i<(n);++i)
#define repA(i,j,n)   for(i=(j);i<=(n);++i)
#define repD(i,j,n)   for(i=(j);i>=(n);--i)
#define pb push_back
#define mp make_pair
#define X first
#define Y second
// #define endl "\n"
typedef long long int lli;
typedef long double mytype;
typedef pair<lli,lli> ii;
typedef vector<ii> vii;
typedef vector<lli> vi;

clock_t time_p=clock();
void aryanc403()
{
    time_p=clock()-time_p;
    cerr<<"Time Taken : "<<(float)(time_p)/CLOCKS_PER_SEC<<"\n";
}

#ifdef ARYANC403
#define dbg(...) { cerr<<"[ "; __aryanc403__(#__VA_ARGS__, __VA_ARGS__);}
#undef endl
template <typename Arg1,typename Arg2>
ostream& operator << (ostream& out, const pair<Arg1,Arg2> &x) {
    return out<<"("<<x.X<<","<<x.Y<<")";
}

template <typename Arg1>
ostream& operator << (ostream& out, const vector<Arg1> &a) {
    out<<"[";for(const auto &x:a)out<<x<<",";return out<<"]";
}

template <typename Arg1>
ostream& operator << (ostream& out, const set<Arg1> &a) {
    out<<"[";for(const auto &x:a)out<<x<<",";return out<<"]";
}

template <typename Arg1,typename Arg2>
ostream& operator << (ostream& out, const map<Arg1,Arg2> &a) {
    out<<"[";for(const auto &x:a)out<<x<<",";return out<<"]";
}

template <typename Arg1>
void __aryanc403__(const string name, Arg1&& arg1){
	cerr << name << " : " << arg1 << " ] " << endl;
}

template <typename Arg1, typename... Args>
void __aryanc403__(const string names, Arg1&& arg1, Args&&... args){
	const string name = names.substr(0,names.find(','));
	cerr<<name<<" : "<<arg1<<" | ";
	__aryanc403__(names.substr(1+(int)name.size()), args...);
}

#else
    #define dbg(args...)
#endif

const lli INF = 0xFFFFFFFFFFFFFFFL;

lli seed;
mt19937 rng(seed=chrono::steady_clock::now().time_since_epoch().count());
inline lli rnd(lli l=0,lli r=INF)
{return uniform_int_distribution<lli>(l,r)(rng);}

class CMP
{public:
bool operator()(ii a , ii b) //For min priority_queue .
{    return ! ( a.X < b.X || a.X==b.X && a.Y <= b.Y);   }};

void add( map<lli,lli> &m, lli x,lli cnt=1)
{
    auto jt=m.find(x);
    if(jt==m.end())         m.insert({x,cnt});
    else                    jt->Y+=cnt;
}

void del( map<lli,lli> &m, lli x,lli cnt=1)
{
    auto jt=m.find(x);
    if(jt->Y<=cnt)            m.erase(jt);
    else                      jt->Y-=cnt;
}

bool cmp(const ii &a,const ii &b)
{
    return a.X<b.X||(a.X==b.X&&a.Y<b.Y);
}
#ifdef ARYANC403
const bool db=true;
#else
const bool db=false;
#endif

lli mod = 1000000007L;

    lli T,n,i,j,k,in,cnt,l,r,u,v,x,y;
    lli m;
    string s;
    vi a;
    //priority_queue < ii , vector < ii > , CMP > pq;// min priority_queue .

lli prt(lli x,lli t=1)
{
    cout<<t<<" "<<x<<endl;
    if(t==1)
    {

        if(db)
            return x*x%mod;

        cin>>x;
        if(x==-1)
            exit(0);
        return x;
    }
    else
    {
        if(db)
        {
            dbg(mod,x);
            if(x!=mod)
                dbg("Fail");
            return true;
        }

        cin>>s;
        if(s=="No"||s=="N")
            exit(0);
        return true;
    }
}

const lli M1=500111;
const lli M2=1009;

vi decomp(lli m,vi bb)
{
    vi a;
    lli n=prt(m),i,lim=1;
    if(n==0)
        n=m;
    else
    {
        n=m*m-n;
        if(n==0)
        {
            lim=m*m;
            for(auto x:bb)
                if(x>lim)
                    a.pb(x);
            return a;
        }
    }
    a.clear();
    for(i=2;i*i<=n;++i)
    {
        if(n%i)
            continue;

        if(i>lim)
            a.pb(i);

        while(n%i==0)
            n/=i;
    }

    if(n>1)
        a.pb(n);
    return a;
}

bool chk(vi a,lli n,bool fl=false)
{
    map<lli,lli> m;
    for(auto x:a)
        m[(n*n)%x]++;

    return (lli)m.size()==(lli)a.size();
}

int main(void) {
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    // freopen("txt.in", "r", stdin);
    // freopen("txt.out", "w", stdout);
// cout<<std::fixed<<std::setprecision(35);
cin>>T;while(T--)
{
    if(db)
    {
        dbg("MOD");
        cin>>mod;
    }

    lli m=M1;//+rnd(1,10);
    vi a=decomp(1LL<<15,{});

    if((lli)a.size()<2)
    {
        prt(a[0],2);
        continue;
    }

    dbg(a);
    vi b;

    for(lli i=2;i<=100000;++i)
    {
        if(chk(a,i))
        {
            chk(a,i,true);
            b=decomp(i,a);
            break;
        }
    }

    lli ans=0;
    for(auto x:a)
    {
        for(auto y:b)
        {
            if(x==y)
                ans=x;
        }
    }

    dbg(a,b);
    prt(ans,2);

}   aryanc403();
    return 0;
}