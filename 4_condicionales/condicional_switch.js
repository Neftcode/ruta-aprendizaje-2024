// Programa que determina la clasificación de la una nota utilizando el condicional SWITCH
console.log("--- Programa que determina la clasificación de la una nota utilizando el condicional SWITCH ---\n")
var nota = prompt("Ingrese su nota entre 1.0 y 5.0 incluyente: ")

console.log("La nota ingresada es: " + nota)

// Validar si la nota ingresada está entre 1.0 y 5.0 incluyente
if ( (nota < 1.0) || (nota > 5.0) ) {
    console.log("Error")
} else {
    if (nota >= 3.3) {
        console.log("APROBÓ")
    } else {
        console.log("REPROBÓ")
    }

    // Condicional if concatenado o extendido
    /*
    Clasificación de notas:
    1.0 - 2.0 -> "Muy mal"
    2.1 - 3.2 -> "Mal"
    3.3 - 3.9 -> "Regular"
    4.0 - 4.5 -> "Sobresaliente"
    4.6 - 5.0 -> "Excelente"
    */

    if (nota>=1.0 && nota<=2){
        console.log("Muy mal")
    } else if (nota>=2.1 && nota<=3.2) {
        console.log("Mal")
    } else if (nota>=3.3 && nota<=3.9) {
        console.log("Regular")
    } else if (nota<=4.0 && nota <=4.5) {
        console.log("Sobresaliente")
    } else {
        console.log("Excelente")
    }

    /*switch (parseFloat(nota)) {
        case 1.0: console.log("Muy mal"); break;
        case 1.1: console.log("Muy mal"); break;
        case 1.2: console.log("Muy mal"); break;
        case 1.3: console.log("Muy mal"); break;
        case 1.4: console.log("Muy mal"); break;
        case 1.5: console.log("Muy mal"); break;
        case 1.6: console.log("Muy mal"); break;
        case 1.7: console.log("Muy mal"); break;
        case 1.8: console.log("Muy mal"); break;
        case 1.9: console.log("Muy mal"); break;
        case 2.0: console.log("Muy mal"); break;
        case 2.1: console.log("Mal"); break;
        case 2.2: console.log("Mal"); break;
        case 2.3: console.log("Mal"); break;
        case 2.4: console.log("Mal"); break;
        case 2.5: console.log("Mal"); break;
        case 2.6: console.log("Mal"); break;
        case 2.7: console.log("Mal"); break;
        case 2.8: console.log("Mal"); break;
        case 2.9: console.log("Mal"); break;
        case 3.0: console.log("Mal"); break;
        case 3.1: console.log("Mal"); break;
        case 3.2: console.log("Mal"); break;
        case 3.3: console.log("Regular"); break;
        case 3.4: console.log("Regular"); break;
        case 3.5: console.log("Regular"); break;
        case 3.6: console.log("Regular"); break;
        case 3.7: console.log("Regular"); break;
        case 3.8: console.log("Regular"); break;
        case 3.9: console.log("Regular"); break;
        case 4.0: console.log("Sobresaliente"); break;
        case 4.1: console.log("Sobresaliente"); break;
        case 4.2: console.log("Sobresaliente"); break;
        case 4.3: console.log("Sobresaliente"); break;
        case 4.4: console.log("Sobresaliente"); break;
        case 4.5: console.log("Sobresaliente"); break;
        case 4.6: console.log("Excelente"); break;
        case 4.7: console.log("Excelente"); break;
        case 4.8: console.log("Excelente"); break;
        case 4.9: console.log("Excelente"); break;
        case 5.0: console.log("Excelente"); break;
    }*/
}

console.log("\n\nFin del programa");