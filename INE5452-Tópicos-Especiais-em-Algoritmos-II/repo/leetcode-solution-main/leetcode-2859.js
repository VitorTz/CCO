var sumIndicesWithKSetBits = function (nums, k) {
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
        if ((i.toString(2).match(/1/g) || []).length === k) {
            sum += nums[i];
        }
    }
    return sum;
};
