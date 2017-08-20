let sentence = 'fulana bonita joaquina bonita';

/**
* Get sufix of the target word
*/
function getSufixo(word) {
  let lastPosition = word.length - 1;
  return word[lastPosition];
};

function searchWord(i, sentence, word, char) {
  let elem = char, count = i;
  let isWord = false;
  while (count >= 0) {
    count--;
    elem = sentence[count] + elem;
    if (elem == word) {
      isWord = true;
      break;
    }
  }
  return (isWord) ? count : -1;
};

function search(sentence, word) {
  let size = sentence.length;
  let char = sentence[0];
  let sufixo = getSufixo(word);
  for (let i = 0; i < size; i++) {
    if (char === sufixo) {
      let pos = searchWord(i, sentence, word, char);
      if (pos >= 0) {
        console.log(`WORD: ${word} | init: ${pos} | end: ${i}`);
      }
    } else {
      char = sentence[i];
    }
  }
};

search(sentence, 'bonita');
