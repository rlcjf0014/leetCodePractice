/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	            -1 if num is lower than the guess number
 *			             1 if num is higher than the guess number
 *                       otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n
 * @return {number}
 */
 var guessNumber = function(n) {
    let left = 1;
    let right = n;
    while (true) {
    const mid = Math.round((left + right) / 2);
    const result = guess(mid);
    if (result === 0) return mid;
    result === 1 ? left = mid + 1 : right = mid - 1;
  }  
};