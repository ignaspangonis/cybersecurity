const fs = require('fs')
const readline = require('readline')
const argon2 = require('argon2')
const targetHash =
  '$argon2id$v=19$m=47104,t=4,p=1$StKuSo6URW7jZyZAJwU0Jg$4K5GCyjmrdWQ6lgJihj+Ka3DM5Z74BlEFfwk0acXCyg'

const fileStream = fs.createReadStream('./data/rockyou_1000.txt')

const rl = readline.createInterface({
  input: fileStream,
  crlfDelay: Infinity,
})

async function checkPassword(line) {
  try {
    const match = await argon2.verify(targetHash, line)
    if (match) {
      console.log(`Password found: ${line}`)
      process.exit(0)
    }
  } catch (err) {
    console.error(`Error verifying password "${line}":`, err)
  }
}

rl.on('line', line => {
  checkPassword(line)
})

rl.on('close', () => {
  console.log('Finished processing file. No match found.')
})
