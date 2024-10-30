const fs = require('fs')
const crypto = require('crypto')
const readline = require('readline')

const dictionaryPath = './data/rockyou.txt'
const targetHash = '05907ae4fcf755eced760655d7790221b840738cd742186c1840987f90a6c820'
const salt = '4e81a60b9599a9d9'

function sha256Hash(password, salt) {
  return crypto
    .createHash('sha256')
    .update(password + salt)
    .digest('hex')
}

let passwordFound = false

const rl = readline.createInterface({
  input: fs.createReadStream(dictionaryPath),
  output: process.stdout,
  terminal: false,
})

rl.on('line', password => {
  const hash = sha256Hash(password.trim(), salt)

  if (hash === targetHash) {
    console.log(`Password found: ${password}`)
    passwordFound = true
    rl.close()
  }
})

rl.on('close', () => {
  if (!passwordFound) {
    console.log('Password not found in the dictionary.')
  }
})
