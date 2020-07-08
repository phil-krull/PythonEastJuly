function parensValid(str) {

    return true/false
}

var parensValidResultOne = parensValid("(abc(9)def)");
console.log(parensValidResultOne);
// true

var parensValidResultTwo = parensValid("(123))456(");
console.log(parensValidResultTwo);
// false

var parensValidResultTwo = parensValid("(mno))xyz");
console.log(parensValidResultTwo);
// false


()
()()()
((()))

())(

    
