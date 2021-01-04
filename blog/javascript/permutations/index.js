import range from "lodash/range";

function joinAtIndex(arr, i) {
  return arr.slice(0, i) + arr.slice(i + 1, arr.length);
}

function ListPermutations(str) {
  function RecPermute(soFar, rest) {
    if (rest === "") {
      console.log(soFar);
    } else {
      range(rest.length).forEach((i) => {
        // append on the next letter to what we've seen so far
        let next_val = soFar + rest[i];

        // everything before rest[i] + after rest[i]
        let remaining = rest.slice(0, i) + rest.slice(i + 1, rest.length);

        RecPermute(next_val, remaining);
      });
    }
  }
  RecPermute("", str);
}

function assertEquals(a, b) {
  if (a !== b) {
    console.log(a);
    console.log(b);
    throw `AssertionError: ${a} != ${b}`;
  }
}

let s = "abc";
console.log('The permutations of "abc" are:');
ListPermutations(s);
