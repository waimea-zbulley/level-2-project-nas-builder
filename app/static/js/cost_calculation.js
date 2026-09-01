const pricedMenus = document.querySelectorAll('.priced')
pricedMenus.forEach(select => select.addEventListener('change', updateTotal))

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

