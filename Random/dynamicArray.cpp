#include <iostream>
using namespace std;
// /**
//  * 
//  * 
//  Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.
 
//  Your DynamicArray class should support the following operations:
 
//  DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
//  int get(int i) will return the element at index i. Assume that index i is valid.
//  void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
//  void pushback(int n) will push the element n to the end of the array.
//  int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
//  void resize() will double the capacity of the array.
//  int getSize() will return the number of elements in the array.
//  int getCapacity() will return the capacity of the array.
//  If we call pushback(int n) but the array is full, we should resize() the array first.
 
//  Note:
 
//  The index i provided to get(int i) and set(int i) is guaranteed to be greater than or equal to 0 and less than the number of elements in the array.

//  */ 




class DynamicArray {
public:
    int *da;
    int final_element = 0; // number of elements in the array
    int size = 0; // size of the array

    DynamicArray(int capacity) {
        da = new int[capacity];
        size = capacity;
    }

    int get(int i) {
        // for (int i = 0 ; i < capacity; i ++)
        //      cout << "\n value at index [" << i << "] is : " << da[i] ;
        return da[i];
    }

    void set(int i, int n) {
        da[i] = n;
    }

    void pushback(int n) {

        if (final_element == size)
            resize();
        da[final_element ] = n;
        final_element += 1; 
    }

    int popback() {
        int ele = da[final_element - 1];
        final_element -= 1;
        return ele;

    }

    void resize() {
        int * new_da = new int[size * 2];
        for (int i = 0 ; i < final_element; i ++){
            new_da[i] = da[i];
        }
        delete[] da;
        da = new_da;
        size *= 2;

    }

    int getSize() {
        // return the no. of elements in the arrray
        return final_element;
    }
    
    int getCapacity() {
        // retur nthe capacity of the array
        return size;
    }
};




int main() {
    DynamicArray arr(1);
    
    std:: cout << "=============================" << std:: endl;

    std::cout << "getSize: " << arr.getSize() << std::endl;      // Output: 0
    std::cout << "getCapacity: " << arr.getCapacity() << std::endl; // Output: 1
    
    // Example 2 operations:
    std:: cout << "=============================" << std:: endl;
    arr.pushback(1);
    std::cout << "getCapacity after first pushback: " << arr.getCapacity() << std::endl; // Output: 1
    arr.pushback(2);
    std::cout << "getCapacity after second pushback: " << arr.getCapacity() << std::endl; // Output: 2
    
    // Example 3 operations:
    std:: cout << "=============================" << std:: endl;

    std::cout << "getSize: " << arr.getSize() << std::endl;      // Output: 2
    std::cout << "getCapacity: " << arr.getCapacity() << std::endl; // Output: 2
    std::cout << "\n get(1): " << arr.get(1) << std::endl;           // Output: 2
    arr.set(1, 3);
    std::cout << "\n get(1) after set: " << arr.get(1) << std::endl; // Output: 3
    std::cout << "popback: " << arr.popback() << std::endl;        // Output: 3
    std::cout << "getSize after popback: " << arr.getSize() << std::endl;      // Output: 1
    std::cout << "getCapacity after popback: " << arr.getCapacity() << std::endl; // Output: 2
    std:: cout << "=============================" << std:: endl;

    return 0;
}

