

// Number to String Conversion:
const number = 42;
const num = String(number)
console.log(num); 
console.log(typeof num); 

//String to integer

var a = parseInt("100") 
console.log(a); 
var b =parseInt("2018cloudeq")
console.log(b); 
var c = parseInt("gcloudeq2018") 
console.log(c); 
var d = parseInt("3.14")
console.log(d); 
var e = parseInt("21 7 2018") 
console.log(e); 

// String to Boolean Conversion:
const BoolValue = "true";
const Stringres = Boolean(BoolValue);
console.log(Stringres); 
console.log(typeof Stringres); 

// String to Number Conversion:
const strNumber = "42";
const numberString = Number(strNumber);
console.log(numberString); 
console.log(typeof numberString); 

// Number to Boolean Conversion:
const numberValue = 42;
const boolValueFromNumber = Boolean(numberValue);
console.log(boolValueFromNumber); // true
console.log(typeof boolValueFromNumber); // "boolean"

// Object to String Conversion:
const obj = { name: "John", age: 25 };
const strObj = JSON.stringify(obj);
console.log(strObj); // "{"name":"John","age":25}"
console.log(typeof strObj); // "string"


// Boolean to String Conversion:
const boolValue = true;
const strBool = String(boolValue);
console.log(strBool); // "true"
console.log(typeof strBool); // "string"