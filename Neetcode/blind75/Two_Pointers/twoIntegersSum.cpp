// # '''
// # Two Integer Sum II
// # Medium
// # Topics
// # Company Tags
// # Hints
// # Given an array of integers numbers that is sorted in non-decreasing order.

// # Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

// # There will always be exactly one valid solution.

// # Your solution must use 
// # O
// # (
// # 1
// # )
// # O(1) additional space.

// # '''

// #  C ++ VERSION:
#include <iostream>
#include <vector>

std::vector<int> twoSum(std::vector<int>& numbers, int target) {

    int l = 0, r = numbers.size() - 1;
    while( l < r){
        if (numbers[l] + numbers[r] == target) 
            return std::vector<int> {l+1, r+1};
        else if (numbers[l] + numbers[r] < target)
            l += 1;
        else if (numbers[l] + numbers[r] > target)
            r -= 1;
    
    }
    return std::vector<int> {};


}


std::vector<int> numbers = {1,2,3,4};
int target = 3;

int main() {
    auto result = twoSum(numbers, target);
    std::cout << '[' << result[0] << ',' << result[1] << ']';
    return 0;
}