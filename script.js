const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
rl.question('Please input something', ans => {
  console.log(`Ok, you input ${ans}`);
  console.log('Closing the interface');
  rl.close();
});

let students = [];
class Student {
  constructor(id, name, age, mark) {
    this.id = id;
    this.name = name;
    this.age = age;
    this.mark = mark;
  }

  toString() {
    return `${this.id}, ${this.name}, ${this.age}, ${this.mark}`;
  }
}

init();

function init() {
  display();
}

function display() {}

// Create
function add(student) {
  students.push(student);
}

// Read
function show(student) {
  console.log(student.toString());
}

// Update
function update(student) {}

// Delete
function remove(student) {
  const index = students.findIndex(x => x.id === student.id);
  if (index > -1) {
    students.splice(index, 1);
  }
}

stds = [
  { name: 'Harry', age: 18, mark: 8 },
  { name: 'Hermione', age: 18, mark: 10 },
  { name: 'Ron', age: 18, mark: 5 },
];

std = { name: 'Malfoy', age: 19, mark: 7 };
std2 = { name: 'kevin', age: 25, mark: 10 };
