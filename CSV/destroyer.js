function destroyer(arr) {

    let toRemove = Object.values(arguments).slice(1);
    let newArr = []

    for (let i = 0; i < arr.length; i++) {
        if (toRemove.includes(arr[i])) {
            delete arr[i]
        }
    }
    return arr.filter(item => item != undefined)
}

console.log(destroyer([1, 2, 3, 1, 2, 3], 4, 3));