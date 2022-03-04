/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
 var numJewelsInStones = function(jewels, stones) {
    let type = [];
    let count = 0;
    for (let i =0; i < jewels.length; i++) {
        if (!type.includes(jewels[i])) {
            type.push(jewels[i]);
        }
    }
    
    for (let i = 0; i < stones.length; i++) {
        if (type.includes(stones[i])) {
            count++;
        }
    }
    return count;
};