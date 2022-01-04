/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLastWord = function(s) {
    let returnWord = "";
    const trimmed = s.trim();
    for (let i = trimmed.length-1; i>=0; i--) {
        if (trimmed[i] === " ") {
           break;
        }
        returnWord += trimmed[i];
    }
    return returnWord.length;
};