// taken the value of x from each array
// sort the new array
// find the max diff from the value of the array

var maxWidthOfVerticalArea = function (points) {
    let xArr = [],
        flag = 0;

    for (let i = 0; i < points.length; i++) {
        xArr.push(points[i][0]);
    }
    xArr.sort((a, b) => a - b);
    for (let i = 0; i < xArr?.length - 1; i++) {
        flag = Math.max(flag, xArr[i + 1] - xArr[i]);
    }

    return flag;
};
