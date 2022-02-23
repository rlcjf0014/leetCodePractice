/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var backspaceCompare = function(s, t) {
    if (s === t) {
        return true;
    }
    
    const resultS = [];
    const resultT = [];
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === "#") {
            resultS.pop();
        } else {
            resultS.push(s[i]);
        }
    }
    
    for (let i = 0; i < t.length; i++) {
        if (t[i] === "#") {
            resultT.pop();
        } else {
            resultT.push(t[i]);
        }
    }
    
    return resultS.join("") === resultT.join("");
    
};