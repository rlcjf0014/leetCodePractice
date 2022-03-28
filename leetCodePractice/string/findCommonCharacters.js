/**
 * @param {string[]} words
 * @return {string[]}
 */
 var commonChars = function(words) {
    let sorted = words.sort((a, b) => {
        return b.length - a.length;
    })
    
    let result = sorted[0].split('');
    
    
    for (let i = 1; i < sorted.length; i++) {
        let filtered = [];
        for (let j = 0; j < sorted[i].length; j++) {
            if (result.includes(sorted[i][j])) {
                filtered.push(sorted[i][j]);
                let index = result.indexOf(sorted[i][j]);
                result.splice(index, 1);
            }   
        }
        result = filtered;
    }
    
    return result;
};