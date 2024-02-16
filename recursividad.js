const isPalin = (word) => {
  let isPalindromo = true;
  for (let i = 0, j = word.length -1; i < word.length; i++, j--) {
    if (word[i] !== word[j]) isPalindromo = false;
  }
  return isPalindromo
}

console.log('',isPalin('ana'));
console.log('',isPalin('hola'));