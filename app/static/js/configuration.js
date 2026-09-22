// PRICING ============================================================

const pricedMenus = document.querySelectorAll('.priced')
pricedMenus.forEach(select => select.addEventListener('change', updateCost))



const totalDisplay = document.getElementById('total')
const totalNum = document.getElementById('totalNum')

function updateCost() {
    let runningTotal = 0
 
    for (const select of pricedMenus) {
        const selectedOption= select.options[select.selectedIndex]
        const price = Number(selectedOption.dataset.price)
        runningTotal += price
    }

    // totalDisplay.textContent = `Total: $${runningTotal.toFixed(2)}`
    totalNum.value = runningTotal.toFixed(2);
}


// Powerdraw ======================================================

const powerdraw = document.querySelectorAll('.power')
powerdraw.forEach(select => select.addEventListener('change', updatePower))

// const totalDisplayPower = document.getElementById('totalPower')
const powerTotal = document.getElementById('totalPower') 

function updatePower() {
    let runningTotal = 0

    for (const select of powerdraw) {
        const selectedOption= select.options[select.selectedIndex]
        const power = Number(selectedOption.dataset.power)
        runningTotal += power
    }

    // totalDisplay.textContent = `Total: $${runningTotal.toFixed(2)}`
    powerTotal.value = runningTotal.toFixed(2);
}

// HDD storage

// const hddStorage = document.getElementById('hdd')
// const hddQuantity = document.getElementById('hddqty')

// hddStorage.addEventListener('change', updateHddStorage)
// hddQuantity.addEventListener('input', updateHddStorage)


// // const totalDisplayPower = document.getElementById('totalPower')
// const totalHddStorage = document.getElementById('totalHddStorage') 

// function updateHddStorage() {
//     let runningTotal = 0
    

//     for (const select of hddStorage) {
//         const selectedOption= select.options[select.selectedIndex]
//         const storage = Number(selectedOption.dataset.hdd)
//         const quantity = Number(hddQuantity.value)

//         runningTotal += storage * quantity
//     }

//     // totalDisplay.textContent = `Total: $${runningTotal.toFixed(2)}`
//     totalHddStorage.value = runningTotal.toFixed(2);
// }

// To initially calculate the price for boot drive
updateCost();
updatePower();


