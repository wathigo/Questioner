

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
  let Url = 'https://questioner-api-048.herokuapp.com/api/v2/meetups/upcoming';

  fetch(Url, {
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
            date.innerHTML = `Date: ${meetup_record.json_build_object.date}`;
            title.innerHTML = `Title: ${meetup_record.json_build_object.title}`;
            description.innerHTML = `Description: ${meetup_record.json_build_object.description}`;
            venue.innerHTML = `Venue: ${meetup_record.json_build_object.vanue}`;
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
      let meetupid = localStorage.getItem('meetupid')
      let Url = `https://questioner-api-048.herokuapp.com/api/v2/meetups/${meetupid}/questions`;
      fetch(Url, {
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
                  console.log(question_data.questionid);
                    closeForm('postquestion')
                    let feedback = createNode('div');
                    let feedback_p = createNode('p');
                    let vote_element = createNode('i');
                    vote_element.setAttribute('id', 'votes');
                    let upvote_element = createNode('i');
                    upvote_element.classList.add('fa', 'fa-thumbs-up');
                    upvote_element.setAttribute('id', 'upvote');
                    let downvote_element = createNode('i');
                    downvote_element.classList.add('fa', 'fa-thumbs-down');
                    let comment_link = createNode('a');
                    comment_link.setAttribute('id', 'comment_icon');
                    let icon_element = createNode('i');
                    icon_element.classList.add('fa', 'fa-comment-o');
                    comment_link.addEventListener("click", function meetups(){pass_question_data(question_data.questionid);});
                    let question_div = document.getElementById('question_container');
                    upvote_element.addEventListener("click", function upvote(){upvote_question(question_data.questionid);});
                    downvote_element.addEventListener("click", function downvote(){downvote_question(question_data.questionid);});
                    let title_element = createNode('h2');
                    let question_element = createNode('h4');
                    title_element.innerHTML = `${question_data.title}` ;
                    question_element.innerHTML = `${question_data.question}`;
                    vote_element.innerHTML = `votes: ${question_data.votes}`;
                    append(question_div, title_element);
                    append(question_div, question_element);
                    append(feedback, feedback_p);
                    append(question_div, vote_element);
                    append(feedback, upvote_element);
                    append(feedback, downvote_element);
                    append(comment_link, icon_element);
                    append(feedback, comment_link);
                    append(question_div, feedback)
            }
              else{
                  console.log(data.Error);
              }
          }))
          .catch((err)=>console.log(err));
  }

function upvote_question(questionid){
  Url = `https://questioner-api-048.herokuapp.com/api/v2/questions/${questionid}/upvote`
  fetch(Url, {
    method: 'PATCH',
    headers: {
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer ' + localStorage.getItem('token')
    },
  })
  .then((response) => response.json())
  .then((data => {
    data = data.data[0];
    let votes = document.getElementById('votes');
    votes.innerHTML = `votes: ${data.json_build_object.votes}`;
  }))
}

function downvote_question(questionid){
  Url = `https://questioner-api-048.herokuapp.com/api/v2/questions/${questionid}/downvote`
  fetch(Url, {
    method: 'PATCH',
    headers: {
        'Content-Type': 'application/json',
        'Authorization' : 'Bearer ' + localStorage.getItem('token')
    },
  })
  .then((response) => response.json())
  .then((data => {
    data = data.data;
    let votes = document.getElementById('votes');
    votes.innerHTML = `votes: ${data.votes}`;
  }))
}

function post_comment(){
  /*
  Function to perform post cmment request
  */
  let questionid = localStorage.getItem('questionid')
  console.log(questionid);
  let Url = `https://questioner-api-048.herokuapp.com/api/v2/questions/${questionid}/comments`;
  fetch(Url, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Authorization' : 'Bearer ' + localStorage.getItem('token')
      },
      body: JSON.stringify({
        'comment' :document.getElementById('comment_body').value
      })
  })
      .then((response) => response.json())
      .then((data => {
          if (data.status === 201){
            window.alert('Successful');
              console.log(data);
              closeForm('comment');
              let comment_element = document.getElementById('comment_element')
              comment_element.innerHTML = `${data.data.comment}`;
          }
          else{
              console.log(data.message);
          }
      }))
      .catch((err)=>console.log(err));
}

function fetch_comments(question_id){
  Url = `https://questioner-api-048.herokuapp.com/api/v2/questions/${question_id}/comments`;
  return fetch(Url, {
    method: "get",
    header: {
      "Content-Type": "application/json"
    }
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 200) {
      console.log(data.data);
      return data.data;
    }
  })
  console.log('not returning!')
}
function get_question(){
  console.log('get question launched!')
  event.preventDefault();
  let meetupid = localStorage.getItem('meetupid')
  Url = `https://questioner-api-048.herokuapp.com/api/v2/meetups/${meetupid}/questions`

  fetch(Url, {
    method: "get",
    header: {
      "Content-Type": "application/json"
    }
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 200) {
      let question_data = data.data;
      let question_div = document.getElementById('question_container');
      return question_data.map(function(question_record) {
        console.log(question_record);
        let comment_div = create_comment_div(question_record.question_id);
        let question_data = createNode('div');
        let title_element = createNode('h2');
        let question_element = createNode('h4');
        let feedback = createNode('div');
        let feedback_p = createNode('p');
        let vote_element = createNode('i');
        vote_element.setAttribute('id', 'votes');
        let upvote_element = createNode('i');
        upvote_element.classList.add('fa', 'fa-thumbs-up');
        upvote_element.setAttribute('id', 'upvote');
        let downvote_element = createNode('i');
        downvote_element.classList.add('fa', 'fa-thumbs-down');
        let comment_link = createNode('a');
        comment_link.classList.add('comment_icon');
        let icon_element = createNode('i');
        icon_element.classList.add('fa', 'fa-comment-o');
        let comment_element = createNode('p');
        comment_element.setAttribute('id', 'comment_element');
        title_element.innerHTML = `${question_record.title}`;
        question_element.innerHTML = `${question_record.question}`;
        vote_element.innerHTML = `votes: ${question_record.votes}`;
        console.log(question_record.questionid)
        append(question_data, title_element);
        append(question_data, question_element);
        append(feedback, feedback_p);
        append(feedback, upvote_element);
        append(feedback, downvote_element);
        append(comment_link, icon_element);
        append(feedback, comment_link);
        append(question_data, vote_element);
        append(question_data, feedback);
        let comment_array = fetch_comments(question_record.questionid);
        comment_array.then(function(value){
          console.log(value.length);
          if (value.length > 0){
            value.map(function(comment_record) {
              let comment_rec = createNode('p');
              comment_rec.innerHTML = `${comment_record.comment}`;
              append(comment_element, comment_rec);
              append(question_data, comment_element);
        })}});
        append(question_div, question_data);
        append(question_div, comment_div);
        upvote_element.addEventListener("click", function upvote(){upvote_question(question_record.questionid);});
        downvote_element.addEventListener("click", function downvote(){downvote_question(question_record.questionid);});
        comment_link.addEventListener("click", function meetups(){pass_question_data(event, question_record.questionid)});


      })
    }

})
}

function send_reserve(reserve_status){
  event.preventDefault();
  meetupid = localStorage.getItem('meetupid');
  Url = `https://questioner-api-048.herokuapp.com/api/v2/meetups/${meetupid}/rsvps`;
  fetch(Url, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Authorization' : 'Bearer ' + localStorage.getItem('token')
      },
      body: JSON.stringify({
        'status' :reserve_status
      })
  })
      .then((response) => response.json())
      .then(data => {
          if (data.status === 201){
            if (reserve_status === 'yes'){
              window.alert('meetup reserved');
            }
            else{
              window.alert('response recorded');
            }
          }
          else{
            window.alert('oops... something went wrong');
          }
        })
}

function create_comment_div(questionid){
  let comment_div = createNode('div');
  comment_div.setAttribute('id', 'comment');
  let comment_body = createNode('textarea');
  comment_body.setAttribute('id', 'comment_body');
  comment_body.setAttribute('placeholder', 'comment');
  let comment_submit = createNode('button');
  comment_submit.setAttribute('type', 'submit');
  comment_submit.setAttribute('id', 'submitbtn');
  comment_submit.classList.add('btn');
  comment_submit.innerHTML = `Submit`;
  comment_submit.addEventListener('click', function comment(){
    console.log('clicked');
    localStorage.setItem('question_id', questionid);
    post_comment();
  });
  let comment_close = createNode('button');
  comment_close.classList.add('clbtn');
  comment_close.setAttribute('type', 'button');
  comment_close.innerHTML = `close`;
  comment_close.addEventListener('click', function comment(){closeForm('comment');});
  append(comment_div, comment_body);
  append(comment_div, comment_submit);
  append(comment_div, comment_close);
  return comment_div
}

  function pass_meetup_data(id){
    localStorage.setItem("meetupid", id);
    Openmeetup('quiz');
    get_question();
  }

  function pass_question_data(event, id){
    localStorage.setItem("questionid", id);
    console.log(id)
    openForm('comment');
  }

  function Openmeetup(div_id){
    document.getElementById("quiz").style.display = "none"
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
