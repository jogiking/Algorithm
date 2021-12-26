// while문의 종료조건을 못보고 삽질함

import Foundation
typealias Position = (y: Int, x: Int)

while true {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    guard input != [0, 0] else {
        break
    }
    let width = input[0]
    let height = input[1]
    var map = [[Int]]()
    var visited = [[Bool]](repeating: [Bool](repeating: false, count: width), count: height)
    
    for _ in (0..<height) {
        map.append(readLine()!.split(separator: " ").map { Int(String($0))! })
    }
    
    func solution() -> Int {
        let dy = [0,0,-1,1,-1,1,-1,1]
        let dx = [1,-1,0,0,-1,1,1,-1]
        var ans = 0
        
        for row in (0..<height) {
            for col in (0..<width) {
                if visited[row][col] || map[row][col] == 0 {
                    continue
                }
                var queue: [Position] = [(y: row, x: col)]
                ans += 1
                
                while !queue.isEmpty {
                    let item = queue.removeFirst()
                    
                    for i in (0..<8) {
                        let next = Position(item.y + dy[i], item.x + dx[i])
                        if ((0..<width) ~= next.x && (0..<height) ~= next.y) &&
                              (!visited[next.y][next.x]) &&
                            (map[next.y][next.x] == 1) {
                            queue.append(next)
                            visited[next.y][next.x] = true
                        }
                    }
                }
            }
        }
        
        return ans
    }
    
    print(solution())
}
