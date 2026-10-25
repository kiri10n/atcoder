#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

int main(){
    int n, k;
    std::cin >> n >> k;
    std::string s;
    std::cin >> s;

    std::sort(s.begin(), s.end()); 

    int ans = 0;
    do{
        bool include_palindrome = false;
        for(int i = 0; i < n-k+1; i++){
            std::string sub_s = s.substr(i, k);
            if(sub_s == std::string(sub_s.rbegin(), sub_s.rend())){
                include_palindrome = true;
                break;
            }
        }
        if(!include_palindrome) ans++;
    } while (std::next_permutation(s.begin(), s.end()));

    std::cout << ans << std::endl;
    
    return 0;
}