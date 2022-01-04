/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLongestSubstring = function(s) {
    if (!s.length || s.length === 1) {
        return s.length;
    }
    let compare = s[0];
    let longest = compare; 
    for (let i = 1; i < s.length; i++) {
      if (!compare.includes(s[i])) {
        compare += s[i];
        if (longest.length >= s.length) {
            return longest.length;
        }
      } else {
          const location = compare.indexOf(s[i]);
          compare = compare.substring(location+1) + s[i];
      }
      longest = compare.length > longest.length ? compare : longest;
    }
    return longest.length;
};