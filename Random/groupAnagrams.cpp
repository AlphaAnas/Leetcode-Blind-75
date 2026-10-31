#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <map>
#include <algorithm>
using namespace std;

vector<vector<string>> groupAnagrams(vector<string> &strs)
{

    unordered_map<char, int> hashmap;
    for (int i = 0; i < 27; i++)
    {
        char alphabet = char((int)'a' + i);
        hashmap[alphabet] = i;
    }
    vector<vector<string>> finalOutput;
    map<vector<int>, vector<string>> check;
    for (const auto &str : strs)
    {

        vector<int> tuple;
        for (const auto &c : str)
        {
            tuple.push_back(hashmap[c]);
        }
        // sort the tuple;
        sort(tuple.begin(), tuple.end());
        if (check.count(tuple))
        { // if key already exists then append
            check[tuple].push_back(str);
        }
        else
        {
            check[tuple] = {str};
        }
    }
    for (const auto & val: check){
        finalOutput.push_back(val.second);
    }

    return finalOutput;
}

int main()
{

    vector<string> strs{"act", "pots", "tops", "cat", "stop", "hat"}; // Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

    vector<vector<string>> output = groupAnagrams(strs);

    for (const vector<string> &out : output)
    {
        cout << "[ ";
        for (const string &val : out)
        {
            cout << val << ", ";
        }
        cout << " ] " << endl;
    }
}