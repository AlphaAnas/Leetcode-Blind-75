#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
        
    unordered_map<int, int> dict;

    for (int i = 0; i< nums.size(); i++){
        dict[nums[i]] = i;
    }

    for (int i = 0; i< nums.size(); i++){
    
        int diff = target - nums[i];
        if (dict.count(diff) && dict[diff] != i){
            return {i, dict[diff]};
        }
    
    }
    return {};
}



int main(){
    vector<int> nums  {2,5,5,11};
    int target = 10; // Output: [1,2]
    vector<int> output = twoSum(nums,target);

    for (const int &ele : output) {
        std::cout << ele << " " ;
    }
    std::cout << std::endl;
}


