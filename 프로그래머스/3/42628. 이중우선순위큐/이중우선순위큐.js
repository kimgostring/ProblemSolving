function solution(operations) {
    const h = new DoubleHeap(operations.length);

    for (const command of operations) {
        let [op, num] = command.split(" ");
        num = Number(num);
        
        if (op === "I") h.insert(num);
        else {
            if (num === 1) h.delete();
            else h.deleteMin();
        }
    }
    
    if (!h.size) return [0, 0];
    else if (h.size === 1) {
        const ele = h.delete();
        return [ele, ele];
    } else {
        const max = h.delete();
        const min = h.deleteMin();
        return [max, min];
    }
}

class DoubleHeap {
    constructor(n) {
        this._ = Array(n);
        this.size = 0;
    }
    
    insert(ele) {
        this._[this.size++] = ele;
        
        let ind = this.size - 1;
        while (1) {
            let parent = Math.ceil(ind / 2) - 1;
            if (parent < 0 || this._[parent] >= this._[ind]) break;
            
            const temp = this._[ind];
            this._[ind] = this._[parent];
            this._[parent] = temp;
            
            ind = parent;
        }
    }
    
    delete() {
        if (this.size <= 0) return;
        
        const answer = this._[0];
        this._[0] = this._[--this.size];
        
        let ind = 0;
        while (1) {
            let child = ind * 2 + 1;
            if (child + 1 < this.size && this._[child + 1] > this._[child]) child++;
            if (child >= this.size || this._[child] <= this._[ind]) break;
            
            const temp = this._[ind];
            this._[ind] = this._[child];
            this._[child] = temp;
            
            ind = child;
        }
        
        return answer;
    }
    
    deleteMin() {
        if (this.size <= 0) return;
        
        let minInd = --this.size;
        const LEAF_MIN = Math.ceil(minInd / 2);
        for (let i = minInd - 1; i >= LEAF_MIN; i--) {
            if (this._[i] < this._[minInd]) minInd = i;
        }
        
        const answer = this._[minInd];
        this._[minInd] = this._[this.size];
        
        let ind = minInd;
        while (1) {
            let parent = Math.ceil(ind / 2) - 1;
            if (parent < 0 || this._[parent] >= this._[ind]) break;
                
            const temp = this._[ind];
            this._[ind] = this._[parent];
            this._[parent] = temp;
            
            ind = parent;
        }
        
        return answer;
    }
}