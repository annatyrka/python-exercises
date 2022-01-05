const users = [
    { name: 'John', age: 34 },
    { name: 'Amy', age: 20 },
    { name: 'camperCat', age: 10 }
];

const sumOfAges = users.reduce((sum, user) => sum + user.age);
console.log(sumOfAges);

const numbers = [15.5, 2.3, 1.1, 4.7];

const sumOfNumbers = numbers.reduce((sum, item) => sum + item);
console.log(sumOfNumbers);

const avergaeOfNumbers = numbers.reduce((average, item) => average + item / numbers.length, 0);
console.log(avergaeOfNumbers);