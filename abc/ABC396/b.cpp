#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <stack>
using namespace std;

int main(){
    int q;
    cin >> q;

    stack<int> cards;
    for(int i=0; i<100; i++){
        cards.push(0);
    }

    for(int i=0; i<q; i++){
        int type;
        cin >> type;

        if(type == 1){
            int x;
            cin >> x;
            cards.push(x);
        } else {
            cout << cards.top() << endl;
            cards.pop();
        }
    }

    return 0;
}