/**
 * @param {string} s
 * @return {string}
 */
 var sortSentence = function(s) {
    let stringArr = s.split(" ");
    let result = [];
    for (let i = 0; i < stringArr.length; i++) {
        let num = stringArr[i][stringArr[i].length - 1];
        let newWord = stringArr[i].slice(0, stringArr[i].length - 1);
        result[num-1] = newWord;
    }
    
    return result.join(" ");
    
};