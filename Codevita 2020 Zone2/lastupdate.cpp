#include <bits/stdc++.h>

using namespace std;

int main()
 {

    int x;

    string sour;

    cin>>x>>sour;

    vector<pair<int,int>> arr(x,{INT_MAX,INT_MAX});
    int av=0;
    while(av<x)

    {

        if(sour[av]=='A')

            {

                int l=0;

                int z=av-1;

                if(z>=0)

                    {

                        while(z>=0)

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
                        z--;

                    }

         }

         else if(sour[av]=='B')

            {

                int l=0;

                int z=av+1;

                if(z<x)

                    {

                            while(z<x)

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
                            z++;

                        }

            }  
        av++; 

    }

    int puja_mcount=0;

    int pujb_ncount=0;
    int nd=0;
    while(nd<x)

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
            nd++;

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