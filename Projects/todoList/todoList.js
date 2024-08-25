//Getting ID values

//Here i am getting the value of the button
const buttonCreatetodo = document.getElementById("buttonCreatetodo");
const titleInput = document.getElementById("title");
const authorInput = document.getElementById("author");
const bodyInput = document.getElementById("body");
const deleteTodo = document.getElementById("deleteTodo")

// eventlisteners
 buttonCreatetodo.addEventListener("click", createList);
 deleteTodo.addEventListener("click", deleteList)

class toDoList {
    constructor(title, body, author){
        this.title = title;
        this.body = body;
        this.author = author;
        this.completed = false
    }

 
    markAsCompleted() {
        this.completed = true;
      }
}

class storeTodo{
    constructor(){
        this.tasks = [];
    }

    addTask(task){
        this.tasks.push(task)
    }

    // getTasks(task){
    //     return this.tasks
    // }
}


  

//Here i am setting the storeTodo into todoStore
const todoStore = new storeTodo();



//everytime the user clicks the button the list will appear.
function createList(){

  //Here i am going to store the value of the user inside of variables
  const title = titleInput.value;
  const body = bodyInput.value;
  const author = authorInput.value;


    //Here i am creating a todo list instace,
   const newTodo = new toDoList(title, body, author); 



    //Here i am creating a div everytime we click the button
   const createTodo =  document.createElement("div")
    createTodo.classList.add("toDoList");

    createTodo.innerHTML =  `<strong>Title:</strong> ${newTodo.title}<br>
    <strong>Body:</strong> ${newTodo.body}<br>
    <strong>Author:</strong> ${newTodo.author}`


        // Append the created div to an existing element in the DOM
        const pageBody = document.querySelector(".pageBody");
        //append means that mkaes a child of pageBody
        pageBody.appendChild(createTodo);


    
    //storing every value into todoStore 
   todoStore.addTask(newTodo);
   console.log(todoStore)


            // Clear input fields after creating the to-do
            titleInput.value = '';
            bodyInput.value = '';
            authorInput.value = '';
}

function deleteList(){
    todoStore.pop()
}
