window.addEventListener('DOMContentLoaded', (event) => {
    const SECONDS_IN_DAY = 86400;
    const MINUTES_IN_DAY = SECONDS_IN_DAY / 60;
    const HOURS_IN_DAY = MINUTES_IN_DAY / 24;

    init();
    setInterval(changeNext, 60000);
});

function secondsSinceMidnight() { 
	return Math.floor(getMsSinceMidnight(new Date()) / 1000);
}

function minutesSinceMidnight() { 
	return Math.floor(getMsSinceMidnight(new Date()) / 60000);
}

function run() {
  var x = document.getElementsByClassName('filled');
}

function getMsSinceMidnight(d) {
  var e = new Date(d);
  return d - e.setHours(0,0,0,0);
}

function changeNext() {
  let next_span = document.querySelector('.blinks');
  next_span.classList.add('filled');
  next_span.classList.remove('blinks');
  next_span.nextSibling.classList.add('blinks');
  
}

function init() {
  const seconds = document.getElementById('container');

	for (let i = 0; i < 1440; i++) {
  	let span = document.createElement('span');
    let minutes_since = minutesSinceMidnight();
    if (i < minutes_since + 1) {
    	if (i === minutes_since) { 
      	span.classList = 'blinks';
      }
      else {
      	span.classList = 'filled';
      }
    }
    
    seconds.appendChild(span);
    
  }
}