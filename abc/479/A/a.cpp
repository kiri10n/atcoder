#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int N;
    int ans=0;
    int a;
    
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>a;
        if(i%2==0) ans+=a;
    }

    cout << ans << endl;
    return 0;
}