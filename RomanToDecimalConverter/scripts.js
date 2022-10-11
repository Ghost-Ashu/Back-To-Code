const input = document.querySelector('input');
const alert = document.querySelector('h4.alert');
const span = document.querySelector('span');
const tableBody = document.querySelector('tbody');

const symbols = [
  { id: 1, symbol: 'I', value: 1 },
  { id: 2, symbol: 'V', value: 5 },
  { id: 3, symbol: 'X', value: 10 },
  { id: 4, symbol: 'L', value: 50 },
  { id: 5, symbol: 'C', value: 100 },
  { id: 6, symbol: 'D', value: 500 },
  { id: 7, symbol: 'M', value: 1000 },
];

async function getRoman(chars) {
  let formatted = chars.replaceAll(' ', "").split("");
  let converted = 0;
  const isValid = new Array();

  formatted.forEach(item => {
    symbols.forEach(symbol => {
      if (symbol.symbol === item) {
        converted += symbol.value;
        isValid.push(item);
      }
    });
  })

  if (isValid.length === formatted.length) {
    return converted;
  }

  alert.innerHTML = 'ERROR, insert only Roman Symbols';
  return
}

async function calculate(roman, decimal) {
  let formatted = roman.replaceAll(' ', "").split("");
  let cal = decimal;

  for (let i = 0; i < roman.length; i++) {
    if (formatted[i] === 'I' && formatted[i + 1] !== 'I' && typeof formatted[i + 1] !== 'undefined') {
      cal -= 2;
    }
    if ((formatted[i] === 'X' && formatted[i + 1] === 'C') || formatted[i] === 'X' && formatted[i + 1] === 'L') {
      cal -= 20;
    }
    if ((formatted[i] === 'C' && formatted[i + 1] === 'M') || formatted[i] === 'C' && formatted[i + 1] === 'D') {
      cal -= 200;
    }
  }

  return cal;
}

input.addEventListener("keyup", async (event) => {
  event.preventDefault();

  const convertValue = input.value.toLocaleUpperCase();
  span.innerHTML = '';
  alert.innerHTML = '';

  if (convertValue.length <= 0) return;

  const convertedRoman = await getRoman(convertValue);


  if (typeof convertedRoman !== 'undefined') {
    span.innerHTML = await calculate(convertValue, convertedRoman);
    return;
  }
});

function init() {
  span.innerHTML = '';
  alert.innerHTML = '';

  symbols.forEach(symbol => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <tr>
        <td>${symbol.symbol}</td>
        <td>${symbol.value}</td>
      </tr>
    `;
    tableBody.appendChild(tr);
  });
}

init();