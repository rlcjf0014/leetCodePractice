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


    // If we take XOR of zero and some bit, it will return that bit
    // a \oplus 0 = aa⊕0=a
    // If we take XOR of two same bits, it will return 0
    // a \oplus a = 0a⊕a=0
    // a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
    let result = 0;
    for (let i=0; i < nums.length; i++) {
        result ^= nums[i];
    }
    return result;
};