//3. Converter um Array de Celsius para Fahrenheit
let temperaturasC = [0,20,30];
let temperaturasf = temperaturasC.map((temperatura) => temperatura * 1.8 + 32);
console.log(temperaturasf)

function temperaturaFahrenheit(grauCelsius){
    return temperaturasC.map((temperatura) => temperatura*1.80 + 32);
}
console.log(temperaturaFahrenheit(temperaturasC));