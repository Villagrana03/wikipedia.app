// 1.- deposit money
// 2.- choose number of lines to bet
// 3.- collect a bet amount
// 4.- spin slot machine
// 5.- check if winner won
// 6.- give user the winning
// 7.- play again

const prompt = require("prompt-sync")();

const ROWS = 3;
const cols = 3;

const symbolsCount = {
    A: 2,
    B: 4,
    C: 6,
    D: 8
};

const symbolValues = { // if i get a row ood "A" i am going to multiply by 5m if i get a line of "C" multiply by 3
    A: 5,
    B: 4,
    C: 3,
    D: 2
}



const deposit = () => {

    while(true){ // here i am looping until is not a invalid value/
        const depositAmount = prompt("Enter a Deposit amount: ") // asking the user to enter a numbr 
        const numberDepositAmount = parseFloat(depositAmount); // Here i am converting depositAmount into a whole number
        
        if(isNaN(numberDepositAmount) || numberDepositAmount <= 0){  //NaN not a number, i am checking if numberDepositAmount is not a number
            console.log("invalid value")
        }else{
            return numberDepositAmount;
            
        }
    }
  
}

const getNumberLinesOfLines = () => {
    while(true){ // here i am looping until is not a invalid value/
        const lines = prompt("Choose how many lines do you want to bet on between 1 and 3: ") // asking the user to enter number of lines to bet
        const numberOfLines = parseFloat(lines); // Here i am converting lines into a whole number
        
        if(isNaN(numberOfLines) || numberOfLines > 3 || numberOfLines <= 0){  //NaN not a number, i am checking if numberDepositAmount is not a number
            console.log("invalid number of lines, try again.")
        }else{
            return numberOfLines;
        }
    }
}

const getBet = (balance, lines) => {
    while(true){ // here i am looping until is not a invalid value/
        const bet = prompt("Enter the bet per line:  ") // asking the user to enter total betbet
        const numberBet = parseFloat(bet); // Here i am converting bet into a whole number
        
        if(isNaN(numberBet) || numberBet <= 0 || numberBet > balance / lines){  //NaN not a number, i am checking if numberBet is not a number
            console.log("invalid bet")
        }else{6
            return numberBet;
        }
    }
}
 
const spin = () => {
    const symbols = [];

    for(const [symbol, count] of Object.entries(symbolsCount)){ //entries means that will get every value of symbolsCount object and i am gettibng each valkue and putting
        for(let i = 0; i < count; i++){
            symbols.push(symbol)  // i put symbols first, because its the array and i will be pushing every value of the object

        }
    }
   const reels = []; // every array represents a column of the slot array
   for(let i = 0; i < cols; i++){
    reels.push([])
    const reelSymbols = [...symbols]; //shallow copy copy the symbols that we have available to choose from each reel, ----------> what is it doing, here its looping the first column, for example, we can only have 2 A in the first column, but we cannot modify the first array which is "symbols", when the next loop start, which is the next column, we will need to have the 2 A available, (in case they were use) thats why we cannot modift the main array(symbols) 
    for(j =0; j < ROWS; j++){ //for every column pick the 3 elements that are inside
        const randomIndex = Math.floor(Math.random() * reelSymbols.length) // here we are generating a random index 
        const selectedSymbol = reelSymbols[randomIndex]; //selecting the symbol at this index
        reels[i].push(selectedSymbol); //adding it to this array
        reelSymbols.splice(randomIndex, 1) //. we are removing so we dont select it again 
   }
}

return reels
}

const transpose = (reels) => {
    const rows = [];

    for(let i = 0; i < ROWS; i++){
        rows.push([]);
        for(let j = 0; j < cols; j++){ //for evry row loops, and for every column loops
            rows[i].push(reels[j][i])
        }
    }

    return rows
}

const printRows = (rows) => {
    for(const row of rows){ // i am looping through the array
        let rowString = "";
        for(const [i, symbol] of row.entries()){
            rowString += symbol;
            if(i != row.length - 1){
                rowString += " | "
            }
        }
        console.log(rowString)
    }
}

const getWinnings = (rows, bet, lines) => {
    let winnings = 0;
    for(let row = 0; row < lines; row++){
        const symbols = rows[row];
        let allSame = true;

        for(const symbol of symbols){
            if(symbol != symbols[0]){
                allSame = false;
                break;
            }
        }

        if(allSame){
            winnings += bet * symbolValues[symbols[0]]
        }
    }
    return winnings;
}

const game = () => {
    let balance = deposit(); //what ever the user types for deposit it will be sotred at balance

    while(true){
        console.log("You have a balance of $ " + balance)
        const numberOfLines = getNumberLinesOfLines();
const bet = getBet(balance, numberOfLines);
balance -= bet * numberOfLines;
const reels = spin();
const rows = transpose(reels)
printRows(rows);
// console.log(reels);
// console.log(ROWS)

const winnings = getWinnings(rows, bet, numberOfLines)
balance += winnings;
console.log("you won, $" + winnings);

        if(balance === 0){
            console.log("you ran out of money")
            break;
        }
        const playAgain = prompt("do you want to play again? (y/n)");

        if(playAgain != "y" || playAgain != "Y"){
            break;
        }
    }
}

game();