/**
 * @param {number[][]} accounts
 * @return {number}
 */
 var maximumWealth = function(accounts) {
    
    const getWealth = (wealth) => {
    let sum = 0;
    for (let i = 0; i < wealth.length; i++) {
        sum += wealth[i];
    }
    return sum;
    }
    
    let max = 0;
    for (let i = 0; i < accounts.length; i++) {
        let sum = getWealth(accounts[i]);
        if (sum > max) {
            max = sum;
        }
    }
    return max;
};


