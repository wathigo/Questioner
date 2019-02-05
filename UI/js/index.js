document.getElementById('signup_form').addEventListener('submit', signUpUser);
document.getElementById('admin_signup_form').addEventListener('submit', signUpAdmin);
document.getElementById('login_form').addEventListener('submit', login_user);
function signUpUser(event) {
    /*
    Function to perform user signup
    */
    event.preventDefault();
    let data = {};
    let fieldnames = [
      'firstname',
      'lastname',
      'othername',
      'email',
      'phonenumber',
      'password',
      'repeatpassword'
    ];
    let signupUrl = 'https://questioner-api-048.herokuapp.com/api/v2/auth/signup';


    for (let name of fieldnames) {
            data[name] = document.getElementById(name).value;
        }
    console.log(data)
    fetch(signupUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then((response) => response.json())
        .then((data => {
            if (data.status === 201){
                console.log('Success:', JSON.stringify(data));
                openForm('login')
            }
            else{
                console.log(data.message);
            }
        }))
        .catch((err)=>console.log(err));
}
function signUpAdmin(event) {
    /*
    Function to perform amin signup
    */
    event.preventDefault();

    let signupUrl = 'https://questioner-api-048.herokuapp.com/api/v2/auth/admin/signup';
    fetch(signupUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          'firstname' : document.getElementById('fname').value,
          'lastname' : document.getElementById('lname').value,
          'othername' : document.getElementById('oname').value,
          'email' :document.getElementById('admn_email').value,
          'phonenumber' : document.getElementById('phone').value,
          'password' : document.getElementById('psw').value,
          'repeatpassword' : document.getElementById('rpsw').value
        })
    })
        .then((response) => response.json())
        .then((data => {
            if (data.status === 201){
                console.log('Success:', JSON.stringify(data));
                openForm('login')
            }
            else{
                console.log(data.message);
            }
        }))
        .catch((err)=>console.log(err));
}

function login_user(event) {
    /*
    Function to perform amin signup
    */
    event.preventDefault();

    let signupUrl = 'https://questioner-api-048.herokuapp.com/api/v2/auth/login';
    fetch(signupUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          'email' :document.getElementById('email_login').value,
          'password' : document.getElementById('psw_login').value
        })
    })
        .then((response) => response.json())
        .then((data => {
            if (data.status === 200){
                console.log('Success:', JSON.stringify(data));
                openForm('login')
            }
            else{
                console.log(data.message);
            }
        }))
        .catch((err)=>console.log(err));
}

function openForm(form_id){
  if (form_id == 'register'){
    document.getElementById('login').style.display='none';
    document.getElementById('Adminsignup').style.display='none';
  }
  else if(form_id == 'login') {
    document.getElementById('register').style.display='none';
    document.getElementById('Adminsignup').style.display='none';
  }
  else{
    document.getElementById('login').style.display='none';
    document.getElementById('register').style.display='none';
  }
  var i, body_content;
  body_content = document.getElementsByClassName("body_content");
  for (i = 0; i < body_content.length; i++){
    body_content[i].style.display = "none";
  }
  document.getElementById(form_id).style.display='block'
}
function closeForm(form_id){
  document.getElementById(form_id).style.display='none'
  var i, body_content;
  body_content = document.getElementsByClassName("body_content");
  for (i = 0; i < body_content.length; i++){
    body_content[i].style.display = "block";
  }
}
