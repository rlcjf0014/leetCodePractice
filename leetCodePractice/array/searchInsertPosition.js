/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var searchInsert = function(nums, target) {
    const mid = Math.floor(nums.length / 2);
    let half1Start = 0;
    let half2Start = mid;
    let iteration = Math.round(nums.length / 2);
    while (half1Start < iteration) {
        if (nums[half1Start] >= target) {
            return half1Start;
        } 
        if (nums[half2Start] >= target && target > nums[half2Start-1]) {
            return half2Start;
        }
        half1Start++;
        half2Start++;
    }
    if (target < nums[0]) {
        return 0;
    }
    if (target > nums[nums.length-1]) {
        return nums.length;
    }
    
    return 0;
};