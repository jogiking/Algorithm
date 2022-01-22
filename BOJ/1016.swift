import Foundation

var input = readLine()!.split(separator: " ").map{Int(String($0))!}
var diff = input[1] - input[0] + 1
var squareNumbers = [Int]()
var i = 2

while i * i <= input[1] {
  squareNumbers.append(i * i)
  i += 1
}

var square_ㄴㄴ = Set<Int>()
for element in squareNumbers {
    for i in stride(from: (input[0]+element-1)/element, through: input[1]/element, by: 1) {
        square_ㄴㄴ.insert(i*element)
    }
}

print(diff-square_ㄴㄴ.count)
