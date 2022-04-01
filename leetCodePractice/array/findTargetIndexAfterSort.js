/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var targetIndices = function(nums, target) {
    let newArr = nums.sort((a, b) => a - b);
    let result = [];
    for (let i =0; i < newArr.length; i++) {
        if (newArr[i] === target) {
            result.push(i);
        }
    }
    return result;
};