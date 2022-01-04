/**
 * @param {number} n
 * @return {number}
 */
 var climbStairs = function(n) {
    if (n < 4) {
        return n;
    }
    let sum=3, a=2, b=3;
    for (let i = 0; i < n-3; i++) {
        const c = a+b;
        sum += a;
        a = b;
        b = c;
    }
    return sum;
};