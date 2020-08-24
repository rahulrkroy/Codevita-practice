#include <bits/stdc++.h>

using namespace std;

 

#define ull       unsigned long long int

#define ll        long long int

#define loop(i,s,e)     for(ll i=(s);i<(e);i++)

#define rloop(i,s,e)    for(ll i=(s);i>=(e);i--)

#define scan(any)       for(auto &i:any) cin>>i;

#define print(any)      for(auto i:any) cout<<i<<" "; nl;

#define nl              cout<<'\n'

#define pi 3.141592654

#define hell 1000000007

#define io ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)

#define fix(n) cout << fixed << setprecision(n)

#define input1(n) int n;cin>>n

#define input2(a, b) int a,b;cin>>a>>b

#define Max(a,b) ((a)>(b)?(a):(b))

#define Min(a,b) ((a)<(b)?(a):(b))

#define rep(i,a,b) for (__typeof((b)) i=(a);i<(b);i++)

#define ren(i,a,b) for(__typeof((a)) i=(a);i>=(b);i--)

#define mp make_pair

#define pb push_back

#define fi first

#define se second

#define vi vector<int>

#define pii pair<int,int>

#define piii pair<pair<int,int>,int>

#define all(v) (v).begin(), (v).end()

#define sz(x) (int)x.size()

#define set(a,n) memset(a,n,sizeof(a))










void methd(int l,vi &arr,int var1,int s,int &u)

{

if(l==var1)

{

if(s==0)

u++;

return;

}


methd(l+1,arr,var1,s+arr[l],u);

methd(l+1,arr,var1,s,u);

}



int main()

{

int n;

cin>>n;

vi av(n);

scan(av);

int m=0;


for(int i=0;i<n;i++)

{

if(av[i]>m)

m=av[i];

}

int incr=0;

while(m)

{

incr++;

m=m>>1;

}

vi arr(n,0);

for(int i=0;i<n;i++)

{

while(av[i])

{

if(av[i]&1)

arr[i]++;

av[i]=av[i]>>1;

}

}

int j=0;

for(int i=0;i<n;i++)

{

arr[j]=incr-2*arr[i];

if(arr[j]==0)

continue;

else

j++;

}

int v=0;

methd(0,arr,j,0,v);

v-=1;

v=v*(1+n-j)+(1<<(n-j))-1;

    vi bin(incr,0); 

    int pp=0;

    while (v > 0) { 

  

        bin[pp] = v &1; 

        v = v>>1; 

    pp++;

    } 

    for (int kk = incr - 1; kk >= 0; kk--) 

        cout << bin[kk]; 

return 0;

}