
const input = document.querySelector('#input')
const output = document.querySelector('#output')
const numberfrom = document.getElementById("numberfrom");
const currencyfrom = document.getElementById("currencyfrom");
const numberto = document.getElementById("numberto");
const currencyto = document.getElementById("currencyto");

axios.get("https://api.apilayer.com/fixer/latest?apikey=rbr5VSR5XLQFhLRf17kidOnGeYCLJEHJ")
.then((res)=> {
    let current = res.data.rates
    valueofcurrency = Object.values(current)
   console.log(valueofcurrency)
    Object.keys(current).map(item => {
        let option = document.createElement("option");
        let option2 = document.createElement("option");
        option.value = item;
        option2.value = item;
        option.text = item;
        option2.text = item;
        document.getElementById("currency1").appendChild(option)
        document.getElementById("currency2").appendChild(option2)
    })

        input.addEventListener('keyup' , ()=> {
            output.value = input.value * current[document.querySelector('#currency2').value] / current[document.querySelector('#currency1').value] ;
            numberto.textContent = output.value ; 
        })
        console.log(current[document.querySelector('#currency1').value])

        input.addEventListener("change", function changeHandler(event) {
        numberfrom.textContent = document.querySelector('#currency1').value; 
        currencyfrom.textContent = input.options[input.selectedIndex].value ; 
        currencyto.textContent = document.querySelector('#currency2').value; 
        });
    })