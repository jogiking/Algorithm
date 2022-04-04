import Foundation

func solution(_ word:String) -> Int {    
    let words = "AEIOU".map{String($0)}   
    let target = word.map{String($0)}
    var flag = false
    var count = 0
    func dfs(_ path: Int, _ temp: [String]) {
        if temp == target {
            flag = true
            return
        }
        
        if path >= 5 {
            return
        }
        
        for i in 0..<5 {
            count+=1
            dfs(path+1, temp + [words[i]])
            if flag {
                return
            }
        }
    }  
    
    dfs(0, [String]())
    
    return count
}
