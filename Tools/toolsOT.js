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

//console.log(sumDigits(123))

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


// converts a base 10 number into a base 2 number
function binCon(a){
    
    return a.toString(10)
}

// console.log(binCon(10))


// Function that finds the maximum number in a list
function maxnum(lst){
    var max=lst[0]
    for(i=0;i<lst.length(); i++){
        if(lst[i]>max){
            max=lst[i]
        }
    }
    return max
}

// console.log(maxnum([1,4,3,65,7,9,56]))


// Function that finds the minimum number in a list

function minnum(lst){

    min=lst[0] //assume correct value to element in the list

    for(i=0; i<lst.length();i++){
        if(lst[i]<min){
            min=lst[i]
        }
    }
    return min
}
// console.log(minnum([1,4,3,65,7,9,56]))

// Function that finds the minimum number in a list
// Uses sort function
function minnumB(lst){
    lst.sort(function(lst,b){ // short hand notation for sorting integers
        return lst-b
    })
    return lst[0]
}

// console.log(minnumB([5,6,7,2,1]))