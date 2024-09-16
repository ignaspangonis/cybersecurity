function caesar(
  type: 'encrypt' | 'decrypt',
  options: { text: string; key: number; alphabet: string },
): string {
  const { text, key, alphabet } = options
  const shift = type === 'encrypt' ? key : alphabet.length - key

  const getShiftedChar = (char: string): string => {
    const index = alphabet.indexOf(char.toLowerCase())
    const isNotInAlphabet = index === -1

    if (isNotInAlphabet) return char

    const newIndex = (index + shift) % alphabet.length
    const isUpperCase = char === char.toUpperCase()
    const shiftedChar = alphabet[newIndex]

    return isUpperCase ? shiftedChar.toUpperCase() : shiftedChar
  }

  return text
    .split('')
    .map(char => getShiftedChar(char))
    .join('')
}

// variantas = studento pažymėjimo numeris mod 10 + 1
// variantas = 1913634 mod 10 + 1 = 5

const alphabet: string = 'aąbcčdeęėfghiįyjklmnoprsštuųūvzž'
const decryptOptions = {
  text: 'Suęų hųęk vęocm ųšęif.',
  key: 27,
  alphabet,
}
const encryptOptions = {
  text: 'Lenk medį, kol jaunas.',
  key: 11,
  alphabet,
}

console.log('\n')
console.log(caesar('decrypt', decryptOptions)) // Output: Ūžia kaip bitės avily.
console.log(caesar('encrypt', encryptOptions)) // Output: Ūlzų vlkš, ųžū uhdzhb.
console.log('\n')
