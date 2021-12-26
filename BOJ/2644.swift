import Foundation

let n = Int(readLine()!)!
let target = readLine()!.split(separator: " ").map { Int(String($0))! }
let relationSize = Int(readLine()!)!
var map = [[Int]](repeating: [0], count: n+1)

for _ in (0..<relationSize) {
    let input = readLine()!.split(separator: " ").map{ Int(String($0))! }
    map[input[0]].append(input[1])
    map[input[1]].append(input[0])
}

var queue = [target[0]]
outer: while queue.isEmpty == false {
    let item = queue.removeFirst()
    
    for i in (1..<map[item].count) {
        let next = map[item][i]
        if next == target[1] {
            map[target[1]][0] = map[item][0] + 1
            break outer
        }
        if map[next][0] > 0 || next == target[0] {
            continue
        }
        queue.append(map[item][i])
        map[next][0] = map[item][0] + 1
    }
}

let ans = map[target[1]][0] == 0 ? -1 : map[target[1]][0]
print(ans)
