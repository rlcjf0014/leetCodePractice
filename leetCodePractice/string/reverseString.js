/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
 var reverseString = function(s) {
    const copy = s.slice();
    for (let i = 0; i < s.length; i++) {
        s[i] = copy[s.length - (i+1)];
    }
};