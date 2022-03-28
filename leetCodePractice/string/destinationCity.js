/**
 * @param {string[][]} paths
 * @return {string}
 */
 var destCity = function(paths) {
    let check = [];
    
    for (let i =0; i < paths.length; i++) {
        check.push(paths[i][0]);
    }
    
    for (let i =0; i < paths.length; i++) {
        if (!check.includes(paths[i][1])) {
            return paths[i][1];
        };
    }
    
};