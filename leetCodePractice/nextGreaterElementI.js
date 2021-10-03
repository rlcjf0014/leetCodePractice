/**
 * 496. Next Greater Element I
 */

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
 var nextGreaterElement = function(nums1, nums2) {
    return nums1.map(n => {
        let found = nums2.indexOf(n) + 1;
        if (found !== -1) {
            // find the next greater element's index
            while (nums2[found] < n) {
                found++
            };
            // -1 if not found
            if (found >= nums2.length) found = -1
            else found = nums2[found];  
             
        }
        
        return found;
    });
};