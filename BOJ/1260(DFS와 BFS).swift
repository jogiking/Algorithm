import Foundation

let input1 = readLine()!.split(separator: " ").map { Int($0)! }
let n = input1[0]
let m = input1[1]
let start = input1[2]

var graph = [[Int]](repeating: [], count: n + 1)
var visited = [Bool](repeating: false, count: n + 1)

for _ in (0..<m) {
    let tmp = readLine()!.split(separator: " ").map { Int($0)! }
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])
}

for i in (0..<graph.count) {
    graph[i].sort()
}

func reset() {
    for i in (0..<visited.count) {
        visited[i] = false
    }
}

var result1 = [Int]()
func dfs(v: Int) {
    visited[v] = true
    result1.append(v)
    for i in graph[v] {
        if !visited[i] {
            dfs(v: i)
        }
    }
}

var result2 = [Int]()
func bfs(v: Int) {
    var queue = [Int]()
    queue.append(v)
    visited[v] = true
    while !queue.isEmpty {
        let i = queue.removeFirst()
        result2.append(i)
        for item in graph[i] {
            if !visited[item] {
                queue.append(item)
                visited[item] = true
            }
        }
    }
}

dfs(v: start)
reset()
bfs(v: start)

for n in result1 {
    print(n, terminator: " ")
}
print()

for n in result2 {
    print(n, terminator: " ")
}
