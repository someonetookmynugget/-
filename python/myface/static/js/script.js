//selecting all required elements
const dropArea = document.querySelector(".drag-area");
dragText = dropArea.querySelector("header"),
button = dropArea.querySelector("button"),
input = dropArea.querySelector("input");

let file; // this is a global variable and we'll use it inside multiple functions

button.onclick = ()=>{
    input.click(); //if user click on the button then the input also clicked
}

input.addEventListener("change", function() {
     //getting user select file and [0] this means if user select multiple files then we'll select only the first one
    file = this.files[0];
    showFile(); //calling function
    dropArea.classList.add("active");
});


//IF user Drag File Over DragArea 
dropArea.addEventListener("dragover", (event)=>{
    event.preventDefault(); //preventing from default behaviour
    dropArea.classList.add("active");
    dragText.textContent = "Release to Upload File";
});

//IF user Leave dragged File from DragArea 
dropArea.addEventListener("dragleave", ()=>{
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
});

//IF user Drop File on DragArea 
dropArea.addEventListener("drop", (event)=>{
    event.preventDefault(); //preventing from default behaviour
    //getting user select file and [0] this means if user select multiple files then we'll select only the first one
    file = event.dataTransfer.files[0];
    showFile(); //calling function
});

function showFile() {
    let fileType = file.type;
    let validExtensions = ["image/jpeg", "image/jpg", "image/png"]; //adding some valid image extensions in array
    if (validExtensions.includes(fileType)) { //if user selected file is an image file
        let fileReader = new FileReader(); //creating new FileReader object
        fileReader.onload = () => {
            let fileURL = fileReader.result;
            let imgTag = `<img src="${fileURL}" alt="">`; //creating an img tag and passing user selected file source inside src attribute
            dropArea.innerHTML = imgTag; //adding that created img tag inside dropArea container
        }
        fileReader.readAsDataURL(file)
    } else {
        alert("This is not an Image File");
        dropArea.classList.remove("active");
    }
}

function downloadimg() {
    const url = "./static/testing"
}
// file.ready(function () {
//     $("#post").submit(function (event) {
//         $.ajax({
//             type: "POST",
//             url: "{% 'next' %}",
//             processData: false,
//             contentType: false,
//             data: file,
//             succes: function() {
//                 alart('送信完了')
//             },
//             error: function(data) {
//                 arert('エラー')
//             }
//         });
//         return false;
//     });
// });