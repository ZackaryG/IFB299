from home.models import Student

function overlayOn(){
    document.getElementById("overlay").style.display = "block";
}

function overlayOff(){
    document.getElementById("overlay").style.display = "none";
}

function formComplete(){
    s = Student(firstname="test", lastname="test", DOB="2000-01-01", gender="test", phone="1234", facebook="test", email="test@test.com", contactPref="e", studentType="n", schoolID="");
    s.save();
    overlayOff()
}