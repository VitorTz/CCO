//assigned k as a first elemnet to return array. then made XOR op between return array and given array same indexed element

var decode = function (nums, k) {
    let arr = [k];
    for (let i = 0; i < nums.length; i++) {
        arr.push(arr[i] ^ nums[i]);
    }
    return arr;
};
