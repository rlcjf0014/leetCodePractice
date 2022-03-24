/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
 var restoreString = function(s, indices) {
    
    let result = [];
    
    for (let i =0; i < s.length; i++) {
        let index = indices[i];
        result[index] = s[i];
    }
    
    return result.join("");
    
    
    
};