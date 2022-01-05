/**
 * @param {number[]} nums
 * @return {number}
 */
 var missingNumber = function(nums) {
    let maxNum = nums.length;
    let check = 0;
    for (let i = 0; i < maxNum; i++) {
        if (!nums.includes(check)) {
            return check;    
        }
        check+=1;
    }
    return maxNum;
};