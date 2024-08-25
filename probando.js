// const username = "";
// const password = "";

// function input(passwordOne){
//     try{
//         if(passwordOne === ""){
//             throw "please enter a password"
//         }
//         console.log("you typed your password")
//     }
//     catch(error){
//         console.log("can you please re type your password?")
//     }

// }

// input(password)




// let age = ["Michelle", "Valeria", "Sofia", "Estefania", "Mango"]

// const u = age.filter(e => {
//     return e[0] === "M"
// })

// console.log(u)



// const age = [23, 45, 12, 10];

// const sum = () => {
//    const result = age.reduce((prev, curr) =>{
//     return prev + curr
//    })
// }

// console.log(sum())



// // Callbacks

// //1.- we call add(2,4, logResult)
// //2.- add() function is working we sotred the result in the result variable
// //3.- after the sum is being completed, the callback will start insie of the callback we stored "result" AND we called the logResult function add(2,4, logResult), its like a combination
// //4.- after the add has been completed, since we called logResult() it will start working on that function "AFTER ADD() is completed"


// const add = (num1, num2, callback) => {
//     let result = num1 + num2
//     callback(result) // after the function is being "perfomed" it goes to the callback with result as a parameter
// }

// function logResult(result){
//     console.log(`The Result it's ${result}`)
// }

// add(2,4, logResult)

// const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// function callback(num){
//     return num % 2 === 0
// }

// const evenNumbersArray = numbers.filter(callback);
// console.log(evenNumbersArray);
// console.log("This is a synchronous code....")





// function multiplyCallback(num){
//     const result = num * 2;
//     console.log(`The input doubled is equal to ${result}`)
// }

// function doSomeMath(input, callback){
//     console.log("We are doubling the input number") 
//     callback(input)
// }

// doSomeMath(2, multiplyCallback) // 1.- step. we call the function the callback "multiplyCallback" we set it in the parameter after the message is being completed, we call the other function










// function callbackFunc(){
//     console.log("Executed last because we are using asynchronous code.")
// }

// setTimeout(callbackFunc, 2000);

// console.log("executed first")
// console.log("executed last")




// const array = ['hello', 'world', 'this', 'is', 'great'];
// let result = array.entries()
// const prueba = () => {
//     let resultado = ""
//     for(const [index, value] of result){
//        resultado += index 
//     }
//     return resultado
// }

// console.log(prueba())


// const words = ['hello', 'world', 'this', 'is', 'great'];

// function smash(words){
//     let iteration = words.entries();
//     let result = " "

//     for(const [index, value] of iteration){
//         result += value + " "
//     }
//     return result
// }

// console.log(smash(words))


// ages = [33,21,5,19,17]


// function differenceInAges(ages){
//   const newAges = ages.sort((a, b) => a - b);
//   let youngest = newAges[0];
//   let oldest = newAges[newAges.length - 1]
//   let difference = oldest - youngest
//   return [difference, youngest, oldest]
// }

// console.log(differenceInAges(ages))



















// const dessertStock = {
//     cheeseCake: 10,
//     moltenCake: 7,
//     spongeCake: 3
// };

// function orderCake(){
//     return new Promise(function(r, re){
//         if(dessertStock.cheeseCake > 0){
//             r("Cheesecake is available!")
//         } else{
//             re("Cheesecake is not available")
//         }
//     })
// }
// const handleSuccess = (successValue) => {
//     console.log(successValue)
// }

// function handleFailure(failureValue){
//     console.log(failureValue)
// }

// const makeOrder = orderCake()
// makeOrder.then(handleSuccess).catch(handleFailure)












// const array = [2,6,3,43,12,7,9,4,3]
// // let ent = array.entries()

// function sortByValueAndIndex(array){
//  let result = ""
  

//     for( const[index,value] of array){
//         result += (index + 1)  + " " + value + ", "
//     }
//     return result
//   }

//   console.log(sortByValueAndIndex(array))




// const n = 4923618


// const descendingOrder = () => {
//     //Here i am converting the integer into a string 
//     const nString = n.toString()
//     //once the integer its a string i will split it and each number will be in an array separated with a comma
//    const result = nString.split("")
//    //once each number is separated i will sort it from descending order
//     result.sort((a,b) => b - a);
//     //and Here i used join() and it automatically joins it as an integer 
//     const finalAnswer =  result.join("")
   

//     return finalAnswer
// }

// console.log(descendingOrder())




// const str = 321

// function blowCandles() {

//     //iteration break

//     // let iteration = 1

//   //
//     const strString = str.toString();
//   const strSplit = strString.split("");
//   let parse = strSplit.map((e) => parseInt(e));
//   // let newValue = 2
//  let iteration = 0
  
   
//   while (parse.map((e) => e -= 1)){
//   parse = parse.map((num) => num > 0 ? num - 1 : num);
//   iteration++
//   console.log(parse)
//   }

//  }
// // console.log(blowCandles())

// blowCandles()




// outerLoop: while(true){
  
//   for(const  value of parse){
//     console.log("hola" + value)
//   }
// }
//   return newValue







// const array = []

// function findAverage(array) {
 
//     let add
//    if(array.length === 0 || array.some(isNaN)){
//    return 0 

//    } else{
//     add = array.reduce((e, w) => e + w,0);
    
//    }
//    const finalAnswer = add / array.length
//     return finalAnswer
//   }

//   console.log(findAverage(array))




// [1, 2, 3, 4, 1]	3	[1, 2, 1]

// const array = [1, 2, 3, 4, 1]
// let n = 4

// function firstNSmallest(array, n){
//    const descArray = array.sort((a,b) => a - b);
//    const result = [];

//    for(let i = 0; i < n; i++){
//     result.push(descArray[i])
//    }
//    return result
//   }

//   console.log(firstNSmallest(array, n))














// const array = [1, 2, 3, 4, 1]
// let n = 4

// function firstNSmallest(array, n){
//    const result = [];
   
//         for(let i = 0; i < array.length; i++ ){
//             if(array[i] < n){
//                 result.push(array[i])
//             }
//         }
    
//         return result
//   }

//   console.log(firstNSmallest(array, n))




// const x = [5, 3, 2, "6", 7, "9", 2, "4"]

// function sumMix(x){
//     let result = 0 

//   for(const value of x){
//     result = result + parseInt(value);
    
//   }
//   return result
// }

// console.log(sumMix(x))





// const objects = {
//   "prop1": "string",
//   "prop2": 'string',
//   prop3: 123,
//   prop4: ["array", "value", 123],
//   prop5: function(){
//     console.log("Hello this is an object!")
//   },
//   prop6: null,
//   prop7: true
// }























// objects.prop5

// class person {
//   constructor(name, age) {
//     this.name = name; //the parameter name will now be inside of this.name
//     this.age = age;
//   }
//   greet(){
//     console.log(`Hello my name is ${this.name} and i am ${this.age} old`)
//   }
// }

// class student extends person{
//   study(){
//     console.log(`${this.name} is studying`)
//   }
// }

// const rene = new person("Rene", 21)
// const michelle = new person("Michelle",19)

// rene.greet(); //Hello my name is Rene and i am 21 old
// michelle.greet()//Hello my name is Michelle and i am 19 old

// //This might not be the best example but i am showing how can a class extend
// const estudiante = new student("Michelle")
// estudiante.study() //Michelle is studying




// word = "abccdefee"
// //cceee

// function deleted(word){
//  let charCount = {} // here we created an empty object to count each charecter
//   for(char of word){ // Here we are iterating over each letter of word
//     charCount[char] = (charCount[char] || 0) + 1; //charCount[char] access the count of current charecter 

//   }
// }

// deleted()


//Case
// function whatday(num){
//   let weekday
//   switch (num){
//     case 1:
//       weekday = "Sunday"
//       break
//     case 2:
//       weekday = "Monday"
//       break 
//     case 3:
//         weekday = "Tuesday"
//         break
//     case 4:
//         weekday = "Wednesday"
//         break    
//     case 5:
//           weekday = "Thrusday"
//           break
//     case 6:
//           weekday = "Friday"
//           break 
//     case 7:
//             weekday = "Saturday"
//           break     
//     default:
//       return "Wrong, please enter a number between 1 and 7"
    
//   }
//   return weekday

// }

// console.log(whatday(7))






//Getting the difference of the largest and smallest number

// const numbers = [21, 34, 54, 43, 26, 12]

// function betweenExtremes() {
//   const sortedArray = numbers.sort((a,b) => a - b)
//   let smallestNumber = sortedArray[0];
//   let largestNumber = sortedArray[sortedArray.length - 1]
//   let difference = largestNumber - smallestNumber
//   return difference
// }
  

// console.log(betweenExtremes())





const example = [1, 1]

function add(){
  let result = 0
  let lastNumber = example[example.length - 1] 
  //let final = 0

  const exampleIterable = example.entries()

  while (example.length !== 20){

    lastNumber = example[example.length - 1] 
   
    for (const [index, value] of exampleIterable){
      result += value
    }
    
    example.push(result)
    example.push(lastNumber)

    final = lastNumber + result + 1
     example.push(final)
  }
}

add()
console.log(example)





// const example = [1, 1]

// function add(){
//   let result = 0
//   let lastNumber = example[example.length - 1] 
//   const exampleIterable = example.entries()
//   for (const [index, value] of exampleIterable){
//     result += lastNumber
//   }
  
//   example.push(result)
//   example.push(lastNumber)
// }

// add()
// console.log(example)


