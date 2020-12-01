window.addEventListener("DOMContentLoaded", (event) => {
  const SECONDS_IN_DAY = 86400;
  const MINUTES_IN_DAY = SECONDS_IN_DAY / 60;
  const HOURS_IN_DAY = MINUTES_IN_DAY / 24;

  init();
  setInterval(changeNext, 60000);
  setInterval(changeNext, 60000);
});

function secondsSinceMidnight() {
  return Math.floor(getMsSince(new Date()) / 1000);
}

function minutesSinceMidnight() {
  return Math.floor(getMsSince(new Date()) / 60000);
}

function run() {
  var x = document.getElementsByClassName("filled");
}

// if no params passed, defaults to 00:00 (midnight)
function getMsSince(d, hr, min, sec, ms) {
  let _hr = 0,
    _min = 0,
    _sec = 0,
    _ms = 0;
  if (hr) _hr = hr;
  if (min) _min = min;
  if (sec) _sec = sec;
  if (ms) _ms = ms;

  const e = new Date(d);
  return d - e.setHours(_hr, _min, _sec, _ms);
}

function changeNext() {
  let next_min = document.querySelector("#container-main .blinks");
  next_min.classList.add("filled");
  next_min.classList.remove("blinks");
  next_min.nextSibling.classList.add("blinks");

  let next_sec = document.querySelector("#container-minute .blinks");
  next_sec.classList.add("filled");
  next_sec.classList.remove("blinks");
  next_sec.nextSibling.classList.add("blinks");
}

function init() {
  const minutes = document.querySelector("#container-main");

  for (let i = 0; i < 1440; i++) {
    let span = document.createElement("span");
    let minutes_since = minutesSinceMidnight();
    if (i < minutes_since + 1) {
      if (i === minutes_since) {
        span.classList = "blinks";
      } else {
        span.classList = "filled";
      }
    }
    minutes.appendChild(span);
  }

  let minutes_since_hr = Math.floor(
    getMsSince(new Date(), new Date().getHours()) / 1000 / 60
  );
  console.log(minutes_since_hr);

  const minutes_container = document.querySelector("#container-minute");

  for (let j = 0; j < 60; j++) {
    let spanMin = document.createElement("span");

    if (j < minutes_since_hr + 1) {
      console.log(1);
      if (j === minutes_since_hr) {
        spanMin.classList = "blinks";
      } else {
        spanMin.classList = "filled";
      }
    }
    minutes_container.appendChild(spanMin);
  }
}
