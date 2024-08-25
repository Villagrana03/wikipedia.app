const arr = [2,4,5,0,8,65,false,2,4,0,8,0,2]


function moveZeros(arr) {
    const firstArr = [];
    const secondArr = [];

    
    for(const value of arr){
      if(value !== 0){
         firstArr.push(value)
    } else{
       secondArr.push(value)
    }
      
    }
return firstArr.concat(secondArr)
  }

  console.log(moveZeros())