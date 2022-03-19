/**
 * @param {string} s
 * @return {string}
 */
 var toLowerCase = function(s) {
    // return s.toLowerCase();
    let result = "";
    
    for (let i = 0; i < s.length; i++) {
        let alphabet = s.charCodeAt(i);
        if (alphabet >= 65 && alphabet <= 90) {
            result +=(String.fromCharCode(alphabet + 32))  
        } else {
                result+=s[i];
            }
    }
    
    return result;
    
};