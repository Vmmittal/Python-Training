//Generator Function..............................................

function* nextNaturalnumber(){
    let nnum=1
    while(true)
    {
        yield nnum++;
    }
}

let gen = nextNaturalnumber()
console.log(gen.next())
console.log(gen.next())
console.log(gen.next())




//First class function................................................

const Arithmetics = {
    add: (a, b) => {
        return a + b;
    },
    subtract: (a, b) => {
        return a-b
    },
    multiply: (a, b) => {
        return a*b
    },
    division: (a, b) => {
        if (b != 0) return a/b
        return `Cannot Divide by Zero!!!`;
    }
 
}
 
console.log(Arithmetics.add(100, 100));
console.log(Arithmetics.subtract(100, 7))
console.log(Arithmetics.multiply(5, 5))
console.log(Arithmetics.division(100, 0));