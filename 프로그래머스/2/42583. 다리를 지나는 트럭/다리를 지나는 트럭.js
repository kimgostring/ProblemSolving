function solution(bridge_length, weight, truck_weights) {
    const len = truck_weights.length;
    let sec = 0;
    let totalWeight = 0;
    let front = 0;
    let bridgeFront = 0;
    let bridge = Array(bridge_length).fill(0);

    while (bridgeFront < bridge.length) {
        totalWeight -= bridge[bridgeFront++];   
        
        if (front < len) {
            if (truck_weights[front] <= weight - totalWeight) {
                bridge.push(truck_weights[front]);
                totalWeight += truck_weights[front++];
            } else bridge.push(0);
        }
        
        sec++;
    }
    
    return sec;
}