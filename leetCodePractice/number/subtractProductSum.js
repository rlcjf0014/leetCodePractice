/**
 * @param {number} n
 * @return {number}
 */
 var subtractProductAndSum = function(n) {
    let digit = String(n).split("");
    let product = Number(digit[0]);
    let sum = Number(digit[0]);
    for (let i =1; i <digit.length; i++) {
        product*=Number(digit[i]);
        sum += Number(digit[i]);
    }
    return product - sum;
    
};