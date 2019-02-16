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
                window.alert(data.Message);
                let token = data.access_token;
                console.log(token);
                localStorage.setItem("token", token);
                if (data.admin === 'isadmin'){
                  window.location.href = './admin.html';}
                else{
                  window.location.href = './profile.html';
                }
            }
            else{
                console.log(data.message);
            }
        }))
        .catch((err)=>console.log(err));
}

function createNode(element) {
    return document.createElement(element);
}

function append(parent, el) {
  return parent.appendChild(el);
}

function get_meetups(){
  let signupUrl = 'https://questioner-api-048.herokuapp.com/api/v2/meetups/upcoming';

  fetch(signupUrl, {
    method: "get",
    header: {
      "Content-Type": "application/json"
    }
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 200) {
      console.log('successful', data.status)
      let meetup_container = document.getElementById('meetups_container')
      let meetup_data = data.data;
      meetup_data = meetup_data.slice(0, 6)
      return meetup_data.map(function(meetup_record) {
        let meetup = createNode('div');
        meetup.classList.add('meetups')
        let date = createNode('p');
        let title = createNode('h4');
        let description = createNode('p');
        let venue = createNode('venue');
        date.innerHTML = `Date: ${meetup_record.json_build_object.date}`;
        title.innerHTML = `Title: ${meetup_record.json_build_object.title}`;
        description.innerHTML = `Description: ${meetup_record.json_build_object.description}`;
        venue.innerHTML = `Venue: ${meetup_record.json_build_object.vanue}`;
        append(meetup, date);
        append(meetup, title);
        append(meetup, description);
        append(meetup, venue);
        append(meetup_container, meetup);
    })
  }
    else{
      console.log(data.message);
    }

})
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
