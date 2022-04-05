/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
 var countConsistentStrings = function(allowed, words) {
    let result = 0;
    
    for (x of words) {
        let i = 0;
        let consistency = true;
        while(i < x.length) {
            if (!allowed.includes(x[i])) {
                consistency = false;
                break;
            }
            i++;
        }
        if (consistency) {
            result++;
        }
    }
    
    return result;
};