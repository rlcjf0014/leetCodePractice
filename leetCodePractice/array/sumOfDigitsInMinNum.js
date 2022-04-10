/**
 * @param {number[]} nums
 * @return {number}
 */
 var sumOfDigits = function(nums) {
    nums.sort((a, b) => a - b);
    let digits = String(nums[0]);
    
    let sum = 0;
    for (let i =0; i < digits.length; i++) {
        sum += Number(digits[i]);    
    }
    
    return sum % 2 === 0 ? 1 : 0;
};