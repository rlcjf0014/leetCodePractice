/**
 * @param {string} sentence
 * @return {boolean}
 */
 var checkIfPangram = function(sentence) {
    const result = [];
    for (let i =0; i < sentence.length; i++) {
        if (!result.includes(sentence[i])) {
            result.push(sentence[i]);
        }
    }
    const truResult = result.sort();
    const alpha = 'abcdefghijklmnopqrstuvwxyz';
    return alpha === truResult.join('') ? true : false;
    
    
};