import Foundation
typealias Position = (y: Int, x: Int)

let numberOfCase = Int(readLine()!)!
for _ in (0..<numberOfCase) {
    let size = Int(readLine()!)!
    var map = [[Int]](repeating: [Int](repeating: 0, count: size), count: size)
    let start = readLine()!.split(separator: " ").map { Int(String($0))! }
    let end = readLine()!.split(separator: " ").map { Int(String($0))! }
    
    var queue: [Position] = [(start[0], start[1])]
    
    let dx = [1,2,2,1,-1,-2,-2,-1]
    let dy = [2,1,-1,-2,-2,-1,1,2]
    
    outer: while !queue.isEmpty {
        let item = queue.removeFirst()
        
        for i in (0..<8) {
            let next = Position(item.y + dy[i], item.x + dx[i])
            if !((0..<size) ~= next.y && (0..<size) ~= next.x) {
                continue
            }
            if map[next.y][next.x] > 0 {
                continue
            }
            if [next.y, next.x] == start {
                continue
            }
            if [next.y, next.x] == end {
                map[next.y][next.x] = map[item.y][item.x] + 1
                break outer
            }
            
            queue.append(next)
            map[next.y][next.x] = map[item.y][item.x] + 1
        }
    }
    
    print(map[end[0]][end[1]])
}
