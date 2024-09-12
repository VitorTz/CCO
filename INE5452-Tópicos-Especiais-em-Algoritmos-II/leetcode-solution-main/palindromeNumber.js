/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    
    let rev = x.toString();
    rev = rev.split('').reverse().join('');
    if(rev==x)
        return true;
    return false;
    
};
