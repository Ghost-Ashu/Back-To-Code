import Controller from "./controller.js";
import Calculadora from "./pages/calculadora.js";

export default class App{
    
    constructor(){
        new Calculadora().carregar();
    }
    
}

new App();
