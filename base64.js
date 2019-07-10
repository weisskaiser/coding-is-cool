const [,, firstInput, ...otherInput] = process.argv;

const defaultSample = `Man is distinguished, not only by his reason, but by this singular passion from other animals, 
which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable 
generation of knowledge, exceeds the short vehemence of any carnal pleasure.`;
const base64table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

const input = (firstInput) ? firstInput : defaultSample;

let groupCount = 0;
let groupVal = 0;
let fullGroups = [];

console.log("original");
console.log(input);

for(let c of input){
    
    groupVal <<= 8;
    groupVal |= c.charCodeAt();
    if(++groupCount == 3){
        fullGroups.push(groupVal);
        groupCount = 0;
        groupVal = 0;
    }
}

let base64str = [];
for(let group of fullGroups){
    let shifts = 4 * 6;
    let base64val = 0;
    while((shifts -= 6) >= 0){
        
        base64val = (group >> shifts) & ((2 ** 6) -1);
        base64str.push(base64table[base64val]);
    } 
}

if(groupCount > 0){
    groupVal <<= ((3 - groupCount) * 8);
    let shifts = 4 * 6;
    let base64val = 0;
    let remainingDigits = groupCount+1;
    while(remainingDigits > 0){

        shifts -= 6;
        base64val = (groupVal >> shifts) & ((2 ** 6) -1);    
        base64str.push(base64table[base64val]);
        remainingDigits--;
    }
    while(groupCount++ != 3){
        base64str.push('=');
    }
}

console.log("encoded");
console.log(base64str.join(""));