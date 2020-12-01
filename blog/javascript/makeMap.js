// The global variable
var s = [23, 65, 98, 5];

// This prototype function on Array will emulate
// the built-in map() function
Array.prototype.myMap = function(callback) {
  var newArray = [];

  // for each item in myMap, run callback 
  // on it and add to newArray
  this.forEach((el) => newArray.push(callback(el)));

  return newArray;
};

var new_s = s.myMap(function(item) {
  return item * 2;
});
