/**
 * @param {string} keyboard
 * @param {string} word
 * @return {number}
 */
 var calculateTime = function(keyboard, word) {
    let curr = 0;
    let sum = 0;
    for (let i = 0; i < word.length; i++) {
        let index = keyboard.indexOf(word[i]);
        sum += Math.abs(curr - index);
        curr = index;
    }
    
    return sum;
    
    
};