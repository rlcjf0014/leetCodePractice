/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
 var getSum = function(a, b) {
    if (a === 0) {
        return b;
    } 
    if (b === 0) {
        return a;
    }
    let absValueA = Math.abs(a);
    let absValueB = Math.abs(b);
    if ((a<0 && b<0) || (a>0 && b>0)) {
        let sign = a < 0 ? "-" : "";
        return Number(sign+new Array(absValueA).concat(new Array(absValueB)).length); 
    }
    else if (a < 0) {
        let sign = absValueA > absValueB ? "-":"";
        let biggerValue = absValueA > absValueB ? absValueA:absValueB;
        let smallerValue = absValueA > absValueB ? absValueB:absValueA;
        return Number(sign + new Array(biggerValue).slice(smallerValue).length);
    }
    else {
        let sign = absValueB > absValueA ? "-":"";
        let biggerValue = absValueA > absValueB ? absValueA:absValueB;
        let smallerValue = absValueA > absValueB ? absValueB:absValueA;
        return Number(sign + new Array(biggerValue).slice(smallerValue).length);
    }
};

// var getSum = function(a, b) {
//     if(b === 0) {
//         return a;
//     }
//     return getSum(a ^ b, (a & b) << 1);
// };