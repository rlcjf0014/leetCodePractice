/**
 * @param {string[]} wordsDict
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
 var shortestDistance = function(wordsDict, word1, word2) {
    let word1Index = [];
    let word2Index = [];
    for (let i = 0; i < wordsDict.length; i++) {
        if (wordsDict[i] === word1) {
            word1Index.push(i);
        } 
        if (wordsDict[i] === word2) {
            word2Index.push(i);
        }
    }
    let result = null;
    
    word2Index.forEach((element) => {
        word1Index.forEach((num) => {
          if (result === null || Math.abs(element - num) < result) {
              result = Math.abs(element-num)
          }  
        })
    })
    return result;
    
    
    
    
};