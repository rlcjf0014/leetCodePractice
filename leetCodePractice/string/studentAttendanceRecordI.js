/**
 * @param {string} s
 * @return {boolean}
 */
 var checkRecord = function(s) {
    let absence = 0;
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === "A") {
            absence++;
        }
    }
    
    if (absence < 2 && !s.includes("LLL")) {
        return true;
    } else {
        return false;
    }
};