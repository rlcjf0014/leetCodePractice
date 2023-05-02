const undirectedPath = (edges, nodeA, nodeB) => {
    const graph = createGraph(edges);
    return hasPath(graph, nodeA, nodeB, new Set());
  };
    
  const createGraph = (edges) => {
      let graph = {}
      for (let edge of edges){
        let first = edge[0]
        let second = edge[1]
        if (!(first in graph)) {
          graph[first] = []
        }
        if (!(second in graph)) {
          graph[second] = []
        }
        graph[first].push(second)
        graph[second].push(first)
      }
      return graph 
    }
    
  const hasPath = (graph, src, dst, visited) => {
    if (src === dst) return true;
    if (visited.has(src)) return false;
    visited.add(src);
    
    for (let neighbor of graph[src]) {
      if (hasPath(graph, neighbor, dst, visited) === true) {
        return true;    
      }
    }
    
    return false;
  };
  
  
  module.exports = {
    undirectedPath,
  };
  