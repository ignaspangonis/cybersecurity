function caesar(
  type: 'encrypt' | 'decrypt',
  options: { text: string; key: number; alphabet: string },
): string {
  const { text, key, alphabet } = options
  const effectiveShift = type === 'encrypt' ? key : alphabet.length - key
  const shift = ((effectiveShift % alphabet.length) + alphabet.length) % alphabet.length

  return text
    .split('')
    .map(char => {
      const index = alphabet.indexOf(char.toLowerCase())
      const isNotInAlphabet = index === -1

      if (isNotInAlphabet) return char

      const newIndex = (index + shift) % alphabet.length
      const shiftedChar = alphabet[newIndex]
      const isUpperCase = char === char.toUpperCase()

      return isUpperCase ? shiftedChar.toUpperCase() : shiftedChar
    })
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

const encrypted = caesar('decrypt', decryptOptions) // Output: Ūžia kaip bitės avily.
const decrypted = caesar('encrypt', encryptOptions) // Output: Ūlzų vlkš, ųžū uhdzhb.

console.log(`
  Encrypted: ${encrypted}
  Decrypted: ${decrypted}
`)
