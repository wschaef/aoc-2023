private func mapRange(_ input: [Int], _ mapping: [Int]) -> ([[Int]], [Int]) {
        let iCube = CubeXD(VectorXD([input[0]]), VectorXD([input[0]+input[1]-1]))
        let mCube = CubeXD(VectorXD([mapping[1]]), VectorXD([mapping[1]+mapping[2]-1]))
        var leftOver: [[Int]] = [input]
        var mapd: [Int] = []
        if let hCube = mCube.Intersect(iCube) {
            let start = hCube.topLeft.v[0] - mapping[1] + mapping[0]
            let wid = hCube.botRight.v[0] - hCube.topLeft.v[0] + 1
            mapd = [start, wid]
            leftOver = []
            if hCube.topLeft.v[0] > input[0] {
                leftOver.append([input[0], hCube.topLeft.v[0] - input[0]])
            }
            if hCube.botRight.v[0] < input[0]+input[1]-1 {
                leftOver.append([hCube.botRight.v[0]+1, input[0]+input[1] - hCube.botRight.v[0] - 1])
            }
        }
        return (leftOver, mapd)
    }

    func mapInputRanges(_ inputs: [Int]) {
        var toMap = inputs
        while toMap.count > 0 {
            let input: [Int] = [Int](toMap[0...1])
            toMap = [Int](toMap.dropFirst(2))
            var didMap = false
            for map in mapping {
                let (leftOver, mapd) = mapRange(input, map)
                if mapd.count > 0 {
                    mapped.append(mapd[0])
                    mapped.append(mapd[1])
                    didMap = true
                }
                if leftOver.count == 0 {
                    break
                }
                if didMap {
                    for lo in leftOver {
                        toMap.append(lo[0])
                        toMap.append(lo[1])
                    }
                    break
                }
            }
            if !didMap {
                mapped.append(input[0])
                mapped.append(input[1])
            }
        }
    }
}