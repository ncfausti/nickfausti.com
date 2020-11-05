let limited = rateLimited(sayTime, 1000);

limited("hello", "there");
limited();
limited();

document.querySelector('#limitedBtn').addEventListener('click', limited);

function rateLimited(cb, ms, args) {
    // setup private var/closure to count with
    var queued = 0;
    return function(...args){
        setTimeout(cb, ms*queued++, ...args);
        setTimeout(()=>{queued--}, ms);
    }
}

function sayTime(s1, s2) {
    console.log(s1);
    console.log(s2);
    console.log(Date.now());
}