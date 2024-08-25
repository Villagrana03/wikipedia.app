//const game = document.querySelector(".game"); //the whole div 
const startGame = document.getElementById("startGame");  //Button to start the game
const gameParent = document.querySelector(".gameParent")




//functions
const mainPage = () => {
    const gameDiv = document.createElement("div"); //Here i create a div that will be inside of .game which is the parent
    gameDiv.classList.add("gameDiv"); // i added the class gameDiv to the div i created.
    gameParent.appendChild(gameDiv)


}

//Event listeners
startGame.addEventListener("click", mainPage)