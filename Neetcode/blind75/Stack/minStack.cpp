

class MinStack {
    int len = 100;
    int *array = new int[len] ;
    int *minArray = new int[len];
    int size;
public:
    MinStack() {
        size = 0;
    }
    
    
    void push(int val) {

        // we need to check and update the size of the array
        if (size == len - 4) {
            int newLen = len * 2;
            int *newArray = new int[newLen];
            int *newMin = new int[newLen];
            

            for (int i = 0; i < size ; i++){
                newArray[i] = array[i];
                newMin[i] = minArray[i];
            }

            delete []minArray;
            delete []array;

            minArray = newMin;
            array = newArray;
            len = newLen;


        }


        array[size] = val;
        minArray[size] = (size == 0 || minArray[size - 1] > val)  ? val : minArray[size - 1];
        ++size;
    }
    
    void pop() {
        size = size -1;
    }
    
    int top() {
        return array[size - 1];        
    }
    
    int getMin() {
        return minArray[size - 1];
    }
};