const hasPath = (graph, src, dst) => {
    if (src === dst) {
      return true
    }
    
    for (let neighbor of graph[src]) {
      if (hasPath(graph, neighbor, dst) === true) {
        return true;
      }
    }
    
    // const stack = [ src ]
    // while (stack.length > 0) {
    //   let curr = stack.pop()
    //   if (curr === dst) {
    //     return true
    //   }
    //   for (let neighbor of graph[curr]) {
    //     stack.push(neighbor)
    //   }
    // }
    return false
    
  };
  
  module.exports = {
    hasPath,
  };
  