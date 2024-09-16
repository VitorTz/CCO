/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var rev=0,rem,c,d;
    while(x!=0)
    {
        rem=x%10;
        rev=rev*10+rem;
        x/=10;
        x=parseInt(x);
    }
    if( rev<= Math.pow(-2, 31) || rev>= Math.pow(2, 31) -1)
    {
        return 0;
    }
   
    return rev;
};
