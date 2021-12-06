/**
 * @param {number[]} nums
 * @return {number}
 */
 var majorityElement = function(nums) {
    let numberToPass = Math.floor(nums.length / 2)
    let numsRecord = nums.reduce((prev, next) => {
        if (next in prev) {
            prev[next]++;
        }
        else {
            prev[next] = 1;
        }
        return prev;
        }, {})
    for (let item in numsRecord) {
        if (numsRecord[item] > numberToPass) {
            return item;
        } 
    }
    
};