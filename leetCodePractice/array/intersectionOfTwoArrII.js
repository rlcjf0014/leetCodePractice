/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
 var intersect = function(nums1, nums2) {
    return nums1.filter(num => {
        let idx = nums2.indexOf(num);
        
        if(idx > -1) {
            nums2[idx]=null
            return true
        }
    })
};