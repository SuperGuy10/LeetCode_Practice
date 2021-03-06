/**
69. Sqrt(x)
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
*/

class Solution {
    public int mySqrt(int x) {
        // if(x==0){
        //     return 0;
        // }else if(x<4){
        //     return 1;
        // }
        // int ans = 0;
        // for(int i = 1; i<=x/2; i++){
        //     if(i*i<=x && i*i>ans){
        //         ans = i;
        //     }else{
        //         break;
        //     }
        // }
        // return ans;
        
        if(x == 0){
            return x;
        }
        
        int left = 1;
        int right = Integer.MAX_VALUE;
        
        while(left<right){
            int mid = left+(right-left)/2;
            if(mid>x/mid){//do not use mid*mid may cause over range
                right = mid - 1;
            }else{
                if(mid+1>x/(mid+1)){
                    return mid;
                }else{
                    left = mid+1;
                }
                
                
            }
        }
        return left;
        
    }
}
