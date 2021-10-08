/**
 * Choose time over splace
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate1 = function(nums) {
    let obj = {};
    for (let i = 0; i < nums.length; i++) {
        if (!obj[nums[i]]) {
            obj[nums[i]] = 1;
        } else if (obj[nums[i]]) {
            obj[nums[i]]++
            if (obj[nums[i]] > 1) {
             return true;   
            }
        }
    }
    return false;
};

/**
 * Choose space over time complexity
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate2 = function(nums) {
    while(nums.length) {
        const whut = nums.pop();
        if (nums.find(element => element === whut) !== undefined) return true;
    }
    return false;
};

/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate3 = function(nums) {
    let obj = {};
    for (let i = 0; i < nums.length; i++) {
        if (obj[nums[i]]) return true;   
        if (!obj[nums[i]]) obj[nums[i]] = 0;   
        obj[nums[i]]++
    }
    return false;
};