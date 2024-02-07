function solution(scoville, K) {
    const h = new MinHeap(scoville);
    let answer = 0;
    while (h.size > 1 && h.root < K) {
        const a = h.delete();
        const b = h.delete();
        
        const newScovile = a + (b * 2);
        h.insert(newScovile);
        answer++;
    }

    return h.root >= K ? answer : -1;
}

class MinHeap {
    constructor(arr) {
        this._ = new Array(arr.length);
        this.size = 0;
        
        // init
        for (const ele of arr) {
            this.insert(ele);
        }
    }
    
    get root() {
        return this._[0];
    }

    insert(ele) {
        this._[this.size++] = ele;
        
        let now = this.size - 1;
        while (1) {
            const parent = Math.floor((now - 1) / 2); 
            if (parent < 0 || this._[parent] <= this._[now]) break;
            else {
                // swap
                const temp = this._[now];
                this._[now] = this._[parent];
                this._[parent] = temp;
            } 
            
            now = parent;
        }
    }
    
    delete() {
        const root = this._[0];
        
        let now = 0;
        this._[0] = this._[--this.size];
        while (1) {
            let child = now * 2 + 1;
            if (child + 1 < this.size && this._[child] > this._[child + 1]) child++;
            if (child >= this.size || this._[child] >= this._[now]) break; 
            else {
                // swap
                const temp = this._[now];
                this._[now] = this._[child];
                this._[child] = temp;
            } 
            
            now = child;
        }
        
        return root;
    }
}