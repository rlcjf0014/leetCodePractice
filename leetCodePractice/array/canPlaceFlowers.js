/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
 var canPlaceFlowers = function(flowerbed, n) {
    let count = n;
    
    for (let i = 0; i < flowerbed.length; i++) {
        if (count === 0) {
            return true;
        }
        if (flowerbed[i] === 0) {
            if (flowerbed[i-1]) {
                if (flowerbed[i-1] === 1) {
                    continue;
                }
            }
            if (flowerbed[i+1]) {
                if (flowerbed[i+1] === 1) {
                    continue;
                }
            }
            count--;
            flowerbed[i] = 1;
        } else {
            continue;
        }
    }
    
    return count === 0 ? true: false;
    
    
};