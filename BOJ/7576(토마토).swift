import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let col = input[0], row = input[1]
var board = [[Int]](repeating: [], count: row)
var queue = Queue<(Int, Int, Int)>()

var days = [[Int]](repeating: [Int](repeating: 0, count: col), count: row)
for y in (0..<row) {
    board[y] = readLine()!.split(separator: " ").map{Int(String($0))!}
    for x in (0..<board[y].count) {
        if board[y][x] == 1 {
            queue.pushBack((y,x,0))
        }
    }
}

let dy = [0,0,1,-1]
let dx = [1,-1,0,0]

while queue.isEmpty == false {
    let (y, x, day) = queue.popLeft()!

    for i in (0..<dy.count) {
        let ny = y + dy[i], nx = x + dx[i]

        if (0..<row) ~= ny && (0..<col) ~= nx && board[ny][nx] == 0 {
            days[ny][nx] = day+1
            board[ny][nx] = day+1
            queue.pushBack((ny,nx,day+1))
        }
    }
}

var ans = -1
outer: for y in (0..<row) {
    for x in (0..<col) {
        if board[y][x] == 0 {
            ans = -1
            break outer
        }
        ans = max(days[y][x], ans)
    }
}

print(ans)

final class Node<T> {
    var prev: Node?
    var next: Node?
    var value: T?
    init(_ value: T? = nil) {
        self.value = value
    }
}

struct Queue<T> {
    private var head: Node<T>?
    private var tail: Node<T>?
    
    mutating func popLeft() -> T? {
        guard isEmpty == false,
              let temp = head?.next
        else {
            return nil
        }
        
        if temp === tail {
            tail = head
        }
        
        head?.next = temp.next
        temp.next?.prev = head
        
        return temp.value
    }
    
    mutating func pushBack(_ item: T) {
        let temp = Node<T>(item)
        temp.prev = tail
        tail?.next = temp
        tail = temp
    }
    
    var isEmpty: Bool {
        return head === tail
    }
    
    init() {
        self.head = Node<T>()
        self.tail = head
    }
}
