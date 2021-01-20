time="17:12"

h=parseInt(time.slice(0,2))
m=time.slice(3, 5)

c=" AM"

if(h>12){
    h=h-12
    c=" PM"
}


console.log(h+":"+m+c)
