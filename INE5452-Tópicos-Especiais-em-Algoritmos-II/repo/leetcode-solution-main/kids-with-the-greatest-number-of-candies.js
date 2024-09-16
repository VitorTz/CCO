// find max value from the given array and check the resultant value is greater than or equal

var kidsWithCandies = function (candies, extraCandies) {
    let resultArr = [],
        maxVal = Math.max(...candies);
    for (let i = 0; i < candies?.length; i++) {
        if (candies[i] + extraCandies >= maxVal) {
            resultArr.push(true);
        } else {
            resultArr.push(false);
        }
    }
    return resultArr;
};
