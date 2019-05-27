const assert = require('assert');

let input = [100, 4, 200, 1, 3, 2];

const consecutive = (array) => {

    let sorted = array.sort((a,b) => a - b);
    let start = 0, end = 0, localstart = 0, localend = 0;

    for(let [i,v] of sorted.entries()){
        if(sorted[Math.max(i-1,0)]+1 == v){
            localend = i;
        }
        else{
            if(end - start < localend - localstart){
                start = localstart;
                end = localend;
            }
            localstart = i;
        }
    }

    return sorted.slice(start, end+1);
}

assert.deepStrictEqual(consecutive(input), [1, 2, 3, 4]);