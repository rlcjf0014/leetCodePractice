/**
 * @param {number} n
 * @return {boolean}
 */
 var isHappy = function(n) {
    if (n === 1) {
        return true;
    }
    if (String(Math.pow(n,2)).length < 2) {
        return false;
    }
    let sum = 0;
    let digits = String(n).split("");
    let checkAnswer = [];
    while (sum !== 1 && !checkAnswer.includes(n)) {
        digits.map((element) => {
            sum += Math.pow(Number(element),2);
        })
        if (sum === 1) {
            return true;
        } else {
            checkAnswer.push(n);
            n = sum;
            digits = String(sum).split("");
            sum = 0;
        }
    }
    return false;
};