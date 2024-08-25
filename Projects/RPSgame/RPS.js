const game = () => {
    let pScore = 0;  // player score
    let cScore = 0;  // computer score


    //start game
    const StartGame = () => {
        const playButton = document.querySelector(".intro button");
        const introScreen = document.querySelector(".intro");
        const match = document.querySelector(".match");


        playButton.addEventListener("click", () => {
                introScreen.classList.add("fadeOut");
                match.classList.add("FadeIn");
        });
    }
    
//play match

const playMatch = () =>{
    const options = document.querySelectorAll(".options button");
    const playerHand = document.querySelector(".player-hand");
    const computerHand = document.querySelector(".computer-hand");
    const hands = document.querySelectorAll(".hands img");
    
    hands.forEach((hand) =>{
        hand.addEventListener("animationend", function(){     // no entiendo esto
            this.style.animation = ""
        })
    })

    //computer options
    const computerOptions = ["rock", "paper", "scissors"];

options.forEach((option) => {
    option.addEventListener("click", function(){                // con el forEach lleva los tres botones
        //computer choice
        const computerNumber = Math.floor(Math.random() * 3);
        const computerChoice = computerOptions[computerNumber];
        
        //here where we callled compareHand




       setTimeout(() =>{
        compareHands(this.textContent,computerChoice) //(this.textContent)

        //Update images
        playerHand.src = `./Projects/RPSgame/RPSpictures/${this.textContent}.png`; // ./fotos/${this.textContent}.png
        computerHand.src = `./Projects/RPSgame/RPSpictures/${computerChoice}.png`;  // /Projects/RPSgame/RPSpictures/picture1.png
       },2000)



//animation
playerHand.style.animation = ("shakePlayer 2s ease");
computerHand.style.animation = ("shakeComputer 2s ease")
    });                                         
});  
};




const updateScore = () => {
    const playerScore = document.querySelector(".player-score p");
    const computerScore = document.querySelector(".computer-score p");
    
    playerScore.textContent = pScore;
    computerScore.textContent = cScore;
}




const compareHands = (playerChoice, computerChoice) => {
    const winner = document.querySelector(".winner");


    //checking a tie
    if(playerChoice === computerChoice){
        winner.textContent = "it's a tie";
        return;
    }

    //check for rock
    if(playerChoice === "rock"){
        if(computerChoice === "scissors"){
            winner.textContent = "Player wins";
            pScore++;
            updateScore();
            return
        }else {
            winner.textContent = "Computer wins"
            cScore++;
            updateScore();
            return
        } 
    }

    //check for paper
    if(playerChoice === "paper"){
        if(computerChoice === "rock"){
            winner.textContent = "Player wins"
            pScore++;
            updateScore();
            return
        }else {
            winner.textContent = "Computer wins"
            cScore++;
            updateScore();
            return
        } 
    }
    //check for scissors

    if(playerChoice === "scissors"){
        if(computerChoice === "paper"){
            winner.textContent = "Player wins"
            return;
        }else {
            winner.textContent = "Computer wins";
            return;
        } 
    }

    if(pScore === 3){
        const playerHand = document.querySelector('.player-hand');
        playerHand.src = '/Projects/RPSgame/RPSpictures/azul.jpg';
    }
}

// call the inner functions.
  StartGame()
  playMatch()
//   compareHands()  while
}

//start the game

game()

fadeOut