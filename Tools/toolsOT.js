// isEven takes a single integer value a >= 0 and returns true if it is even and false otherwise


function isEven(a){
    if(a%2==0){
        return true;
    }
    return false;
}

// console.log(isEven(4))


function sumDigits(a){
    var sumdigits=0
    a=a.toString(10)
    for(i=0; i<a.length;i++){
        sumdigits=sumdigits+parseInt(a[i],10)
    }
    return sumdigits
}

console.log(sumDigits(123))

function scaleElementsA(num, list){
    for(i=0; i<list.length; i++){
        list[i]=list[i]*num
    }
    return list
}   

// console.log(scaleElementsA(2, [1,2,3,4]))

function scaleElementsB(num, list){
    var newlst=[]
    for(i=0;i<list.length; i++){
        newlst.push(list[i]*num)
    }
    return newlst
}

// console.log(scaleElementsB(2, [1,2,3,4]))

function addStringsSmallLarge(stra, strb){
    var str=""
    if(stra.length>strb.length){
        str=stra+strb
    }else{
        str=strb+stra
    }

    return str
}

// console.log(addStringsSmallLarge("banana", "mango"))