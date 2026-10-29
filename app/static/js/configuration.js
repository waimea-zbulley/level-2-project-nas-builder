// PRICING ============================================================

const pricedMenus = document.querySelectorAll('.priced')
pricedMenus.forEach(select => select.addEventListener('change', updateCost))
const quantityInputs = document.querySelectorAll('.quantity')
quantityInputs.forEach(select => select.addEventListener('change', updateCost))



const totalDisplay = document.getElementById('total')
const totalNum = document.getElementById('totalNum')

function updateCost() {
    let runningTotal = 0
 
    for (const select of pricedMenus) {
        let qty = 1

        const fieldset = select.closest('fieldset')
        if (fieldset) {
            const qtyInput = fieldset.querySelector('input[type="number"]')

            if (qtyInput) {
                qty = qtyInput.value
            }
        }

        const selectedOption= select.options[select.selectedIndex]
        const price = Number(selectedOption.dataset.price)
        
        
        runningTotal += qty * price
    }

    // totalDisplay.textContent = `Total: $${runningTotal.toFixed(2)}`
    totalNum.value = runningTotal.toFixed(2);
    totalDisplay.textContent = runningTotal.toFixed(0);
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


updateCost();
updatePower();


