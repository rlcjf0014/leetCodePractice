/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var isAnagram = function(s, t) {
    if (s.length !== t.length) {
        return false;
    }
    for (let i=0; i < s.length; i++) {
        t = t.replace(s[i], "");
    }
    return t.length === 0;
};