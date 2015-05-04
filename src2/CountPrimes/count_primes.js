"use strict"
/**
 * @param {number} n
 * @return {number}
 */
function show(n){
	console.log(n);
}

var countPrimes = function(n) {
	var scanned = new Int8Array(n);
	for (var i = 2; i < n; i++){
		if (!scanned[i]){
			for (var j = i * i; j < n; j+=i){
				scanned[j] = true;
			}
		}
	}
	show(scanned);

	var count = 0;
	for (var k = 2; k < n; i++){
		if (!scanned[k]){
			count++;
		}
	}
	return count;
};


show(countPrimes(1));
show(countPrimes(3));
show(countPrimes(10));
// show(countPrimes(25));
show(countPrimes(1000));