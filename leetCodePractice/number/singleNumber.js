/**
 * @param {number[]} nums
 * @return {number}
 */
 var singleNumber = function(nums) {
    // Space Complexity
    // for (let i=0; i < nums.length; i++) {
    //     if (nums.indexOf(nums[i]) === nums.lastIndexOf(nums[i])) {
    //         return nums[i];
    //     }
    // }
    
    // Time Complexity
    // let storage = {};
    // for (let i=0; i < nums.length; i++) {
    //     if (!storage[nums[i]]) {
    //         storage[nums[i]] = 1;
    //     } else {
    //         storage[nums[i]]++
    //     }
    // }
    // for (let element in storage) {
    //     if (storage[element] === 1) {
    //         return element;
    //     }
    // }

    let result = 0;
    for (let i=0; i < nums.length; i++) {
        result ^= nums[i];
    }
    return result;
};