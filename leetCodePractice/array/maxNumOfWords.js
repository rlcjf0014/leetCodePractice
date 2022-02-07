/**
 * @param {string[]} sentences
 * @return {number}
 */
 var mostWordsFound = function(sentences) {
    let result = 0;
    sentences.forEach((element) => {
        let arr = element.split(" ");
        if (arr.length > result) {
            result = arr.length;
        }
    });
    return result;
};