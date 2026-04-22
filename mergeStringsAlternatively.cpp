
#include <bits/stdc++.h>
using namespace std;




string mergefunction(string word1, string word2){
        int short_len = word1.size() < word2.size() ? word1.size() : word2.size();
        string merged = "";
        for (int i = 0; i < short_len; i++){

            merged += word1[i];
            merged += word2[i];

        }

        if (short_len == word1.size()) merged+= word2.substr(word1.size());
        if (short_len == word2.size()) merged+= word1.substr(word2.size());
        

        return merged;


}
string mergeAlternately(string word1, string word2);

#ifndef LEETCODE
class Solution {
public:
    // cout << "LEETCODE";
    string mergeAlternately(string word1, string word2) {


        string merged = mergefunction(word1, word2);
        return merged;
     
        
    }
};


#else
int main(){
        // cout << "LOCAL";
        string out = mergefunction("ab", "pqr");
        cout << "Output :" << out << "\n" ;
}

#endif