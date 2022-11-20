function isPrime(number){
  for ( x = 2; x < number; x++) {
    if ((number % x) == 0) {
      return false;
    }
  }
  return true;
}
startTime = performance.now()
var count = 0;
for (y = 1; y <= 100000; y++) {
  if (isPrime(y)) {
    count++;
  }
}
console.log("1000000以内质数的个数是 ",count);
endTime = performance.now();

console.log("整个程序用时：",(endTime-startTime)/1000,"s");