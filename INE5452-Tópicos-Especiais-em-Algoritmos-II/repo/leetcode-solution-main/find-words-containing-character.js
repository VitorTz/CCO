var findWordsContaining = function(words, x) {
    let resultArr = [];
    for (let i = 0; i < words.length; i++) {
    if (words[i].includes(x)) {
      resultArr.push(i);
    }
  }

  return resultArr;
};
