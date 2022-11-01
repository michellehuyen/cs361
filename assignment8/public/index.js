var convert_btn = document.getElementById('convert-btn')
convert_btn.addEventListener('click', function() {
    console.log("Button was clicked!")
    
    var macronutrient = document.getElementById('macronutrient_name')
    var grams = document.getElementById('grams')
    
    if (macronutrient.value.length == 0 || grams.value.length == 0) {
        window.alert("You must fill in all the boxes!")
    }
    else {
        var url = 'http://127.0.0.1:5000/calculate-cals/' + macronutrient.value + '/' + grams.value
        console.log(httpGet(url))
        clearInput()
    }
})

// https://stackoverflow.com/a/4033310
function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest()
    xmlHttp.open( "GET", theUrl, false ) // false for synchronous request
    xmlHttp.send( null )
    var amount = JSON.parse(xmlHttp.responseText).calories
    window.alert("The input is " + amount + " calories")
}

function clearInput() {
    document.getElementById('macronutrient_name').value = ''
    document.getElementById('grams').value = ''
}