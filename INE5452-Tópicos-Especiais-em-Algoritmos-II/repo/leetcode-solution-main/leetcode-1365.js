//using time complexity n*n

var smallerNumbersThanCurrent = function (nums) {
    let resultArr = [];

    for (let i = 0; i < nums.length; i++) {
        let flag = 0;
        for (let j = 0; j < nums.length; j++) {
            if (nums[j] < nums[i]) {
                flag++;
            }
        }
        resultArr.push(flag);
    }

    return resultArr;
};


//using time complexity n

var smallerNumbersThanCurrent = function (nums) {
    let resultArr = [],
        shallowNum = [...nums];
    nums = nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length; i++) {
        resultArr.push(nums.indexOf(shallowNum[i]));
    }

    return resultArr;
};
