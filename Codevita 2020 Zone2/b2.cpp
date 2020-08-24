#include <bits/stdc++.h>
using namespace std;
#define scan(k)  for(auto &j:k) cin>>j;
#define vi vector<int>
// function to calculate
void funct(int j,vi &v1,int length,int z,int &required)
{
    if(j==length)
    {
        if(z==0) required++;
        return;
    }

    funct(j+1,v1,length,z+v1[j],required);
    funct(j+1,v1,length,z,required);
}
// main function
int main()
{
    
    int num;int co=0;cin>>num;
    vi a(num);scan(a);
    vi ar(num,0);
    int p=0,b=0;

    while(b<num)
    {
        if(a[b]>p)
            {p=a[b];}
        b++;
    }
    int flag=0;

    while(p>0)
    {
        flag++;
        p=p>>1;
    }

    for(int j=0;j<num;j++)
    {
        while(a[j]>0)
        {
            if(a[j]&1)  ar[j]++;
                a[j]=a[j]>>1;
        }
    }
    
    for(int k=0;k<num;k++)
    {
        ar[co]=flag-(2*ar[k]);
        if(ar[co]==0) continue;
        else co++;
    }

    int required=0;
    funct(0,ar,co,0,required);
    required-=1;
    required=(required*(1+num-co))+(1<<(num-co))-1;


    vi binary(flag,0); 
    int j=0;
    while (required > 0) 
    {
        binary[j] = required &1; 
        required = required>>1; 
        j++;
    } 

    // printing solutions
    for (int k = flag - 1; k >= 0; k--) 
        cout << binary[k];




    return 0;
}

