/**
 * @param {number} n
 * @return {number[]}
 */
 var sumZero = function(n) {
    let numRef = []
    let i = -(n - 1)
    while (i <= n) {
        numRef.push(i)
        i += 2
    }
    return numRef
};