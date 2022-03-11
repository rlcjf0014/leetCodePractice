/**
 * @param {number} numRows
 * @return {number[][]}
 */
 var generate = function(numRows) {
    const res=[]
    
    res.push([1]); 
    
    for(let i=1;i<numRows;i++){ 
        const temp=[]
        temp.push(1)
        for(let j=1;j<i;j++){
            temp.push(res[i-1][j-1]+res[i-1][j]) 
        }
        temp.push(1) 
        res.push(temp)
    }
    
    return res
};