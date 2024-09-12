var finalValueAfterOperations = function(operations) {

    let sum = 0;
    for (const op of operations) {
        if(op[1]=== '+'){
            sum++;
        }
        else{
            sum--;
        }
    }
    return sum;
};

const operations = ["--X","X++","X++"];
console.log(finalValueAfterOperations(operations));
