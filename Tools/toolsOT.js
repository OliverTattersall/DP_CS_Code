// isEven takes an integer value and returns true if it is even and false otherwise
// Parameters: Integer a
function isEven(a){
    if(a%2==0){
        return true;
    }
    return false;
}

// console.log(isEven(4))

//SumDigits takes an integer value and returns the sum of its digits
// Parameters: Integer a
// Condition: a>0
function sumDigits(a){
    var sumdigits=0
    a=a.toString(10)
    for(i=0; i<a.length;i++){
        sumdigits=sumdigits+parseInt(a[i],10)
    }
    return sumdigits
}

//console.log(sumDigits(123))

// This function takes an integer, a,  and a list of integers, b, and scales
// each integer in the list by a, the first integer. 

// parameters: Integer a, List b
function scaleElementsA(num, list){
    for(i=0; i<list.length; i++){
        list[i]=list[i]*num
    }
    return list
}   

// console.log(scaleElementsA(2, [1,2,3,4]))


// This function takes an integer, nu ,  and a list of integers, b, and scales
// each integer in the list by num, the first integer. 

// parameters: Integer num, List b
// return newlst
// precondition: num>0, len(b)>0
// postcondition: b is not changed
function scaleElementsB(num, b){
    var newlst=[]
    for(i=0;i<b.length; i++){
        newlst.push(b[i]*num)
    }
    return newlst
}

// console.log(scaleElementsB(2, [1,2,3,4]))
// console.log(scaleElementsB(3, [2,4,6,8]))


// This function takes two strings, stra and strb, and returns a new string
// in the form of Larger string+Smaller string

// parameters: String stra, String strb
// Conditions: len(stra)>0, len(strb)>0

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
// Parameters: Integer a

function binCon(a){
    
    return a.toString(2)
}
// console.log(binCon(10))
// console.log(binCon(4))
// console.log(binCon(-4))


// Function to find maximum value in a list
// Parameters: List lst
// Conditions: len(lst)>0
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


// Function to find minimum value in a list
// Parameters: List lst
// Conditions: len(lst)>0

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


// Function to find minimum value in a list
// Parameters: List lst
// Conditions: len(lst)>0
function minnumB(lst){
    lst.sort(function(lst,b){ // short hand notation for sorting integers
        return lst-b
    })
    return lst[0]
}

// console.log(minnumB([5,6,7,2,1]))