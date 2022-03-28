/**
 * @param {string} rings
 * @return {number}
 */
 var countPoints = function(rings) {
    
    let sum = 0;
    
    for (let i = 0; i < 10; i++) {
        if (rings.includes(`B${i}`) && rings.includes(`G${i}`) && rings.includes(`R${i}`)) {
            sum+=1;
        }
    }
    
    return sum;
    
};