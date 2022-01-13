/**
 * @param {number[]} nums
 * @return {number}
 */
 var arraySign = function(nums) {
    let result = nums[0];
    for (let i =1; i < nums.length; i++) {
        result *= nums[i];
    }
    if (result > 0) {
        return 1;
    } 
    if (result < 0) {
        return -1;
    }
    return 0;
    
};