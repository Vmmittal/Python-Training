// Set Interval function

function greet() {
    console.log('Print after 5 seconds');
}

setInterval(greet, 5000);



function showTime() {
    let dateTime= new Date();
    let time = dateTime.toLocaleTimeString();
    console.log(time)
}

let display = setInterval(showTime, 3000);




// Set setTimeout function
function timeout() {
    console.log('Timeout is called');
}

let id = setTimeout(timeout, 5000);
console.log('This message is shown first');



function greet(name, lastName) {
    console.log('Hello' + ' ' + name + ' ' + lastName);
}

setTimeout(greet, 1000, 'vipul', 'Mittal');




