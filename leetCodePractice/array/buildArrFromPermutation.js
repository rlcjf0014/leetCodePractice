/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var buildArray = function(nums) {
    let result = [];
    
    for (let i = 0; i < nums.length; i++) {
        let value = nums[nums[i]];
        result.push(value);
    }

    return result;
    
};