var getResult = function (accounts) {
  flag = 0;
  for (let i = 0; i < accounts.length; i++) {
    const sum = 0;
    flag = Math.max(
      flag,
      accounts[i].reduce((acc, curr) => acc + curr, sum)
    );
  }

  return flag;
};
