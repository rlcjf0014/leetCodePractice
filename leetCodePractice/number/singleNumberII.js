/**
 * @param {number[]} nums
 * @return {number}
 */
 var singleNumber = function(nums) {
    let storage = {};
   for (let i=0; i < nums.length; i++) {
       if (!storage[nums[i]]) {
           storage[nums[i]] = 1;
       } else {
           storage[nums[i]]++
       }
   }
   for (let element in storage) {
       if (storage[element] === 1) {
           return element;
       }
   }
};