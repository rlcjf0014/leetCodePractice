/**
 * @param {number[]} heights
 * @return {number[]}
 */
 var findBuildings = function(heights) {
    const ans = [];
    let max = 0;
    for (let i = heights.length - 1; i >= 0; i -= 1) {
      if (max < heights[i]) {
        ans.unshift(i);
        max = heights[i];
      }
    }
    return ans;
      
  };