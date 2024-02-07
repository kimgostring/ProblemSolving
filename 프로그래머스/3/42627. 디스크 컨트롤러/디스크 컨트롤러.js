function solution(jobs) {
    const LEN = jobs.length;
    const h = new MinHeap(LEN);
    
    jobs.sort((a, b) => {
        if (a[0] !== b[0]) return a[0] - b[0];
        return a[1] - b[1];
    });
    
    let now_time = jobs[0][0];
    let index = 0;
    let total = 0;
    while (index < LEN || h.size) {
        while (index < LEN && jobs[index][0] <= now_time) h.insert(jobs[index++]);
        
        if (h.size) {
            const [start_time, processing_time] = h.delete();
            total += ((now_time + processing_time) - start_time);
            now_time += processing_time;
        } else if (index < LEN) now_time = jobs[index][0]; 
    }
    
    return Math.floor(total / LEN);
}

class MinHeap {
    constructor(n) {
        this._ = Array(n);
        this.size = 0;
    }
    
    insert(ele) {
        this._[this.size++] = ele;
     
        let pointer = this.size - 1;
        while (1) {
            const parent = Math.floor((pointer - 1) / 2);
            if (parent < 0 || this._[parent][1] <= this._[pointer][1]) break;
            
            const temp = this._[pointer];
            this._[pointer] = this._[parent];
            this._[parent] = temp;
            
            pointer = parent;
        }
    }
    
    delete() {
        const root = this._[0];
        this._[0] = this._[--this.size];
        
        let pointer = 0;
        while (1) {
            let child = pointer * 2 + 1; 
            if (child + 1 < this.size && this._[child + 1][1] < this._[child][1]) child++;
            if (child >= this.size || this._[child][1] >= this._[pointer][1]) break;
            
            const temp = this._[pointer];
            this._[pointer] = this._[child];
            this._[child] = temp;
            
            pointer = child;
        }
        
        return root;
    }
}
