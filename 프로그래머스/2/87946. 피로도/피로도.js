function solution(k, dungeons) {
    return bfs(k, dungeons);
}

const bfs = (k, dungeons) => {
    class Node {
        static LAST_NUM = dungeons.length - 1;
        static nowMax = 0;
        
        constructor({ nodeNum, remainFatigue, clearNum, visited }) { 
            // 노드번호, 남은피로도, 해결개수, 방문노드 
            if (this.nodeNum > Node.LAST_NUM
                || remainFatigue + dungeons[nodeNum]?.[1] < dungeons[nodeNum]?.[0]
                || remainFatigue < 0 
                || clearNum + (Node.LAST_NUM - nodeNum) < Node.nowMax
                || visited[nodeNum]
               ) this.isWrong = true;
    
            this.nodeNum = nodeNum;
            this.remainFatigue = remainFatigue;
            this.clearNum = clearNum;
            this.visited = [...visited];
            this.visited[nodeNum] = true;
        }
        
        changeNowMax() {
            if (this.clearNum > Node.nowMax) Node.nowMax = this.clearNum;
        }
    
        mkNextNodes() {
            const nextNodes = [];
            for (let i = 0; i <= Node.LAST_NUM; i++) {
                const newNode = this.mkNextNode(i);
                if (!newNode.isWrong) nextNodes.push(newNode); 
            }
            
            return nextNodes;
        } 
        
        mkNextNode(nodeNum) {
            return new Node({
                nodeNum,
                remainFatigue: this.remainFatigue - dungeons[nodeNum]?.[1],
                clearNum: this.clearNum + 1,
                visited: this.visited,
            });
        }
    }
        
    const root = new Node({
        nodeNum: -1,
        remainFatigue: k,
        clearNum: 0,
        visited: new Array(Node.LAST_NUM + 1).fill(false),
    });
    const q = [root];

    while (q.length) {
        const nowNode = q.shift();
        nowNode.changeNowMax();
        q.push(...nowNode.mkNextNodes());
    }

    return Node.nowMax;
};



