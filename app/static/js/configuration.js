// CONMPATABILITY ============================================================


const compatMenus = document.querySelectorAll('select')
compatMenus.forEach(select => select.addEventListener('change', updateCompatability))

function updateCompatability() {
    
}

// PRICING ============================================================

const pricedMenus = document.querySelectorAll('.priced')
pricedMenus.forEach(select => select.addEventListener('change', updateTotal))

// const hddqty = document.getElementById('hddqty')
// const ssdqty = document.getElementById('ssdqty')
// const ramqty = document.getElementById('ramqty')



const totalDisplay = document.getElementById('total')
const totalNum = document.getElementById('totalNum')

function updateTotal() {
    let runningTotal = 0
 
    for (const select of pricedMenus) {
        const selectedOption= select.options[select.selectedIndex]
        const price = Number(selectedOption.dataset.price)
        runningTotal += price
    }

    // totalDisplay.textContent = `Total: $${runningTotal.toFixed(2)}`
    totalNum.value = runningTotal.toFixed(2);
}

// To initially calculate the price for boot drive
updateTotal();
