

var addTwoNumbers = function(l1, l2) {
    const higherNumber = l1.length > l2.length ? l1.length : l2.length;
    let l1Composition = '';
    let l2Composition = '';
    for (let i = l1.length - 1; i > 0; i--) {
        l1 += l1[i];
        if (l2[i]) {
            l2 += l2[i];
        }
    }
    const sum = String(Number(l1Composition) + Number(l2Composition)).split('');  
    return sum;   
  };