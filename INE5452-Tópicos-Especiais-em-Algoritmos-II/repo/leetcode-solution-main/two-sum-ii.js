var twoSum = function(numbers, target) {
    var start=0,end=numbers.length-1,sum,d;
    while(start<end)
    {
        sum= numbers[start]+numbers[end];
        if(sum==target)
            break;
        else if(sum<target)
            start++;
        else
            end--;
    }
    return [start+1,end+1]
};
