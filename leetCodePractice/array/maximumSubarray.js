/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
    let max = -Infinity;
    let currentMax = 0;
    
    for(let i = 0; i < nums.length; i++) {
        currentMax = Math.max(nums[i], currentMax + nums[i]);
        max = Math.max(currentMax, max);               
    }
    
    return max;
};