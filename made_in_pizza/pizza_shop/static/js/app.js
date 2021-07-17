// document.addEventListener('DOMContentLoaded', function (){   //DOM content loaded wywoła sie po załadowaniu całej strony
//     let button = document.getElementById('add_ingredients');
//     let notMain = document.querySelectorAll('.ingredient:not(.main)');
//     button.addEventListener('click', function (){
//         for (let i = 0; i < notMain.length; i++) {
//             notMain[i].classList.toggle('show');
//         }
//     })
//     button.click()
// })
let notMain = document.querySelectorAll('.ingredient:not(.main)');

function show_ingredients(){
        for (let i = 0; i < notMain.length; i++) {
            notMain[i].classList.toggle('show');
        }
    }

function show_regular_price(){  //tylko dla pizzy przelaczanie sie z jednej ceny wg rozmiaru na drugą
    price.textContent = price.textContent - priceDifference;
}


function show_big_price(){
    price.textContent = parseInt(price.textContent) + priceDifference;
}


let price =  document.getElementById('price')
let smallPizzaPrice = document.getElementById('smallPizza')  //przycisk radio
let bigPizzaPrice = document.getElementById('bigPizza') //przycisk radio

if(smallPizzaPrice && bigPizzaPrice){
    let priceDifference = parseInt(document.getElementById('big_price').textContent) - parseInt(document.getElementById('regular_price').textContent);
    smallPizzaPrice.addEventListener('click', show_regular_price, false);
    bigPizzaPrice.addEventListener('click', show_big_price, false);
}


let btnPlus = document.querySelectorAll('.plus');
let btnMinus = document.querySelectorAll('.minus');


function addValue(){
    this.nextElementSibling.textContent++;
    let btnPlus = this;
    let ingredientPrice = this.parentElement.querySelector('.price');
    let mainPrice = parseInt(ingredientPrice.textContent) + parseInt(price.textContent);
    price.textContent = mainPrice;
}


for(let i=0; i<btnPlus.length; ++i){
    btnPlus[i].addEventListener('click', addValue);
}


function decreaseValue(){
    let counter = this.previousElementSibling;
    if (counter.textContent > 0){
        this.previousElementSibling.textContent--;
    }
    let btnMinus = this;
    let ingredientPrice = this.parentElement.querySelector('.price');
    let mainPrice = parseInt(price.textContent) - parseInt(ingredientPrice.textContent);
    price.textContent = mainPrice;
}


for(let i=0; i<btnMinus.length; ++i){
    btnMinus[i].addEventListener('click', decreaseValue);
}


// function countDifference(){
//     let pizzaPriceDifference = bigPizzaPrice - smallPizzaPrice;
//     console.log(pizzaPriceDifference);
// }


function addHiddenInput(){
        let counter = document.querySelectorAll(".counter")
    for(let i=0; i<counter.length; ++i){
        let newItem = document.createElement("input")
        newItem.value = counter[i].innerText
        newItem.name = 'ingredientQuantity'
        newItem.type = 'hidden'
        if(newItem.value !=="0"){
        counter[i].parentElement.appendChild(newItem)
        }

    }
}


let form = document.querySelector("form")
form.addEventListener('submit', function(event){
    event.preventDefault()
    addHiddenInput()
    add_user_price()
    this.submit()
});


function add_user_price(){
    let price = document.getElementById('price')
    let priceValue = price.innerText
    let newInput = document.createElement('input')
    newInput.type = 'hidden'
    newInput.name = 'user_price'
    newInput.value = priceValue
    form.appendChild(newInput)
}








//1. w funkcji addValue znalezc element zawierajacy cene skladnika, w ktorym znajduje sie przycisk plus(this)
// 2. uzyc elementu price i dodac do niego (textContent) dodac do niego znaleziona w p.1 cenę. Uwaga: pamietaj o parseFloat()
//3. i dla przycisku minus w funkcji decreaseValue









// let ingredientPrice = 1;
// let count_ingredientPrice = document.getElementById('ingredientPrice');
// count_ingredientPrice.addEventListener('click', function(){
//     ingredientPrice++;
//     count_ingredientPrice.value = ingredientPrice;
// }
//
// function minus(){
//     if (ingredientPrice > 1){
//         ingredientPrice--;
//         count_ingredientPrice.value = ingredientPrice;
//     }
// }







// function renderTime() {
//     let myDate = new Date();
//     let year = myDate.getFullYear();
//     let day = myDate.getDay();
//     let month = myDate.getMonth();
//     console.log(year, day, month);
//
//     let dayArray = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
//     let monthArray = ['January', 'February', 'March', 'April', 'May', 'June',
//                       'July', 'August', 'September', 'October', 'November', 'December'];
//
//     let currentDate = document.getElementById('date_display');
//     currentDate.textContent = dayArray[day]+ ' ' +monthArray[month]+ ' ' +year;
//
// }
//     renderTime();
