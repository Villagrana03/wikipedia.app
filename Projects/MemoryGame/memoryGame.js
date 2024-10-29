
//Here i am selecting all the cards
const cards = document.querySelectorAll(".memory-card")

let hasFlippedCard = false;
let lockBoard = false;
let firstCard
let secondCard

// i set this at first because we will also start the game, when we want to call a function we set it like this, multiply(), but in this case i am calling the function and the syntax its like this (function functionExample(){}) ()
(    function shuffle(){
    //Here i am looping trhough each value at cards. and i will use Math random to random their position
    cards.forEach((card) => {
        let randomPos = Math.floor( Math.random() * 12);

        //The line card.style.order = randomPos; sets the CSS order property of each card element to a random value, effectively shuffling the order of the cards on the screen.
        card.style.order = randomPos
    })
})()

function flipCard(){
    //Here i am checking if lockBoard is true
    //This is how it works, as soon as the function starts, (it starts once the user click to the first item, automatically it sets lockBoard to true) so the flipCard function
   
    //also, it checks if lockBoard is ture, snce its false continue to the code, ut once the first card is clicked it will become ture at unflipcards() function.
    if(lockBoard === true) return;
    if(this === firstCard) return;
    
 //Here we will access each memory with the this ALSO NOTE "this" must be in a normal function and not arrow
    //In event handlers, this typically refers to the element that received the event. for inatance, each button is being pressed
    this.classList.add('flip')
    
    //check if hasFlippedCard is true

    // what  "this" is, storing the "value" of the card everytime the user clicks on iut, to se if it matchs with the other card, if not we will start again.
    if(!hasFlippedCard){
        //First time user clicked the card
        hasFlippedCard = true;  // Set hasFlipped to true indicating that a card has been flipped
        firstCard = this; // Store the reference to the first flipped card
    } else{
        //second CLick
        hasFlippedCard = false;
        secondCard = this;
        // console.log(firstCard, secondCard)

        checkForMatch()
    
    }
   
}

    function checkForMatch(){
                //Check if cards are the same 
    if(firstCard.dataset.framework === secondCard.dataset.framework){
       disableCards()
    } else{
       unFlipCards()
    }
    }

    function disableCards(){
        //If the cards selected are the same we wilkl disable their function so it does not flip again
        firstCard.removeEventListener("click", flipCard);
        secondCard.removeEventListener("click", flipCard);
    }

    const unFlipCards = () =>  {
        // if it going to perfom this function, or flip cards it will lock th board, then continue to the timeout and then unlock the board by setting it to false
        lockBoard = true

        setTimeout(() => { //in case the user did not select the correct answers, we will flip the cards again using the .remove classlist, since we add it at the beggining of the function
            firstCard.classList.remove('flip');
        secondCard.classList.remove('flip');

        // here it unlocked the board and set it to false 
        lockBoard = false;
        }, 1000)
    }

    function resetBoard(){
        //this happens when the page is refreshed
        // [value1, value2] = [value1, value2]
        [hasFlipped, lockBoard] = [false, false];
        [firstCard, secondCard] = [null, null]
    }



//Here i am going to loop through every card, since i selected all the cards. And for every card selected, flipCard function will occur.
cards.forEach((card) => {
    card.addEventListener("click", flipCard)
}) 