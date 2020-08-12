document.querySelector('#input-img').addEventListener('change', function() {

    var reader = new FileReader();
    reader.onload = function() {
  
      var arrayBuffer = this.result,
        array = new Uint8Array(arrayBuffer);
  
        document.querySelector('#input-img-data').value = array;
        // Display int array at client side for testing purpose
        // document.querySelector('#result').textContent = array;
    }
    reader.readAsArrayBuffer(this.files[0]);
});

document.addEventListener("DOMContentLoaded", () => {
    document.querySelector('#input-img-submit').disabled = true;
    document.querySelector('#input-img').onchange = function(){
        if(this.value != ""){
            document.querySelector('#input-img-submit').disabled = false;
        }
    };
    document.querySelector('#upload-img').onsubmit = function(){
      // Prevent form from reloading page
      // return false;
    };
    if(document.querySelector('#response-container')){
      var img = document.createElement('img');
      img.id = "response-img";
      img.alt = "response image";
      img.src = `static/image/new_image?${performance.now()}`;
      var response_container = document.querySelector('#response-container');
      response_container.insertBefore(img, response_container.childNodes[0]);
    }
});

function bin2String(array) {
    var result = "";
    for (var i = 0; i < array.length; i++) {
      result += String.fromCharCode(parseInt(array[i], 2));
    }
    return result;
  }

  function string2Bin(str) {
  var result = [];
  for (var i = 0; i < str.length; i++) {
    result.push(str.charCodeAt(i).toString(2));
  }
  return result;
}

// References:
// onchange event on input file: https://stackoverflow.com/questions/32556664/getting-byte-array-through-input-type-file
// bin2String and string2Bin: https://stackoverflow.com/questions/3195865/converting-byte-array-to-string-in-javascript