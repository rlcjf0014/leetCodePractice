/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
 var canVisitAllRooms = function(rooms) {
    
    const dfs = (currentRoom) => {
        currentRoom.forEach((key) => {
            if (!visited.has(key)) {
                visited.add(key);
                total += 1;
                dfs(rooms[key])
            }
        })
        
    }
    let visited = new Set();
    visited.add(0);
    let total = 0;
    
    dfs(rooms[0]);
    
    return total === rooms.length - 1 ? true : false;
};