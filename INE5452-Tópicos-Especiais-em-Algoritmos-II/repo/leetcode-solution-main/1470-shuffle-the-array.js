var getResult = function (nums, n) {
  let resultArr = [];
  for (let i = 0; i < n; i++) {
    resultArr.push(nums[i]);
    resultArr.push(nums[i + n]);
  }

  return resultArr;
};

console.log(getResult([2, 5, 1, 3, 4, 7], 3));
