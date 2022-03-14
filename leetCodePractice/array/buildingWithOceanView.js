/**
 * @param {number[]} heights
 * @return {number[]}
 */
 var findBuildings = function(heights) {
    let result = heights;
    
    for (let i = 0; i < heights.length; i++) {
        for (j = i+1; j < heights.length; j++) {
            if (heights[j] > heights[i]) {
                let index = result.indexOf(heights[i]);
                if (index > -1) {
                    array.splice(index, 1); // 2nd parameter means remove one item only
                }
                continue;
            }
        }
    
};