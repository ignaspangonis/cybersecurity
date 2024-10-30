import { createReadStream } from 'fs'
import { compare } from 'bcrypt'
import { createInterface } from 'readline'

const dictionaryPath = './data/rockyou_1000.txt'
const targetHash = '$2b$11$DwhtchaYhmpRQtKSsKoVe.zMAeMEqEuBu5tu7Ul0issmSvMYGeeju'

let passwordFound = false

const rl = createInterface({
  input: createReadStream(dictionaryPath),
  output: process.stdout,
  terminal: false,
})

rl.on('line', async password => {
  if (passwordFound) return

  try {
    const isMatch = await compare(password.trim(), targetHash)

    if (isMatch) {
      console.log(`Password found: ${password}`)
      passwordFound = true
      rl.close()
    }
  } catch (error) {
    console.error('Error comparing password:', error)
    rl.close()
  }
})

rl.on('close', () => {
  if (!passwordFound) {
    console.log('Password not found in the dictionary.')
  }
})
