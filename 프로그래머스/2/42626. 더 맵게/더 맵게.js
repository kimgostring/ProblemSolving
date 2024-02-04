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
            const parent = Math.floor(now / 2);
            if (parent === now || this._[parent] <= this._[now]) break;
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
            const left = now * 2;
            const right = left + 1;
            let selected = this._[left] < this._[right] ? left : right;
            
            if (selected >= this.size || this._[selected] >= this._[now]) break; 
            else {
                // swap
                const temp = this._[now];
                this._[now] = this._[selected];
                this._[selected] = temp;
            } 
            
            now = selected;
        }
        
        return root;
    }
}