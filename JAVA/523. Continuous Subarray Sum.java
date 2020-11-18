/**
Given a list of non-negative numbers and a target integer k,
write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k,
that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 
Constraints:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
*/
class Solution {
//     public boolean checkSubarraySum(int[] nums, int k) {
     
//         return backtrack(nums, k, 0);
        
//     }
    
//     public boolean backtrack(int[]nums, int k, int start){
//         if(start>nums.length){
//             return false;
//         }
//         int sum = 0;
//         int count = 0;
//         for(int i = start; i<nums.length; i++){
//             sum+=nums[i];
//             count++;
//             if( count>1 && sum == k){ // case [0,0,0], k = 0
//                 return true;
//             }
            
//             if(count>1 && k!=0 && sum%k==0){  // case[1,2,3], k=0
//                 return true;
//             }
            
//         }
        
//         return backtrack(nums, k, start+1);
//     }

   public boolean checkSubarraySum(int[] nums, int k) {
        int sum = 0;
        HashMap < Integer, Integer > map = new HashMap < > ();
        map.put(0, -1);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (k != 0)
                sum = sum % k;
            if (map.containsKey(sum)) {
                if (i - map.get(sum) > 1)
                    return true;
            } else
                map.put(sum, i);
        }
        return false;
    }

}
