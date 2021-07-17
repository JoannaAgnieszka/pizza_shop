let deliveryPoint = document.getElementById('id_delivery_point')

let address = []
address.push(document.getElementById('id_city'))
address.push(document.getElementById('id_postal_code'))
address.push(document.getElementById('id_street'))
address.push(document.getElementById('id_house_nr'))
console.log(address)

deliveryPoint.addEventListener('change', function() {

    if (deliveryPoint.selectedIndex === 7) {
    unlockAddress()
    }
    else {
    lockAddress()
    }
})

function unlockAddress() {
    for (let i=0; i<address.length; ++i){
    address[i].removeAttribute('disabled')
    }
}

function lockAddress() {
    for (let i=0; i<address.length; ++i){
    address[i].setAttribute('disabled', '')
    }
}

let pickupMethod = document.getElementById('id_pickup_method')

pickupMethod.addEventListener('change', function() {
    if (pickupMethod.selectedIndex === 1) {          //odblokowac
        deliveryPoint.removeAttribute('disabled')
    }
    else {
        deliveryPoint.setAttribute('disabled', '')
        lockAddress()
    }
})
