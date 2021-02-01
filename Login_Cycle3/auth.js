const login_form = document.querySelector("#login-form");
const login_nav = document.getElementById("login_nav");
const logout_nav = document.getElementById("logout_nav");
const elements_nav = document.getElementById("elements_nav");
const elements_game_nav = document.getElementById("elements_game_nav");
var users = [["hello@gmail.com","password"]]
users.push(["h@c.ca", "p"])
console.log(users)

login_form.addEventListener('submit', (e)=>{
    e.preventDefault()

    let uname = login_form["username"].value;
    let pword = login_form["password"].value;
    let found=false;
    let corPas = true;
    for(i-0;i<users.length(); i++){
        if(users[i][0]==uname){
            if(users[i][1]==pword){
                found=true
                corPas = true
                break
            }else{
                corPas = false
            }
        }
    }
    
    if(corPas){
        if(found){
            console.log(uname, pword)
            logout_nav.style.display="block";
            elements_nav.style.display="block";
            elements_game_nav.style.display="block";
            login_nav.style.display="none";

        }else{
            users.push([uname, pword])
        }
    }else{
        alert("incorrect password")
    }



    const modal = document.querySelector("#login_modal")
    M.Modal.getInstance(modal).close();
});


logout_nav.addEventListener("click", (e)=>{
    console.log(e)
    logout_nav.style.display="none";
    elements_nav.style.display="none";
    elements_game_nav.style.display="none";
    login_nav.style.display="block";
    
})