#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
#include <algorithm>
using namespace std;

   
   
vector<vector<int>> threeSum(vector<int>& nums) {
    

    // make hashmap
    unordered_map<int, int> hashmap ;
    set<vector<int>> final ;

   

    for (int i =0; i < nums.size() ; i++){
        hashmap[nums[i]] = i;
    }
    for (int i = 0; i < nums.size(); i++){
        for (int j = i + 1 ; j < nums.size(); j++){
            if (hashmap.count( -1 * (nums[i] + nums[j])) && hashmap[-1 * (nums[i] + nums[j])] != i
                                                         && hashmap[-1 * (nums[i] + nums[j])] != j        
        )
            {
                int k = hashmap[-1 * (nums[i] + nums[j])];
                vector<int> triplet = {{nums[i], nums[j], nums[k]}};
                sort(triplet.begin(), triplet.end());
                final.insert(triplet);

            }
        }
    }

    return vector<vector<int>>(final.begin(), final.end());


}


int main(){


vector<int> nums  {-1,0,1,2,-1,-4} ;// [[-1,-1,2],[-1,0,1]]


vector<vector<int>> output = threeSum(nums);

for (const vector<int> & out : output){
    for (int num: out){
        cout << num << " ";
    }
    cout << " " << endl;
}

}