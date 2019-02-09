

function createNode(element) {
    return document.createElement(element);
}

function append(parent, el) {
  return parent.appendChild(el);
}
function get_current_time(){
  let today = new Date()
  var dd = today.getDate();
  var mm = today.getMonth()+1;
  var yyyy = today.getFullYear();
  if (dd < 10) {
  dd = '0' + dd;
  }

  if (mm < 10) {
  mm = '0' + mm;
  }
  return yyyy + '-' + mm + '-' + dd;
}
function get_time(date1, date2){
  var timeDiff = Math.abs(date2.getTime() - date1.getTime());
  return Math.ceil(timeDiff / (1000 * 3600 * 24));

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
      let meetup_container = document.getElementById('meetups_container')
      let meetup_data = data.data;
      return meetup_data.map(function(meetup_record) {
        let date = meetup_record.json_build_object.date;
        date = new Date(date);
        let today = new Date(get_current_time());
        let days = get_time(date, today);;
          if (days < 20){
            let meetup = createNode('div');
            let meetupid = meetup_record.json_build_object.meetupid;
            meetup.addEventListener("click", function meetups(){pass_meetup_data(meetupid);});
            meetup.classList.add('meetups')
            let date = createNode('p');
            let title = createNode('h4');
            let description = createNode('p');
            let venue = createNode('venue');
            date.innerHTML = `${meetup_record.json_build_object.date}`;
            title.innerHTML = `${meetup_record.json_build_object.title}`;
            description.innerHTML = `${meetup_record.json_build_object.description}`;
            venue.innerHTML = `${meetup_record.json_build_object.vanue}`;
            append(meetup, date);
            append(meetup, title);
            append(meetup, description);
            append(meetup, venue);
            append(meetup_container, meetup);
        }
    })
  }
    else{
      console.log(data.message);
    }

})

    .catch((err)=>console.log(err));
  }

document.getElementById('quiz').addEventListener('submit', create_questioon);
  function create_questioon(event) {
      /*
      Function to perform post a question
      */
      event.preventDefault();

      let signupUrl = 'https://questioner-api-048.herokuapp.com/api/v2/meetups/58/questions';
      fetch(signupUrl, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'Authorization' : 'Bearer ' + localStorage.getItem('token')
          },
          body: JSON.stringify({
            'title' :document.getElementById('title').value,
            'question' : document.getElementById('quest').value
          })
      })
          .then((response) => response.json())
          .then((data => {
              if (data.status === 201){
                  window.alert('question posted');
                  let question_data = data.data;
                  console.log(question_data);
                    closeForm('postquestion')
                    let question_div = document.getElementById('question_container');
                    let feedback = document.getElementById('votes');
                    let feedback_items = document.getElementById('feedback');
                    let title_element = createNode('h3');
                    let question_element = createNode('h4');
                    title_element.innerHTML = `${question_data.title}` ;
                    question_element.innerHTML = `${question_data.question}`;
                    feedback_items.style.display = "block"
                    feedback.innerHTML = `votes: ${question_data.votes}`
                    append(question_div, title_element);
                    append(question_div, question_element);
                    append(question_div, feedback)
            }
              else{
                  console.log(data.Error);
              }
          }))
          .catch((err)=>console.log(err));
  }


  function pass_meetup_data(id){
    localStorage.setItem("meetupid", id);
    Openmeetup('quiz');
  }
  function Openmeetup(div_id){
    if (div_id == "quiz"){
      document.getElementById("profile").style.display = "none"
    }
    else{
      document.getElementById("quiz").style.display = "none"
    }
    var i, body_content;
    body_content = document.getElementsByClassName("body_container");
    for (i = 0; i < body_content.length; i++){
      body_content[i].style.display = "none";
    }
    document.getElementById(div_id).style.display='block'
  }
  function openForm(fid) {
    document.getElementById(fid).style.display = "block";
}
function closeForm(fid) {
  document.getElementById(fid).style.display = "none";
}