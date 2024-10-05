const ALPHABET = 'aąbcčdeęėfghiįyjklmnoprsštuųūvzž'

function kasiskiTest(lowerCaseText) {
  const SEQUENCE_LENGTH = 2
  const MIN_KEY_LENGTH = 3
  const MAX_KEY_LENGTH = 15

  const sequencePositions = {}

  for (let i = 0; i < lowerCaseText.length - SEQUENCE_LENGTH + 1; i++) {
    const sequence = lowerCaseText.substring(i, i + SEQUENCE_LENGTH)

    if (!sequencePositions[sequence]) {
      sequencePositions[sequence] = []
    }
    sequencePositions[sequence].push(i)
  }

  const distances = {}

  Object.values(sequencePositions).map(positions => {
    if (positions.length <= 1) return

    for (let i = 1; i < positions.length; i++) {
      const distance = positions[i] - positions[i - 1]

      if (!distances[distance]) distances[distance] = 0

      distances[distance]++
    }
  })

  const possibleKeyLengths = {}

  Object.keys(distances).forEach(distance => {
    const distanceNumber = Number(distance)

    for (let keyLength = MIN_KEY_LENGTH; keyLength <= MAX_KEY_LENGTH; keyLength++) {
      if (distanceNumber % keyLength === 0) {
        if (!possibleKeyLengths[keyLength]) {
          possibleKeyLengths[keyLength] = 0
        }
        possibleKeyLengths[keyLength] += distances[distance]
      }
    }
  })

  const mostProbableKeyLength = Object.keys(possibleKeyLengths).sort(
    (a, b) => possibleKeyLengths[b] - possibleKeyLengths[a],
  )[0]

  return Number(mostProbableKeyLength)
}

function getDecryptedCharIndex(charIndex, shift) {
  return (charIndex - shift + ALPHABET.length) % ALPHABET.length
}

function decryptVigenere(ciphertext, key) {
  let keyIndex = 0

  return ciphertext
    .split('')
    .map(cipherChar => {
      const lowerCaseChar = cipherChar.toLowerCase()

      if (!ALPHABET.includes(lowerCaseChar)) return cipherChar

      const keyChar = key.charAt(keyIndex).toLowerCase()
      const charIndex = ALPHABET.indexOf(lowerCaseChar)
      const shift = ALPHABET.indexOf(keyChar)

      const decryptedCharIndex = getDecryptedCharIndex(charIndex, shift)
      const decryptedChar = ALPHABET[decryptedCharIndex]
      const isLowerCase = cipherChar === lowerCaseChar
      const adjustedChar = isLowerCase ? decryptedChar : decryptedChar.toUpperCase()
      keyIndex = (keyIndex + 1) % key.length

      return adjustedChar
    })
    .join('')
}

function calculateFrequencies(lowerCaseText) {
  const frequencies = {}
  let totalChars = 0

  for (let char of lowerCaseText) {
    frequencies[char] = (frequencies[char] || 0) + 1
    totalChars++
  }

  for (let char in frequencies) {
    frequencies[char] = frequencies[char] / totalChars
  }

  return frequencies
}

function filterByAlphabet(text) {
  let filteredText = ''
  for (let i = 0; i < text.length; i++) {
    const char = text.charAt(i)
    if (ALPHABET.includes(char.toLowerCase())) {
      filteredText += char
    }
  }
  return filteredText
}

// Identical to a Caesar decipher
function shiftText(formattedText, shift) {
  return formattedText
    .split('')
    .map(char => {
      if (!ALPHABET.includes(char))
        throw new Error('The text includes non-alphabet or uppercase char')

      const charIndex = ALPHABET.indexOf(char)
      const shiftedIndex = getDecryptedCharIndex(charIndex, shift)

      return ALPHABET[shiftedIndex]
    })
    .join('')
}

function guessKeyAndDecrypt(ciphertext, keyMultiplier = 1) {
  const filteredCipherText = filterByAlphabet(ciphertext)
  const filteredLowerCaseText = filteredCipherText.toLowerCase()

  const keyLength = kasiskiTest(filteredLowerCaseText) * keyMultiplier

  let key = ''

  for (let groupIndex = 0; groupIndex < keyLength; groupIndex++) {
    // Grouping the chars that are decrypted by the same key char
    let group = ''

    for (let jump = groupIndex; jump < filteredLowerCaseText.length; jump += keyLength) {
      const char = filteredLowerCaseText.charAt(jump)

      if (!ALPHABET.includes(char))
        throw new Error('Provided ciphertext should be in alphabet and lowercase')

      group += char
    }

    let bestShift = 0
    let minDifference = Number.MAX_SAFE_INTEGER

    for (let shift = 0; shift < ALPHABET.length; shift++) {
      const shiftedText = shiftText(group, shift)
      const shiftedTextFrequencies = calculateFrequencies(shiftedText)

      let sumOfFrequencies = 0
      const COMMON_LETTERS = ['i', 'a', 's', 'o', 'r', 'e']
      const SUM_OF_COMMON_LETTERS_FREQUENCIES = 0.5002 // In Lithuanian language

      COMMON_LETTERS.forEach(commonChar => {
        const observedFreq = shiftedTextFrequencies[commonChar] || 0
        sumOfFrequencies += observedFreq
      })
      const difference = Math.abs(sumOfFrequencies - SUM_OF_COMMON_LETTERS_FREQUENCIES)
      if (difference < minDifference) {
        minDifference = difference
        bestShift = shift
      }
    }

    key += ALPHABET[bestShift]
  }

  const decryptedText = decryptVigenere(ciphertext, key)

  return { key, decryptedText }
}

const CIPHER_TEXT = `Miųyaykcruęday vdščnkšvį sknghišši mvjbrnūsmso – iųlvsbsį. Šūk sssruęifa fūcųtncųzej blfh cdūžgkvc cčega grupįthia (ųyoumyg) kčhpcsdiyilayū, sūžkcvžž mžkšęiicmi,
ęvl ųyoąbsėa cžijbmūčnkę hheetcckov jiydvėoę zaįža. Žši ašpbnūk akjštlivc sjsaęrcjiv,
ipvbstica scodigą ibcneeviskd „kevvžkb“ vūžnhim eįtoiįg pgkėec, a tšuūakgjč zuhjmtčs
iiėbeatnk įšžijv iijvkjo iscyęe. Sdyeyedmso refi tėkb fūfslldej, t. d. aiūrkūigcš včskmfri
ęfiįriv ąięclgtkk akjštlivc ūčdūk. Žckašš, thūck afrees ūofa ibhšlrha, ecš ūzięšs eeūktc
ląiyaušgv sūktvjį – tars rsiacmieš, ūev jsš lptrfs ofmžis. Kicai oda cpcųyeglrbabt vccže
įrhyėūmk – tpyvekims aiūrkūigdc včskmfgs kmmckdmzs ybcjię. Fikv refifi įūaądzsašpš, ksš
sjmūitccc elsęuįbmč jitv cemghzs ieudsknm. Žšii cljeūfisji sšnęckūscą gsyššebž ūvbsfd
oicbeųigoy įięmeflc elmcžkbeę krcršij ddlč, jaodal fčsčeęi obsčk kcrav edhc – ęrid ialbažijsc yruudac bšūutc rsęi fdk ofmtšs ibhteęts, gcc tšuūakgjh ttffžžčey cįbtzk tsnąajaoueū nrkalęašis cb shskngs uurvofi kbk ūl vccžuj plcžį – odžrsašta scckūmk kalęašš
nla grupįthia. Rčtsc kiūanmso, ūev nseūgtčėo inakyafaeū nšja ttlu štyūcitū ryębaši
khlh įagcoefzu ulhūh fuč zuhjmtn bėaęg.
4.2.2. Rūųoevžžes įmąbsfjac
Nšėijsžkčs ežgcodūši įmfbaęd airfeyo clžda. Djoąnišši cčyeiedafv ižgigdcūs ęjikfc,
ūčbhųsėa ežiępzmn, nlbhųyfo bsųštčafm ci vūjšlrštčafm įūgūktįsavz. Thūy ėenčagfgššs
črsęict vccža geke ūbrmmi ūvekzlč ąįggetmm, įeūčų sdfbnfds smcemghds fuč dšhnštčų gilųofįjm, l dmėsėšsk – vūkoy mbubrszhį adkalęašis geh elkddm įšžisv fdedčhoyc ąūigįifgsr. Macm ąel rcyhdacmyy nmkčskbsb sgmecįše ėikį grupu – dsnašš pįšvęaūza, ęvl ųyoąbsėoę zuhjmtes sdfbnfęjv mbejiūmūr tūžs gsvmhil ikėicmivo ihyeye. Obsū moėcctč akzcftūžs
ęušilific nyazoff cehtdūcfaū iuh kesčnca sųrrko. Hmmūšccžžį sūktvjav, juūmįbnfįs ys
diųhgšgū įetnąv, bičksvsį yet urršryigdc, eap riyf ižgigdcūs arivrššši tėkl vzfdhjš ųzr
fmuąacdzfz, ūayiy ąįbdšmų inši šdįmyg bksigfa ūzgcckio ežiępzį. Lacą yktrdkcvze baėšfčbš yeįįmsli ibharkhą cp fmznhc obefįs č įšžt, t. d. ąįggetms kmvmscmermk ku afgmhėy ikėicmivo fmzts. Ūsb peįcvoaūčuy ysbgūt vdįloli ošvfą djoąništ iį ąvieūia inši ėikay, gprjaufžy jiydvėa zja srceėigrs kž aįnkcūvlo imįduccifz šū yeąšyjrh jecįčščų imįiaėęmš.
Rarčo fmuąacdzfl ąūčvsvlėaę ęrs riv, ėaū ąįggetmho iųjalrhjoę iuh riūįuyiobo
agacbę, žščcil haęfiįv ąūigįifr nšja smcemghds fuč kaoš ūsšiūę. Irvzsdrfem, įrhrįrmk
caėf bekykš č šef fuįfį všvh fcūtl dr lūbekykš ūkobžnco itl igckiuaūieš šū įagijbaū. Mo cpfihgkš ąrlū yaūddm šnkbhdi ežgcodūn phbs. Niria įcrmjtįę igrk jitlųe vuhzvfų ętuąlųmgo
ošvją, č fikv – štjtįeętižo vccdę štfšgjyžž. Tvlbmkksš ąrlūha ysrefvhdc še utlh biab rvrcįteo phnę vm sęšįjiccaco cemglzh ęyuhegfzmj, tskcru djaęršzėac ll ęyuheghc tšuūšgai
pąl cjąszmvžkrcūėoy mižiglzh – hautl hmmūšccųsį vūžnsnmmėšfšjeaū caėfze huydsjyfd, aį
bšūuafi yk dgįmvkšščs, sb yk icktįsūfčjhzcį, ie yaąvv žši sąyruuįtc vdščnk`
const KEY_MULTIPLIER = 2 // When the key length is 14, Kasiski test may give 7. Multiplier fixes it.

const result = guessKeyAndDecrypt(CIPHER_TEXT, KEY_MULTIPLIER)

console.log('Guessed Key:', result.key)
console.log('Decrypted Text:', result.decryptedText)
