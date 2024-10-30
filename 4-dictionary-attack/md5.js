import { readFile } from 'fs'
import { createHash } from 'crypto'

const dictionaryPath = './data/rockyou.txt'
const targetHash = 'b3fb79c1d901987585297639cb52522d'
const salt = 'd61eaeba5b1781e7'

function md5Hash(password, salt) {
  return createHash('md5')
    .update(password + salt)
    .digest('hex')
}

readFile(dictionaryPath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading dictionary file:', err)
    return
  }

  const passwords = data.split('\n')

  for (const password of passwords) {
    const hash = md5Hash(password.trim(), salt)

    if (hash === targetHash) {
      console.log(`Password found: ${password}`)
      return
    }
  }

  console.log('Password not found in the dictionary.')
})

// Answer: 3584975
