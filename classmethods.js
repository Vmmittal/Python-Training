class MyClass{
    constructor(name){
        this.name = name
    }
    
    //This method is called with instance of a class.......................

    displayname(){
        console.log("This is :"+ this.name)
    }
}

const obj1 = new MyClass ("Vipul")
obj1.displayname()


//Static methods: Static methods are called with the classname itself. There is no need of creating an instance of class to call a function...........................

class Myclass2{
    

    static areaRect(length,breadth){      //Static method 1
      return length * breadth
    }

    static areaTriangle(length,breadth){   //Static method 2
        return (1/2)* length * breadth
    }
}

console.log(Myclass2.areaRect(2,4))
console.log(Myclass2.areaTriangle(10,5))


//Private class features....................................

class ClassWithPrivateField {
    #privateField;
  
    constructor() {
      this.#privateField = 'This is private';
    }

    display(){
        console.log(this.#privateField)
    }
  }

const obj3 = new ClassWithPrivateField()
obj3.display()

// console.log(obj3.#privateField)     
// It will give syntax error because it is private to the class and cannot be accessible outside the class.