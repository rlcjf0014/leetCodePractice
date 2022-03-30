/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
 var kidsWithCandies = function(candies, extraCandies) {
    let max = Math.max(...candies);
    
    return candies.map((num) => {
        if ((num + extraCandies) >= max) {
            return true;
        } else {
            return false;
        }   
    })
    
};