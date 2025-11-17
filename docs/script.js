// let backendUrl = "https://your-backend.onrender.com/api/test";
// let secretKey = null;

// document.getElementById("unlock").onclick = () => {
//   const entered = document.getElementById("secret").value.trim();
//   if (!entered) return alert("Enter secret");

//   secretKey = entered;
//   document.getElementById("main").style.display = "block";
// };

// document.getElementById("recordBtn").onclick = async () => {
//   let stream = await navigator.mediaDevices.getUserMedia({ audio: true });
//   let mediaRecorder = new MediaRecorder(stream);
//   let chunks = [];

//   mediaRecorder.ondataavailable = e => chunks.push(e.data);
//   mediaRecorder.onstop = async () => {
//     let blob = new Blob(chunks, { type: "audio/webm" });

//     let formData = new FormData();
//     formData.append("secret", secretKey);
//     formData.append("audio", blob, "test.webm");

//     let res = await fetch(backendUrl, { method: "POST", body: formData });
//     let text = await res.text();
//     document.getElementById("result").innerText = text;
//   };

//   mediaRecorder.start();
//   setTimeout(() => mediaRecorder.stop(), 1000);
// };
