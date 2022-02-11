/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
 var containsNearbyDuplicate = function(nums, k) {
    let dict = {};
    
    
    nums.forEach((element, index) => {
        if (dict[element]) {
            dict[element].push(index);
        } else {
            dict[element] = [];
            dict[element].push(index);
        }
    })
    
    for (let key in dict) {
        if (dict[key].length > 1) {
            for (let i = 0; i < dict[key].length; i++) {
                for (let j = i+1; j < dict[key].length; j++) {
                    if (Math.abs(dict[key][i] - dict[key][j]) <= k) {
                            return true;
                    }   
                }
             }
        }
    }
    
    
    // for (let i = 0; i < nums.length; i++) {
    //     for (let j = i+1; j < nums.length; j++) {
    //         if (nums[i] === nums[j]) {
    //             if( Math.abs(i - j) <= k) {
    //                 return true;
    //             }
    //         }   
    //     }
    // }
    return false;
};