function removeBlanks(str) {
    var newStr = "";
    for(var i=0; i < str.length; i++) {
        if(str[i] !== ' ') {
            newStr += str[i]
        }
    }
    return newStr;
}

var result = removeBlanks('Today is Monday');
console.log(result);