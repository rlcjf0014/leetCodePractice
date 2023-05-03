const largestComponent = (graph) => {
    const visited = new Set();
    let largest = 0;
    for (let node in graph) {
      let sizeComponents = explore(graph, node, visited)
      if (sizeComponents > largest) {
        largest = sizeComponents
      }
    }
    return largest;
  };
  
  const explore = (graph, current, visited) => {
    if (visited.has(current)) {
      return 0
    }
    visited.add(String(current));
  
    let size = 1;
    for (let neighbor of graph[current]) {
      size += explore(graph, neighbor, visited);
    }
    return size;
  }
  
  module.exports = {
    largestComponent,
  };
  