#include <bits/stdc++.h>

using namespace std;

int main() {

int n;

string spi;

cin>>n>>spi;

vector<pair<int,int>> finder(n,{INT_MAX,INT_MAX});

for(int ms=0;ms<n;ms++)

{

if(spi[ms]=='A')


{

int t=0;

int j=ms-1;

if(j>=0)

{

for(j;j>=0;j--)

{

if(spi[j]=='-')

{

finder[j].first=min(finder[j].first,t);

}

else if(spi[j]=='A'||spi[j]=='B')

{

break;

}

++t;

}

}

}

else if(spi[ms]=='B')

{

int t=0;

int j=ms+1;

if(j<n)

{

for(j;j<n;j++)

{

if(spi[j]=='-')

{

finder[j].second = min(finder[j].second,t);

}

else if(spi[j]=='B'||spi[j]=='A')

{

break;

}

t++;

}

}

}

}

int cana_count=0;

int canb_count=0;

for(int mt=0;mt<n;mt++)

{

int x = finder[mt].first;

int y = finder[mt].second;

if(spi[mt]=='A')

{

cana_count++;

}

else if(spi[mt]=='B')

{

canb_count++;

}

if(spi[mt]=='-')

{

if(x>y)

{

canb_count++;

}

else if(x<y)

{

cana_count++;

}

}

}

if(cana_count>canb_count)

{

cout<<"A";

}

else if(canb_count>cana_count)

{

cout<<"B";

}

else

{

cout<<"Coalition government";

}

}