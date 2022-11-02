function sendEmail() {
    this.contact_number.value = Math.random() * 100000 | 0;
    var params = {
        first_name : document.getElementById("fname").value,
        last_name : document.getElementById("lname").value,
        email : document.getElementById("email_id").value,
        messaage: document.getElementById("message").value,

    }

    emailjs.send("service_5id5id1", "template_d79ltqf", params).then(
        function () {
            console.log('SUCCESS!');
        }, function (error) {
            console.log("falied...", error);
        }
    )
}

const items = document.querySelectorAll('.appear');

const active = function(entries){
    entries.forEach(entry => {
        if(entry.isIntersecting){
        entry.target.classList.add('inview'); 
        }else{
            entry.target.classList.remove('inview'); 
        }
    });
}
const io2 = new IntersectionObserver(active);
 for(let i=0; i < items.length; i++){
    io2.observe(items[i]);
 }
