var mostWordsFound = function (sentences) {
    let flag = 0;
    for (let i = 0; i < sentences.length; i++) {
        flag = Math.max(flag, sentences[i].split(" ").length);
    }

    return flag;
};
