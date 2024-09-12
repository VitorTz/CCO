var romanToInt = function(s) {
    const roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M'];
    const value = [1,5,10,50,100,500,1000];
    let sum = 0;

    for(let i=0; i<s.length; i++){
        let a = roman.indexOf(s[i]);
        let b = roman.indexOf(s[i+1]);
        if(a < b ){
            if(roman[a]=='I' && (roman[b]=='V' || roman[b]=='X')){
                sum+= value[b]-value[a];
            }
            else if(roman[a]=='X' && (roman[b]=='L' || roman[b]=='C')){
                sum+= value[b]-value[a];
            }
            else if(roman[a]=='C' && (roman[b]=='D' || roman[b]=='M')){
                sum+= value[b]-value[a];
            }
            i++;
        }
        else{
            sum+=value[a];
        }
    }

    return sum;

};

romanToInt('LVIII')
