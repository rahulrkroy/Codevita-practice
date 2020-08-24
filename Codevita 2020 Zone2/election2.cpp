#include <bits/stdc++.h>

using namespace std;

int main() {

int x;

string sour;

cin>>x>>sour;

vector<pair<int,int>> arr(x,{INT_MAX,INT_MAX});

for(int av=0;av<x;av++)

{

if(sour[av]=='A')

{

int l=0;

int z=av-1;

if(z>=0)

{

for(z;z>=0;z--)

{

if(sour[z]=='-')

{

arr[z].first=min(arr[z].first,l);

}

else if(sour[z]=='A'||sour[z]=='B')

{

break;

}

++l;

}

}

}

else if(sour[av]=='B')

{

int l=0;

int z=av+1;

if(z<x)

{

for(z;z<x;z++)

{

if(sour[z]=='-')

{

arr[z].second = min(arr[z].second,l);

}

else if(sour[z]=='B'||sour[z]=='A')

{

break;

}

l++;

}

}

}

}

int puja_mcount=0;

int pujb_ncount=0;

for(int nd=0;nd<x;nd++)

{

int p = arr[nd].first;

int q = arr[nd].second;

if(sour[nd]=='A')

{

puja_mcount++;

}

else if(sour[nd]=='B')

{

pujb_ncount++;

}

if(sour[nd]=='-')

{

if(p>q)

{

pujb_ncount++;

}

else if(p<q)

{

puja_mcount++;

}

}

}

if(puja_mcount>pujb_ncount)

{

cout<<"A";

}

else if(pujb_ncount>puja_mcount)

{

cout<<"B";

}

else

{

cout<<"Coalition government";

}

}